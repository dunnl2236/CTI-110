# Celius to Fahrenheit
# 11/30/2018
# CTI-110 P4HW2-Celius to Fahrenheit
# Lacey Dunn 

# Display a table Celsius temperatures 0-20 & their Fahreheit equivalents.
# Formula: f=5/9*c+32

celsius=0

for celsius in range(0, 21, 1):
    #celsius=celsius+count
    fahrenheit=(celsius*9/5)+32
    print("Celsius: ",celsius, '\t',"=      Fahrenheit:",fahrenheit)
