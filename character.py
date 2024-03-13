class make_character:
    def __init__(self,health,moves):
        self.health = health
        self.cooldowns = {move: 0 for move in moves}
