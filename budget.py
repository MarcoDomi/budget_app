
class budget:
    income = 0.0
    expense_count = 0
    expenses = {}
    total_expense_amount = 0.0
    
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
      
        
    def set_income(self,value:float) -> None:
        if self.__is_valid_amount(value):
            self.income = float(value)
        else:
            print("Invalid monthly income")


    def add_expense(self, name:str, amount:float):
        name = name.lower()
        if self.__is_valid_amount(amount):
            if name in self.expenses:
                self.expenses[name] += float(amount)
            else:
                self.expenses[name] = float(amount)
            self.total_expense_amount += float(amount)
            self.expense_count += 1
        else:
            print("Invalid expense amount.")


    def print_expenses(self):
        print(self.first_name, self.last_name)
        str_income = self.__append_zero(self.income)
        print(f"Monthly Income: ${str_income}")

        print("-"*(15)) #print dash bar

        for category in self.expenses:
            str_amount = str(self.expenses[category])
            str_amount = self.__append_zero(str_amount)
            print(f"{category}: -{str_amount}")
        str_total_amount = self.__append_zero(self.total_expense_amount)
        print(f"Total expenses: ${str_total_amount}")

        print("-"*(15))

        remaining_income = self.income - self.total_expense_amount
        remaining_income = round(remaining_income,2)
        str_remaining_income = self.__append_zero(remaining_income)
        print(f"Remaining income: ${str_remaining_income}")


    def __append_zero(self, amount:float):
        '''appends a zero to a numerical string if needed'''
        str_amount = str(amount)
        second_to_last = len(str_amount) - 2
        if str_amount[second_to_last] == '.': #if the second to last index is a decimal then append a 0
            str_amount += '0'
        return str_amount
        

    def __is_valid_amount(self,value:float) -> bool:
        '''check if a floating point value has no more than 2 values after the decimal point'''
        str_value = str(float(value))
        after_decimal = str_value.find('.') + 1 #find the index that is after the decimal

        return len(str_value[after_decimal:]) <= 2
