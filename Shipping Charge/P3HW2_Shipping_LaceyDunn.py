# Shipping Charges
# 11/08/2018
# CTI-110 P3HW2-Shipping Charges
# Lacey Dunn

# get number of packages and weight

weightPackages=float(input("Enter package weight: "))

# calculate price


if weightPackages <=2:
    shippingCharge = 1.50
elif weightPackages <=7:
    shippingCharge = 3.00
elif weightPackages <=11:
    shippingCharge = 4.00
elif weightPackages >11:
    shippingCharge =4.75
print("For a package weighing " + str(weightPackages)+ ", You'll Pay $" + \
      format(shippingCharge, ",.2f"))
      
 
