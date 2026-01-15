from pygame import *
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSER', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))
background = (200, 255, 255)
win_height = 500
win_width = 600
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

window = display.set_mode((win_width, win_height))
rocket_1 = Player('rocket.png', 30, 200, 4, 50, 150)
rocket_2 = Player('rocket.png', 520, 200, 4, 50, 150)
ball = GameSprite('b.png', 200, 200, 4, 50, 50)
clock = time.Clock()
Ping = 60
game = True
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        rocket_1.update_r()
        rocket_2.update_l()
        rocket_1.reset()
        rocket_2.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.reset()
        if sprite.collide_rect(rocket_1, ball) or sprite.collide_rect(rocket_2, ball):
            speed_x *= -1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
        display.update()
        clock.tick(Ping)