from character import make_character
from functions import *
import movesets

def main():
    moveset_dict = movesets.set2
    moveset_name = moveset_dict["name"]
    print(f"    playing with '{moveset_name}'")

    player = make_character(moveset_dict["player_health"])
    enemy = make_character(moveset_dict["enemy_health"])

    print(moveset_dict["intro_text"]) # already has newline front and back

    bot_or_player = input("    play with 1 - bot or 2 - player (1,2): ")

    gameRunning = True
    if validate_bot_or_player(bot_or_player) == False:
        print("\n    invalid input")
        gameRunning = False
    else:
        bot_or_player = int(bot_or_player)

        if bot_or_player == 1:
            bot = True
            enemy_bot = 2
        elif bot_or_player == 2:
            bot = False

    print()

    while gameRunning == True:

        if player.health <= 0: player.health = 0
        if enemy.health <= 0: enemy.health = 0

        health_display(player,enemy)
        print()

        if (player.health == 0) or (enemy.health == 0): break

        moves_available = moveset_dict["moves"]
        player_move = input(f"    What skill would you like to use {moves_available}: ")
        print()

        if bot == True:
            validation_result = validate_number(player_move,moveset_dict["moves"])
            if validation_result == "quit":
                break
            elif validation_result == False:
                print("    invalid move\n")
            elif validation_result == True:
                player_move = int(player_move)

                enemy_move = bot_move(enemy_bot,enemy,moveset_dict)
                damage_calculator(player, enemy, player_move, enemy_move, moveset_dict)

                move_display(player_move, enemy_move, moveset_dict)
                print()

        if bot == False:
            numbers_arr = [1,2,3,4,5,6,7,8,9,0]

            if player_move.lower() == "quit":
                break

            elif len(player_move) != 2:
                print("    input should be two digits\n")

            # Validate input are numbers
            elif (validate_number(player_move[0],numbers_arr) == False) or (validate_nmuber(player_move[1],number_arr) == False):
                print("    input was not numbers")

            else:
                first_chr = int(player_move[0])
                second_chr = int(player_move[1])

                # assignment of player1_move and player2_move from player_move
                if first_chr <= 5:
                    player1_move = int(first_chr)
                    player2_move = int(second_chr) - 5
                elif first_chr > 5:
                    player1_move = int(second_chr)
                    player2_move = int(first_chr) - 5

                if player2_move == 0: player2_move = 5

                # validate numbers are valid moves, eg move 5 does not exist
                validate_first = validate_number(str(player1_move), moveset_dict["moves"])
                validate_second = validate_number(str(player2_move), moveset_dict["moves"])

                if (validate_first == False) or (validate_second == False):
                    print("    numbers out of range")
                else:
                    damage_calculator(player, enemy, player1_move, player2_move, moveset_dict)
                    move_display(player1_move, player2_move, moveset_dict)
                    print()

    if bot == True:
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
    validation_result = validate_number(bot_or_player,[1,2])
    if (validation_result == False) or (validation_result == "quit"):
        return False
    else:
        return True

if __name__ == "__main__":
    main()
