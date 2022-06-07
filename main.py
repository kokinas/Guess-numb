import random
import computer_guess_numb
import user_guess_numb

print ("Добро пожаловать в игру угадай число.")
while 1:
    mode_setting = input("Выберите режим игры, кто будет загадывать число? напишите в терминал 'COMP' или 'USER' ")
    if mode_setting == "USER":
        computer_guess_numb.f_guess()
    elif mode_setting == "COMP":
        user_guess_numb.f_guess()
    repeat_game = input('Повторить попытку: да: ')
    if repeat_game == "да":
        print("Ну что ж поиграем")
    else:
        break

print ("Игра окончена ждем вас в следующий раз")



