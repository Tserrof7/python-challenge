# -*- coding: UTF-8 -*-


# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll\\Resources\\election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll\\analysis\\election_data.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
vote_count = {}   # Dictionary to store candidates and their vote counts

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:


        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the vote_count dictionary, add them
        if candidate_name not in vote_count:
            vote_count[candidate_name] = 0

        # Add a vote to the candidate's count
        vote_count[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Election Results")
    print(f"--------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"--------------------------")
    # Write the total vote count (to text file)
    txt_file.write(f"Election Results\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"----------------------------\n")
    # Initialize variables to track the winning candidate's details
    winning_candidate = ""
    winning_vote_count = 0
   

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in vote_count.items():
        # Get the vote percentage
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_vote_count:
            winning_vote_count = votes
            winning_candidate = candidate


        # Print each candidate's vote count and percentage
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    # Print and save the winning candidate summary
    print(f"--------------------------")
    print(f"Winner: {winning_candidate}")

    print(f"--------------------------")
  
    txt_file.write("\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write(f"----------------------------\n")
