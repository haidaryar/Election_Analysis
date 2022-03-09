#Import Dependencies
import csv
import os

# The data we need to retrieve
#file_to_load = "users/waheedhaidaryar/Documents/Data_Analytics_Bootcamp_2022/Projects/Election_Analysis/Resources/election_results.csv"

file_to_load = os.path.join("..", "Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")
election_data = open(file_to_load, 'r')
total_votes = 0 
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0 


candidate_votes["Charles Casper Stockham"] = 85213
candidate_votes["Diana DeGette"] = 272892
candidate_votes["Raymon Anthony Doane"] = 11606

    #Open Election Results
with open(file_to_load) as election_data:
    #Perform_Analysis
    #Read and Analyze Data

    file_reader = csv.reader(election_data)

    #print header row
    headers = next(file_reader)

   
    for row in file_reader:
        total_votes +=1 
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


# Winning Vote Count + Percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage 
        

        winning_candidate_summary = (
            f"------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------------\n")
        print(winning_candidate_summary)

with open(file_to_save, 'w') as txt_file:
    
    
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)
                
            # Dictionary is causing the code not to run properly
        
    for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage 
                winning_candidate = candidate_name
    
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)

    txt_file.write(winning_candidate_summary)

           

   