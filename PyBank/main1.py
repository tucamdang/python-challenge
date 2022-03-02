#import modules
import os
import csv

#set path for file
budget_csv = os.path.join("Resources", "budget_data.csv")

#Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
revenue_changes = []
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0


#open the csv file
with open(budget_csv) as csvfile:  
    csvreader = csv.DictReader(csvfile)

    #Loop through to find total months
    for row in csvreader:

        #Count the total of months
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        #Calculate the average change in revenue between months over the entire period
        revenue_change = int(row["Profit/Losses"])- previous_revenue
        previous_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row["Date"]]
       
# append each revenue_change to the revenue_changes[]
        revenue_changes.append(revenue_change)

        #The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row['Date']
        
#sum and average of the changes in "profit/losses" over entire period
sum_profit_loss = sum(revenue_changes)   
net_total_months = total_months - 1   
revenue_average = round(sum_profit_loss/(net_total_months),2)
    
    # print result
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total : ${total_revenue}")
print(f"Average change : ${revenue_average}")
print([f"Greatest Increase in Revenue:  {greatest_increase[0]}, (${greatest_increase[1]})"])
print([f"Greatest Decrease in Revenue:  {greatest_decrease[0]}, (${greatest_decrease[1]}"])

#set the output of the text file
output_file = "Analysis1.txt"

# open output file, create/ write
with open(output_file, 'w') as writer:
    writer = csv.writer(writer)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["--------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${total_revenue}"])
    writer.writerow([f"Average Change: ${round(revenue_average)}"])
    writer.writerow([f"Greatest Increase in Revenue:  {greatest_increase[0]}, (${greatest_increase[1]})"])
    writer.writerow([f"Greatest Decrease in Revenue:  {greatest_decrease[0]}, (${greatest_decrease[1]})"])