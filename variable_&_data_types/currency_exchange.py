rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "PKR": 283.65,
    "INR": 87.32
}

from_ = input("Convert from : ").upper()
to_ = input("Convert to : ").upper()
amount = float(input("Enter amount: "))

if from_ not in rates or to_ not in rates:
    print("Invalid currency code.")
    exit()

amount_in_usd = amount / rates[from_]

converted_amount = amount_in_usd * rates[to_]

print(f"{amount} {from_} = {converted_amount:.2f} {to_}")
