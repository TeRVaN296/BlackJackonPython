import random
import time


ruletka = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
ruletka_bet = "чт нч к ч 1с 2с 1р 2р 3р пт вт тт"
black_num = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_num = [1, 3, 5, 7, 9, 12, 14,  16, 18, 19, 21, 23, 25, 27, 30, 32, 34]
one_c = "1 4 7 10 13 16 19 22 25 28 31 34"
two_c = "2 5 8 11 14 17 20 23 26 29 32 35"
three_c = "3 6 9 12 15 18 21 24 27 30 33 36"
money = 10000



def start_game(money,ruletka,ruletka_bet,black_num, red_num,one_c,two_c,three_c):
    while True:
        bet_mass = []
        money_mass = []
        bet_answ = input(f"У вас в бюджете: {money}$. Желаете сделать ставку?\n").lower()
        if bet_answ == "да":
            print("Окей, правила ты знаешь.Давай напишу тебе расшифровку:")
            while True:
                print('"чт"-четное, "нч"- нечетное, \n"к"-красное, "ч"-черное, \n"1с"-от 1 до 18, "2с"-от 19 до 36,\n"1р"-от 1+3..., "2р"-от 2+3..., "3р"-от 3+3...,\n"пт"-от 1 до 12, "вт"-от 13 до 24, "тт"- от 25 до 36.\nНу или просто число:')
                bet = input().lower()
                if bet.isdigit() and 0 <= int(bet) <= 36 or bet in ruletka_bet:
                    bet_mass.append(bet)
                    while True:
                        bet_m = input("Сумма ставки?\n")
                        if bet_m.isdigit() and int(bet_m) <= int(money):
                            money_mass.append(bet_m)
                            money = int(money) - int(bet_m)
                            break
                        else:
                            print("сумма не та")
                    while True:
                        add_bet_answ = input("Ставка принята. Хотите добавить еще одну ставку?\n").lower()
                        if add_bet_answ == "да":
                            while True:
                                bet = input('Сделайте еще одну ставку:\n"чт"-четное, "нч"- нечетное, \n"к"-красное, "ч"-черное, \n"1с"-от 1 до 18, "2с"-от 19 до 36,\n"1р"-от 1+3..., "2р"-от 2+3..., "3р"-от 3+3...,\n"пт"-от 1 до 12, "вт"-от 13 до 24, "тт"- от 25 до 36.\nНу или просто число:\n')
                                if bet.isdigit() and 0 <= int(bet) <= 36 or bet in ruletka_bet:
                                    bet_mass.append(bet)
                                    bet_m = input("Сумма ставки?\n")
                                    if bet_m.isdigit() and int(bet_m) <= int(money):
                                        money_mass.append(bet_m)
                                        money = int(money) - int(bet_m)
                                        break
                                    else:
                                        print("сумма не та")
                                else:
                                    print("Давай четче...")
                        elif add_bet_answ == "нет":
                            print("Ставки сделаны, ставок больше нет!Кручу рулетку")
                            print("Рулетка крутится...")
                            time.sleep(1)
                            print("Рулетка крутится..")
                            time.sleep(1)
                            print("Рулетка крутится.")
                            time.sleep(1)
                            print("Рулетка крутится..")
                            time.sleep(1)
                            print("Рулетка крутится...")
                            time.sleep(1)
                            number = random.choice(ruletka)
                            if int(number) in black_num:
                                print(f'Выпало {number} черное')
                            elif int(number) in red_num:
                                print(f'Выпало {number} красное')
                            else:
                                print(f'Выпало {number} зеленое')
                            i = 0
                            while i < len(bet_mass):
                                if bet_mass[i].isdigit() and bet_mass[i] == number:
                                    print(f"Поздравляем!Ваш выйгрыш ставки {i + 1} составил- {int(money_mass[i]) * 35}$")
                                    money = money + int(money_mass[i]) * 35
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                elif bet_mass[i] == "чт" and number % 2 == 0:
                                    print(f"Поздравляем!Ваш выйгрыш ставки {i + 1} составил- {int(money_mass[i]) * 2}$")
                                    money = money + int(money_mass[i]) * 2
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                elif bet_mass[i] == "нч" and number % 2 !=0:
                                    print(f"Поздравляем!Ваш выйгрыш ставки {i + 1} составил- {int(money_mass[i]) * 2}$")
                                    money = money + int(money_mass[i]) * 2
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                elif bet_mass[i] == "к" and int(number) in red_num:
                                    print(f"Поздравляем!Ваш выйгрыш ставки {i + 1} составил- {int(money_mass[i]) * 2}$")
                                    money = money + int(money_mass[i]) * 2
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                elif bet_mass[i] == "ч" and int(number) in black_num:
                                    print(f"Поздравляем!Ваш выйгрыш ставки {i + 1} составил- {int(money_mass[i]) * 2}$")
                                    money = money + int(money_mass[i]) * 2
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                elif bet_mass[i] == "1с" and 0 < number < 19:
                                    print(f"Поздравляем!Ваш выйгрыш ставки {i + 1} составил- {int(money_mass[i]) * 2}$")
                                    money = money + int(money_mass[i]) * 2
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                elif bet_mass[i] == "2с" and 18 < number <37:
                                    print(f"Поздравляем!Ваш выйгрыш ставки {i + 1} составил- {int(money_mass[i]) * 2}$")
                                    money = money + int(money_mass[i]) * 2
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                elif bet_mass[i] == "1р" and str(number) in one_c:
                                    print(f"Поздравляем!Ваш выйгрыш ставки {i + 1} составил- {int(money_mass[i]) * 3}$")
                                    money = money + int(money_mass[i]) * 3
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                elif bet_mass[i] == "2р" and str(number) in two_c:
                                    print(f"Поздравляем!Ваш выйгрыш ставки {i + 1} составил- {int(money_mass[i]) * 3}$")
                                    money = money + int(money_mass[i]) * 3
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                elif bet_mass[i] == "1р" and str(number) in three_c:
                                    print(f"Поздравляем!Ваш выйгрыш ставки {i + 1} составил- {int(money_mass[i]) * 3}$")
                                    money = money + int(money_mass[i]) * 3
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                else:
                                    print(f'Твоя ставка {i + 1} не выйграла :(')
                                    if i + 1 == len(bet_mass):
                                        start_game(money,ruletka,ruletka_bet,black_num,red_num,one_c,two_c,three_c)
                                    else:
                                        print("")
                                i += 1
                        elif add_bet_answ == "?":
                            print(bet_mass)
                        else:
                            print("Давай четче...")
                else:
                    print("Давай четче...")
        elif bet_answ == "нет":
            print('А зачем тогда пришел? Тут, как в магаизне, "просто посмотреть" не получится! Давай на выход!')
            time.sleep(2)
            main_menu()
        else:
            print("Давай четче...")







def quit_menu():
    answ_qm = input('Хотите выйти из игры? Да/Нет:\n').lower()
    while True:
        if answ_qm == "да":
            print("Выход из игры")
            time.sleep(1)
            print("Выход из игры.")
            time.sleep(0.5)
            print("Выход из игры..")
            time.sleep(0.2)
            print("Выход из игры...")
            quit()
        elif answ_qm == "нет":
            print("Отлично!")
            main_menu()
            break
        else:
            print("Ответ не понятен :(")
            quit_menu()
            break
def main_menu ():
    answ_mm = input('Добро пожаловать в меню игры "Гребаная ракетка". Желаете начать игру? Да/Нет:\n').lower()
    while True:
        if answ_mm == "да":
            print("Загрузка")
            time.sleep(1)
            print("Загрузка.")
            time.sleep(0.8)
            print("Загрузка..")
            time.sleep(0.5)
            print("Загрузка...")
            time.sleep(0.2)
            start_game(money,ruletka, ruletka_bet,black_num,red_num,one_c,two_c,three_c)
            break
        elif answ_mm == "нет":
            quit_menu()
        elif answ_mm == "выход":
            quit_menu()
        else:
            print("Ничего не понял :(")
            main_menu()
            break

main_menu()







