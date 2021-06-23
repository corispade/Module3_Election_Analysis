## Opening election_results.csv

# import modules (add our dependencies)
import csv
import os

# assign a variable for the csv file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use with statement to open the csv election results and read the file
with open(file_to_load) as election_data:

 # To Do: Read and Analyze data here

 #Read the file object with the reader function
 file_reader = csv.reader(election_data)

 #Read and print the header row using next method
 headers = next(file_reader)
 print(headers)

# 1. The total number of votes cast

# 2. A complete list of candidates who received votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based on popular vote

