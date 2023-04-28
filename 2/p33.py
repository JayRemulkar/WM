# Demonstrate Text Mining and Webpage Pre-processing using meta information from the web pages (Local/Online)

import feedparser

def main():
    FEED_URL="http://feeds.feedburner.com/oreilly/radar/atom"

    fp = feedparser.parse(FEED_URL)

    for e in fp.entries:
        print (e.title)
        print (e.links[0].href)
        print (e.content[0].value)

if __name__ == "__main__":
    main()