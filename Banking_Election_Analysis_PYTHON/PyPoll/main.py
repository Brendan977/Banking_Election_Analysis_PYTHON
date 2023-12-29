import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')

print("Election Results")
print("----------------------------------")

total_votes = 0
candidates_votes = {}

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:
        # Total votes
        total_votes += 1
        
        # Candidate votes
        candidate_name = row[2]
        if candidate_name not in candidates_votes:
            candidates_votes[candidate_name] = 1
        else:
            candidates_votes[candidate_name] += 1

print(f'Total Votes: {total_votes}')
print("-----------------------------------")

for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f'{candidate}: {percentage:.3f}% ({votes})')

print("-----------------------------------")
winner = max(candidates_votes, key=candidates_votes.get)
print(f'Winner: {winner}')
print("-----------------------------------")

# Write to output file
output_file = os.path.join('analysis', 'pypoll_result.csv')
with open(output_file, "w") as datafile:
    datafile.write("Election Results\n")
    datafile.write("-----------------------------------\n")
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write("-----------------------------------\n")
    
    for candidate, votes in candidates_votes.items():
        percentage = (votes / total_votes) * 100
        datafile.write(f'{candidate}: {percentage:.3f}% ({votes})\n')
    
    datafile.write("-----------------------------------\n")
    datafile.write(f'Winner: {winner}\n')
    datafile.write("-----------------------------------\n")

