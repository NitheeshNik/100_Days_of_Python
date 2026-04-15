print("**********COMPOUNT INTEREST CALCULATOR**********")

principal = int(input("Enter the principal (P): "))
interest_rate = float(input("Enter the interest rate % (r): "))
years = int(input("Enter the # of years (t): "))
times_compound = int(input("Enter # of times compounded per year (n): "))

rate = interest_rate / 100
amount = principal * pow((1 + rate / times_compound), times_compound * years )
print(f"After {years} year(s), the total will ${amount:.2f}")
