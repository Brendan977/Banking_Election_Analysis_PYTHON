import os
import csv

csv_path= os.path.join('Resources', 'election_data.csv')

print("Election Results")
print("----------------------------------")

total_votes = []
candidates_full = []
vote_1 = []
vote_2 = []
vote_3 = []


with open(csv_path) as csvfile:

    csvreader= csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        #Total votes
        total_votes.append(row[0])
        #List of candidates(pt.1)
        candidates_full.append(row[2])
        #Candidates number of votes
        if row[2] == "Charles Casper Stockham":
            vote_1 += '1'
        elif row[2] == "Raymon Anthony Doane":
            vote_2 += '1'
        elif row[2] == "Diana DeGette":
            vote_3 += '1'
    print(f'Total Votes: {len(total_votes)}')
    print("-----------------------------------")
    candidates_set = set(candidates_full)
    candidates_list = (list(candidates_set))
    print(candidates_list)
    print(f'{candidates_list[0]}: {len(vote_3)}')
    print(f'{candidates_list[1]}: {len(vote_1)}')
    print(f'{candidates_list[2]}: {len(vote_2)}')

output_file = os.path.join('analysis', 'pypoll_result.csv')

with open(output_file, "w") as datafile:
    datafile.write()