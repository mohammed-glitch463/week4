usage = float(input("Enter electricity usage (kWh): "))

if usage <= 100:
    cost = usage * 0.10
elif usage <= 300:
    cost = usage * 0.15
else:
    cost = usage * 0.20

print("Total bill: $", cost)

salary = float(input("Enter salary: "))
years = float(input("Enter years of service: "))

if years >= 10:
    bonus = salary * 0.25
elif years >= 5:
    bonus = salary * 0.15
elif years >= 1:
    bonus = salary * 0.05
else:
    bonus = 0

print("Bonus: $", bonus)

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or a == c or b == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

salary = float(input("Enter salary: "))
credit_score = int(input("Enter credit score: "))
years = float(input("Enter years of employment: "))

conditions = 0

if salary >= 3000:
    conditions += 1
if credit_score >= 650:
    conditions += 1
if years >= 2:
    conditions += 1

if conditions == 3:
    print("Loan Approved")
elif conditions == 2:
    print("Conditional Approval")
else:
    print("Loan Rejected")

vehicle = input("Enter vehicle type (motorcycle/car/bus): ").lower()
hours = float(input("Enter parking hours: "))

if vehicle == "motorcycle":
    first_hour = 1
    extra = 0.5
elif vehicle == "car":
    first_hour = 2
    extra = 1
elif vehicle == "bus":
    first_hour = 3
    extra = 2
else:
    print("Invalid vehicle type")
    exit()

if hours <= 1:
    fee = first_hour
else:
    fee = first_hour + (hours - 1) * extra

print("Parking fee: $", fee)