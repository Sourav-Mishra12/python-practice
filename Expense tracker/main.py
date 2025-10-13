

expenses = []

while True:
    print("\n 1) ADD EXPENSES")
    print("\n 2) VIEW EXPENSES")
    print("\n 3) EXIT")
    
    choice = input("ENTER YOUR CHOICE :")
    
    if choice == "1":
        item = input("ENTER THE CATEGORY NAME : ").strip()
        while True:
            try:
                amount = float(input("ENTER THE AMOUNT : "))
                break
            except ValueError:
                print("PLEASE ENTER A VALID NUMBER")

        expenses.append({'category' : item , 'amount' : amount})
        print("EXPENSES ADDED")

    elif choice == "2":
        total = 0 

        if not expenses:
            print("NO EXPENSES TO SHOW")
            
        else:
            for exp in expenses:
                print(f"{exp['category']} : {exp['amount']}")
                total += exp['amount']
                print(f"THE TOTAL EXPENSE IS {total}")

    elif choice == "3":
        print("GOODBYEE")
        break

    else:
        print("INVALID CODE")
