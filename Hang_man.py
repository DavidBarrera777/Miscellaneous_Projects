import random

#This function is used to create the list that will be used to display the random word
def word(length):
    return ['_' for _ in range(length)]



#This function prompts the user to guess a letter to the randomly selected word
# If the letter is present in the word it will add it to the empty list at the same
# index in which the random word has that letter
# If the letter is not in the word it prompts the user to enter another letter and tells the user
# how many lives they have left a
def choose_letter(w, random_word, lives):

    letter = input('Enter a letter: ').lower()
    
    if letter in random_word:
        for i in range(len(random_word)):
            if letter == random_word[i]:
                w[i] = letter
    else:
        (print('letter not in word'))
        print(f'Lives left: {lives-1}')
        return 1



#This is the main function where all the logic is put together
# The user is welcomed to the game and told how many letters are in the word they wanna guess
# Then the word is randomly chosen from a list
#Then the main logic is in the while loop 
#The winner is chosen if the user guesses all the letters to word and doesnt run out of lives
def main():
    print('Welcome to hangMan!')
    print('The Word you wanna guess contains 8 letters!')
    words = ['generate', 'computer', 'generous', 'genomics', 'frequent']
    random_word = random.choice(words)
    length = len(random_word)
    lives = 8
    w = word(length)
    print(w)

    while True:
        player_lives = choose_letter(w, random_word, lives)
        print(w)

        if player_lives is not None:
            lives -= 1

        if '_' not in w:
            print('You won!')
            break

        if lives == 0:
            print("Game over")
            break

    return





if __name__ == "__main__":
    main()
