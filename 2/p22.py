# Perform Spam Classifier

import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from math import log, sqrt
import pandas as pd
import numpy as np
import re
from IPython import get_ipython

def main():

    #get_ipython().run_line_magic('matplotlib', 'inline')
    mails = pd.read_csv(r"spam.csv", encoding = 'latin-1')
    print(mails.head())
    
    mails.rename(columns = {'v1': 'labels', 'v2': 'message'}, inplace = True)
    print(mails.head())
    
    mails['labels'].value_counts()
    mails['label'] = mails['labels'].map({'ham': 0, 'spam': 1})
    print(mails.head())
    
    mails.drop(['labels'], axis = 1, inplace = True) 
    print(mails.head())

if __name__ == "__main__":
    main()

