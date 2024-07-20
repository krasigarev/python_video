puzle = 2.60
kukla = 3
meche = 4.10
minioni = 8.20
kamion = 2

price = float(input())
count_puzle = int(input())
count_kukli = int(input())
count_meche = int(input())
count_minioni = int(input())
count_kaomin = int(input())

sum_total = count_puzle * puzle + count_kukli * kukla + meche * count_meche + count_minioni * minioni + kamion * count_kaomin
count_igrachki = count_kaomin + count_minioni + count_kukli + count_meche + count_puzle

if  count_igrachki >= 50:
    sum_total = sum_total - (sum_total * 0.25)

sum_total = sum_total - sum_total * 0.10

diff = abs(sum_total - price)

if sum_total >= price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
