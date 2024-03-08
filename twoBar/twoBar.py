from character import make_character
from functions import health_display, damage_calculator

def main():
    player = make_character(100)
    enemy = make_character(100)
    gameRunning = True

    print ( """
    Welcome to One Bar
    Skill 1: Zap. Enemy -10
    Skill 2: Lightning Strike. Player -10, Enemy -20
    Skill 3: Heal Hacks. Player +15
    """ )

    enemy_bot = int(input("    Which bot would you like to face (1 or 1): "))
    print()
    if enemy_bot != 1 : gameRunning = False

    while gameRunning == True:
        if player.health <= 0: player.health = 0
        if enemy.health <= 0: enemy.health = 0
        health_display(player,enemy)
        print()

        if (player.health == 0) or (enemy.health == 0): break

        player_move = int(input("    What skill would you like to use (1,2,3): "))
        print()
        if (player_move in [1,2,3]) == False:
            print("invalid move\n")
        else:
            damage_calculator(player,enemy,player_move,enemy_bot)

if __name__ == "__main__":
    main()
