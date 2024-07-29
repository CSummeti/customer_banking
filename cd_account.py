"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
# cd_account.py
import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.
    
    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        float: The interest earned.
    """
    # Create an instance of the Account class with the provided balance and an initial interest rate of 0
    cd_account = Account(balance, 0)
    
    # Set the interest rate to the provided value
    cd_account.set_interest_rate(interest_rate)
    
    # Calculate the interest earned
    interest_earned = balance * (interest_rate / 100 * months / 12)
    
    # Update the balance with the earned interest
    updated_balance = cd_account.balance + interest_earned
    
    # Pass the updated balance to the set balance method using the instance of the Account class
    cd_account.set_balance(updated_balance)
    
    # Return the updated balance and interest earned
    return updated_balance, interest_earned
