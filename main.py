import random
print(3//2)
max_numb = 100
level = {
    '1': 3,
    '2': 5,
    '3': 10
    }
level_set = input('Введите уровень сложности :')
number_attempts_max = level[level_set]
max_attempt = max_numb
min_attempt = 0
for numb_attempt in range(number_attempts_max):
    delt = max_attempt-min_attempt
    comp_attampts = (max_attempt + min_attempt)//2 + 1 + random.randint(-delt//number_attempts_max,delt//number_attempts_max)
    clue_st_er = True
    while clue_st_er:
        clue = input (f'Компьютер считает что загаданное число {comp_attampts} напишите >, < или =')
        if clue == '=':
            break
        elif clue == '>':
            min_attempt = comp_attampts
        elif clue == '<':
            max_attempt = comp_attampts
        else:
            print(f'Ваша подсказка компьютеру "{clue}" не корректна')
            clue_st_er = True
            next
        clue_st_er = False
    if (max_attempt - min_attempt) < 2:
        print('Вы жулик!!! С вами я больше играть не буду!!!')
        break
    if clue == '=':
        print('Компьютер победил')
        break
    if numb_attempt == number_attempts_max-1:
        print('Вы победили компьютер')
print ('Игра окончина')



