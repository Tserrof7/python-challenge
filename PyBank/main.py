# -*- coding: UTF-8 -*-


# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources\\budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis\\budget_data.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
changes = [] # List to store monthly changes
dates = [] # List to store corresponding dates for changes
previous_profit = None
greatest_increase = {"date": None, "amount": float('-inf')}
greatest_decrease = {"date": None, "amount": float ('inf')}

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        date = row[0]
        current_profit = int(row[1])

        # Track the total
        total_months += 1
        total_net += current_profit

        # Track the net change
        if previous_profit is not None:
            change = current_profit - previous_profit
            changes.append(change)
            dates.append(date)

        # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase["amount"]:
                    greatest_increase = {"date": date, "amount": change}

        # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease["amount"]:
                 greatest_decrease = {"date": date, "amount": change}
        
        #Update previous profit and loss
        previous_profit = current_profit


# Calculate the average net change across the months
average_change = sum(changes) / len(changes) if changes else 0

# Generate the output summary
output = (
     f"Financial Analysis\n"
     f"--------------------------\n"
     f"Total Months: {total_months}\n"
     f"Total: ${total_net}\n"
     f"average Change ${average_change: .2f}\n"
     f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
     f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
