class Account:
    def __init__(self, balance, account_type):
        self.balance = balance
        self.account_type = account_type

    def get_funds(self):
        return self.balance

    @staticmethod
    def from_csv_string(record):
        record = record.split(',')
        return Account(float(record[1]), record[2])

    def deposit(self, amount):
        return self.balance + amount

    def check_withdraw(self, amount):
        if self.balance - amount > 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError

    def get_standing(self):
        if self.balance >= 1000:
            return True
        else:
            return False



# if __name__ == '__main__':
