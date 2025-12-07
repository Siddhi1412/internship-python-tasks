def monthly_report(expenses, month, year):
    print(f"\n===== Monthly Report for {month}/{year} =====")

    total = 0
    found = False

    for exp in expenses:
        date, category, amount, note = exp

        # date is DD-MM-YYYY
        exp_day, exp_month, exp_year = date.split("-")

        if exp_year == year and exp_month == month:
            print(f"{date} | {category} | ₹{amount} | {note}")
            total += float(amount)
            found = True

    if not found:
        print("No expenses found for this month.")
    else:
        print("-----------------------------------")
        print(f"Total for {month}/{year}: ₹{total}")
