def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_of_months = int(input("How many months? "))

    for month in range(1, num_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(num_of_months, incomes)


def print_income_report(num_of_months, incomes):
    """Print income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
