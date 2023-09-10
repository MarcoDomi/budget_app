
class budget:
    monthly_income = 0.0
    expense_count = 0
    expense_names = []
    expense_amounts = []
    total_expense_amount = 0.0
    
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        
    def set_monthly_income(self,value) -> None:
        try:
            self.monthly_income = float('%.2f'%value)
        except ValueError:
            print("Non-numerical values are not valid.")

    def add_expense(self, name, amount):
        self.expense_names += [name]

        amount = float("{:.2f}".format(amount))
        self.expense_amounts += [amount]
        self.total_expense_amount += amount
        self.expense_count += 1


    def print_expenses(self):
        print(self.first_name, self.last_name)
        total_len = len(self.first_name) + len(self.last_name)
        print("-"*(total_len + 1)) #add 1 to length so the dash bar length matches the length of first and last name

        for i in range(self.expense_count):
            str_amount = str(self.expense_amounts[i])
            second_to_last = len(str_amount) - 2
            if str_amount[second_to_last] == '.': #if the second to last index is a decimal then append a 0
                str_amount += '0'

            print(f"{self.expense_names[i]}: ${str_amount}")

        self.total_expense_amount = round(self.total_expense_amount, 2)
        print(f"Total expenses: ${self.total_expense_amount}")



#b = budget("max","domi")
#b.set_monthly_income(4.33)
#b.print_expenses()

