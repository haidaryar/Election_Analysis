# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
from http.client import CannotSendRequest
import os
from tkinter import N
# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
# 1: Create a county list and county votes dictionary.
county_list = []
county_dict = {}
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0 
# Track the winning candidate, vote count and percentage
winning_candidate = ""
# 2: Track the largest county and county voter turnout.
winning_count = 0
winning_percentage = 0
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)
    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row. ######
        county_name = row[1]


        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

 
        if county_name not in county_list:
            county_list.append(county_name)
            county_dict[county_name] = 0 
        county_dict[county_name] += 1
# Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count (to terminal)
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")
        txt_file.write(election_results)
        # 6a: Write a for loop to get the county from the county dictionary.
        for county_name in county_dict:
                votes = county_dict.get(county_name)
                percentage_for_ct = float(votes) / float(total_votes) * 100
                county_results = (
                    f"{county_name}: " 
                    f"{percentage_for_ct:.1f}% " 
                    f"({votes:,})\r\n")

             
                print(county_results)
                txt_file.write(county_results)
                

                if (votes > winning_county_count): 
                            winning_county_count = votes 
                            winning_county = county_name
                            
        turnout_summary = (

               
            f"\n-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n\n")
        
        print()
        print(turnout_summary)
        txt_file.write(turnout_summary)
        # 8: Save the county with the largest turnout to a text file.
        for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
                votes = candidate_votes.get(candidate_name)
                vote_percentage = float(votes) / float(total_votes) * 100
                candidate_results = (
                    f"{candidate_name}: "
                    f" {vote_percentage:.1f}% " 
                    f" ({votes:,})\n\n")
                print(candidate_results)
                #  Save the candidate results to our text file.
                txt_file.write(candidate_results)
                # Determine winning vote count, winning percentage, and candidate.
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                            winning_count = votes
                            winning_candidate = candidate_name
                            winning_percentage = vote_percentage
                                                # Print the winning candidate (to terminal)
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)