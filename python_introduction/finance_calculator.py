# finance_calculator.py

# Prompt the user for their financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with a fixed 5% interest rate
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings after 1 year (including 5% interest) are: ${annual_savings:.2f}")
