import pygame, random, time

pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mr. Money Bags Slot Machine")

# Fonts & Colors
FONT = pygame.font.SysFont("arial", 24, bold=True)
BIGFONT = pygame.font.SysFont("arial", 36, bold=True)
HUGEFONT = pygame.font.SysFont("arial", 48, bold=True)

WHITE, BLACK = (255,255,255), (0,0,0)
RED, GREEN, YELLOW = (220,40,40), (40,220,40), (240,240,60)
GREY, DARKGREY = (140,140,140), (30,30,30)

# ---------------------
# Load reel images safely
# ---------------------
def load_image(path):
    img = pygame.image.load(path)
    if path.lower().endswith(".png"):
        return img.convert_alpha()
    else:
        return img.convert()

symbols = {
    "cherry": load_image("images/cherry.jpg"),
    "diamond": load_image("images/diamond.png"),
    "seven": load_image("images/seven.jpg"),
    "clover": load_image("images/clover.jpg"),
    "money": load_image("images/money.jpg"),
    "star": load_image("images/star.jpg"),
}

# Scale all images
for key in symbols:
    symbols[key] = pygame.transform.smoothscale(symbols[key], (80, 80))

symbol_list = list(symbols.keys())

# ---------------------
# Game state
# ---------------------
balance = 10000
bet = 100
reels_final = [[random.choice(symbol_list) for _ in range(3)] for _ in range(3)]
spinning = False
spin_stage = 0
spin_start = 0
red_spin = False
free_spin = False
result_msg = ""

# Reel spin state
reel_offsets = [0, 0, 0]
reel_speed = [0, 0, 0]
reel_stopping = [False, False, False]

# ---------------------
# Buttons
# ---------------------
class Button:
    def __init__(self, rect, text, color, action):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect, border_radius=10)
        pygame.draw.rect(surf, BLACK, self.rect, 3, border_radius=10)
        label = FONT.render(self.text, True, BLACK)
        surf.blit(label, (self.rect.x + (self.rect.w - label.get_width()) // 2,
                          self.rect.y + (self.rect.h - label.get_height()) // 2))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            return self.action
        return None

buttons = [
    Button((100, 500, 80, 40), "-100", GREY, "bet_down"),
    Button((200, 500, 80, 40), "+100", GREY, "bet_up"),
    Button((300, 500, 120, 40), "Max Bet", GREY, "bet_max"),
    Button((500, 500, 160, 60), "SPIN", YELLOW, "spin"),
]

# ---------------------
# Functions
# ---------------------
def draw_text(text, font, color, x, y, center=False):
    label = font.render(text, True, color)
    if center:
        screen.blit(label, (x - label.get_width()//2, y))
    else:
        screen.blit(label, (x, y))

def start_spin(is_free=False):
    global spinning, spin_stage, spin_start, red_spin, reels_final, free_spin
    spinning = True
    spin_stage = 0
    spin_start = time.time()
    red_spin = random.random() < 0.1
    reels_final = [[random.choice(symbol_list) for _ in range(3)] for _ in range(3)]
    for i in range(3):
        reel_offsets[i] = 0
        reel_speed[i] = 30 + i*5
        reel_stopping[i] = False
    if is_free:
        free_spin = False  # consuming the free spin

def stop_reel(reel_index):
    global reel_stopping
    reel_stopping[reel_index] = True
    reel_speed[reel_index] = 0
    if reel_index == 2:
        finish_spin()

def finish_spin():
    global spinning, balance, result_msg
    spinning = False
    balance += calculate_payout()
    if free_spin:
        start_spin(is_free=True)  # auto-start free spin

def calculate_payout():
    global reels_final, bet, result_msg, red_spin, free_spin
    payout = 0
    # 9-line payout
    lines = [
        [reels_final[0][0], reels_final[0][1], reels_final[0][2]],  # top row
        [reels_final[1][0], reels_final[1][1], reels_final[1][2]],  # middle row
        [reels_final[2][0], reels_final[2][1], reels_final[2][2]],  # bottom row
        [reels_final[0][0], reels_final[1][1], reels_final[2][2]],  # diag TL->BR
        [reels_final[2][0], reels_final[1][1], reels_final[0][2]],  # diag BL->TR
        [reels_final[0][0], reels_final[1][1], reels_final[0][2]],  # V left
        [reels_final[2][0], reels_final[1][1], reels_final[2][2]],  # V right
        [reels_final[0][2], reels_final[1][1], reels_final[2][0]],  # Z top
        [reels_final[2][2], reels_final[1][1], reels_final[0][0]]   # Z bottom
    ]

    line_wins = []
    for row in lines:
        if row.count(row[0]) == 3:
            if row[0] == "seven":
                line_wins.append(bet * 50)
            elif row[0] == "diamond":
                line_wins.append(bet * 25)
            elif row[0] == "money":
                line_wins.append(bet * 20)
            else:
                line_wins.append(bet * 10)

    total = sum(line_wins)
    if red_spin:
        result_msg = "RED SPIN! You get a FREE SPIN!"
        free_spin = True  # grant free spin
    elif total > 0:
        result_msg = f"You win ${total}"
    else:
        result_msg = "No win"

    return total - bet

# ---------------------
# Main loop
# ---------------------
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(DARKGREY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for b in buttons:
                act = b.check_click(pos)
                if act == "bet_down":
                    bet = max(100, bet - 100)
                elif act == "bet_up":
                    bet = min(25000, bet + 100)
                elif act == "bet_max":
                    bet = min(25000, balance)
                elif act == "spin" and not spinning and balance >= bet:
                    balance -= bet
                    start_spin()

    # Draw machine border
    border_color = RED if red_spin else GREY
    pygame.draw.rect(screen, border_color, (150, 120, 500, 320), border_radius=20)
    pygame.draw.rect(screen, BLACK, (150, 120, 500, 320), 6, border_radius=20)

    # Draw balance & bet
    draw_text(f"Balance: ${balance}", BIGFONT, WHITE, 50, 30)
    draw_text(f"Bet: ${bet}", BIGFONT, YELLOW, 50, 80)

    # Draw reels
    for c in range(3):
        for r in range(3):
            rect = pygame.Rect(180 + c*140, 150 + r*100, 120, 90)
            pygame.draw.rect(screen, WHITE, rect, border_radius=8)
            pygame.draw.rect(screen, BLACK, rect, 3, border_radius=8)

            if spinning and not reel_stopping[c]:
                idx = (r + int(reel_offsets[c] // 100)) % len(symbol_list)
                img = symbols[symbol_list[idx]]
            else:
                key = reels_final[r][c]
                if key not in symbols or key == "":
                    key = random.choice(symbol_list)
                    reels_final[r][c] = key
                img = symbols[key]

            screen.blit(img, (rect.x + 20, rect.y + 5))

    # Update reels
    if spinning:
        for c in range(3):
            if not reel_stopping[c]:
                reel_offsets[c] += reel_speed[c]
                if reel_offsets[c] >= 100:
                    reel_offsets[c] = 0

        # Stop reels one by one
        if time.time() - spin_start > 1.0 and not reel_stopping[0]:
            stop_reel(0)
        elif time.time() - spin_start > 2.0 and not reel_stopping[1]:
            stop_reel(1)
        elif time.time() - spin_start > 3.0 and not reel_stopping[2]:
            stop_reel(2)

    # Show result
    if result_msg and not spinning:
        color = GREEN if "win" in result_msg else WHITE
        draw_text(result_msg, HUGEFONT, color, WIDTH//2, 460, center=True)

    # Draw buttons
    for b in buttons:
        b.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
