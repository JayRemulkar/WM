# Sentiment analysis

import csv
from textblob import TextBlob

def main():

    with open("review.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            text = row[0]
            blob = TextBlob(text)
            sentiment = blob.sentiment.polarity
            print(f"Sentiment score for '{text}': {sentiment}")

if __name__ == "__main__":
    main()