menu =  """ 
Welcome to the currency converter 💰💰💰
1 - Canadien Dollar
2 - Chilean Peso
3 - Pounds

Choose an option: """
   
option = int(input(menu))

if option == 1:
    dollar_cad = input("how much Canadian Dollars you have:? ")
    dollar_cad = float(dollar_cad)
    dollar_value = 1.37
    dollars = dollar_cad / dollar_value  
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " dollars")
elif option == 2:
    chilean_peso = input("how much Chilean Pesos you have:? ")
    chilean_peso = float(chilean_peso)
    dollar_value = 938
    dollars = chilean_peso / dollar_value  
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " dollars")
elif option == 3:
    pounds = input("how much pounds you have:? ")
    pounds = float(pounds)
    dollar_value = 0.90
    dollars = pounds / dollar_value  
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " dollars")
else:
    print("choose a valid option please")


