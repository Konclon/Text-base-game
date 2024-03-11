import random

def health_display(player,enemy):
    if player.health <= 0: player.health = 0
    if enemy.health <= 0: enemy.health = 0

    print("    ",end="")
    print(f"player [{pipes(player)}] {player.health}",end="")
    print("    ",end="")
    print(f"enemy [{pipes(enemy)}] {enemy.health}")

def pipes(character):
    health = character.health
    pipes = []
    for i in range (int(health/5)):
        pipes.append("|")
    return "".join(pipes)

def validate_number(variable,array):
    if variable.lower() == "quit":
        return "quit"
    elif variable.isdigit() == False:
        return False
    elif (int(variable) not in array):
        return False
    else:
        return True

def damage_calculator(player, enemy, player_move, enemy_move, moveset):
    # additive
    if moveset[player_move][3] == "additive":
        player.health += moveset[player_move][0]
        enemy.health += moveset[player_move][1]
    if moveset[enemy_move][3] == "additive":
        enemy.health += moveset[enemy_move][0]
        player.health += moveset[enemy_move][1]

    # multiplicative
    if moveset[player_move][3] == "multiplicative":
        player.health = player.health * moveset[player_move][0]
        enemy.health = enemy.health * moveset[player_move][1]
    if moveset[enemy_move][3] == "multiplicative":
        enemy.health = enemy.health * moveset[enemy_move][0]
        player.health = player.health * moveset[enemy_move][1]

    # divisive
    if moveset[player_move][3] == "divisive":
        player.health = int(player.health / moveset[player_move][0])
        enemy.health = int(enemy.health / moveset[player_move][1])
    if moveset[enemy_move][3] == "divisive":
        enemy.health = int(enemy.health / moveset[enemy_move][0])
        player.health = int(player.health / moveset[enemy_move][1])

def bot_move(enemy_bot,enemy,moveset_dict):
    if enemy_bot == 1:
        if enemy.health > 30:
            enemyMove = random.choice([1,2])
        if enemy.health <= 30:
            enemyMove = random.choice([1,3])
        return enemyMove

    if enemy_bot == 2: # main bot, avoids health < highest damaging move
        damages = []
        for move in moveset_dict["moves"]:
            damages += [moveset_dict[move][1]]
        max_damage = min(damages)

        if enemy.health > abs(max_damage):
            return random.choice(moveset_dict["moves"])

        if enemy.health <= abs(max_damage):
            healing_moves = []

            for move in moveset_dict["moves"]:
                healing_to_bot = moveset_dict[move][0]

                if healing_to_bot > 0:
                    healing_moves += [move]

            return random.choice(healing_moves)

def move_display(player_move, enemy_move, moveset):
    player_move_text = moveset[player_move][2]
    enemy_move_text = moveset[enemy_move][2]

    print(f"    Player used {player_move_text}, Enemy used {enemy_move_text}")


