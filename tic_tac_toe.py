import random



#This function is used to slect whether the player will be x or y
#based on the flip of a coin
def select_player():
    #Ask the user to select heads or tails to determine if they will be X or O
    player_selection = input('Select heads or tails to choose a character: ').lower()

    #use the random library to determine which choice(heads or tails) is randomly generated
    #stored as random_character and prints the choice to the user
    choices = ['heads', 'tails']
    random_character = random.choice(choices)
    print(f'Coin landed on {random_character}')

    #if the player chooses the same as the random input then they will be awarded by going first
    #then the inputs are returned by the function in a specific order(X,0 or O,X)
    if player_selection == random_character:
        print('You got X (You go first)')
        return 'X', 'O'
    else:
        print('You got O (You go second)')
        return 'O', 'X'

def board():
    #Returning a list in order to represent the board and the _ is used as a placeholder and
    #isnt important. Basically no point in naming the list, its not important and is faster
    #This is equivalent to:
    #def board():
    #   result = []
    #   for i in range(9):
    #       result.append(' ')
    #   return result
    return [' ' for _ in range(9)]

#This function returns the board and will account for filling in the pieces with the 
#properly alloccated piece
def print_board(b):
    print(f'{b[0]} | {b[1]} | {b[2]}')
    print('--+---+--')
    print(f'{b[3]} | {b[4]} | {b[5]}')
    print('--+---+--')
    print(f'{b[6]} | {b[7]} | {b[8]}')

 
#This function asks the user to select a position in order to place it on the board
#If the space is available then thee position will befilled with the desired piece
#If the spot is full then the player will be prompted to select another position and the 
#the fucntion will run aagin 
def player_move(b, player):
    while True:
        try:
            #This will subtract the user input for easier user input
            move = int(input('Please select a position from 1-9: ')) - 1

            if move < 0 or move > 8:
                print('Invalid range!')
            elif b[move] != ' ':
                print('Spot taken!')
            else:
                b[move] = player
                break
        except:
            print('Enter a number')


#This function is responsible for the computer player
#Keeps choosing a random spot until it finds a empty spot and breaks out of the while loop
def computer_player(b, player):
    print('Ai is thinking....')

    while True:
        move = random.randint(0,8)
        if b[move] == ' ':
            b[move] = player
            break


#This functions checks if there areany wins within the user input
#Thisi is done by checking them with all the possible wins patterns in the win list 
#It just checks if a symbol is the same in each of the win positions
#If they are the same, it returns thee character in order to be used 
#so the proper winner can be printed
#The if statent basically just says if there are no empty spaces,then it is a tie and returns tie
def check_winner(b):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [2,4,6], [0,4,8]]

    for combo in wins:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] != ' ':
            return b[combo[0]]
        
    if ' ' not in b:
        return 'Tie'
    
    return None



def main():
    print('Welcome to Tic-Tac-Toe')

    #The empty player board that will be used for the game
    b = board()

    #Determines which player is X and which player is O
    player, computer = select_player()

    #Assigns the player and the ai player a symbol
    current_player = player
    ai_player = computer

    #The board is printed, the player makes a move, it checks for a win
    #Then the ai player makes a move and then it checks for a win 
    #Checks are in place to ensure the game stops after someone wins
    while True:
        print_board(b)

        player_move(b, current_player)

        winner = check_winner(b)
        if winner:
            print_board(b)
            print(f"{winner} wins!" if winner != 'Tie' else "It's a tie!")
            break

        computer_player(b, ai_player)

        winner = check_winner(b)
        if winner:
            print_board(b)
            print(f"{winner} wins!" if winner != 'Tie' else "It's a tie!")
            break


    



if __name__ == "__main__":
    main()



    



