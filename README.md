# Colorado Election Analysis

## **Project Overview**
We are completing an election audit of the tabulated election results of a U.S. Congressional presinct in Colorado. We are automating the processing using Python to determine the final election results and generate a vote count report to certify the winner of the local congressional election.

### **Process**
Step 1: Calculate the total number of votes cast

Step 2: Get a complete list of candidates who received votes

Step 3: Calculate the total number of votes each candidate received

Step 4: Calculate the percentage of votes each candidate won

Step 5: Determine the winner of election based on the popular vote

Step 6: Calculate the total number of votes cast by each county

Step 7: Calculate the percentage of votes cast by each county

Step 8: Determine county with largest voter turnout

### **Resources**
Data Source: [election_results.csv](https://github.com/corispade/Module3_Election_Analysis/blob/main/Resources/election_results.csv)

Software: Python 3.7.6, Visual Studio Code: 1.57.1

## **Election Audit Results**
Find the summary of the election audit results [here](https://github.com/corispade/Module3_Election_Analysis/blob/main/analysis/election_analysis.txt).

### Total Number of Votes:
There were 369,711 votes cast in the election

### Voter Results By County:
* Jefferson had 38,855 votes, which calculated to 10.5% of the total votes.
* Denver had 306,055 votes, which calculated to 82.8% of the total votes.
* Arapahoe had 24,801 votes, which calculated to 6.7% of the total votes.

### County with Largest Voter Turnout:
The county with the largest voter turnout was Denver with 306,055 votes and 82.8% of the total votes.

### Candidate Results:
* Charles Casper Stockham received 85,213 votes, which calculated to 23.0% of the total votes.
* Diana DeGette received 272,892 votes, which calculated to 73.8% of the total votes.
* Raymon Anthony Doane received 11,606 votes, which calculated to 3.1% of the total votes.

## Winner of the Election:
The winner of the election was Diana DeGette who received 272,892 votes and 73.8% of the total votes. 

## Election Audit Summary

We created a [python script](https://github.com/corispade/Module3_Election_Analysis/blob/main/PyPoll_Challenge.py) to loop through the election results [Excel file](https://github.com/corispade/Module3_Election_Analysis/blob/main/Resources/election_results.csv) and make over 300,000 data points easily accessible and readable. Python was able to evaluate, interpret, and create complex calculations on these data points in a matter of seconds. We propose to use this script in future elections to reduce the amount of time it takes to generate reports and declare a winner.

Well documented python scripts are easy to understand and adjust for future elections. Please see a few suggestions for script modification below:

1. The script can be modified to link to any .csv file. So anytime there is a new election with new candidates and new counties, the script can be modified to loop through the necessary rows to return the needed information. 
![image](csv_file.png)

2. The script can be modified to return more information. If the comission would like to analyze voter outcome by zipcode, we can add that information to the data, loop through and find the zipcodes with the highest and lowest voter turnouts. 

3. Voter information can also be analyzed by age, ethnicity, gender and income. 

