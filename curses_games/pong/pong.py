import curses
import time
import random


class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0

        self.score = 0

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def render(self, screen):
        y_range = range(int(self.y), int(self.y) + len(self.text_sprite))
        x_range = range(int(self.x), int(self.x) + len(self.text_sprite[0]))

        for y in y_range:
            for x in x_range:
                screen_height, screen_width = screen.getmaxyx()
                if 0 <= y < screen_height and 0 <= x < screen_width:
                    screen.addch(
                        int(y),
                        int(x),
                        self.text_sprite[y - int(self.y)][x - int(self.x)]
                        )

    def colliding(self, other):
        return self.x+len(self.text_sprite[0]) + self.x_vel > other.x and self.x + self.x_vel < other.x+len(other.text_sprite[0]) and \
               self.y+len(self.text_sprite) + self.y_vel > other.y and self.y + self.y_vel < other.y+len(other.text_sprite)

class Player(GameObject):
    text_sprite = [
        ['╗'],
        ['║'],
        ['║'],
        ['║'],
        ['║'],
        ['║'],
        ['\u255D'],
    ]

class Enemy(GameObject):
    text_sprite = [
        ['╔'],
        ['║'],
        ['║'],
        ['║'],
        ['║'],
        ['║'],
        ['╚'],
    ]

    def follow_ball(self, ball, difficulty=0.5):
        if ball.y > self.y + (len(self.text_sprite) // 2):
            self.y_vel = difficulty
        elif ball.y < self.y + (len(self.text_sprite) // 2):
            self.y_vel = -difficulty

class Ball(GameObject):
    text_sprite = [['⚽']]

    def __init__(self, *args):
        super().__init__(*args)
        self.reset()

    def reset(self):
        direction = random.choice([-1, 1])
        self.x_vel = (0.8 + (random.random() * 1.5)) * direction
        self.y_vel = (random.random() * 0.25) - 0.5

    def render(self, screen):
        screen_height, _ = screen.getmaxyx()
        if not 1 <= int(self.y) <= screen_height - 1:
            self.y_vel *= -1

        super().render(screen)

def print_title(screen, x, y):
    title = ''' _______  _______  _        _______
(  ____ )(  ___  )( (    /|(  ____ \\
| (    )|| (   ) ||  \  ( || (    \/
| (____)|| |   | ||   \ | || |
|  _____)| |   | || (\ \) || | ____
| (      | |   | || | \   || | \_  )
| )      | (___) || )  \  || (___) |
|/       (_______)|/    )_)(_______)'''

    lines = title.split('\n')
    for index, line in enumerate(lines):
        screen.addstr(y + index, x - (len(lines[0]) // 2), line)


def main_loop(screen):
    curses.curs_set(0)
    screen_height, screen_width = screen.getmaxyx()

    game_objects = list()
    game_objects.append(Player(2, 2))
    game_objects.append(Enemy(screen_width-3, 2))
    game_objects.append(Ball((screen_width  // 2) - 2, (screen_height // 2) - 2))

    screen.nodelay(1)
    while True:

        ball = game_objects[-1]
        player = game_objects[0]
        enemy = game_objects[1]

        if player.score < 5 and enemy.score < 5:
            screen.clear()
        else:
            screen.addch(
                random.randint(0, screen_height - 1),
                random.randint(0, screen_width - 1),
                chr(random.randint(96, 121))
                )

        print_title(screen, (screen_width // 2) - 2, 0)

        key_pressed = screen.getch()
        if key_pressed == curses.KEY_UP:
            player.y_vel = -3
        elif key_pressed == curses.KEY_DOWN:
            player.y_vel = 3
        else:
            player.y_vel = 0

        if ball.colliding(player) or ball.colliding(enemy):
            ball.x_vel *= -1.003


        if ball.x < 0:
            ball.reset()
            ball.x = (screen_width  // 2) - 2
            ball.y = (screen_height  // 2) - 2
            enemy.score += 1
        elif ball.x > screen_width - 1:
            ball.reset()
            ball.x = (screen_width  // 2) - 2
            ball.y = (screen_height  // 2) - 2
            player.score += 1

        enemy.follow_ball(ball)

        for game_object in game_objects:
            game_object.update()
            game_object.render(screen)


        screen.addstr(10, (screen_width // 2) - 15, f'Player: {player.score}')
        screen.addstr(10, (screen_width // 2) + 8, f'CPU: {enemy.score}')

        screen.refresh()
        time.sleep(0.04)

if __name__ == '__main__':
    try:
        curses.wrapper(main_loop)
    except KeyboardInterrupt:
        print("Thanks for playing! Sucka......")
