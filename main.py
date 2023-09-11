from budget import budget


my_budget = budget("Marco", "Dominguez")

expense_file = open("expenses.txt")
for line in expense_file:
    data = line.split(' ')
    expense_name = data[0]
    expense_amount = float(data[1])
    my_budget.add_expense(expense_name, expense_amount)

expense_file.close()

my_budget.set_monthly_income(100.93)
my_budget.print_expenses()