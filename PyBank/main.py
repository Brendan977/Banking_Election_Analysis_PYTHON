import os
import csv

csv_path = os.path.join('Resources', 'budget_data.csv')

print("Financial Analysis")
print("-------------------------------------")

months = []
net_total = []
avg_change = []


with open(csv_path) as csvfile:

    csvreader= csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        #Total Months
        months.append(row[0])
        #Net Total
        net_total.append(int(row[1]))
        #Average Change
        avg_change.append(int(row[1]))
    print(f'Total Months: {len(months)}')
    print(f'Total: ${sum(net_total)}')
    print(f'Average Change: $')


  
        
    



    


