print("---welcome!---")


stock = {
    "tablet": 5000,
    "iphone-18": 10000,
    "charger": 1000
}

def calculate(stock, name, quantity):
    total = stock[name] * quantity
    return total

total_investment = 0

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio\n")
                                      
    while True:

        name = input("enter stock name : ").strip().lower()
        quantity = int(input("enter quantity: "))
        if name in stock:
            result = calculate(stock, name, quantity)

            print(f"Total for {name}:${result}")
            total_investment = total_investment + result
            file.write(
                f"{name} x {quantity} = ${result:,}\n"
            )
            again = input(
                "Do you want to add another stock? (yes/no): ").strip().lower()
            if again == "no":
                print(f"total investment: ${total_investment}")
                file.write(
                    f"Total investment: ${total_investment:,}\n"
                )

                break
        else:
            print("stock not found.please enter available stock")
