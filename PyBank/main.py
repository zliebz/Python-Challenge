#import packages
import os
import csv

#Path to csv file, "Budget Data"
budget_csv = os.path.join('Resources', 'Budget_Data.csv')

#Define Lists & Variables to be used
months = []
pl_changes = []
month_count = 0
net_pl = 0
previous_month_pl = 0
current_month_pl = 0
pl_change = 0

#Read & open the file
with open(budget_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:

        month_count += 1

        # Net the total P&L over the total months
        current_month_pl = int(row[1])
        net_pl += current_month_pl

        if (month_count == 1):
            #Then make 
            previous_month_pl = current_month_pl
            continue

        else:
            #Calculate change in P/L, then append each month to the months list that was created
            pl_change = current_month_pl - previous_month_pl

            months.append(row[0])
            #Append P/L change to P/L changes list that was created
            pl_changes.append(pl_change)

            #Equalize this for the next loop
            previous_month_pl = current_month_pl

    #Define sum & average for P/L changes, and define & calcluate highest & lowest P/L changes
    pl_sum = sum(pl_changes)
    avg_pl = pl_sum / month_count

    max_pl_change = max(pl_changes)
    min_pl_change = min(pl_changes)

    #Locate index of Max & Min P/L Changes
    max_pl_index = pl_changes.index(max_pl_change)
    min_pl_index = pl_changes.index(min_pl_change)

    best_month_profit = months[max_pl_index]
    worst_month_loss = months[min_pl_index]

    #Print the Financial summary/analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: " + str(month_count))
    print(f"Total: ${net_pl}")
    print(f"Average Change: ${avg_pl}")
    print(f"Greatest Increase in Profits: {best_month_profit} ${max_pl_change}")
    print(f"Greatest Decrease in Losses: {worst_month_loss} ${min_pl_change}")

    #Write analysis into txt file
    budget_file = os.path.join("Analysis", "analysis.txt")
    with open(budget_file, "w") as outfile:

        outfile.write("Financial Analysis")
        outfile.write("----------------------------")
        outfile.write(f"Total Months: " + str(month_count))
        outfile.write(f"Total: ${net_pl}")
        outfile.write(f"Average Change: ${avg_pl}")
        outfile.write(f"Greatest Increase in Profits: {best_month_profit} ${max_pl_change}")
        outfile.write(f"Greatest Decrease in Losses: {worst_month_loss} ${min_pl_change}")


