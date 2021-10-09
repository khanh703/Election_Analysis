# Election Analysis 

## Objective 
The election commission would like to complete the election audit. In order for the audit to complete, the election commission needs to know how each county performed in terms of total voter turnout by count and percentage. The final report should include:
-   The voter turnout for each county
-   The percentage of votes from each county out of the total count
-   The county with the highest turnout
-   Candidate that received the most votes
-  County that saw the highest turnout


## Challenge 
The data provided by the election commission is too large to manually count. Using multiple dictionaries to build a single report.

## Solution 
Using Python code, a set tasks to perform:

### Create dictionaries to hold counts for ballots casted for each Candidate and County 
1. Read the election_results.csv provided by the election commission
2. Loop through each line of data, with each iteration
	- Add 1 count to total_votes
	- Determine the Candidate this voter voted for
    -- Add 1 count to this candidate_votes count
	- Determine this voter's County
	-- Add 1 count to this county_votes count

 ### Determine winning Candidate and County with the highest turnout 
 1. Loop through each Candidate in candidate_votes dictionary and set Candidate as the winning_candidate if this candidate received more vote than the previous Candidate.
 2. Loop through each County in county_votes dictionary and set County as the winning_county if this county received more vote than the previous County


## Results 


**Total Votes**: 369,711

--- 

**County Votes**: 
Jefferson: 10.5% (38855) 
Denver: 82.8% (306055) 
Arapahoe: 6.7% (24801) 

---

**Largest County Turnout:** Denver with 306,055, (82.78)%


**Charles Casper Stockham:** 23.0% (85,213)
**Diana DeGette:** 73.8% (272,892)
**Raymon Anthony Doane:** 3.1% (11,606)

---

Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

---

### Download a copy of Results
 [Election Analysis](analysis/election_analysis.txt)