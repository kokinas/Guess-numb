import random
def f_guess():
    comp_numb = random.randint(0, 100)
    level = {
        "1" : 10,
        "2" : 6,
        "3" : 3
    }
    level_set = input ("Выберите уровень сложности от 1 до 3: ")
    if level_set in level:
        max_count = level[level_set]
        for i in range (1, max_count):
            user_version = int(input('Угадайте какое число я задумал: '))
            if comp_numb == user_version:
                print (f"Вы победили, я задумал число {comp_numb}")
                break
            elif comp_numb > user_version:
                print("Мимо!!! Мое число больше")
            elif comp_numb < user_version:
                print("Мимо!!! Мое число меньше")
        if i == max_count - 1:
            print("Вы проиграли!!!")
    else:
        print("Вы ввели не корректный уровень сложности")


