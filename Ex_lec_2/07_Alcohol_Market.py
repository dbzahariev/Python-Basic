price_wiskey = float(input())
count_beer = float(input())
count_wine = float(input())
count_rakiq = float(input())
count_wiskey = float(input())

price_rakiq = price_wiskey / 2
price_wine = price_rakiq - (0.4 * price_rakiq)
price_beer = price_rakiq - (0.8 * price_rakiq)

all_price_rakiq = count_rakiq * price_rakiq
all_price_wine = count_wine * price_wine
all_price_beer = count_beer * price_beer
all_price_wiskey = count_wiskey * price_wiskey

all_price = all_price_rakiq + all_price_wine + all_price_beer + all_price_wiskey

print(f"{all_price:.2f}")