#This is my code for tic tac toe
#the title card, says "tic tac toe"
X = 0
#LOOP forever
while X == 0:
#display title card    
    print("        ,----,                            ,----,                                ,----,                   \n      ,/   .`|                          ,/   .`|                              ,/   .`|                   \n    ,`   .'  :                        ,`   .'  :                            ,`   .'  :                   \n  ;    ;     / ,--,   ,--.          ;    ;     /            ,--.          ;    ;     /                   \n.'___,/    ,',--.'|  /  /|        .'___,/    ,'            /  /|        .'___,/    ,'  ,---.             \n|    :     | |  |,  '  / '        |    :     |            '  / '        |    :     |  '   ,'\            \n;    |.';  ; `--'_ /  / /         ;    |.';  ;  ,--.--.  /  / /         ;    |.';  ; /   /   |   ,---.   \n`----'  |  | ,' ,'/  / ,          `----'  |  | /       \/  / ,          `----'  |  |.   ; ,. :  /     \  \n    '   :  ; '  | \ '\ \              '   :  ;.--.  .-. \ '\ \              '   :  ;'   | |: : /    / '  \n    |   |  ' |  | :\  \ '             |   |  ' \__\/: . .\  \ '             |   |  ''   | .; :.    ' /   \n    '   :  | '  : |_\  . |            '   :  | ,' .--.; | \  . |            '   :  ||   :    |'   ; :__  \n    ;   |.'  |  | '.'\__\.            ;   |.' /  /  ,.  |  \__\.            ;   |.'  \   \  / '   | '.'| \n    '---'    ;  :    ;                '---'  ;  :   .'   \                  '---'     `----'  |   :    : \n             |  ,   /                        |  ,     .-./                                     \   \  /  \n              ---`-'                          `--`---'                                          `----'   \n                                                              ")
    print("="*105)
    print("                                          MAIN MENU")
    print("="*105)

#    Display:
#        Starts Game
    print("1. Start Playing!\n")
#         Displays Instructions    
    print("2. Disply rules\n")
#         Exits program
    print("3. Leave game\n")
    
#    Ask user for a choice
    X = int(input("Choose a number 1-3!: "))
    
    print("")

    print("="*105)
#    IF choice is 1
#        Exit menu and start game
    if X == 1:
        print("")
        print("_"*40)
        print("              GAME START!!!")
        print("‾"*40)

#        Creates 9 board spaces (b1 to b9) & Sets each space to empty
        b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = " "

        used = " "

        while True:
            game_over = False
            
            b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = " "
            used = " "        

            Now_Player = "X"
            
            for move in range(9):
                print(" " * 12, "CURRENT BOARD")
                print(" " *10, "=" * 17 )
                print(f"               {b1 if b1 != ' ' else '1'} | {b2 if b2 != ' ' else '2'} | {b3 if b3 != ' ' else '3'}")
                print("              -----------")
                print(f"               {b4 if b4 != ' ' else '4'} | {b5 if b5 != ' ' else '5'} | {b6 if b6 != ' ' else '6'}")
                print("              -----------")
                print(f"               {b7 if b7 != ' ' else '7'} | {b8 if b8 != ' ' else '8'} | {b9 if b9 != ' ' else '9'}")
                print(" " *10, "=" * 17 )                

#checks for the win after the fifth move
#checks the rows
                if move >= 5:
                    if b1 == b2 == b3 and b1 != " ":
                        winner = b1
                        game_over = True
                    elif b4 == b5 == b6 and b4 != " ":
                        winner = b4
                        game_over = True
                    elif b7 == b8 == b9 and b7 != " ":
                        winner = b7
                        game_over = True
#checks the collumns
                    elif b1 == b4 == b7 and b1 != " ":
                        winner = b1
                        game_over = True
                    elif b2 == b5 == b8 and b4 != " ":
                        winner = b2
                        game_over = True
                    elif b3 == b6 == b9 and b7 != " ":
                        winner = b3
                        game_over = True
#checks the diagonals
                    elif b1 == b5 == b9 and b1 != " ":
                        winner = b1
                        game_over = True
                    elif b3 == b5 == b7 and b3 != " ":
                        winner = b3
                        game_over = True
#Checks the poard when game is over
                    if game_over == True:
                        print(" " * 10 + "Final Board")
                        print(" " * 10 + "=" *17)
                        print(f"               {b1} | {b2} | {b3}")
                        print("              ")
                        print(f"               {b4} | {b5} | {b6}")
                        print("              ")
                        print(f"               {b7} | {b8} | {b9}")
                        print(" " * 10 + "=" * 17 + "\n")

                    if winner == X:
                        print("""
                                🥳🎉🎉🎉PLAYER WINS!!!🎉🎉🎉🥳
                                          Congrats!!!
                                      Here's a Trophy!🏆
                              """)
                    else:
                        print("""
                             ☠☠☠GAME OVER☠☠☠
                              The computer won.
                              Bummer.😭
                                """)
                    if move == 8 and not game_over:
                        print(" " * 10 + "Its a DRAW!!")
                        print(" " * 9 + "NO WINNERS!!!")
                        game_over = True

                    if game_over:
                        break

            
            if Now_Player == X:
                while True:
                    try:
                        pos = int(input("Enter Number 1-9: "))
                        if pos < 1 or pos > 9:
                            print("INVALID! Enter a Number 1-9: ")
                    except:
                        print("INVALID!\nPlease Enter A NUMBER 1-9: ")
                        continue

                    taken = False
                    for i in range(len(used)):
                        if int(used[i]) == pos:
                            taken = True
                            break
                    if taken:
                        print("That spot is already taken, Sorry.")
                        continue

                    if pos == 1: b1 = "X"
                    elif pos == 2: b2 = "X"
                    elif pos == 3: b3 = "X"
                    elif pos == 4: b4 = "X"
                    elif pos == 5: b5 = "X"
                    elif pos == 6: b6 = "X"
                    elif pos == 7: b7 = "X"
                    elif pos == 8: b8 = "X"
                    elif pos == 9: b9 = "X"

                    used += str(pos)
                    Now_Player = "0"
                    break

            else:
                placed = False

                for test in range (1, 10):
                    if placed: break
                    temp_b1, temp_b2, temp_b3 = b1, b2, b3
                    temp_b4, temp_b5, temp_b6 = b4, b5, b6
                    temp_b7, temp_b8, temp_b9 = b7, b8, b9
                    if test == 1 and b1 == " ": temp_b1 = "0"
                    if test == 2 and b2 == " ": temp_b2 = "0"
                    if test == 3 and b3 == " ": temp_b3 = "0"
                    if test == 4 and b4 == " ": temp_b4 = "0"
                    if test == 5 and b5 == " ": temp_b5 = "0"
                    if test == 6 and b6 == " ": temp_b6 = "0"
                    if test == 7 and b7 == " ": temp_b7 = "0"
                    if test == 8 and b8 == " ": temp_b8 = "0"
                    if test == 9 and b9 == " ": temp_b9 = "0"
            break



#    ELSE IF choice is 2
    elif x == 2:
        print("-"*40)
        print("              The Rules!")
        print("-"*40)
#        Display instructions:
        print("\n- YOU are X\n")
        print("- COMPUTER is O\n")
        print("- Enter a number 1-9 to place your mark\n")
        print("-the board looks like this:\n\n        1 | 2 | 3\n       -----------\n        4 | 5 | 6\n       -----------\n        7 | 8 | 9\n")      
        print("- Get three in a row FIRST to win!\n")
#       Waits for user to press Enter        
        input(" Good Luck! :D \n\nPress Enter to continue! ")
        x = 0

#    ELSE IF choice is 3, Prints "Goodbye" & ends program
    elif x ==3:   
        print("\nSee ya later Gamer!\n")
        break
    else:
        print("\n\nSorry, That choice was INVALID!!\n\n\n")
        x = 0
