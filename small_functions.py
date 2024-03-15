import random


def health_display(player, enemy):
    if player.health <= 0:
        player.health = 0
    if enemy.health <= 0:
        enemy.health = 0

    print("    ", end="")
    print(f"player [{pipes(player)}] {player.health}", end="")
    print("    ", end="")
    print(f"enemy [{pipes(enemy)}] {enemy.health}")


def pipes(character):
    health = character.health
    pipes = []
    for _ in range(int(health / 5)):
        pipes.append("|")
    return "".join(pipes)


def validate_number(variable, array):
    if variable.lower() == "quit":
        return "quit"
    elif not variable.isdigit():
        return False
    elif int(variable) not in array:
        return False
    else:
        return True


def move_option_display(moveset_dict, moves_available):
    moves_text = ["    |"]

    for move_number in moves_available:
        move_text = moveset_dict[move_number]["name"]
        moves_text.append(f" {move_number}: {move_text} |")

    moves_text = "".join(moves_text)
    return moves_text


def damage_calculator(player, enemy, player_move, enemy_move, moveset):
    # additive
    if moveset.moves_dict[player_move]["type"] == "additive":
        player.health += moveset.moves_dict[player_move]["user"]
        enemy.health += moveset.moves_dict[player_move]["opponent"]
    if moveset.moves_dict[enemy_move]["type"] == "additive":
        enemy.health += moveset.moves_dict[enemy_move]["user"]
        player.health += moveset.moves_dict[enemy_move]["opponent"]

    # multiplicative
    if moveset.moves_dict[player_move]["type"] == "multiplicative":
        player.health = player.health * moveset.moves_dict[player_move]["user"]
        enemy.health = enemy.health * moveset.moves_dict[player_move]["opponent"]
    if moveset.moves_dict[enemy_move]["type"] == "multiplicative":
        enemy.health = enemy.health * moveset.moves_dict[enemy_move]["user"]
        player.health = player.health * moveset.moves_dict[enemy_move]["opponent"]

    # divisive
    if moveset.moves_dict[player_move]["type"] == "divisive":
        player.health = int(player.health / moveset.moves_dict[player_move]["user"])
        enemy.health = int(enemy.health / moveset.moves_dict[player_move]["opponent"])
    if moveset.moves_dict[enemy_move]["type"] == "divisive":
        enemy.health = int(enemy.health / moveset.moves_dict[enemy_move]["user"])
        player.health = int(player.health / moveset.moves_dict[enemy_move]["opponent"])

    player_move_cooldown = moveset.moves_dict[player_move]["cooldown"]
    enemy_move_cooldown = moveset.moves_dict[enemy_move]["cooldown"]

    player.cooldowns[player_move] = player_move_cooldown + 1
    enemy.cooldowns[enemy_move] = enemy_move_cooldown + 1


def bot_move(enemy, moveset):
    damages = []
    moveset_dict = moveset.moves_dict
    enemy_moves_available = []

    for move, cooldown in enemy.cooldowns.items():
        if cooldown == 0:
            enemy_moves_available.append(move)

    # find max damage bot may receive
    for move in moveset.moves:
        if moveset_dict[move]["type"] == "additive":
            damages.append(moveset_dict[move]["opponent"])
    max_damage = min(
        damages
    )  # because negative numbers (-50 does more damage than -10)

    # if health high do whatever
    if enemy.health > abs(max_damage):
        return random.choice(enemy_moves_available)

    if enemy.health <= abs(max_damage):
        healing_moves = []
        for move in enemy_moves_available:
            if moveset_dict[move]["type"] == "additive":
                healing_to_bot = moveset_dict[move]["user"]

                if healing_to_bot > 0:
                    healing_moves += [move]

        if len(healing_moves) > 0:
            return random.choice(healing_moves)
        else:
            return random.choice(enemy_moves_available)


def moves_used_display(player_move, enemy_move, moveset_dict):
    player_move_text = moveset_dict[player_move]["name"]
    enemy_move_text = moveset_dict[enemy_move]["name"]

    print(f"    Player used {player_move_text}, Enemy used {enemy_move_text}")
