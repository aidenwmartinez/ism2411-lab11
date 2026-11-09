# Exercise 1 - One customer

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

# Exercise 2 - Update and add

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer ["email"]
print(customer)

# Exercise 3 - Safe Lookup

print(customer.get("email, no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email was not found")