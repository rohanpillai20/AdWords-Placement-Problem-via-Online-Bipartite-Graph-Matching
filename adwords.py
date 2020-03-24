import pandas as pd
import numpy as np
import sklearn
import sys
import copy

np.random.seed(0)

def greedy(bidders_dict, queries_dict, queries):
    revenue = 0
    for _,q in queries.itertuples():
        b = queries_dict[q]
        for temp in b.itertuples():
            if(bidders_dict[temp[1]]>temp[2]):
                bidders_dict[temp[1]]-=temp[2]
                revenue += temp[2]
                break 
                
    return revenue

def msvv(bidders_dict, queries_dict, queries, original_bidders_dict):
    revenue = 0
    for _,q in queries.itertuples():
        b = queries_dict[q]
        temp_bidders_dict = {}
        for temp in b.itertuples():
            fraction = (original_bidders_dict[temp[1]]-bidders_dict[temp[1]])/original_bidders_dict[temp[1]]
            temp_bidders_dict[temp[1]] = temp[2]*(1-np.exp(fraction-1))
        max_bidder = max(temp_bidders_dict, key=temp_bidders_dict.get)
        bid = b[b['Advertiser']==max_bidder]['Bid Value'].iloc[0]
        if(bidders_dict[max_bidder]>bid):
            bidders_dict[max_bidder]-=bid
            revenue += bid
        
    return revenue

def balance(bidders_dict, queries_dict, queries):
    revenue = 0
    for _,q in queries.itertuples():
        b = queries_dict[q]
        temp_bidders_dict = {}
        for temp in b.itertuples():
            temp_bidders_dict[temp[1]] = bidders_dict[temp[1]]
        max_bidder = max(temp_bidders_dict, key=temp_bidders_dict.get)
        bid = b[b['Advertiser']==max_bidder]['Bid Value'].iloc[0]
        if(bidders_dict[max_bidder]>bid):
            bidders_dict[max_bidder]-=bid
            revenue += bid
                
    return revenue

def choose_algorithm(algorithm, *args):
    if algorithm=='greedy':
        return greedy(bidders_dict, queries_dict, queries)
    elif algorithm=='msvv':
        return msvv(bidders_dict, queries_dict, queries, original_bidders_dict)
    elif algorithm=='balance':
        return balance(bidders_dict, queries_dict, queries)
    else:        
        return 0

bidders = pd.read_csv('bidder_dataset.csv')
queries = pd.read_csv('queries.txt',header=None)
optimal = np.nansum(bidders['Budget'])

bidders_dict = {}
for b in bidders.itertuples():
    if b[1] not in bidders_dict.keys():
        bidders_dict[b[1]] = b[4]
        
original_bidders_dict = copy.deepcopy(bidders_dict)
    
queries_dict = {}
for _,q in queries.itertuples():
    if q not in queries_dict.keys():
        temp = bidders[bidders["Keyword"].str.contains(q)].loc[:,("Advertiser","Bid Value")]
        sorted_temp = temp.sort_values(by= "Bid Value", ascending = False)
        queries_dict[q] = sorted_temp

algorithm = sys.argv[1]
revenue_result = 0
for _ in range(100):
    queries = sklearn.utils.shuffle(queries)
    bidders_dict = copy.deepcopy(original_bidders_dict)
    revenue_result += choose_algorithm(algorithm, bidders_dict, queries_dict, queries, original_bidders_dict)

revenue_result/=100

if revenue_result==0:
    print("No method or wrong method choosen.")
else:
    print("Average Revenue for {} Algorithm: {}".format(algorithm, revenue_result))
    print("Competitive Ratio: {}".format(revenue_result/optimal))