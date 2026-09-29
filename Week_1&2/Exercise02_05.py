subtotal = float(input("Enter the subtotal: "))
rate = float(input("Enter the gratuity rate: "))

gratuity = subtotal * rate / 100
total = subtotal + gratuity

print("The gratuity is", gratuity,
      "and the total is", total )


