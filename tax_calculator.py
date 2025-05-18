def calculate(amount, percent):
    return (amount * percent) / 100

def calculate_income_tax(total_income: 
                         float) -> float:

    if total_income <= 1200000:
        return 0
    elif total_income <= 400000:
        return calculate(total_income - 
                         400000, 0)
    elif total_income <= 800000:
        return calculate(total_income - 
                         400000, 5) 
    elif total_income <= 1200000:
        return calculate(total_income - 
                         800000, 10)
    elif total_income <= 1600000:
        return calculate(total_income - 
                         1200000, 15) 
    elif total_income <= 2000000:
        return calculate(total_income - 
                         1600000, 20)
    elif total_income <= 2400000:
        return calculate(total_income - 
                         2000000, 25)      
    else:
        return calculate(total_income - 
                         2400000, 30)


if __name__ == '__main__':
    total_income = float(input("What's your \
                    annual income?\n>>> "))
    tax = calculate_income_tax(total_income)
    print(f"Total tax applicable at \
                    ₹{total_income} is ₹{tax}")
