class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        self._account_balance += amount

    def withdraw(self, amount):
        """Withdraws the specified amount if there are sufficient funds.
        Returns True if successful, otherwise returns False.
        """
        if amount > self._account_balance:
            return False
        else:
            self._account_balance -= amount
            return True

    def display_balance(self):
        """Prints the current account balance."""
        print(f"Current balance: ${self._account_balance:.2f}")
