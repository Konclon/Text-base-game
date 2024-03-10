from character import make_character
from functions import *
import movesets

def main():
    moveset_dict = movesets.set1
    moveset_name = moveset_dict["name"]
    print(f"    playing with '{moveset_name}'")

    player = make_character(100)
    enemy = make_character(100)
    gameRunning = True

    print ( """
    Welcome to One Bar
    Skill 1: Zap. Enemy -10
    Skill 2: Lightning Strike. Player -10, Enemy -20
    Skill 3: Heal Hacks. Player +15
    """ )

    enemy_bot = input("    Which bot would you like to face (1 or 1): ")
    validation_result = validate_number(enemy_bot,[1])
    if (validation_result == False) or (validation_result == "quit") :
        print("\n    invalid input")
        gameRunning = False
    else:
        enemy_bot = int(enemy_bot)

    print()

    while gameRunning == True:

        if player.health <= 0: player.health = 0
        if enemy.health <= 0: enemy.health = 0

        health_display(player,enemy)
        print()

        if (player.health == 0) or (enemy.health == 0): break

        player_move = input("    What skill would you like to use (1,2,3): ")
        print()
        
        validation_result = validate_number(player_move,moveset_dict["moves"])
        if validation_result == "quit":
            break
        elif validation_result == False:
            print("    invalid move\n")
        elif validation_result == True:
            player_move = int(player_move)

            enemy_move = bot_move(enemy_bot,enemy)
            damage_calculator(player, enemy, player_move, enemy_move, moveset_dict)

            move_display(player_move, enemy_move, moveset_dict)
            print()
    
    if (enemy.health == 0) and (player.health == 0):
        print("    draw lmao")
    elif enemy.health == 0:
        print("    player win yay")
    elif player.health == 0:
        print("    player lost :(")
    print()

if __name__ == "__main__":
    main()
