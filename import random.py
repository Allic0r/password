import random
sym = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
l = int(input())
password = ""
for i in range(l):
    # Используем random.randint(0, len(sym) - 1) для корректного выбора индекса
    letter = random.randint(0, len(sym) - 1)
    password += sym[letter]
print("Сгенерированный пароль:", password)