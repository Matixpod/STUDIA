import pygame.font

class Button():
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg,True,self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class EasyButton(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.button_color = (0, 255, 0)
        self.rect = pygame.Rect(1180, 800, self.width, self.height)
        self.msg_image_rect.center = self.rect.center

class MediumButton(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.button_color = (153, 255, 255)
        self.rect = pygame.Rect(1180, 870, self.width, self.height)
        self.msg_image_rect.center = self.rect.center

class HardButton(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.button_color = (255, 0, 0)
        self.rect = pygame.Rect(1180, 940, self.width, self.height)
        self.msg_image_rect.center = self.rect.center

class ExitButton(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.button_color = (230, 0, 0)
        self.rect = pygame.Rect(1180, 1040, self.width, self.height)
        self.msg_image_rect.center = self.rect.center