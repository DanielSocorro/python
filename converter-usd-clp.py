dollars = input("how much dollars you have:? ")
dollars = float(dollars)
pound_value = 0.0011
pounds = dollars / pound_value
pounds = round(pounds)
pounds = str(pounds)
print("You have $" + pounds + " pounds")