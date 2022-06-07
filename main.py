import utils
import players


if __name__ == '__main__':
    print('Ввведите имя игрока')
    name = input()
    pl = players.Pleer(name)
    print(f'Привет, {pl.username}!')
    word = utils.load_random_word()
    print(f'Составьте {word.len_allowed_subwords()} слов из слова {word.original_word}')
    print('Слова должны быть не короче 3 букв')
    print('Поехали, ваше первое слово?')
    x = 0
    while x < word.len_allowed_subwords():
        x += 1
        answear = input()
        if answear == 'stop' or answear == 'стоп':
            utils.end_game(pl)
        elif word.test_words(answear):
            pl.add_words(answear)
            print('верно')
        else:
            print('не верно')

    utils.end_game(pl)
