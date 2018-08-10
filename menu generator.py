import random
print("")
print("Welcome to Herierto Conley's Restaurant!")
print("Conley: My name is Conley and I will be your server for today.")
print("Conley: Right this way please.")
app = ["Salad", "Bread", "Garlic Sticks"]
main = ["Roast Beef", "Beef Hamburger", "Spaghetti", "Orange Chicken"]
side = ["Garlic Bread", "Carrots", "None"]
dessert = ["Cookie", "Choco Cake", "S'mores bar" "Ice cream"]
drink = ["Ocha", "Water", "Soda", "Iced tea", "No thank you"]
review = ["The meal was good! You leave a 5star review on Yelp", "The meal was terrible! You throw up in the bathroom and decide to never return."]

print("In front of you is a MENU.")
print("Print 'open' to open the MENU")
answer = input()
if answer == "open":
    print("")
    print("Conley: What APPETIZER can we get started for you?")
    print(random.choice(app))
    print("")
    print("Conley: Great! What would you like as the MAIN DISH?")
    print(random.choice(main))
    print("")
    print("Conley: Excellent choice! Would you like a SIDE?")
    print(random.choice(side), "please")
    print("")
    print("Conley: Would you like a DRINK with that?")
    print(random.choice(drink))
    print("")
    print("Conley: and what would you like for DESSERT?")
    print(random.choice(dessert))
    print("")
    print("")
    print("Conley: Alright that's all! Your order will be served shortly, enjoy your meal!")
print("...")
print("...")
print("...")
print("...")
print("...")
print("......")
print(random.choice(review))
