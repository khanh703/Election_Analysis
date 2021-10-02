# Modules
import os
import csv

# Open the data file.
file_to_load = os.path.join(".", "election_results.csv")
file_to_save = os.path.join(".", "election_analysis.txt")
total_votes = 0
candidates = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data, delimiter=',')
    header = next(file_reader)
    
    for row in file_reader:

        total_votes += 1

        # Initialize candidate name and assign zero votes to start if candidate NOT IN dictionary
        candidate_name = row[2]
        if candidate_name not in candidates.keys():
            candidates[row[2]] = 0
        
        # Add a vote count for each candidate.
        candidates[candidate_name] += 1
    
    with open(file_to_save, "w") as txt_file:
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

    #print(f"There were {total_votes} ballots casted")


        for candidate_name in candidates:
            # Retrieve vote count of a candidate.
            votes = candidates[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            #  To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            #print(f"{candidate_name}: Received {vote_percentage:.2f}% of the vote.")
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)


            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        
        
        #  To do: print out the winning candidate, vote count and percentage to
        #   terminal.
        # print(f"The winning candidate is {winning_candidate} with {winning_count:,} votes, thats {winning_percentage:.2f}% of the total {total_votes:,} ballots casted.")
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        txt_file.write(winning_candidate_summary)

        #print(winning_candidate_summary)
    


    #returns zero if ran after and will cause empty data if ran before For loop
    #total_votes = len(list(file_reader))