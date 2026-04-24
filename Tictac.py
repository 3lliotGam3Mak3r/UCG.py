# TIC TAC TOE GAME
while True:

    # ================= TITLE CARD =================
    print(
        "        ,----,                            ,----,                                ,----,                   \n"
        "      ,/   .`|                          ,/   .`|                              ,/   .`|                   \n"
        "    ,`   .'  :                        ,`   .'  :                            ,`   .'  :                   \n"
        "  ;    ;     / ,--,   ,--.          ;    ;     /            ,--.          ;    ;     /                   \n"
        ".'___,/    ,',--.'|  /  /|        .'___,/    ,'            /  /|        .'___,/    ,'  ,---.             \n"
        "|    :     | |  |,  '  / '        |    :     |            '  / '        |    :     |  '   ,'\            \n"
        ";    |.';  ; `--'_ /  / /         ;    |.';  ;  ,--.--.  /  / /         ;    |.';  ; /   /   |   ,---.   \n"
        "`----'  |  | ,' ,'/  / ,          `----'  |  | /       \/  / ,          `----'  |  |.   ; ,. :  /     \  \n"
        "    '   :  ; '  | \\ '\\ \\              '   :  ;.--.  .-. \\ '\\ \\              '   :  ;'   | |: : /    / '  \n"
        "    |   |  ' |  | :\\  \\ '             |   |  ' \\__\\/: . .\\  \\ '             |   |  ''   | .; :.    ' /   \n"
        "    '   :  | '  : |_\\  . |            '   :  | ,' .--.; | \\  . |            '   :  ||   :    |'   ; :__  \n"
        "    ;   |.'  |  | '.'\\__\\.            ;   |.' /  /  ,.  |  \\__\\.            ;   |.'  \\   \\  / '   | '.'| \n"
        "    '---'    ;  :    ;                '---'  ;  :   .'   \\                  '---'     `----'  |   :    : \n"
        "             |  ,   /                        |  ,     .-./                                     \\   \\  /  \n"
        "              ---`-'                          `--`---'                                          `----'   \n"
    )

    print("=" * 105)
    print("                                          MAIN MENU")
    print("=" * 105)
    print("1. Start Playing!\n")
    print("2. Display rules\n")
    print("3. Leave game\n")

    try:
        choice = int(input("Enter a Number 1-3: "))
    except:
        choice = 0

    print("=" * 105)

    if choice == 1:

        b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = " "
        used = ""
        Now_Player = "X"
        game_over = False

        for move in range(9):

            print("\n" + " " * 12 + "CURRENT BOARD")
            print(" " * 10 + "=" * 17)
            print(
                f"               {b1 if b1 != ' ' else '1'} | {b2 if b2 != ' ' else '2'} | {b3 if b3 != ' ' else '3'}"
            )
            print("              -----------")
            print(
                f"               {b4 if b4 != ' ' else '4'} | {b5 if b5 != ' ' else '5'} | {b6 if b6 != ' ' else '6'}"
            )
            print("              -----------")
            print(
                f"               {b7 if b7 != ' ' else '7'} | {b8 if b8 != ' ' else '8'} | {b9 if b9 != ' ' else '9'}"
            )
            print(" " * 10 + "=" * 17)

            # ================= PLAYER TURN =================
            if Now_Player == "X":
                while True:
                    try:
                        pos = int(input("Enter Number 1-9: "))
                        if pos < 1 or pos > 9:
                            print("INVALID! Enter a Number 1-9: ")
                            continue
                    except:
                        print("INVALID!\nPlease Enter A NUMBER 1-9: ")
                        continue

                    if str(pos) in used:
                        print("That spot is already taken, Sorry.")
                        continue

                    if pos == 1:
                        b1 = "X"
                    elif pos == 2:
                        b2 = "X"
                    elif pos == 3:
                        b3 = "X"
                    elif pos == 4:
                        b4 = "X"
                    elif pos == 5:
                        b5 = "X"
                    elif pos == 6:
                        b6 = "X"
                    elif pos == 7:
                        b7 = "X"
                    elif pos == 8:
                        b8 = "X"
                    elif pos == 9:
                        b9 = "X"

                    used += str(pos)
                    break

            # ================= COMPUTER TURN =================
            else:
                print("\n💻 Computer's Turn (O)...")
                placed = False

                # Try winning move
                for test in range(1, 10):
                    if placed:
                        break
                    temp = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
                    if temp[test - 1] == " ":
                        temp[test - 1] = "O"
                        if (
                            temp[0] == temp[1] == temp[2] == "O"
                            or temp[3] == temp[4] == temp[5] == "O"
                            or temp[6] == temp[7] == temp[8] == "O"
                            or temp[0] == temp[3] == temp[6] == "O"
                            or temp[1] == temp[4] == temp[7] == "O"
                            or temp[2] == temp[5] == temp[8] == "O"
                            or temp[0] == temp[4] == temp[8] == "O"
                            or temp[2] == temp[4] == temp[6] == "O"
                        ):
                            if test == 1:
                                b1 = "O"
                            elif test == 2:
                                b2 = "O"
                            elif test == 3:
                                b3 = "O"
                            elif test == 4:
                                b4 = "O"
                            elif test == 5:
                                b5 = "O"
                            elif test == 6:
                                b6 = "O"
                            elif test == 7:
                                b7 = "O"
                            elif test == 8:
                                b8 = "O"
                            elif test == 9:
                                b9 = "O"
                            used += str(test)
                            placed = True

                # Fallback move
                if not placed:
                    for i in range(1, 10):
                        if str(i) not in used:
                            if i == 1:
                                b1 = "O"
                            elif i == 2:
                                b2 = "O"
                            elif i == 3:
                                b3 = "O"
                            elif i == 4:
                                b4 = "O"
                            elif i == 5:
                                b5 = "O"
                            elif i == 6:
                                b6 = "O"
                            elif i == 7:
                                b7 = "O"
                            elif i == 8:
                                b8 = "O"
                            elif i == 9:
                                b9 = "O"
                            used += str(i)
                            break

            # ================= WIN CHECK =================
            winner = None
            if b1 == b2 == b3 != " ":
                winner = b1
            elif b4 == b5 == b6 != " ":
                winner = b4
            elif b7 == b8 == b9 != " ":
                winner = b7
            elif b1 == b4 == b7 != " ":
                winner = b1
            elif b2 == b5 == b8 != " ":
                winner = b2
            elif b3 == b6 == b9 != " ":
                winner = b3
            elif b1 == b5 == b9 != " ":
                winner = b1
            elif b3 == b5 == b7 != " ":
                winner = b3

            if winner:
                print("\n" + " " * 10 + "Final Board")
                print(" " * 10 + "=" * 17)
                print(f"               {b1} | {b2} | {b3}")
                print("              -----------")
                print(f"               {b4} | {b5} | {b6}")
                print("              -----------")
                print(f"               {b7} | {b8} | {b9}")
                print(" " * 10 + "=" * 17 + "\n")

                if winner == "X":
                    print(
                        """
🥳🎉🎉🎉 PLAYER WINS!!! 🎉🎉🎉🥳
       Congrats!!!
      Here's a Trophy! 🏆
                        """
                    )
                else:
                    print(
                        """
☠☠☠ GAME OVER ☠☠☠
     The computer won.
         Bummer. 😭
                        """
                    )
                game_over = True
                break

            if move == 8 and not winner:
                print("\n" + " " * 10 + "It's a DRAW!!")
                print(" " * 9 + "NO WINNERS!!!")
                game_over = True

            Now_Player = "O" if Now_Player == "X" else "X"

        # Play again
        print("\n" + "=" * 40)
        again = input("Play Again? (y/n): ").lower()
        if again not in ["y", "yes"]:
            break

    elif choice == 2:
        print("-" * 40)
        print("              The Rules!")
        print("-" * 40)
        print("\n- YOU are X\n")
        print("- COMPUTER is O\n")
        print("- Enter a number 1-9 to place your mark\n")
        print("- Get three in a row FIRST to win!\n")
        input(" Good Luck! :D \nPress Enter to continue! ")

    elif choice == 3:
        print("\nSee ya later Gamer!\n")
        break

    else:
        print("\n\nSorry, That choice was INVALID!\n\n\n")
