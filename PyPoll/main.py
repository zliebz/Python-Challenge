import os
import csv

#Define Variables
total_votes = 0
li_votes = 0
khan_votes = 0
correy_votes = 0
tooley_votes = 0

#Path to source data file
poll_csv = os.path.join("Resources", "election_data.csv")

#Open and read
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read header first
    csvheader = next(csvfile)

    #Loop
    for row in csvreader:
        total_votes = total_votes + 1

        #Vote counting by candidate, third column [2]. If candidate present, add to vote count per candidate.
        if str(row[2]) == "Li":
            li_votes += 1
        if str(row[2]) == "Khan":
            khan_votes += 1
        if str(row[2]) == "Correy":
            correy_votes += 1
        if str(row[2]) == "O'Tooley":
            tooley_votes += 1

    #Use above vote counts against total votes to determine a percentage. 
    li_rate = (li_votes / total_votes) * 100
    khan_rate = (khan_votes / total_votes) * 100
    correy_rate = (correy_votes / total_votes) * 100
    tooley_rate = (tooley_votes / total_votes) * 100

    #Find Winner
    winner = max(li_votes, khan_votes, correy_votes, tooley_votes)

    #Store value for winner
    if winner == li_votes:
        winning_candidate = "Li"
    if winner == khan_votes:
        winning_candidate = "Khan"
    if winner == correy_votes:
        winning_candidate = "Correy"
    if winner == tooley_votes:
        winning_candidate = "O'Tooley"

#Print the election results

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {khan_rate:.2f}% ({khan_votes})")
print(f"Correy: {correy_rate:.2f}% ({correy_votes})")
print(f"Li: {li_rate:.2f}% ({li_votes})")
print(f"OTooley: {tooley_rate:.2f}% ({tooley_votes})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

#Export Results to Text File

summary_file = os.path.join("PollAnalysis", "pollanalysis.txt")
with open(summary_file, 'w') as outfile:

    outfile.write("Election Results")
    outfile.write("-------------------------")
    outfile.write(f"Total Votes: {total_votes}")
    outfile.write("-------------------------")
    outfile.write(f"Khan: {khan_rate:.2f}% ({khan_votes})")
    outfile.write(f"Correy: {correy_rate:.2f}% ({correy_votes})")
    outfile.write(f"Li: {li_rate:.2f}% ({li_votes})")
    outfile.write(f"OTooley: {tooley_rate:.2f}% ({tooley_votes})")
    outfile.write("-------------------------")
    outfile.write(f"Winner: {winning_candidate}")
    outfile.write("-------------------------")



