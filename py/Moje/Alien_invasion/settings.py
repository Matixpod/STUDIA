class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_limit = 2
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        self.fleet_drop_speed = 100
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50
        self.score_scale = 1.5


    def increse_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def easy_gamemode(self):
        self.speedup_scale = 1.1
        self.alien_points = 50
        self.score_scale = 1.5
        print("easy game mode set")
    
    def medium_gamemode(self):
        self.speedup_scale = 1.2
        self.alien_points = 60
        self.score_scale = 1.6
        print("medium game mode set")

    def hard_gamemode(self):
        self.speedup_scale = 1.3
        self.alien_points = 70
        self.score_scale = 1.7
        print("hard game mode set")
    
    
