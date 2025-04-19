import Угадайчисло
import Блэкджек
def main():
    print("Игры")
    print('1.Угадай число')
    print('2.Блэк_Джэк')
    print('0.Выход')

    Выбор = input("Выбери игру: ")
    if Выбор == "1":
        Угадайчисло
    elif Выбор == "2":
        Блэкджек
    elif Выбор == "0":
        print("Выход")
    else:
        print('Неверный ввод')
if __name__ == "__main__":
    main()