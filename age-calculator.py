from datetime import date

year = date.today().year
birth = int(input("Enter your birth year: "))

while True:
    yn = input("Have you already celebrated your birthday this year (Y/N)? ").lower().strip()
    if yn not in "yn":
        print("Enter Y or N!")
        continue
    break

if yn == 'n':
    year -= 1

print(f"You're {year - birth} years old")
