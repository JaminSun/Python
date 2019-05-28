Product = input("Enter a product:")
Price = input("What is the price of the product entered?")
Qty = input("What is the Quantity?")
Amount = int(Qty) * float(Price)
VAT = Amount *  15 / 100
Bill = Amount + VAT
print ("Your Bill:")
print (Product)
print (Amount)
print (VAT)
print (Bill)