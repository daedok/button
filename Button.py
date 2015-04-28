import pygame
from pygame.locals import *

import sys

class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.bg_color = (0, 0, 0)
        self.bd_color = (63, 63, 191)
        self.selected_color = (63, 191, 63)

        self.border_selected = False
        self.full_selected = False

        self.handler_function = None
        self.handler_function = self.printMsg

        self.caption = ""
        self.caption_font = pygame.font.Font("fonts/Europe Normal.ttf", 20)

    def setFullSelect(self, bool_flag):
        self.full_selected = bool_flag

    def setBorderSelect(self, bool_flag):
        self.border_selected = bool_flag

    def printMsg(self):
        print(self)

    def leftMouseClick(self):
        if not self.full_selected:
            self.handler_function()
        self.setFullSelect(True)

    def render(self, surface):
        button_surface = pygame.Surface((self.width, self.height))
        button_surface.fill(self.bg_color)
        if self.full_selected is True:
            button_surface.fill(self.selected_color)
            self.border_selected = False
        if self.border_selected is True:
            button_surface.fill(self.bd_color, (1, 1, self.width - 2, self.height - 2))
            button_surface.fill(self.bg_color, (5, 5, self.width - 10, self.height - 10))
        if self.caption != "":
            caption_surface = self.caption_font.render(self.caption, True, (255, 255, 255))
            w, h = caption_surface.get_size()
            button_surface.blit(caption_surface, (self.width / 2 - w / 2, self.height / 2 - h / 2))
        surface.blit(button_surface, (self.x, self.y))

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480), 0, 32)
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()

    button_0 = Button(10, 10, 200, 50)
    button_1 = Button(10, 70, 200, 50)
    button_2 = Button(10, 130, 200, 50)
    button_3 = Button(10, 190, 200, 50)

    button_0.caption = "New game"
    button_1.caption = "Load game"
    button_2.caption = "Options"
    button_3.caption = "Exit"

    buttons = [button_0, button_1, button_2, button_3]

    fps_counter = 0;
    fps_timer = 1000;
    while(True):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        fps_counter += 1
        fps_timer -= clock.tick(60)
        if fps_timer <= 0:
            print("FPS: " + str(fps_counter))
            fps_timer = 1000
            fps_counter = 0

        x, y = pygame.mouse.get_pos()
        left_mouse_button = pygame.mouse.get_pressed()[0]
        right_mouse_button = pygame.mouse.get_pressed()[2]
        
        current_button = None
        for button in buttons:
            if x >= button.x and x < (button.x + button.width):
                if y >= button.y and y < (button.y + button.height):
                    button.setBorderSelect(True)
                    current_button = button
                    continue;
            button.setBorderSelect(False)
        
        if left_mouse_button:
            for button in buttons:
                if button == current_button:
                    button.leftMouseClick()
                    continue
                button.setFullSelect(False)
        if right_mouse_button:
            if current_button in buttons:
                current_button.setFullSelect(False)


        for button in buttons:
            button.render(screen)
                
        pygame.display.update()
        
