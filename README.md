#Election Analysis

##Overview and purpose

Performed election analysis for three Colorado counties: Arapahoe, Denver, and Jefferson. Raw data was provided by the Coloardo Board of Elections. Analysis was to determine number of votes each candidate received as well the percentage for each candidate in relation to the total number of votes casted. Additionally, number and percentage of votes against each county was extracted from the same set of data. 

##Outcomes. 

A total of 369,711 votes were casted in the elections. Winner bagged 73.8% of the total votes with 272,892 votes. The county with biggest turnout was Denver; 82.8% of the votes were casted in Denver county. Jefferson and Arapahoe account for 10.5% and 6.7% of the votes respectively. Elections winner is Diana DeGette.  Below is a snapshot of the outcomes. 

​	-Total numer of  votes casted: 369,711

​	-Election Winner: Diana DeGette.

​	-County with largest  turnout: Denver. 

#Modifying this code for future use

This code is designed to extract data of same structure from a CSV file and then perform analysis. For future use the raw data file can be placed in a root folder that contains the sub folder folder for the code. Incase the file name is changed to reflect the election year the code insidne the last two set of parentheses in line 10 needs to change accordingly. Currently the file for raw data is named 'election_results.csv'. If you are not comfortable changing the code you can change folder names in which you place the file to reflect the appropriate election year. Similary,  if you want to change the output file to a different name you can change it in the code in line 12. 

​	file_to_load = os.path.join("..", "Resources", "election_results.csv")

​	file_to_save = os.path.join("analysis", "election_analysis.txt")
End
