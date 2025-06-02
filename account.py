

# Create a new class Transaction to store all transactions with attributes
#  for date and time, narration, amount, transaction type etc.
# The Account class should have a new attribute called transactions which will 
# store every transaction that happens in the account.
# Each transaction should be stored as an instance of the Transaction
# The get balance method should use the transactions list to compute the current balance
# Add encapsulation to the Account class to have sensitive attributes like balance 
# and account number only accessible via given class methods.

class Transaction:
    def __init__(self, amount, transaction_type, narration):
        self.date_time = datetime.now()
        self.amount = amount
        self.transaction_type = transaction_type
        self.narration = narration
    def __repr__(self):
        return f"{self.date_time} | {self.transaction_type.} | {self.narration} | {self.amount}"
class Account:
    interest_rate = 0.05
    _account_counter = 40000
    minimum_balance = 300
    def __init__(self, owner):
        self.owner = owner
        self.account_number = Account._account_counter
        Account._account_counter += 1
        self.loan = 0
        self.is_frozen = False
        self.closed = False
        self.transactions = []
    def _add_transaction(self, amount, transaction_type, narration):
        self._transactions.append(Transaction(amount, transaction_type, narration))
    def deposit(self, amount):
        if amount <= 0 or self.is_frozen or self.closed:
            return "Invalid deposit."
        self.add_transaction(amount, "Deposit")
        return f"Deposit successful. New balance is {self.get_balance()}"
    def withdraw(self, amount):
        if self.is_frozen or self.closed:
            return "Account  not active."
        if amount <= 0:
            return "Invalid withdrawal amount."
        if self.get_balance() - amount < Account.minimum_balance:
            return "Insufficient funds."
        self.add_transaction(amount,  "Withdrawal")
        return f"Withdrawal successful. New balance is {self.get_balance()}"
    def transfer_funds(self, amount, other_account):
        withdrawal_result = self.withdraw(amount)
        if withdrawal_result.startswith("Withdrawal successful"):
            deposit_result = other_account.deposit(amount)
            if deposit_result.startswith("Deposit successful"):
                return "Transfer successful."
            else:
                self.add_transaction(amount, "Reversed Transfer")
                return f"Transfer failed: {deposit_result}"
        return withdrawal_result
    def request_loan(self, amount):
        if self.is_frozen or self.closed or amount <= 0:
            return "Loan request denied"
        self.loan += amount
        self.add_transaction(-amount,"Loan requested: {amount}")
        return f"Loan of {amount} approved. Current loan is {self.loan}"
    def repay_loan(self, amount):
        if amount <= 0:
            return "Invalid repayment."
        if amount >= self._loan:
            self.add_transaction(self.loan, "you have repaid your loan")
            self.loan = 0
            return "you have repaid your loan."
        else:
            self.loan -= amount
            self.add_transaction(amount,"you have repaid insuffiecient amount for your loan"): {amount}")
            return f"you have repaid insuffiecient amount for your loan. Remaining amount is {self.loan}"
    def get_balance(self):
        balance = sum(txn.amount for txn in self._transactions)
        return balance - self._loan
    def view_account_details(self):
        return f"Owner: {self.owner}, Balance: {self.get_balance()}, Loan: {self._loan}, Account Number: {self._account_number}"
    def change_account_owner(self, new_owner):
        self.owner = new_owner
        return f"Account owner changed to {self.owner}"
    def account_statement(self):
        lines = ["Account Statement:"]
        for transaction in self.transactions:
            lines.append(str(transaction))
        lines.append(f"Current Balance is {self.get_balance()}")
        return "\n".join(lines)
    def apply_interest(self):
        if self.is_frozen or self.closed:
            return "no interest."
        interest = self.get_balance() * Account.interest_rate
        self.add_transaction(interest, 'interest', "Interest Applied")
        return f"Interest of {interest:.2f} applied. New balance is {self.get_balance()}"
    def freeze_account(self):
        self.is_frozen = True
        return "Account has been frozen."
    def unfreeze_account(self):
        self.is_frozen = False
        return "Account has been unfrozen."
    def set_minimum_balance(self, amount):
        Account.minimum_balance = amount
        return f"Minimum balance set to {amount}."
    def close_account(self):
        self.transactions.clear()
        self.loan = 0
        self.closed = True
        return "Your account has been closed and all data have been reset."
    def get_account_number(self):
        return self.account_number
    def get_loan_amount(self):
        return self.loan
    def is_account_frozen(self):
        return self.is_frozen
    def is_account_closed(self):
        return self.closed
    def get_transactions(self):
        return list(self.transactions)