def get_user_input():
    house = float(input("Enter your monthly housing expense: "))
    transport = float(input("Enter your monthly transportation expense: "))
    health = float(input("Enter your monthly healthcare expense: "))
    fun = float(input("Enter your monthly entertainment expense: "))
    edu = float(input("Enter your educational expense: "))
    exp = [house, transport, health, fun, edu]
    print("Here are your categorywise monthly expenses: ")
    print(f"Housing Expense: {house} Rs") 
    print(f"Transportation Expense: {transport} Rs")
    print(f"Healthcare Expense: {health} Rs")
    print(f"Entertainment Expense: {fun} Rs")
    print(f"Educational Expense: {edu} Rs")

    n = input("Do you want your monthly summary of expenses? (y/n)")
    if n == "y":
        print("Monthly summary of your expenses: ")
        print(f"Maximum spending in the month: {max(exp)} Rs")
        print(f"Minimum spending in the month: {min(exp)} Rs")
        print(f"Average spending in the month: {sum(exp)/5} Rs")
        print(f"Total spending in the month: {sum(exp)} Rs");
    else:
        pass

def main():
    print("WELCOME TO EXPENSE TRACKER! ")
    user_input = get_user_input()   

if __name__ == "__main__":
    main()