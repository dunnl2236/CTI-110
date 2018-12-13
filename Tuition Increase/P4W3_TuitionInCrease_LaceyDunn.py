# Tuition Increase
# 12/03/2018
# CTI-110 P4HW3-Tuition Increase
# Lacey Dunn 


# enter tuition $8,000.00

# totalTuition=(tuition*.03)

# print("Year of Tuition increase: ", format(tuition .00))
    
# print("Year:", totalTuition)

tuition=8000

for totalTuition in range(1, 6):
    tuition+=(3/100)*tuition
    print("Year:", totalTuition,"\t","Tuition Amount: $", format(tuition, ".2f"))
    
    
   
