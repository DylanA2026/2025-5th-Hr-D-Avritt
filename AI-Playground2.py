import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack — 100k bankroll, bets up to 25k")
clock = pygame.time.Clock()

# Fonts and colors
FONT = pygame.font.SysFont("arial", 24)
BIGFONT = pygame.font.SysFont("arial", 32, bold=True)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)

# Card setup
suits = ['♠','♥','♦','♣']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
values = {str(i):i for i in range(2,11)}
values.update({"J":10, "Q":10, "K":10, "A":11})

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(r,s) for r in ranks for s in suits]*6
        random.shuffle(self.cards)
    def deal(self):
        if len(self.cards)<30:
            self.__init__()
        return self.cards.pop()

# Hand value calculation
def hand_value(hand):
    total = sum(card.value for card in hand)
    aces = sum(1 for card in hand if card.rank=='A')
    while total>21 and aces>0:
        total-=10
        aces-=1
    return total

# Draw card function
def draw_card(surf, card, pos, hidden=False):
    x, y = pos
    rect = pygame.Rect(x, y, 70, 100)
    pygame.draw.rect(surf, WHITE if not hidden else BLACK, rect)
    pygame.draw.rect(surf, BLACK, rect, 2)
    if not hidden:
        text = FONT.render(str(card), True, RED if card.suit in ['♥','♦'] else BLACK)
        surf.blit(text, (x+5, y+5))

# Button class
class Button:
    def __init__(self, rect, text, action):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.action = action
    def draw(self, surf):
        pygame.draw.rect(surf, WHITE, self.rect)
        pygame.draw.rect(surf, BLACK, self.rect, 2)
        t = FONT.render(self.text, True, BLACK)
        surf.blit(t, (self.rect.centerx-t.get_width()//2, self.rect.centery-t.get_height()//2))
    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

# Game state
bankroll = 100000
bet = 0
deck = Deck()
player_hand = []
dealer_hand = []
phase = 'betting'
message = 'Place your bet'
first_decision = True

# Betting actions
def adjust_bet(amount):
    global bet
    if phase!='betting': return
    if bet + amount <= min(25000, bankroll):
        bet += amount

def clear_bet():
    global bet
    if phase=='betting': bet=0

def max_bet():
    global bet
    if phase=='betting': bet = min(25000, bankroll)

def deal():
    global phase, player_hand, dealer_hand, message, bankroll, first_decision
    if phase!='betting' or bet==0: return
    bankroll -= bet
    player_hand = [deck.deal(), deck.deal()]
    dealer_hand = [deck.deal(), deck.deal()]
    phase = 'player'
    first_decision = True
    message = 'Hit, Stand, or Double?'

def hit():
    global player_hand, phase, message, first_decision
    if phase!='player': return
    player_hand.append(deck.deal())
    first_decision=False
    if hand_value(player_hand)>21:
        phase='dealer'
        dealer_play()

def stand():
    global phase
    if phase=='player':
        phase='dealer'
        dealer_play()

def double():
    global bankroll, bet, player_hand, phase, first_decision
    if phase=='player' and first_decision and bankroll>=bet:
        bankroll-=bet
        bet*=2
        player_hand.append(deck.deal())
        first_decision=False
        phase='dealer'
        dealer_play()

def dealer_play():
    global phase, bankroll, message
    while hand_value(dealer_hand)<17:
        dealer_hand.append(deck.deal())
    player_val = hand_value(player_hand)
    dealer_val = hand_value(dealer_hand)
    if player_val>21:
        message='Player busts! Dealer wins.'
    elif dealer_val>21 or player_val>dealer_val:
        message='Player wins!'
        bankroll+=bet*2
    elif dealer_val==player_val:
        message='Push'
        bankroll+=bet
    else:
        message='Dealer wins!'
    phase='betting'

def create_buttons():
    global buttons
    buttons = [
        Button((50,600,70,40), '+25', lambda: adjust_bet(25)),
        Button((130,600,70,40), '+50', lambda: adjust_bet(50)),
        Button((210,600,70,40), '+100', lambda: adjust_bet(100)),
        Button((290,600,70,40), '+500', lambda: adjust_bet(500)),
        Button((370,600,70,40), '+1000', lambda: adjust_bet(1000)),
        Button((450,600,70,40), '+5000', lambda: adjust_bet(5000)),
        Button((530,600,90,40), '+25000', lambda: adjust_bet(25000)),
        Button((630,600,70,40), 'Clear', clear_bet),
        Button((710,600,70,40), 'Max', max_bet),
        Button((790,600,70,40), 'Deal', deal),
        Button((900,500,100,40), 'Hit', hit),
        Button((1020,500,100,40), 'Stand', stand),
        Button((1140,500,100,40), 'Double', double),
    ]

create_buttons()

running=True
while running:
    screen.fill(GREEN)
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            running=False
        if e.type==pygame.MOUSEBUTTONDOWN:
            for b in buttons:
                b.click(e.pos)

    # Draw bankroll and bet
    b_txt = BIGFONT.render(f"Bankroll: ${bankroll}", True, WHITE)
    screen.blit(b_txt,(50,20))
    bet_txt = BIGFONT.render(f"Bet: ${bet}", True, YELLOW)
    screen.blit(bet_txt,(400,20))

    # Draw dealer hand
    dealer_label = BIGFONT.render("Dealer:", True, WHITE)
    screen.blit(dealer_label,(50,100))
    for i, card in enumerate(dealer_hand):
        hidden = (i==0 and phase=='player')
        draw_card(screen, card, (160+i*80,100), hidden)
    if dealer_hand:
        if phase=='player':
            visible_val = hand_value([dealer_hand[1]])
            vtxt = FONT.render(f"Visible: {visible_val}", True, WHITE)
            screen.blit(vtxt,(160,210))
        else:
            total = hand_value(dealer_hand)
            vtxt = FONT.render(f"Total: {total}", True, WHITE)
            screen.blit(vtxt,(160,210))

    # Draw player hand
    player_label = BIGFONT.render("Player:", True, WHITE)
    screen.blit(player_label,(50,300))
    for i, card in enumerate(player_hand):
        draw_card(screen, card, (160+i*80,300))
    if player_hand:
        ptotal = hand_value(player_hand)
        ptxt = FONT.render(f"Total: {ptotal}", True, WHITE)
        screen.blit(ptxt,(160,410))

    # Draw buttons
    for b in buttons:
        if phase=='betting' and b.text not in ['Hit','Stand','Double']:
            b.draw(screen)
        elif phase=='player' and b.text in ['Hit','Stand','Double']:
            b.draw(screen)

    # Message
    msg_txt = BIGFONT.render(message, True, WHITE)
    screen.blit(msg_txt,(50,500))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()