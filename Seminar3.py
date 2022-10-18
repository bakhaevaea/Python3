
# Создайте файл. Запишите в него N первых
# элементов последовательности Фибоначчи.
from base64 import decode
import encodings


def Fib():
    print ("Сколько чисел Фибоначчи вывести? ")
    N = int(input())
    F = [1, 1]
    for i in range(2,N):
        F.append(F[i-2]+F[i-1])   
    data = open("Fib.txt", "w")
    data.writelines(str(F[:N]))
    data.close()



# В файле находятся названия фруктов.
# Выведите все фрукты, названия которых начинаются на
# заданную букву.
def Fruits():
    print("На какую букву фрукты вывести?")
    letter = input()
    data = open ("Fruits.txt", encoding ="UTF-8")
    Fru = data.readlines()
    data.close()
    countFru = 0
    for i in Fru:
        if i[0] == letter.upper() or i[0] == letter.lower():
            print(i, end = "")
            countFru +=1
    if countFru == 0:
        print("Нет фруктов на эту букву")



# Задача 3. Создайте скрипт бота, который находит ответы
# на фразы по ключу в словаре. Бот должен, как минимум,
# отвечать на фразы «привет», «как тебя зовут». Если фраза
# ему неизвестна, он выводит соответствующую фразу.
def Bot():
    quest_dict = {}
    data = open("Bot.txt",  encoding ="UTF-8")
    questions = data.readlines()
    data.close()

    # заполняем словарь считанными из файла значениями. 
    # В файле вопрос и ответ разделены |
    for i in range(len(questions)):
        quest_dict[questions[i].split("|")[0]] = questions[i].split("|")[1]

    quest = input("Можете задать вопрос (для выхода нажмите Q)   ")
    while quest != "Q":
        if quest_dict.get(quest.lower()) != None and quest != "Q":
            print(quest_dict.get(quest.lower()))
        else:
            answ = input("Я этого не знаю. Как правильно ответить на этот вопрос?  ")
            quest_dict[quest.lower()]=answ
            data = open("Bot.txt", "a", encoding ="UTF-8")
            data.write(f'{quest.lower()}|{answ}\n' )
            data.close()
        quest = input("")


# Fib()
# Fruits()
# Bot()