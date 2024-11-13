import random
import time





cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
random.shuffle(cards)
money = 100
def start_game(money,cards):
    while True:
        print("Начинаем игру!")
        while True:
            add_money_answ = input(f"У вас в бюджете: {money}$ Желаете добавить денег? Да/Нет:\n").lower()
            flag = True
            while flag == True:
                if add_money_answ == "да":
                    count_money = input("Сколько денег вы хотите добавить?\n")
                    if count_money.isdigit():
                        money = int(money) + int(count_money)
                        break
                    elif count_money == "выход":
                        answ_mm = input("Вы точно хотите выйти в главное меню? Ваш бюджет будет изменен до 100$!\n").lower()
                        if answ_mm != "нет":
                            while True:
                                if answ_mm == "да":
                                    print("Хорошо")
                                    main_menu()
                                    break
                                elif answ_mm == "нет":
                                    break
                                else:
                                    print("Ничего не понял :(")
                                    break
                        else:
                            break
                    else:
                        print("Ничего не понял :(")
                elif add_money_answ == "нет" and int(money) == 0:
                    print("А на что ты играть собрался, дятел? На жопу?!")
                    break
                elif add_money_answ == "выход":
                    answ_mm = input("Вы точно хотите выйти в главное меню? Ваш бюджет будет изменен до 100$!\n").lower()
                    if answ_mm != "нет":
                        while True:
                            if answ_mm == "да":
                                print("Хорошо")
                                main_menu()
                                break
                            elif answ_mm == "нет":
                                break
                            else:
                                print("Ничего не понял :(")
                                break
                    else:
                        break
                elif add_money_answ == "нет":
                    print("Окей, тогда начинаем.")
                    while flag == True:
                        bet = input("Сделайте вашу ставку: ")
                        if bet.isdigit() and 0 < int(bet) <= int(money):
                            print("Ставка сделана. Ставок больше нет!")
                            money = money - int(bet)
                            print("Игра пошла!")
                            grab_cards_d = random.choice(cards)
                            grab_cards_u = random.choice(cards)
                            cards_d = []
                            cards_u = []
                            cards_d.append(grab_cards_d)
                            cards_u.append(grab_cards_u)
                            cards.remove(grab_cards_d)
                            cards.remove(grab_cards_u)
                            print(f"У крупье {sum(cards_d)}, У вас {sum(cards_u)}")
                            while flag == True:
                                grab_card_answ = input("Желаете взять карту?Да/Нет\n")
                                while flag == True:
                                    if flag == False:
                                        break
                                    elif grab_card_answ == "да":
                                        print("Вы берете карту...")
                                        time.sleep(0.5)
                                        print("Вы берете карту..")
                                        time.sleep(1)
                                        print("Вы берете карту.")
                                        time.sleep(1)
                                        print("Вы берете карту")
                                        time.sleep(2)
                                        grab_cards_u = random.choice(cards)
                                        cards_u.append(grab_cards_u)
                                        cards.remove(grab_cards_u)
                                        print(f"У крупье {sum(cards_d)}, У вас {sum(cards_u)}")
                                        if sum(cards_u) > 21:
                                            print("Ты проиграл :(")
                                            flag = False
                                            break
                                        break
                                    elif grab_card_answ == "нет":
                                        while True:
                                            if sum(cards_d) < sum(cards_u):
                                                grab_cards_d = random.choice(cards)
                                                cards_d.append(grab_cards_d)
                                                cards.remove(grab_cards_d)
                                                print("Крупье берет карту...")
                                                time.sleep(0.5)
                                                print("Крупье берет карту..")
                                                time.sleep(1)
                                                print("Крупье берет карту.")
                                                time.sleep(1)
                                                print("Крупье берет карту")
                                                time.sleep(3)
                                                print(f"У крупье {sum(cards_d)}, У вас {sum(cards_u)}")
                                            elif sum(cards_d) == sum(cards_u):
                                                print("Ничья!")
                                                money = int(money) + int(bet)
                                                flag = False
                                                break
                                            elif 21 >= sum(cards_d) > sum(cards_u):
                                                print("Ты проиграл :(")
                                                flag = False
                                                break
                                            elif 21 < sum(cards_d) > sum(cards_u):
                                                print("Ты выиграл!")
                                                money = int(money) + int(bet) * 2
                                                flag = False
                                                break
                                    elif grab_card_answ == "выход":
                                        answ_mm = input("Вы точно хотите выйти в главное меню? Ваш бюджет будет изменен до 100$!\n").lower()
                                        if answ_mm != "нет":
                                            while True:
                                                if answ_mm == "да":
                                                    print("Хорошо")
                                                    main_menu()
                                                    break
                                                elif answ_mm == "нет":
                                                    break
                                                else:
                                                    print("Ничего не понял :(")
                                                    break
                                        else:
                                            break
                        elif bet.isdigit() and 0 < int(bet) > money:
                            print("Притормози. У тебя денег нет столько!")
                        elif bet == "выход":
                            answ_mm = input("Вы точно хотите выйти в главное меню? Ваш бюджет будет изменен до 100$!\n").lower()
                            if answ_mm != "нет":
                                while True:
                                    if answ_mm == "да":
                                        print("Хорошо")
                                        main_menu()
                                        break
                                    elif answ_mm == "нет":
                                        break
                                    else:
                                        print("Ничего не понял :(")
                                        break
                            else:
                                break
                        else:
                            print("Фальшивка, ебаный в рот. Давай нормальную ставку")
                else:
                    print("Ничего не понял :(")
                    break

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
    answ_mm = input('Добро пожаловать в меню игры "Очко". Желаете начать игру? Да/Нет:\n').lower()
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
            start_game(money,cards)
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