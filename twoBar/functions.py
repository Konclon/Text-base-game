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

def damage_calculator(player, enemy, player_move, enemy_bot):
    match player_move:
        case 1:
            enemy.health -= 10
        case 2:
            enemy.health -= 20
            player.health -= 10
        case 3:
            player.health += 15

    match enemy_bot:
        case 1:
            enemy_move = bot1(enemy)

    match enemy_move:
        case 1:
            player.health -= 10
        case 2:
            player.health -= 20
            enemy.health -= 10
        case 3:
            enemy.health += 15

def bot1(enemy):
    if enemy.health > 30:
        enemyMove = random.choice([1,2])
    else:
        enemyMove = random.choice([1,3])
    return enemyMove
