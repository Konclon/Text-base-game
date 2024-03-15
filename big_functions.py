from character import make_character
from small_functions import (
    pipes,
    validate_number,
    bot_move,
    damage_calculator,
    moves_used_display,
)


def moveset_display(moveset):
    return f"    playing with'{moveset.name}"


def validate_bot_or_player(bot_or_player):
    validation_result = validate_number(bot_or_player, [1, 2])
    if (not validation_result) or (validation_result == "quit"):
        return False
    else:
        return True


def health_display(player, enemy):
    if player.health <= 0:
        player.health = 0
    if enemy.health <= 0:
        enemy.health = 0

    return f"    player [{pipes(player)}] {player.health}    enemy [{pipes(enemy)}] {enemy.health}"


def player_move_option_display(moveset_dict, player):
    player_moves_available = []
    for move, cooldown in player.cooldowns.items():
        if cooldown == 0:
            player_moves_available.append(move)

    moves_text = ["    |"]

    for move_number in player_moves_available:
        move_text = moveset_dict[move_number]["name"]
        moves_text.append(f" {move_number}: {move_text} |")

    moves_text = "".join(moves_text)
    return moves_text
