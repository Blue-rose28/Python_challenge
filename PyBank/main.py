# Code for Pybank 
#import data file from csv
import csv 
import os

#make file path and open file
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #initialize variables
    header = next(csvreader)
    total_months = 0
    total_profit = 0.0
    delta = []
    greatest_profit = 0.0
    greatest_profit_month = ""
    greatest_loss = 0.0
    greatest_loss_month = ""
    #x is a storage variable for calulating the profil/loss change
    x = 0.0
#loop through each row and do the calculations
    for row in csvreader:
        #total profit up to row
        total_profit += float(row[1])
        #add profit/loss change to list
        delta.append(float(row[1])-x)
        #update storage variable 
        x = float(row[1])
        #check if it's the greatest profit, if not check if it's the greatest loss
        if delta[total_months] > greatest_profit:
            greatest_profit = delta[total_months]
            greatest_profit_month = row[0]
        elif delta[total_months] < greatest_loss:
            greatest_loss = delta[total_months]
            greatest_loss_month = row[0]
        #track number of months - this is last in the loop because this doubles as the index for delta
        total_months += 1

#calculate average of profit change
y = 0
for x in range(85):
    a = delta[x+1]
    y = y + a
    average_change = y/(total_months-1)

#output to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + greatest_profit_month + " (" + str(greatest_profit) + ")")
print("Greatest Decrease in Profits: " + greatest_loss_month + " (" + str(greatest_loss) + ")")

# Export output to .txt file
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, 'w') as output:
    output.write("Financial Analysis\n----------------------------\n")
    output.write("Total Months: " + str(total_months))
    output.write("\nTotal: $" + str(total_profit))
    output.write("\nAverage Change: $" + str(round(average_change, 2)))
    output.write("\nGreatest Increase in Profits: " + greatest_profit_month + " ($" + str(greatest_profit) + ")")
    output.write("\nGreatest Decrease in Profits: " + greatest_loss_month + " ($" + str(greatest_loss) + ")")