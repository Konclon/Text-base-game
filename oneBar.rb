player = 100
enemy = 100

# Move breakdown
puts ""
puts "Welcome to One Bar"
puts "Skill 1: Zap. Enemy -10"
puts "Skill 2: Lightning Strike. Player -10, Enemy -20"
puts "Skill 3: Heal Hacks. Player +15"

until player <= 0 || enemy <= 0

    # Health display
    puts ""
    print "["

    ((player/5).ceil).times do
        print "|"
    end
    print "] #{player}  ["
 
    ((enemy/5).ceil).times do
        print "|"
    end

    print "] #{enemy}"
    puts ""
    puts ""


    # AI Move
    rng = rand(1..2)
    if enemy > 30
        
        if rng == 1
            enemyMove = 1

        elsif rng == 2
            enemyMove = 2
        
        end 

    elsif enemy <= 30

        if rng == 1
            enemyMove = 1

        elsif rng == 2
            enemyMove = 3
        
        end
        
    end

    # Player input
    print "What skill would you like to use (1,2,3) "
    playerMove = gets.chomp

    if playerMove != "1" && playerMove != "2" && playerMove != "3"
        break
    end

    # Move Calculator

    if enemyMove == 1
        player -= 10

    elsif enemyMove == 2
        player -= 20
        enemy -= 10

    elsif enemyMove == 3
        enemy += 15
        
        if enemy > 100
            enemy = 100
        end
    end

    if playerMove == "1"
        enemy -= 10

    elsif playerMove == "2"
        enemy -= 20
        player -= 10

    elsif playerMove == "3"
        player += 15
        
        if player > 100
            player = 100
        end
    end    


    # Move Display
    if playerMove == "1"
        playerMove = "Mini Zap"

    elsif playerMove == "2"
        playerMove = "Lightning Strike"

    elsif playerMove == "3"
        playerMove = "Heal Hacks"
    
    end

    if enemyMove == 1
        enemyMove = "Mini Zap"

    elsif enemyMove == 2
        enemyMove = "Lightning Strike"

    elsif enemyMove == 3
        enemyMove = "Heal Hacks"
    
    end

    puts ""
    puts "Player used #{playerMove}, enemy used #{enemyMove}."
end

# End screen
puts ""
if player <= 0
    puts "Enemy Wins"

elsif enemy <= 0
    puts "Player Wins"

elsif player <= 0 && enemy <= 0
    puts "Draw"
end
