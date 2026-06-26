import random

name = input("Who are you?\n> ")

print(f"Hello, {name}!")

heads = 0
tails = 0

print("Tossing a coin...")

for i in range(1,4):
    toss = random.choice(["Heads","Tails"])
    print(f"Round {i}: {toss}")

    if toss == "Heads":
        heads += 1
    else:
        tails += 1

print(f"Heads: {heads}, Tails: {tails}")