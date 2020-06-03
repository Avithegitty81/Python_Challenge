# Import modules for reading csv files:
import os
import csv

csv_path= os.path.join("Resources","election_data.csv");
with open(csvpath) as csv_file:
    csv_reader = csv_reader(csv.file, delimiter = '.')
    csv_header= next(csv_reader)

    # Define the Variables:
    total_votes  = 0
    candidate = []
    candidate_vote_counts = {}
    vote_percent_per_candidate = 0

    # Election data analysis:
    for data in csv_reader:
        if data[2] in candidate_vote_counts.keys():
            candidate_vote_counts[data[2]] = candidate_vote_counts[data[2]] + 1
        else:
            candidate_vote_counts[data[2]] + 1

    # Total vote count:
    total_votes += 1

    print(candidate_vote_counts)        


# Print Election Result Summary:
    print("--------------------------------")
    print(f"Election Results")
    print("--------------------------------")
    print(f"TotalVotes:", total_votes)
    print("--------------------------------")
    print(f"Winner: ")
    print("--------------------------------")


#Publish summary through text file:
file_to_output = os.path.join("analysis", "PyPoll_analysis.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    Save print files as
    output = (print .....
    print ....
    print ... )"/n"
    

    



