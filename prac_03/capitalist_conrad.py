import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_prices.txt"

# Initialize variables
price = INITIAL_PRICE
number_of_days = 0

# Open the output file for writing
out_file = open(OUTPUT_FILE, 'w')

# Output the starting price
print(f"Starting price: ${price:.2f}")
print(f"Starting price: ${price:.2f}", file=out_file)

# Simulate the stock prices until it goes out of range
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:.2f}")
    print(f"On day {number_of_days} price is: ${price:.2f}", file=out_file)

# Close the output file
out_file.close()
