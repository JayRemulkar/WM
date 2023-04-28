# Apriori Algorithm implementation in case study

import numpy as np
import pandas as pd
from apyori import apriori

def main():
    
    store_data = pd.read_csv('TransactionData.csv',header=None)
    print(store_data)
    
    records = []
    for i in range(0,20):
        records.append([str(store_data.values[i,j]) for j in range(0,6)])
    
    association_rules = apriori(records,min_support=0.50,min_confidence=0.7)
    association_results = list(association_rules)
    
    print(len(association_results))
    print(association_results)

if __name__ == "__main__":
    main()