# Finally, write code that opens the file project_twitter_data.csv which has the fake generated twitter data; 
# the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. 
# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.

# Now, you will write code to create a csv file called `resulting_data.csv`, 
# which contains the Number of Retweets, Number of Replies, Positive Score 
# (which is how many happy words are in the tweet), 
# Negative Score (which is how many angry words are in the tweet), 
# and the Net Score (how positive or negative the text is overall) for each tweet. 
# The file should have those headers in that order. 

# Remember that there is another component to this project:
# You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. 
# Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.

import csv

# function to strip individual words of any punctuation
def strip_punctuation(strArg: str) -> str:
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

    for chr in punctuation_chars:
        strArg = strArg.replace(chr,'')

    return strArg

# function to find positive words in one or more sentences
def get_pos(strArgSent: str) -> int:
    intOutput: int = 0
    strArgSent = strArgSent.lower()
    listWords = strArgSent.split(' ')
    positive_words: list = []

    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    
        for word in listWords:
            if strip_punctuation(word) in positive_words:
                intOutput = intOutput +1

    return intOutput

# same as above, but for negative words
def get_neg(strArgSent: str) -> int:
    intOutput: int = 0
    strArgSent = strArgSent.lower()
    listWords = strArgSent.split(' ')
    negative_words = []

    with open("negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())

        for word in listWords:
            if strip_punctuation(word) in negative_words:
                intOutput = intOutput +1

    return intOutput

# 1: reads csv data from file
# 2: opens new csv file for writing
# 3: loops over original csv file and writes analyzed data to new file
def classifier():
    print('Reading Twitter data')
    with open('project_twitter_data.csv','r') as inputData:
        twData = csv.reader(inputData)
        next(twData)

        print('Opening new file')
        with open('resulting_data.csv','w',newline='') as outputData:
            csvWriter = csv.writer(outputData)
            csvHeaders = ['Number of Retweets','Number of Replies','Positive score','Negative score','Net score']
            csvWriter.writerow(csvHeaders)
            
            for line in twData: 
                intNeg = get_neg(line[0])
                intPos = get_pos(line[0])
                intScore = intPos-intNeg
                csvRow = [line[1],line[2],intPos,intNeg,intScore]
                csvWriter.writerow(csvRow)

# runs the classifier
classifier()