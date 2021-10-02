# Modules
import os
import csv

# Open the data file.
file_to_load = os.path.join(".", "election_results.csv")
file_to_save = os.path.join(".", "election_analysis.txt")

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data, delimiter=',')
    header = next(file_reader)

    total_votes = 0
    candidates = {}
    
    for i in file_reader:

        # Write down the names of all the candidates.
        if i[2] not in candidates.keys():
            candidates[i[2]] = 0
        
        # Add a vote count for each candidate.
        candidates[i[2]] = candidates[i[2]] + 1
            
    
    # Get the total votes for each candidate.
    # Get the total votes cast for the election.
    for candidate in candidates.keys():
        print(f"{candidate} received {candidates[candidate]:.5f} votes.")
        total_votes = total_votes + candidates[candidate]

    print(f"total_votes = {total_votes} casted")



    #total_votes = len(list(file_reader))