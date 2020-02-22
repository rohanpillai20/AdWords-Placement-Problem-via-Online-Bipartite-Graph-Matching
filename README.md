# AdWords-Placement-Problem-via-Online-Bipartite-Graph-Matching

## Problem:
We are given a set of advertisers each of whom has a daily budget 𝐵𝑖. When a user performs a query, an ad request is placed online and a group of advertisers can then bid for that advertisement slot. The bid of advertiser 𝑖 for an ad request 𝑞 is denoted as 𝑏𝑖𝑞. We assume that the bids are small with respect to the daily budgets of the advertisers (i.e., for each 𝑖 and 𝑞, 𝑏𝑖𝑞≪𝐵𝑖). Moreover, each advertisement slot can be allocated to at most one advertiser and the advertiser is charged his bid from his/her budget. The objective is to maximize the amount of money received from the advertisers.

For this project, we make the following simplifying assumptions:
1. For the optimal matching (used for calculating the competitive ratio), we will assume everyone’s budget is completely used. (optimal revenue = the sum of budgets of all advertisers)
2. The bid values are fixed (unlike in the real world where advertisers normally compete by incrementing their bid by 1 cent).
3. Each ad request has just one advertisement slot to display.

## Datasets
You are provided with a small dataset called bidder_dataset.csv. This dataset contains information about the advertisers. There are four columns: advertiser ID, query that they bid on, bid value for that query, and their total budget (for all the keywords). The total budget is only listed once at the beginning of each advertiser’s list.
In addition, the file queries.txt contains the sequence of arrivals of the keywords that the advertisers will bid on. These queries will arrive online and a fresh auctioning would be made for each keyword in this list.

## Implementation


### Algorithms:
* Greedy:
1. For each query 𝑞
    1. If all neighbors (bidding advertisers for 𝑞) have spent their full budgets.
        1. continue
    2. Else, match 𝑞 to the neighbor with the highest bid.
    
* MSVV:
Let 𝑥<sub>𝑢</sub> be the fraction of advertiser's budget that has been spent up and 𝜓(𝑥<sub>𝑢</sub>) = 1−𝑒<sup>(𝑥<sub>𝑢</sub>−1)</sup>.
1. For each query 𝑞
    1. If all neighbors have spent their full budgets.
        1. continue
    2. Else, match 𝑞 to the neighbor 𝑖 that has the largest 𝑏<sub>𝑖𝑞</sub>∗𝜓(𝑥<sub>𝑢</sub>) value.

* Balance:
1. For each query 𝑞
    1. If all neighbors have spent their full budgets.
        1. continue
    2. Else, match 𝑞 to the neighbor with the highest unspent budget.
    
    
## Output
Run `adwords.py` with the following command `python adwords.py [greedy|msvv|balance]`

Using Python with random.seed(0) for shuffling queries, the following was obtained.

|command|revenue|competitive ratio|
|----------|-------|---------------|
|python adwords.py greedy|16800.5|0.9412|
|python adwords.py mssv|17714.7|0.9924|
|python adwords.py balance|12386.5|0.6939|
