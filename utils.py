import random
import requests
import basic_word
import sys


def load_random_word():
    """
    Получает список слов с внешнего ресурса и вызвращает сллучайное слово.
    """
    response = requests.get('https://jsonkeeper.com/b/PC1Y')
    questions = response.json()
    question = random.choice(questions)
    word = basic_word.Question(question['word'], question['subwords'])
    return word


def end_game(pleer):
    """
    Окончание игры, выводит инфорацию об угаданых словах
    и завершает программу
    """
    print('слова закончились, игра завершена!')
    print(f'вы угадали {pleer.return_len()} слов!')
    sys.exit()
