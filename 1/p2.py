
import pandas as pd 
import re 
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


def Spam_Classifier():
    msg = pd.read_csv("SMSSpamCollection",sep = "\t",names = ["label","message"])
    #print(msg)

    ps = PorterStemmer()
    corpus = []

    for i in range(len(msg)):
        #print("Raw Data : ",msg["message"][i])
        review = re.sub("[^a-zA-Z]"," ",msg["message"][i])
        #print("after applying re.Sub : ",review)
        review = review.lower()
        #print("after lowering : ",review)
        review = review.split()
        #print("after spliting : ",review)
        review = [ps.stem(word) for word in review if not word in stopwords.words("english")]
        #print("after stemmming : ",review)
        review = " ".join(review)
        #print("after joining : ",review)
        corpus.append(review)

    # Creating the bag of Words model
    cv = CountVectorizer(max_features = 5000)
    #print("cv : ",cv)
    x = cv.fit_transform(corpus).toarray()
    #print("x : ",x)
    y = pd.get_dummies(msg["label"])
    #print("y : ",y)
    y = msg["label"]
    #print("y : ",y)

    # Train Test Split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)

    # Training model using Naive bayes classifier
    spam = MultinomialNB()

    spam.fit(x_train, y_train)

    y_pred = spam.predict(x_test) 

    matrix = confusion_matrix(y_test, y_pred)
    print(matrix)

    Accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy of model : ",Accuracy * 100)

def main():
    Spam_Classifier()

if __name__ == "__main__":
    main()