def calculate_total_interest(principal, annual_rate, monthly_payment):
    # Convert annual rate to monthly rate
    monthly_rate = annual_rate / 12 / 100
    
    # Initialize variables
    total_interest = 0
    remaining_balance = principal
    months = 0
    
    while remaining_balance > 0:
        # Calculate interest for the current month
        interest_payment = remaining_balance * monthly_rate
        # Calculate principal payment for the current month
        principal_payment = monthly_payment - interest_payment
        # Update remaining balance
        remaining_balance -= principal_payment
        # Accumulate total interest paid
        total_interest += interest_payment
        # Increment the month counter
        months += 1
        
        # Break if the loan is paid off
        if remaining_balance <= 0:
            break
    
    return total_interest, months

# Example usage
principal = 20000  # Principal loan amount
annual_rate = 6    # Annual interest rate in percent
monthly_payment = 386.66  # Monthly payment amount

total_interest, total_months = calculate_total_interest(principal, annual_rate, monthly_payment)
print(f"Total interest paid: ${total_interest:.2f}")
print(f"Total months to pay off: {total_months}")
