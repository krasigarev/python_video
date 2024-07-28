import math

name = input()
budget = float(input())
bottle = int(input())
chips = int(input())

sum_beers = bottle * 1.20
price_chips = sum_beers * 0.45
sum_chips = math.ceil(chips * price_chips)
total = sum_beers + sum_chips
diff = abs(total - budget)

if budget >= total:
    print(f"{name} bought a snake and has {diff:.2f} leva left.")
else:
    print(f'{name} needs {diff:.2f} more leva.')