# Exercise 1: One customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold:",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2: Update and add

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer ["email"]
print(customer)

# Exercise 3: Safe Lookup

print(customer.get("email, no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email was not found")

# Exercise 4: Iterate Through a Dictionary

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives us the keys, not the values stored with them.
for key in customer:
    print(key)

# Exercise 5: Customer Tier Discounts

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

price = 200
final_price = price * (1 - discount)

print("Tier", tier)
print("Discount:", f"{discount * 100}%")
print("Final Price:", f"{final_price:.2f}", sep= "")

# Exercise 6: List of customer dictionaries

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Carlos", "tier": "silver"},
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    savings = 300 * discount

    print(f"{name}: ({tier}) discount: ${savings:.2f}")
    