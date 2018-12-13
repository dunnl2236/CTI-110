# Bug Collector
# 12/03/2018
# CTI-110 P4T2-Bug Collector
# Lacey Dunn 

# set total to 0
# set loop: 7 days
    # input bugs collected by day
    # add bugs collected per day to total
# display total

total=0

for day in range(1,8):
    print('Enter the bugs collected on day',day,':')
    bugs=int(input())
    total+=bugs
print('You collected a total of', total, 'bugs.')  

    

