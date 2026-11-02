# --- Exercise 1 ---
# Calculate sales tax

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")



    # Exercise 2: Apply Discount

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(200, tier):.2f}")

    # --- Exercise 3 ---
# Exercise 3: Final Price

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax_amount = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax_amount

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

    # Exercise 4: Sales Report

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

    # Exercise 6: Scope Experiment

x = 100  # global variable

def double_it():
    x = 999  # local variable
    return x * 2

print(x)
print(double_it())
print(x)

# The x inside the function is a local variable.
# It is separate from the global x.
# The function returns 1998, but the global x stays 100.