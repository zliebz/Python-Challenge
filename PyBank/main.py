#import packages
import os
import csv

#Define Variables to be used
months = []
total_profit_loss = []
month_count = 0
net_profit_loss = 0
last_month_profit_loss = 0 
this_month_profit_loss = 0
profit_loss_change = 0

#Path to csv file, "Budget Data"
budget_csv = os.path.join('Resources', 'Budget_Data.csv')

#Read & open the file
with open(budget_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:

        #Total Month count
        total_months = len(months)
        print(total_months)