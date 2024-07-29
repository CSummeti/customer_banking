# customer_banking

from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    # Prompt the user for savings account details
    print("Savings Account:")
    savings_balance = float(input("Enter the balance for the savings account: "))
    savings_interest_rate = float(input("Enter the interest rate for the savings account: "))
    savings_months = int(input("Enter the number of months for the savings account: "))
    
    # Call the create_savings_account function
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate)
    
    # Print the interest earned and updated savings account balance
    print(f"Savings Account - Interest Earned: {savings_interest_earned:.2f}")
    print(f"Savings Account - Updated Balance: {updated_savings_balance:.2f}\n")
    
    # Prompt the user for CD account details
    print("CD Account:")
    cd_balance = float(input("Enter the balance for the CD account: "))
    cd_interest_rate = float(input("Enter the interest rate for the CD account: "))
    cd_months = int(input("Enter the number of months for the CD account: "))
    
    # Call the create_cd_account function
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate)
    
    # Print the interest earned and updated CD account balance
    print(f"CD Account - Interest Earned: {cd_interest_earned:.2f}")
    print(f"CD Account - Updated Balance: {updated_cd_balance:.2f}")

# Call the main function
if __name__ == "__main__":
    main()


