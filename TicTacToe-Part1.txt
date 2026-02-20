Display Tic-Tac-Toe title

LOOP forever
    Display:
        1. Start Game
        2. Instructions
        3. Exit

    Ask user for a choice

    IF choice is 1
        Exit menu and start game

    ELSE IF choice is 2
        Display instructions:
            - You are X
            - Computer is O
            - Enter 1–9 to place a mark
            - First to get 3 in a row wins
        Wait for user to press Enter

    ELSE IF choice is 3
        Print "Goodbye"
        End program

    ELSE
        Print "Invalid choice"
END LOOP
