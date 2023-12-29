import os
import csv
import numpy as np

csv_path = os.path.join('Resources', 'budget_data.csv')

print("Financial Analysis")
print("-------------------------------------")

months = []
net_total = []
p_l = []
change = []

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        # Total Months
        months.append(row[0])
        # Net Total
        net_total.append(int(row[1]))
        # Profit/Loss
        p_l.append(int(row[1]))

    for a, b in zip(p_l[:-1], p_l[1:]):
        # Average Change
        change.append(b - a)

    # Calculate statistics
    total_months = len(months)
    total_net = sum(net_total)
    avg_change = round(np.mean(change), 2)

    increase = max(change)
    increase_month = months[change.index(increase) + 1]

    decrease = min(change)
    decrease_month = months[change.index(decrease) + 1]

    # Print the results
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_net}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {increase_month} (${increase})')
    print(f'Greatest Decrease in Profits: {decrease_month} (${decrease})')

    # Write to output file
    output_file = os.path.join('analysis', 'pybank_result.csv')
    with open(output_file, "w") as datafile:
        datafile.write("Financial Analysis\n")
        datafile.write("-------------------------------------\n")
        datafile.write(f'Total Months: {total_months}\n')
        datafile.write(f'Total: ${total_net}\n')
        datafile.write(f'Average Change: ${avg_change}\n')
        datafile.write(f'Greatest Increase in Profits: {increase_month} (${increase})\n')
        datafile.write(f'Greatest Decrease in Profits: {decrease_month} (${decrease})\n')


