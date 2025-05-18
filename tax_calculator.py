def calculate_tax(income):
    tax = 0

    if income <= 1200000:
        
        return 0
    elif income == 1210000:
        tax= 10000
        return tax * 0.04
    elif income == 1225000:
        tax= 25000
        return tax * 0.04
    elif income == 1250000:
        tax= 50000   
        return tax * 0.04
    else:
       
        if income > 2400000:
            tax += (income - 2400000) * 0.30
            income = 2400000

        if income > 2000000:
            tax += (income - 2000000) * 0.25
            income = 2000000

        if income > 1600000:
            tax += (income - 1600000) * 0.20
            income = 1600000

        if income > 1200000:
            tax += (income - 1200000) * 0.15
            income = 1200000

        if income > 800000:
            tax += (income - 800000) * 0.10
            income = 800000

        if income > 400000:
            tax += (income - 400000) * 0.05
            income = 400000

        Cess
        tax += tax * 0.04

        return tax

user_income = float(input("Enter your annual income in ₹: "))

tax_amount = calculate_tax(user_income)

print(f"\nYour total tax on ₹{user_income:,.2f} is ₹{tax_amount:,.2f}")
