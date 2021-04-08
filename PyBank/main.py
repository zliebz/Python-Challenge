# Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

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

#Find current directory of file
cwd = os.path.dirname("budget_data.csv")

#Path to csv file, "Budget Data"
budget_data_csv = os.path.join(cwd, "budget_data.csv")

#Read & open the file
with open(budget_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Read CSV header first
    csv_header = next(csvfile)

    for row in csvfile:

        #Count of months
        month_count += 1

        this_month_profit_loss = int(row[1])
        net_profit_loss += this_month_profit_loss

        if (month_count == 1):
            last_month_profit_loss = this_month_profit_loss
        else:
            profit_loss_change = this_month_profit_loss - last_month_profit_loss

            months.append(row[0])

            profit_loss_changes.append(profit_loss_change)

            last_month_profit_loss = this_month_profit_loss

