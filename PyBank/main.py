import os
import csv
import numpy as np

csv_path = os.path.join('Resources', 'budget_data.csv')

print("Financial Analysis")
print("-------------------------------------")

months = []
net_total = []
p_l = []
change= []


with open(csv_path) as csvfile:

    csvreader= csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        #Total Months
        months.append(row[0])
        #Net Total
        net_total.append(int(row[1]))
        #Average Change(pt.1)
        p_l.append(int(row[1]))
    for a, b  in zip(p_l[0::], p_l[1::]):
        #Average Change(pt.2)
        change.append(int(b-a))
        avg_change= np.mean(change)
    #Greatest Increase
    increase= max(change)
    #Greatest Decrease
    decrease = min(change)
    print(f'Total Months: {len(months)}')
    print(f'Total: ${sum(net_total)}')
    print(f'Average Change: ${round(avg_change, 2)}')
    print(f'Greatest Increase in Profits: ${increase}')
    print(f'Greatest Decrease in Profits: ${decrease}')


  
        
    



    


