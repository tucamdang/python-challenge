import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# list value
total_votes = 0
candidate_choices = []
canditate_votes = {}
winner_candidate = ""
winning_count = 0 
# open file
with open(csvpath) as csvfile:
    # delimiter=","
    csvreader = csv.reader(csvfile)
    # skipping header
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1 
        candidate_name = row[2]
        
        if candidate_name not in candidate_choices:
            # add to list
            candidate_choices.append(candidate_name)
            canditate_votes[candidate_name] = 0
      
            # add vote to candidate's count related to a particular candidate's name
        canditate_votes[candidate_name] +=1
        
# set output of text file
output_file = "Analysis2.txt"
with open(output_file, "w") as writer:
    writer = csv.writer(writer)
    print(f"Election Result")
    print(f"--------------------")
    print(f"Total Votes: {total_votes}")
    print(f"--------------------")

    writer.writerow(["Election Result"])
    writer.writerow(["--------------------"])
    writer.writerow([f"Total Number of Votes: {total_votes}"])
    writer.writerow(["--------------------"])

    for candidate in canditate_votes:
        votes = canditate_votes[candidate]
        percent_vote = (votes/total_votes) *100
    
        print(f"{candidate}: {percent_vote:.3}% ({votes})")
        writer.writerow([f"{candidate}: {percent_vote:.3}% ({votes})"])
        # looking for winner
        if (votes > winning_count):
            winning_count = votes
            winner_candidate = candidate 
             
    print(f"--------------------")
    print(f"Winner: {winner_candidate}")

    writer.writerow(["--------------------"])
    writer.writerow([f"The winner: {winner_candidate}"])