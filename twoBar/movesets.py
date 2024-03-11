# where [add to caster, add to opponent, name of skill]
set1_intro_text = """
    Welcome to One Bar
    Skill 1: Zap. Enemy -10
    Skill 2: Lightning Strike. Player -10, Enemy -20
    Skill 3: Heal Hacks. Player +15
"""

set1 = {
    "name":"set1",
    "moves":[1,2,3],
    "player_health":100,
    "enemy_health":100,
    "intro_text": set1_intro_text,
    1:[0,-10,"Zap","additive"],
    2:[-10,-20,"Lightning Strike","additive"],
    3:[15,0,"Heal Hacks","additive"],
}

set2_intro_text = """
    Welcome to One Bar
    Skill 1: Small jab, takes 30 damage off your opponent
    Skill 2: Big die. Wanna go the kaboom?? Takes damage off both people
    Skill 3: Life steal, healing but better
    Skill 4: cutInHalf, cuts both healthbar in half
"""

set2 = {
    "name":"set2",
    "moves":[1,2,3,4],
    "player_health":200,
    "enemy_health":200,
    "intro_text": set2_intro_text,
    1:[0,-40,"Small jab","additive"],
    2:[-50,-80,"Big die","additive"],
    3:[35,-10,"Life steal","additive"],
    4:[2,2,"cutInHalf","divisive"]
}
