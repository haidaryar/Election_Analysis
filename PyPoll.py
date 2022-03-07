#Import Dependencies
import csv
import os

# The data we need to retrieve
#file_to_load = "users/waheedhaidaryar/Documents/Data_Analytics_Bootcamp_2022/Projects/Election_Analysis/Resources/election_results.csv"
file_to_load = os.path.join("..", "Resources", "election_results.csv")
election_data = open(file_to_load, 'r')
total_votes = 0 
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0 


candidate_votes["Charles Capser Stockham"] = 85213
candidate_votes["Diana DeGette"] = 272892
candidate_votes["Raymon Anthony Doane"] = 11606



#Dictionary with keys 


#votes = total_votes #Testing Code

    #Open Election Resultsn
with open(file_to_load) as election_data:
    #Perform_Analysis
    print(election_data)
    #Read and Analyze Data

    file_reader = csv.reader(election_data)

    #print header row
    headers = next(file_reader)
    print(headers)
   
    for row in file_reader:
        total_votes +=1 
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

                
            # Dictionary is causing the code not to run properly
        
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage 
            winning_candidate = candidate_name

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning  Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)

    


        #print(f"{candidate_name}: received {vote_percentage}% of the vote")


    #Print each row in the CSV file

    #Create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, 'w') as txt_file:

    txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")

#print(candidate_options)
#print(candidate_votes)






#print(candidate_votes)
#print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    #write results using open() function with "w"
    



    #Close the file



# 1. The total number of votes cast. 
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidates won
# 5. The winner of the election
