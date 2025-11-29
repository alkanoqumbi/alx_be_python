
class BankAccount:
    def _init_(self, initial_balance=0.0):
        # Use underscore for encapsulation
        self._account_balance = initial_balance 

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            # FIX: Use += to add the amount
            self._account_balance += amount 
            return True # Return True on success
        return False

    def withdraw(self, amount):
        """Deduct the amount from the account balance if funds are sufficient.
        Returns True if successful, otherwise False."""
        # FIX: Check if amount is positive AND balance is sufficient
        if amount > 0 and amount <= self._account_balance: 
            self._account_balance -= amount
            return True
        return False # Return False if funds are insufficient or amount is invalid

    def display_balance(self):
        """Display the current balance in a user-friendly format."""
        # FIX: Use .2f for currency formatting
        print(f"Current Balance: ${self._account_balance:.2f}")
