
class budget:
    monthly_income = 0.0
    expense_count = 0
    expense_names = []
    expense_amounts = []
    total_expense_amount = 0.0
    
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
      
        
    def set_monthly_income(self,value:float) -> None:
        if self.__is_valid_amount(value):
            self.monthly_income = value
        else:
            print("Invalid monthly income")


    def add_expense(self, name:str, amount:float):
        if self.__is_valid_amount(amount):
            self.expense_names += [name]
            self.expense_amounts += [amount]
            self.total_expense_amount += amount
            self.expense_count += 1
        else:
            print("Invalid expense amount.")


    def print_expenses(self):
        print(self.first_name, self.last_name)
        str_monthly_income = self.__append_zero(str(self.monthly_income))
        print(f"Monthly Income: ${str_monthly_income}")

        total_len = len(self.first_name) + len(self.last_name)
        print("-"*(total_len + 1)) #add 1 to length so the dash bar length matches the length of first and last name

        for i in range(self.expense_count):
            str_amount = str(self.expense_amounts[i])
            str_amount = self.__append_zero(str_amount)
            print(f"{self.expense_names[i]}: ${str_amount}")

        print(f"Total expenses: ${self.total_expense_amount}")


    def __append_zero(self, str_amount:str):
        second_to_last = len(str_amount) - 2
        if str_amount[second_to_last] == '.': #if the second to last index is a decimal then append a 0
            str_amount += '0'
        return str_amount
        

    def __is_valid_amount(self,value:float) -> bool:
        '''check if a floating point value has no more than 2 values after the decimal point'''
        str_value = str(value) 

        decimal_index = str_value.find('.') 
        after_decimal = decimal_index + 1

        return len(str_value[after_decimal:]) <= 2
