# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join('..', 'Resources', 'election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # To do: read and analyze the data here.

    headers = next(file_reader)
    print(headers)

    ########
    #for row in file_reader:

     #   print(row)
#To do: Perform Analysis

#Read the file object with the reader function


#with open(file_to_load) as election_Data:
    #file_reader = csv.reader(election_data)
    # print each row in the csv file
#e = file_reader

#Close file




# The data we need to retrieve. 

#1. The total number of votes cast. 
#2. A complete list of candidates who received votes. 
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won 
#5. The winnder of the election nbased on popular vote. 
