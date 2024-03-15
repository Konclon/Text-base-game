from character import make_character
from small_functions import (
    health_display,
    validate_number,
    move_option_display,
    bot_move,
    damage_calculator,
    moves_used_display,
)
import movesets


def main():
    # change this for different movesetss
    moveset = movesets.set2
    # change this for different movesetss

    # moveset_display
    moveset_dict = moveset.moves_dict
    print(f"    playing with '{moveset.name}'")

    player = make_character(moveset.player_health, moveset.moves)
    enemy = make_character(moveset.enemy_health, moveset.moves)

    # intro_text
    print(moveset.intro_text)  # already has newline front and back

    # input_option_bot_or_not_bot
    bot_or_player = input("    play with 1 - bot or 2 - player (1,2): ")

    gameRunning = True
    bot = False

    if (not validate_bot_or_player(bot_or_player)) or (
        validate_bot_or_player(bot_or_player) == "quit"
    ):
        print("\n    invalid input")
        gameRunning = False
    else:
        bot_or_player = int(bot_or_player)

        if bot_or_player == 1:
            bot = True
        elif bot_or_player == 2:
            bot = False
    print()

    while gameRunning:
        if player.health <= 0:
            player.health = 0
        if enemy.health <= 0:
            enemy.health = 0

        health_display(player, enemy)
        print()

        if (player.health == 0) or (enemy.health == 0):
            break

        player_moves_available = []
        for move, cooldown in player.cooldowns.items():
            if cooldown == 0:
                player_moves_available.append(move)

        print(move_option_display(moveset_dict, player_moves_available))

        player_move = input(
            f"    What skill would you like to use {player_moves_available}: "
        )
        print()

        if bot:
            validation_result = validate_number(player_move, player_moves_available)
            if validation_result == "quit":
                break
            elif not validation_result:
                print("    invalid move\n")
            elif validation_result:
                player_move = int(player_move)

                enemy_move = bot_move(enemy, moveset)
                damage_calculator(player, enemy, player_move, enemy_move, moveset)

                moves_used_display(player_move, enemy_move, moveset_dict)
                cooldown_reduce(player, enemy)
                print(enemy.cooldowns)
                print()

        if not bot:
            player_move = ""
            enemy_move = ""
            numbers_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

            if player_move.lower() == "quit":
                break

            elif len(player_move) != 2:
                print("    input should be two digits\n")

            # Validate input are numbers
            elif (not validate_number(player_move[0], numbers_arr)) or (
                not validate_number(player_move[1], numbers_arr)
            ):
                print("    input was not numbers")

            else:
                first_chr = int(player_move[0])
                second_chr = int(player_move[1])

                # assignment of player1_move and player2_move from player_move
                player1_move = player2_move = 0

                if first_chr <= 5:
                    player1_move = int(first_chr)
                    player2_move = int(second_chr) - 5
                elif first_chr > 5:
                    player1_move = int(second_chr)
                    player2_move = int(first_chr) - 5

                if player2_move == 0:
                    player2_move = 5

                # validate numbers are valid moves, eg move 5 does not exist
                validate_first = validate_number(
                    str(player1_move), player_moves_available
                )
                validate_second = validate_number(
                    str(player2_move), player_moves_available
                )

                if (not validate_first) or (not validate_second):
                    print("    numbers out of range")
                else:
                    damage_calculator(
                        player, enemy, player1_move, player2_move, moveset
                    )
                    moves_used_display(player1_move, player2_move, moveset_dict)
                    cooldown_reduce(player, enemy)
                    print()

    if gameRunning:
        if bot:
            if (enemy.health == 0) and (player.health == 0):
                print("    draw lmao")
            elif enemy.health == 0:
                print("    player win yay")
            elif player.health == 0:
                print("    player lost :(")
            print()

        if not bot:
            if (enemy.health == 0) and (player.health == 0):
                print("    draw lmao")
            elif enemy.health == 0:
                print("    player1 win yay")
            elif player.health == 0:
                print("    player2 win yay")
            print()


def validate_bot_or_player(bot_or_player):
    validation_result = validate_number(bot_or_player, [1, 2])
    if (not validation_result) or (validation_result == "quit"):
        return False
    else:
        return True


def cooldown_reduce(player, enemy):
    for move, cooldown in player.cooldowns.items():
        if cooldown > 0:
            player.cooldowns[move] += -1
    for move, cooldown in enemy.cooldowns.items():
        if cooldown > 0:
            enemy.cooldowns[move] += -1


if __name__ == "__main__":
    main()
