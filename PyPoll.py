## Opening election_results.csv

# import modules (add our dependencies)
import csv
import os

# assign a variable for the csv file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Initialize a total vote counter.
total_votes = 0

# Declare list and print candidate name from each row
candidate_options = []

# Declare candidate votes dictionary for candidate name and votes per candidate
candidate_votes = {}

# Declare a variable that holds empty string for winning candidate
winning_candidate = ""
# Declare a variable for "winning_count" equal to 0
winning_count = 0
# Delcare a variable for "winning_percentage" equal to 0
winning_percentage = 0


# Use with statement to open the csv election results and read the file
with open(file_to_load) as election_data:
 #Read the file object with the reader function
 file_reader = csv.reader(election_data)

 #Read the header row
 headers = next(file_reader)


 # Create a for loop to loop through all rows for candidate and vote information

 #Print each row in the CSV file
 for row in file_reader:

  # add to the total vote count
  total_votes += 1

  # get candidates names from the row 
  candidate_name = row[2]

  # if candidate does not match any existing candidate, create if statement. Within for loop.
  if candidate_name not in candidate_options:
   # add the candidate name to the candidate_options list using append
   candidate_options.append(candidate_name)

   # create each candidate as a key for the dictionary above. Begin tracking candidates vote count.
   candidate_votes[candidate_name] = 0

  # add a vote to each candidates count to find total votes per candidate (inside the for loop)
  candidate_votes[candidate_name] += 1


#Create for loop to determine percentage of votes for each candidate by looping through vote counts

# Iterate through the candidate list
for candidate_name in candidate_votes:
 # Retreive the vote count of the candidate
 votes = candidate_votes[candidate_name]
 # Calculate the percentage of votes
 vote_percentage = float(votes) / float(total_votes) * 100
 #3. Print the candidate name and percentage of votes
 #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")


 #Print out each candidates name, vote count and percentage of votes to termincal

 #determine winning vote count and candidate
 #determine if the votes is greater than the winning count
 if (votes > winning_count) and (vote_percentage > winning_percentage):
  #If true, then set winning_count and winning_percent equal to the vote_percentage
  winning_count = votes
  winning_percentage = vote_percentage
  #and set the winning_candidate equal to the candidates name
  winning_candidate = candidate_name

 # 5. The winner of the election based on vote count and percentage of votes
 print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#Print out the winning candidate summary
winning_candidate_summary = (
 f"-----------------------------\n"
 f"Winner: {winning_candidate}\n"
 f"Winning Vote Count: {winning_count:,}\n"
 f"Winning Percentage: {winning_percentage:.1f}%\n"
 f"-----------------------------\n"
)
print(winning_candidate_summary)
# Diane DeGette was the winner of the election with 73.8% of the vote and 272,892 votes



#1. Total # votes cast. After printing total votes, we found total votes is 369,711
#print(total_votes)
#2. Complete list of candidates. After printing candidate_options we found 3 candidate names
#print(candidate_options)
#4. Number votes each candidate won. After printing candidate votes we tallied votes per candidate name
#print(candidate_votes)




