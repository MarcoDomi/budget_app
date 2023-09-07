
class budget_app:
    income = 0.0
    expense_name = []
    expenses_amount = []
    total_expense_amount = 0.0
    
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        
    def set_income(self,value) -> None:
        try:
            self.income = float('%.2f'%value)
        except ValueError:
            print("Non-numerical values are not valid.")

    def add_expense(self, name, amount):
        pass


        
b = budget_app("max","domi")
b.set_income(4.33)
print(b.income)
