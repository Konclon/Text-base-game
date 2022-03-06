import random

# Gay jake

player = 100
enemy = 100
gameState = 0

# Move breakdown
print ("")
print ("Welcome to One Bar")
print ("Skill 1: Zap. Enemy -10")
print ("Skill 2: Lightning Strike. Player -10, Enemy -20")
print ("Skill 3: Heal Hacks. Player +15")
print ("")

# Opponent Bot
bot = input("Which bot would you like to face (1,2) ")
if bot != "1" and bot != "2":
    gameState = 1

while gameState == 0:

    # Health display

    if player <= 0:
        player = 0

    if enemy <= 0:
        enemy = 0

    print ("")
    print ("[",end="")

    playerDisplay = int(player/5)
    for i in range (playerDisplay):
        print ("|",end ="")

    print ("]",player,"     [",end="")

    enemyDisplay = int(enemy/5)
    for j in range (enemyDisplay):
        print ("|",end="")

    print ("]",enemy)
    print ("")

    if player <= 0 or enemy <= 0:
        break

    # AI Move
    if bot == "1":
        rng = random.randint(1,2)
        if enemy > 30:

            if rng == 1:
                enemyMove = 1

            elif rng == 2:
                enemyMove = 2

        elif enemy <= 30:

            if rng == 1:
                enemyMove = 1

            elif rng == 2:
                enemyMove = 3
    if bot == "2":
        print ("Bot 2 is in development.")
        # Add AI here

    # Player input
    playerMove = input("What skill would you like to use (1,2,3) ")
    
    if playerMove != "1" and playerMove != "2" and playerMove != "3":
        break

    # Move Calculator
    if enemyMove == 1:
        player -= 10

    elif enemyMove == 2:
        player -= 20
        enemy -= 10

    elif enemyMove == 3:
        enemy += 15

        if enemy > 100:
            enemy = 100

    if playerMove == "1":
        enemy -= 10

    elif playerMove == "2":
        enemy -= 20
        player -= 10

    elif playerMove == "3":
        player += 15

        if player > 100:
            player = 100

    # Move Display
    if playerMove == "1":
        playerMove = "Mini Zap"

    elif playerMove == "2":
        playerMove = "Lightning Strike"

    elif playerMove == "3":
        playerMove = "Heal Hacks"

    if enemyMove == 1:
        enemyMove = "Mini Zap"

    elif enemyMove == 2:
        enemyMove = "Lightning Strike"

    elif enemyMove == 3:
        enemyMove = "Heal Hacks"

    print ("")
    print ("Player used " + playerMove + ", enemy used " + enemyMove)

# End Screen

if player <= 0 and enemy > 0:
    print ("Eneny Wins")

elif enemy <= 0 and player > 0:
    print ("Player Wins")

elif enemy <= 0 and player <= 0:
    print ("Draw")

print ("")
