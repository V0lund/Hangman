print("H A N G M A N")
print("The game will be available soon.")
# Global variables
words = ['python', 'java', 'kotlin', 'javascript']


# functions
def word_choice() -> str:
    from random import randint
    return words[randint(0, 3)]


def game_play() -> int:
    tries = 8
    while tries > 0 and '-' in letters_hidden_list:
        pl_ch = input('Input a letter:')
        if pl_ch in letters_left:
            i = letters_left.index(pl_ch)
            del letters_left[i]
            letters_left.insert(i, '-')
            del letters_hidden_list[i]
            letters_hidden_list.insert(i, pl_ch)
            print(''.join(str(_) for _ in letters_hidden_list))
        else:
            print("That letter doesn't appear in the word")
            tries -= 1
    return tries


# Game
word = word_choice()
word_list = list(word)
word_hidden = ''.join(str('-') for _ in word_list)
print(word_hidden)
letters_left = list(word)
letters_hidden_list = list(word_hidden)

if game_play() > 0:
    print("Thanks for playing!\nWe'll see how well you did in the next stage")
else:
    print("Thanks for playing!\nWe'll see how well you did in the next stage")
