from datetime import datetime
import random


def привет():
    print('Привет! Давай сыграем в игру "Угадай число"')
    print('У тебя есть 6 попыток для того чтобы отгадать число')


def случ_знач():
    return random.randint(1, 100)


def количество_попыток():
    while True:
        try:
            return int(input('Введите число от 1 до 100: '))
        except ValueError:
            print("Ошибка! Введите целое число.")


def число(загаданное, попытка):
    if попытка > загаданное:
        print('Загаданное число меньше')
        return False
    elif попытка < загаданное:
        print('Загаданное число больше')
        return False
    else:
        print('Ура! Ты угадал!')
        return True


def save_attempts(попытки, результат):
    with open("player.txt", "a", encoding="utf-8") as f:
        f.write(f"Попыток: {попытки}\n")
        f.write(f"Результат: {'Победа' if результат else 'Поражение'}\n")
        f.write(f"Дата: {datetime.now()}\n\n")


def играть():
    привет()
    загаданное_число = случ_знач()
    макс_попыток = 6
    попытки = 0
    угадал = False

    while попытки < макс_попыток and not угадал:
        print(f"Попытка {попытки + 1} из {макс_попыток}")
        попытка = количество_попыток()
        попытки += 1
        угадал = число(загаданное_число, попытка)

    if not угадал:
        print(f"Проигрыш! Загаданное число было {загаданное_число}")

    save_attempts(попытки, угадал)


if __name__ == "__main__":
    играть()

