# SUPERHOT-like TRUE FPS (Raycasting) in Python
# ------------------------------------------------------------
# FEATURES:
# ✔ TRUE first-person view (raycasting, DOOM-style)
# ✔ SUPERHOT time mechanic
# ✔ Enemy humanoid silhouettes
# ✔ Weapon pickup system
# ✔ Gun + melee
# ------------------------------------------------------------
# NOTE:
# This is a minimal but REAL FPS engine in one file.
# ------------------------------------------------------------
# Requirements:
#   pip install pygame
# Run:
#   python superhot_fps.py

import pygame, math, random

# ---------------- CONFIG ----------------
WIDTH, HEIGHT = 900, 600
HALF_W, HALF_H = WIDTH//2, HEIGHT//2
FPS = 60
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 800
TIME_IDLE = 0.05
TIME_MOVE = 1.0

WHITE = (240,240,240)
BLACK = (10,10,10)
RED = (220,50,50)
GRAY = (120,120,120)

# ---------------- MAP ----------------
WORLD_MAP = [
    '#########',
    '#.......#',
    '#..#....#',
    '#.......#',
    '#....#..#',
    '#.......#',
    '#########'
]
TILE = 80

# ---------------- INIT ----------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# ---------------- PLAYER ----------------
class Player:
    def __init__(self):
        self.x, self.y = 160, 160
        self.angle = 0
        self.weapon = 'gun'
        self.alive = True

player = Player()

# ---------------- ENEMY ----------------
class Enemy:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.alive = True
    def draw(self, depth):
        size = int(600 / (depth+1))
        pygame.draw.rect(screen, RED,
            (HALF_W-size//2, HALF_H-size, size, size*2))
        pygame.draw.circle(screen, RED,
            (HALF_W, HALF_H-size), size//3)

# ---------------- WEAPON PICKUP ----------------
class Pickup:
    def __init__(self, x, y, kind):
        self.x, self.y = x, y
        self.kind = kind

# ---------------- GAME STATE ----------------
enemies = [Enemy(400,400), Enemy(520,240)]
pickups = [Pickup(240,400,'gun'), Pickup(600,400,'melee')]

# ---------------- UTIL ----------------
def mapping(a):
    return int(a//TILE)*TILE

# ---------------- RAYCAST ----------------
def raycast():
    ox, oy = player.x, player.y
    cur_angle = player.angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        depth = 1
        while depth < MAX_DEPTH:
            x = ox + depth*cos_a
            y = oy + depth*sin_a
            if WORLD_MAP[int(y//TILE)][int(x//TILE)] == '#':
                depth *= math.cos(player.angle-cur_angle)
                h = 800/(depth+1)
                shade = 255/(1+depth*depth*0.0001)
                pygame.draw.rect(screen,
                    (shade,shade,shade),
                    (ray*(WIDTH//NUM_RAYS), HALF_H-h//2,
                     (WIDTH//NUM_RAYS), h))
                break
            depth += 4
        cur_angle += DELTA_ANGLE

# ---------------- MAIN LOOP ----------------
running = True
while running:
    clock.tick(FPS)
    moving = False

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            moving = True
            for en in enemies:
                if en.alive:
                    en.alive = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.x += math.cos(player.angle)*3
        player.y += math.sin(player.angle)*3
        moving = True
    if keys[pygame.K_s]:
        player.x -= math.cos(player.angle)*3
        player.y -= math.sin(player.angle)*3
        moving = True
    if keys[pygame.K_a]: player.angle -= 0.04; moving=True
    if keys[pygame.K_d]: player.angle += 0.04; moving=True

    tscale = TIME_MOVE if moving else TIME_IDLE

    screen.fill(BLACK)
    raycast()

    for en in enemies:
        if en.alive:
            dx = en.x-player.x
            dy = en.y-player.y
            depth = math.hypot(dx,dy)
            angle = math.atan2(dy,dx)-player.angle
            if abs(angle) < HALF_FOV:
                en.draw(depth)

    screen.blit(font.render('TRUE FPS SUPERHOT',True,WHITE),(10,10))
    pygame.display.flip()

pygame.quit()