import random

# 1.a
def get_random_country():
    countries = []
    with open('countries-and-capitals.txt', 'r') as file:
        for line in file:
            # country = ""
            # for char in line:
            #     if char == '|':
            #         break
            #     country += char
            # country = country.strip()
            country_and_capital = line.split(' | ')
            countries.append(country_and_capital[0])
    return random.choice(countries)     


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



def print_revealed_word(revealed_word):
    print(' '.join(revealed_word))


def main():
    random_country = get_random_country()
    # word = "United States of America"
    # revealed_word = get_revealed_word(word)
    # revealed_word = reveal('a', revealed_word, word)
    # print_revealed_word(revealed_word)


if __name__ == "__main__":
    main()

'''
HANGMAN
1.a kitalálandó szó
    - be kell olvasni a file tartalmát egy listába
    - feldolgozni egy sort, venni " | " -től balra eső szót (országnév)
    - adott egy szavakat tartalmazó lista
    - véletlenszerűen válasszunk egy szót a listából
1.b hány élettel játszuk (nehézségi szint)
    2.a megjelenítjük az elfedett szót
    2.b be kell kérni egy betűt
    2.c fel kell fedni a betűt (ha benne van az eredeti szóban)
    2.d ellenőrzik, hogy nyert -e a játékos
    2.e ellenőrizzük, hogy veszített-e

'''