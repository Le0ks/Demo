from random import choice

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(guessed_word):
    word_completion = ["_" for i in range(len(guessed_word))]
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Давай сыграем в висилицу!")
    print(display_hangman(tries))
    print(*word_completion)
    while tries != 0 and word_completion != list(guessed_word):
        letter_or_word = input("Попробуешь угадать слово или букву? ").lower()
        while letter_or_word != "слово" and letter_or_word != "буква":
            letter_or_word = input("Напиши слово или буква: ").lower()
        if letter_or_word == "слово":
            word = input("Введи слово: ").strip().upper()
            while not word.isalpha():
                word = input("В слове должны быть только буквы. Введи слово: ").strip().upper()
            if word in guessed_word:
                print("Ты уже пробовал такое слово.")
                continue
            else:
                guessed_words.append(word)
            if word != guessed_word:
                tries -= 1
                print("Ты не угадал!")
                print(display_hangman(tries))
                print(*word_completion)
            else:
                print(*word_completion)
        else:
            letter = input("Введи букву: ").strip().upper()
            while not letter.isalpha():
                letter = input("Это не буква. Введи букву: ").strip().upper()
            if letter in guessed_letters:
                print("Ты уже пробовал такую букву")
                continue
            else:
                guessed_letters.append(letter)
            if letter not in guessed_word:
                tries -= 1
                print("Ты не угадал!")
                print(display_hangman(tries))
                print(*word_completion)
            else:
                for i in range(len(guessed_word)):
                    if guessed_word[i] == letter:
                        word_completion[i] = letter
                print("Ты угадал")
                print(*word_completion)
    if tries == 0:
        print("Загаданное слово было", guessed_word)
        print("Game over!")
    else:
        print("You are win!!!")


word_list = ['КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ', 
'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА', 'СКОВОРОДА', 
'МНОГОНОЖКА', 'ЕВРЕЙ', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН', 'МИКРОВОЛНОВКА', 'ТОРТ', 'МАК', 
'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР', 'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА', 'ОВЦА', 'БАНАН', 
'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД', 'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН', 'ТЕЛЕФОН', 
'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН', 'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК', 'ОМАР', 
'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО', 'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'ДИДЖЕЙ', 'МЕШОК', 'ТЮБИК', 
'МОЗГ', 'ПОЕЗД', 'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ', 'ПИЦЦА', 
'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП', 'ЛЕЩ', 'КАМЕНЬ', 'ДИСК']

again = "да"

while again == "да":
    guessed_word = choice(word_list)
    play(guessed_word)
    again = input("Хочешь продолжить играть (да или нет): ").strip().lower()
    while again != "да" and again != "нет":
        again = input("Напиши да или нет: ")

print("Надеюсь скоро увидимся...")