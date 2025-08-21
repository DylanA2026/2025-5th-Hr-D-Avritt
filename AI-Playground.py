import math
import sys
import random
import pygame

"""
Getting Over It — tiny Python/Pygame prototype
------------------------------------------------
Single-file, no assets. Tested with pygame 2.x.

Controls
- Move mouse to aim the hammer.
- Left mouse (hold): hook hammer if tip touches geometry; pull yourself toward it.
- Right mouse (tap): push — quick impulse away from hammer tip.
- Mouse wheel: change hammer length.
- R: restart
- Esc: quit

Goal
- Climb to the flag at the top. If you fall below the bottom, you respawn.

Notes
- This is a simplified homage, not a 1:1 clone. Physics are arcade-y on purpose.
"""

# ----------------------- helpers -----------------------
Vec = pygame.math.Vector2

SCREEN_W, SCREEN_H = 1000, 700
FPS = 120
GRAVITY = 2400.0  # px/s^2
GROUND_FRICTION = 0.90
AIR_DRAG = 0.999

PLAYER_RADIUS = 26
PLAYER_BOUNCE = 0.0

HAMMER_MIN = 60
HAMMER_MAX = 240
HAMMER_LEN_DEFAULT = 140
HAMMER_PULL_STRENGTH = 2800.0
HAMMER_PUSH_IMPULSE = 900.0
HAMMER_TIP_RADIUS = 8

CAM_LERP = 0.08

WHITE = (240, 240, 240)
BLACK = (12, 12, 12)
GREY = (70, 70, 80)
BLUE = (85, 140, 255)
ORANGE = (255, 160, 70)
GREEN = (70, 220, 120)
RED = (230, 70, 70)
YELLOW = (255, 220, 85)


# ----------------------- world generation -----------------------

def make_tower(seed=1):
    random.seed(seed)
    platforms = []  # each as pygame.Rect in world coords

    # Ground shelf
    platforms.append(pygame.Rect(-800, 200, 2000, 80))

    # A rising, wonky tower of blocks
    x = 0
    y = 120
    for i in range(35):
        w = random.randint(140, 280)
        h = random.randint(30, 60)
        x += random.randint(-120, 120)
        y -= random.randint(60, 140)
        platforms.append(pygame.Rect(x, y, w, h))

        # occasional narrow ledges or tall posts
        if random.random() < 0.35:
            w2 = random.randint(40, 80)
            h2 = random.randint(120, 220)
            px = x + random.randint(-100, 100)
            py = y - h2
            platforms.append(pygame.Rect(px, py, w2, h2))

    # Final goal platform
    top_y = min(r.top for r in platforms)
    goal_rect = pygame.Rect(-120, top_y - 220, 240, 30)
    platforms.append(goal_rect)
    flag_pole = pygame.Rect(goal_rect.centerx - 4, goal_rect.top - 160, 8, 160)
    platforms.append(flag_pole)

    return platforms, goal_rect, flag_pole


# ----------------------- collision -----------------------

def circle_rect_penetration(circle_center: Vec, radius: float, rect: pygame.Rect):
    """Return penetration vector to separate circle from rect, or None if no overlap.
    Uses closest-point-on-rect method.
    """
    cx, cy = circle_center.x, circle_center.y
    rx, ry, rw, rh = rect
    # closest point on rect to circle center
    closest_x = max(rx, min(cx, rx + rw))
    closest_y = max(ry, min(cy, ry + rh))
    diff = Vec(cx - closest_x, cy - closest_y)
    dist_sq = diff.length_squared()
    if dist_sq >= radius * radius:
        return None
    dist = math.sqrt(dist_sq) if dist_sq > 0 else 0.0
    if dist == 0:
        # center is exactly on a corner or inside; choose axis of least penetration
        # push out toward the smallest overlap edge
        left = cx - rx
        right = (rx + rw) - cx
        top = cy - ry
        bottom = (ry + rh) - cy
        min_overlap = min(left, right, top, bottom)
        if min_overlap == left:
            return Vec(-(radius - left), 0)
        if min_overlap == right:
            return Vec((radius - right), 0)
        if min_overlap == top:
            return Vec(0, -(radius - top))
        return Vec(0, (radius - bottom))
    # push out by (radius - dist) along normal
    n = diff / dist
    return n * (radius - dist)


# ----------------------- game objects -----------------------

class Player:
    def __init__(self, pos: Vec):
        self.pos = Vec(pos)
        self.vel = Vec(0, 0)
        self.radius = PLAYER_RADIUS
        self.hammer_len = HAMMER_LEN_DEFAULT
        self.hook_point = None  # world coords Vec
        self.on_ground = False

    def update(self, dt, solids, inputs, camera):
        # apply gravity
        self.vel.y += GRAVITY * dt

        # pull toward hook if active and mouse held
        if self.hook_point and inputs['lmb']:
            to_hook = (self.hook_point - self.pos)
            dist = to_hook.length()
            if dist > 1e-4:
                dirn = to_hook / dist
                pull = dirn * HAMMER_PULL_STRENGTH * dt
                self.vel += pull
        else:
            # decay hook if not held
            self.hook_point = None

        # air drag
        self.vel *= AIR_DRAG

        # integrate position
        self.pos += self.vel * dt

        # collisions with rectangles
        self.on_ground = False
        for r in solids:
            pen = circle_rect_penetration(self.pos, self.radius, r)
            if pen is not None:
                self.pos += pen
                # reflect/cancel velocity along penetration normal axis
                if abs(pen.x) > 0:
                    self.vel.x *= -PLAYER_BOUNCE
                if abs(pen.y) > 0:
                    if self.vel.y > 0 and pen.y < 0:
                        self.on_ground = True
                    self.vel.y *= -PLAYER_BOUNCE

        # friction if on ground
        if self.on_ground:
            self.vel.x *= GROUND_FRICTION

        # hammer length adjust
        scroll = inputs['wheel']
        if scroll != 0:
            self.hammer_len = max(HAMMER_MIN, min(HAMMER_MAX, self.hammer_len + scroll * 8))

        # compute hammer tip & try hooking
        mouse_world = inputs['mouse_world']
        aim = (mouse_world - self.pos)
        if aim.length_squared() < 1e-6:
            aim = Vec(1, 0)
        else:
            aim = aim.normalize()
        tip = self.pos + aim * self.hammer_len

        if inputs['lmb']:
            # If tip overlaps any solid, attach hook (stick to the first)
            for r in solids:
                if circle_rect_penetration(tip, HAMMER_TIP_RADIUS, r):
                    self.hook_point = closest_point_on_rect(tip, r)
                    break

        # right click = push impulse
        if inputs['rmb_clicked']:
            # push away from tip toward player (i.e., shove the world)
            out = (self.pos - tip)
            if out.length_squared() > 1e-6:
                out.scale_to_length(HAMMER_PUSH_IMPULSE)
                self.vel += out / 60.0  # modest impulse

        return tip


def closest_point_on_rect(p: Vec, r: pygame.Rect) -> Vec:
    x = max(r.left, min(p.x, r.right))
    y = max(r.top, min(p.y, r.bottom))
    return Vec(x, y)


# ----------------------- camera -----------------------

class Camera:
    def __init__(self, target: Player):
        self.pos = Vec(target.pos.x - SCREEN_W * 0.5, target.pos.y - SCREEN_H * 0.6)

    def update(self, target: Player):
        desired = Vec(target.pos.x - SCREEN_W * 0.5, target.pos.y - SCREEN_H * 0.6)
        self.pos += (desired - self.pos) * CAM_LERP

    def world_to_screen(self, p: Vec) -> Vec:
        return p - self.pos

    def screen_to_world(self, p: Vec) -> Vec:
        return p + self.pos


# ----------------------- rendering -----------------------

def draw_world(surf, camera: Camera, solids, goal_rect, flag_pole, player: Player, hammer_tip: Vec):
    surf.fill((22, 24, 34))

    # decorative gradient sky bands
    for i, y in enumerate(range(-2000, 2000, 200)):
        rect = pygame.Rect(-5000, y, 10000, 200)
        screen_pos = camera.world_to_screen(Vec(rect.x, rect.y))
        sky_rect = pygame.Rect(int(screen_pos.x), int(screen_pos.y), rect.w, rect.h)

        pygame.draw.rect(
            surf,
            (28 + i % 2 * 8, 30 + i % 2 * 6, 40 + i % 3 * 5),
            sky_rect
        )

    # platforms
    for r in solids:
        rs = pygame.Rect(camera.world_to_screen(Vec(r.x, r.y)).x, camera.world_to_screen(Vec(r.x, r.y)).y, r.w, r.h)
        pygame.draw.rect(surf, GREY, rs, border_radius=6)
        pygame.draw.rect(surf, (120, 120, 140), rs, width=2, border_radius=6)

    # goal flag
    gr = pygame.Rect(camera.world_to_screen(Vec(goal_rect.x, goal_rect.y)).x,
                     camera.world_to_screen(Vec(goal_rect.x, goal_rect.y)).y, goal_rect.w, goal_rect.h)
    pr = pygame.Rect(camera.world_to_screen(Vec(flag_pole.x, flag_pole.y)).x,
                     camera.world_to_screen(Vec(flag_pole.x, flag_pole.y)).y, flag_pole.w, flag_pole.h)
    pygame.draw.rect(surf, (90, 90, 100), pr)
    pygame.draw.rect(surf, (160, 160, 170), gr)
    # little flag triangle
    pole_top = Vec(pr.centerx, pr.top)
    flag_pts = [
        (pole_top.x, pole_top.y + 6),
        (pole_top.x + 46, pole_top.y + 16),
        (pole_top.x, pole_top.y + 26),
    ]
    pygame.draw.polygon(surf, YELLOW, flag_pts)

    # player (cauldron-ish circle)
    pc = camera.world_to_screen(player.pos)
    pygame.draw.circle(surf, BLUE, (int(pc.x), int(pc.y)), player.radius)
    pygame.draw.circle(surf, WHITE, (int(pc.x), int(pc.y)), player.radius, 2)

    # hammer
    tip_screen = camera.world_to_screen(hammer_tip)
    pygame.draw.line(surf, ORANGE, (int(pc.x), int(pc.y)), (int(tip_screen.x), int(tip_screen.y)), 5)
    pygame.draw.circle(surf, ORANGE, (int(tip_screen.x), int(tip_screen.y)), HAMMER_TIP_RADIUS)
    pygame.draw.circle(surf, WHITE, (int(tip_screen.x), int(tip_screen.y)), HAMMER_TIP_RADIUS, 1)

    # hook link (if latched)
    if player.hook_point:
        hook_screen = camera.world_to_screen(player.hook_point)
        pygame.draw.line(surf, (255, 200, 140), (int(pc.x), int(pc.y)), (int(hook_screen.x), int(hook_screen.y)), 2)
        pygame.draw.circle(surf, (255, 220, 160), (int(hook_screen.x), int(hook_screen.y)), 5)


# ----------------------- ui -----------------------

def draw_hud(surf, player: Player, elapsed_s: float, won: bool):
    font = pygame.font.SysFont("consolas", 20)
    text = f"Hammer {int(player.hammer_len)} | Height {-int(player.pos.y)} | Time {elapsed_s:5.1f}s"
    img = font.render(text, True, WHITE)
    surf.blit(img, (14, 12))

    if won:
        big = pygame.font.SysFont("consolas", 44, bold=True)
        msg = big.render("You reached the top! Press R to play again.", True, GREEN)
        surf.blit(msg, (SCREEN_W / 2 - msg.get_width() / 2, 60))


# ----------------------- main -----------------------

def run():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Getting Over It — tiny pygame prototype")
    clock = pygame.time.Clock()

    # world
    solids, goal_rect, flag_pole = make_tower(seed=7)

    player = Player(Vec(0, -40))
    camera = Camera(player)

    elapsed = 0.0
    won = False

    def reset():
        nonlocal solids, goal_rect, flag_pole, player, camera, elapsed, won
        solids, goal_rect, flag_pole = make_tower(seed=random.randint(1, 99999))
        player = Player(Vec(0, -40))
        camera = Camera(player)
        elapsed = 0.0
        won = False

    while True:
        dt = clock.tick(FPS) / 1000.0
        elapsed += dt

        # input
        wheel_delta = 0
        lmb = False
        rmb_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
                if event.key == pygame.K_r:
                    reset()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    lmb = True
                elif event.button == 3:
                    rmb_clicked = True
                elif event.button == 4:
                    wheel_delta = 1
                elif event.button == 5:
                    wheel_delta = -1

        pressed = pygame.mouse.get_pressed(3)
        lmb |= pressed[0]

        mouse_screen = Vec(pygame.mouse.get_pos())
        mouse_world = camera.screen_to_world(mouse_screen)

        inputs = {
            'wheel': wheel_delta,
            'lmb': lmb,
            'rmb_clicked': rmb_clicked,
            'mouse_world': mouse_world,
        }

        # update
        tip = player.update(dt, solids, inputs, camera)
        camera.update(player)

        # boundaries / fail state
        if player.pos.y > 1200:
            # fell too far — reset to ground
            player.pos = Vec(0, -40)
            player.vel = Vec(0, 0)
            player.hook_point = None

        # win check
        if player.pos.y < (goal_rect.top - 160) and abs(player.pos.x - goal_rect.centerx) < 200:
            won = True

        # draw
        draw_world(screen, camera, solids, goal_rect, flag_pole, player, tip)
        draw_hud(screen, player, elapsed, won)
        pygame.display.flip()


if __name__ == "__main__":
    run()
