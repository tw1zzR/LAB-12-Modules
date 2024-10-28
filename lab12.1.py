import random

def first_Fragments(text, N):
    for i in range(0, len(text), N):
        print(text[i:i + N])

print("\nВикликаємо першу функцію:")
first_Fragments("Давайте розділимо цей текст на фрагменти", 4)

def scnd_Fragments(text):
    for i in range(0, len(text), 2):
        print(text[i:i + 2], random.randrange(9), random.randrange(9))

print("\nВикликаємо другу функцію:")
scnd_Fragments("Давайте розділимо цей текст на фрагменти")