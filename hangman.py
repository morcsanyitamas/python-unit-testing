def reveal(char, revealed_word, word):
    for index, letter in enumerate(word):
        if letter.upper() == char.upper():
            revealed_word[index] = word[index]
    return revealed_word


def get_revealed_word(word):
    revealed_word = []
    for char in word:
        if char != ' ':
            revealed_word.append('_')
        else:
            revealed_word.append(' ')
    return revealed_word


# list comprehension
# word = "United States of America"
# a = [char + ' ' for char in word if char == 'a']
# print(a)


def print_revealed_word(revealed_word):
    print(' '.join(revealed_word))


def main():
    word = "United States of America"
    revealed_word = get_revealed_word(word)
    revealed_word = reveal('a', revealed_word, word)
    print_revealed_word(revealed_word)


if __name__ == "__main__":
    main()