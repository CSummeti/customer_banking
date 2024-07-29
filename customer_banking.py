# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    print("Savings Account:")
    # Prompt the user for savings account details
    savings_balance = float(input("Enter the balance for the savings account: "))
    savings_interest_rate = float(input("Enter the interest rate for the savings account: "))
    savings_months = int(input("Enter the number of months for the savings account: "))
    
    # Call the create_savings_account function and pass the variables from the user
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)
    
    # Print the interest earned and updated savings account balance
    print(f"Updated Savings Account Balance: {updated_savings_balance:.2f}")
    print(f"Savings Interest Earned: {savings_interest_earned:.2f}")

    print("\nCD Account:")
    # Prompt the user for CD account details
    cd_balance = float(input("Enter the balance for the CD account: "))
    cd_interest_rate = float(input("Enter the interest rate for the CD account: "))
    cd_months = int(input("Enter the number of months for the CD account: "))
    
    # Call the create_cd_account function and pass the variables from the user
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)
    
    # Print the interest earned and updated CD account balance
    print(f"Updated CD Account Balance: {updated_cd_balance:.2f}")
    print(f"CD Interest Earned: {cd_interest_earned:.2f}")

if __name__ == "__main__":
    # call the main function.
    main()
