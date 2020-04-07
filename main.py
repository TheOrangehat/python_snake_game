from time import sleep
import pygame
import sys
import random


class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction

    def change_direction_to(self, direction):
        if direction == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if direction == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if direction == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if direction == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, food_position):
        if self.direction == "RIGHT":
            self.position[0] += 10
        if self.direction == "LEFT":
            self.position[0] -= 10
        if self.direction == "UP":
            self.position[1] -= 10
        if self.direction == "DOWN":
            self.position[1] += 10
        self.body.insert(0, list(self.position))
        if self.position == food_position:
            return 1
        else:
            self.body.pop()
            return 0

    def check_collision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1
        elif self.position[1] > 490 or self.position[1] < 0:
            return 1
        for body_part in self.body[1:]:
            if self.position == body_part:
                return 1
        return 0

    def get_head_pos(self):
        return self.position

    def get_body(self):
        return self.body


class FoodSpawner:
    def __init__(self):
        self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        self.is_food_on_screen = True

    def spawn_food(self):
        if not self.is_food_on_screen:
            self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
            self.is_food_on_screen = True
        return self.position

    def set_food_on_screen(self, b):
        self.is_food_on_screen = b


window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Wow Snake")
fps = pygame.time.Clock()

score = 0
snake = Snake()
food_spawner = FoodSpawner()


def game_over():
    sleep(2)
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction_to('RIGHT')
            if event.key == pygame.K_LEFT:
                snake.change_direction_to('LEFT')
            if event.key == pygame.K_UP:
                snake.change_direction_to('UP')
            if event.key == pygame.K_DOWN:
                snake.change_direction_to('DOWN')
    food_pos = food_spawner.spawn_food()
    if snake.move(food_pos) == 1:
        score += 1
        food_spawner.set_food_on_screen(False)

    window.fill(pygame.Color("black"))
    for pos in snake.get_body():
        pygame.draw.rect(window, pygame.Color("white"), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, pygame.Color("green"), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    if snake.check_collision() == 1:
        game_over()
    pygame.display.set_caption("Wow Snake | Score : " + str(score))
    pygame.display.flip()
    fps.tick(24)
