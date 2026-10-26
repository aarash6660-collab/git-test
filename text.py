import random

secret = random.randint(1, 100)
tries = 0

print("بازی حدس عدد!")
print("من یه عدد بین ۱ تا ۱۰۰ انتخاب کردم. حدس بزن!")

while True:
    guess = int(input("حدست چیه؟ "))
    tries += 1

    if guess < secret:
        print("بزرگ‌تر بگو!")
    elif guess > secret:
        print("کوچک‌تر بگو!")
    else:
        print(f" درست حدس زدی ")
