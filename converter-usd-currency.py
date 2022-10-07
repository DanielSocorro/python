def converter(type_cad, dollar_value):
    dollar_cad = input("how much " + type_cad + " you have:? ")
    dollar_cad = float(dollar_cad)
    dollars = dollar_cad / dollar_value  
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " dollars")

menu =  """ 
Welcome to the currency converter 💰💰💰
1 - Canadien Dollar
2 - Chilean Peso
3 - Pounds

Choose an option: """
   
option = int(input(menu))

if option == 1:
  converter("Canadian Dollar", 1.37)
elif option == 2:
    converter("Chilean Peso", 938)
elif option == 3:
    converter("Pounds", 0.90)
else:
    print("choose a valid option please")


