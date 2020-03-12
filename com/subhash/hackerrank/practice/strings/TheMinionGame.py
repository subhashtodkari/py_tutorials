vowels = ['A', 'E', 'I', 'O', 'U']


def minion_game(string):
    # your code goes here
    v_word_count = 0
    c_word_count = 0

    for i in range(len(string)):
        no_of_words = len(string) - i
        # print("c: {}, no_of_words: {}".format(string[i], no_of_words))
        if string[i] in vowels:
            v_word_count += no_of_words
        else:
            c_word_count += no_of_words

    if v_word_count > c_word_count:
        print("Kevin {}".format(v_word_count))
    elif v_word_count < c_word_count:
        print("Stuart {}".format(c_word_count))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)

