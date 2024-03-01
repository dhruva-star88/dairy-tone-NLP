import glob
from pathlib import Path
from datetime import datetime
from nltk.sentiment import SentimentIntensityAnalyzer

# Get List of filepaths
filepaths = glob.glob("diary/*.txt")


# Define function which returns dates
def get_dates():
    # Extract only the dates without extension
    dates = [Path(filepath).stem for filepath in filepaths]
    # Convert dates into datetime type
    d = [datetime.strptime(i, "%Y-%m-%d") for i in dates]
    # Modify dates into string
    d = [i.strftime("%b %d %Y") for i in d]
    return d


# Create data list
data = []
# Using for loop extract content of every file and store them in list
for files in filepaths:
    with open(files, "r") as file:
        content = file.read()
        data.append(content)

# Create the SentimentIntensityAnalyzer object Instance
analyzer = SentimentIntensityAnalyzer()


# Define function for Positivity graph
def get_pos_scores():
    # Create list
    pos_score = []
    # Using for loop get positive scores of content and store them in list
    for i in data:
        scores = analyzer.polarity_scores(i)
        pos_score.append(scores["pos"])
    return pos_score


# Define function for Positivity graph
def get_neg_scores():
    # Create list
    neg_score = []
    # Using for loop get positive scores of content and store them in list
    for i in data:
        scores = analyzer.polarity_scores(i)
        neg_score.append(scores["neg"])
    return neg_score


"""
The following part executes only when we execute this page, but not in other pages
"""
if __name__ == "__main__":
    print(get_pos_scores())
    print(get_neg_scores())
