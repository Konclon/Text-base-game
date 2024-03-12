class Moveset:
    def __init__(self, name, moves, player_health, enemy_health, intro_text, moves_dict):
        self.name = name
        self.moves = moves
        self.player_health = player_health
        self.enemy_health = enemy_health
        self.intro_text = intro_text
        self.moves_dict = moves_dict

    def get_move(self, move_number):
        return self.moves_dict.get(move_number)

# Define movesets
set1_intro_text = """
    Welcome to One Bar
    Skill 1: Zap. Enemy -10
    Skill 2: Lightning Strike. Player -10, Enemy -20
    Skill 3: Heal Hacks. Player +15
"""
set1_moves_dict = {
    1: {"user": 0, "opponent": -10, "type": "additive", "name": "Zap"},
    2: {"user": -10, "opponent": -20, "type": "additive", "name": "Lightning"},
    3: {"user": 15, "opponent": 0, "type": "additive", "name": "Heal Hacks"},
}
set1 = Moveset("set1", [1, 2, 3], 100, 100, set1_intro_text, set1_moves_dict)

set2_intro_text = """
    Welcome to One Bar
    Skill 1: Small jab, takes 30 damage off your opponent
    Skill 2: Big die. Wanna go the kaboom?? Takes damage off both people
    Skill 3: Life steal, healing but better
    Skill 4: cutInHalf, cuts both healthbars in half
"""
set2_moves_dict = {
    1: {"user": 0, "opponent": -35, "type": "additive", "name": "Small jab"},
    2: {"user": -50, "opponent": -90, "type": "additive", "name": "Big die"},
    3: {"user": 15, "opponent": -10, "type": "additive", "name": "Life steal"},
    4: {"user": 2, "opponent": 2, "type": "divisive", "name": "cutInHalf"},
}
set2 = Moveset("set2", [1, 2, 3, 4], 200, 200, set2_intro_text, set2_moves_dict)
# balance change v0.1
