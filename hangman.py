from random import randint


def displayIntro():
    with open('hangman-words.txt', 'r') as rules:
        listed_rules = list(rules)
        for i in range(23):
            listed_rules[i] = str(listed_rules[i])[:-1]
    pass


def displayEnd(result):
    with open('hangman-ascii.txt', 'r') as ending:
        listed_ending = list(ending)
        if result:
            for i in range(190, 204):
                listed_ending[i] = str(listed_ending[i])[:-1]
                print(listed_ending[i])
        else:
            for i in range(99, 113):
                listed_ending[i] = str(listed_ending[i])[:-1]
                print(listed_ending[i])


def displayHangman(state):
    with open('hangman-ascii.txt', 'r') as drawer:
        listed_draw = list(drawer)
        if state == 5:
            for i in range(24, 33):
                listed_draw[i] = str(listed_draw[i])[:-1]
                print(listed_draw[i])
        elif state == 4:
            for i in range(37, 46):
                listed_draw[i] = str(listed_draw[i])[:-1]
                print(listed_draw[i])
        elif state == 3:
            for i in range(50, 59):
                listed_draw[i] = str(listed_draw[i])[:-1]
                print(listed_draw[i])
        elif state == 2:
            for i in range(63, 72):
                listed_draw[i] = str(listed_draw[i])[:-1]
                print(listed_draw[i])
        elif state == 1:
            for i in range(76, 85):
                listed_draw[i] = str(listed_draw[i])[:-1]
                print(listed_draw[i])
        elif state == 0:
            for i in range(89, 98):
                listed_draw[i] = str(listed_draw[i])[:-1]
                print(listed_draw[i])
    pass


def getWord():
    with open('hangman-words.txt', 'r') as words:
        list_of_words = list(words)
        guess_word = list_of_words[randint(0, len(list_of_words) - 1)]
    return guess_word


def valid(c):
    if c.isalpha() and len(c) == 1 and c.islower:
        return True
    else:
        return False


def play():
    res = False
    checker = getWord()
    words = list(checker[:-1])
    hided_word = ''
    lst = []
    for i in range(len(words)):
        lst.append("_")
    lives: int = 5
    while lives >= 0:
        if lives == 0:
            displayHangman(lives)
            print(f"Hidden word was:  {checker}")
            break
        for i in lst:
            hided_word += i
        if lst == words:
            res = True
            print(f"Hidden word was:  {checker}")
            break
        displayHangman(lives)
        print(f"Guess the word:  {hided_word}")
        print("Enter the letter: ")
        letter = input("> ")
        if valid(letter):
            for i in range(len(words)):
                if letter == words[i]:
                    lst[i] = letter
        if list(hided_word) == lst:
            lives = lives - 1
        hided_word = ""
    return res


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        if input("> ") == "yes":
            continue
        else:
            break


if __name__ == "__main__":
    hangman()
