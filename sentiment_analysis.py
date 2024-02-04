
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')


#Criteria 3
''' This is a function to analyse the sentiment of the sentence'''
def sentiment_analysis(review_doc):
    review_doc = nlp(review_doc)
    
    # Check and categorise polarity of the statement
    polarity_result = ""
    polarity = review_doc._.blob.polarity
    if polarity > 0.2:
        polarity_result = "positive"
    elif polarity < -0.2:
        polarity_result = "negative"
    else:
        polarity_result = "neutral"

    # Check and categorise subjectivity
    subjectivity_result = ""
    subjectivity = review_doc._.blob.sentiment.subjectivity
    if subjectivity > 0.6:
        subjectivity_result = "opinionated"
    elif subjectivity < 0.4:
        subjectivity_result = "objective"
    else:
        subjectivity_result = "neutral"
    
    # Outputs
    print(f"\nThis statement is {polarity_result} and subjectively {subjectivity_result}.")
    sentiment = review_doc._.blob.sentiment
    print(f"{sentiment}\n")


'''This is a function to clean 1 review at a time. 
It checks the value entered is an integer, find the relevant row, changes all text to lower case, removes stop words
and tokenises the results ready for sentiment analysis.
The point of this function is to remove the need to run the code that was required in the task to analyse the whole 
source file to complete this criteria'''

def clean_text(user_input,text_to_clean):
    #check if input is a string
    try:
        user_input= int(user_input)
    except ValueError:
        print("Error: You have input text. Please enter a number")
        return text_to_clean
    
    # Check the selected review
    user_input = int(user_input)
    max_index = len(just_reviews) - 1
    if 0 <= user_input <= max_index:
        # Process the sentence removing stop words, white space and changing to lowercase
        my_review_of_choice = just_reviews.iloc[user_input, 0]
        remove_stop_words = nlp(my_review_of_choice)
        filtered_tokens = [token.text.lower() for token in remove_stop_words if not token.is_stop]
        filtered_text = ' '.join(filtered_tokens).strip()
        print(f"The review you selected - \"{my_review_of_choice}\"")
        text_to_clean = filtered_text
    
    # Handle error if user selects a number outside then the range of reviews 
    else:
        print(f"Error: Please enter a number between 0 and {max_index}")
    return text_to_clean


# Criteria 1
file_path = r"Data Science (Fundamentals)\T21 - Capstone Project - NLP Applications\amazon_product_reviews.csv"

#Read csv, remove blank entries and remove white space
amazon_reviews = pd.read_csv(file_path,low_memory=False)
amazon_reviews = amazon_reviews.dropna(subset=['reviews.text'])
amazon_reviews['reviews.text'] = amazon_reviews['reviews.text'].str.strip()

# Redefine as a variable and reset indexes
just_reviews = amazon_reviews[['reviews.text']]
just_reviews = just_reviews.reset_index(drop=True)


# Criteria 2
'''This code processes all reviews, changes all text to lower case, removes stop words and creates a new column with the processed results
Comment out if you want to run the criteria 3 or 4 code blocks in isolation or you will need to wait 20 mins for it to run each time !!'''

filtered_tokens_list = []
polarity_column = []

for review_text in just_reviews['reviews.text']:
    remove_stop_words = nlp(review_text) # Tokenise each entry
    filtered_tokens = [token.text.lower() for token in remove_stop_words if not token.is_stop] # Remove stop words and convert to lowercase
    filtered_text = ' '.join(filtered_tokens) # Join Filtered words to string
    filtered_tokens_list.append(filtered_text)# Append the result to the list
    polarity_temp = nlp(filtered_text)._.blob.polarity
    if polarity_temp > 0.2:
        pol_result = "positive"
    elif polarity_temp < -0.2:
        pol_result = "negative"
    else:
        pol_result = "neutral"
    polarity_column.append(pol_result)

just_reviews['no_stopwords'] = filtered_tokens_list
just_reviews['polarity'] = polarity_column


# Criteria 4 - check sentiment
print("Criteria 4 Part 1: Check the sentiment of a review")

# User selection
cleaned_text = ""
while True:
    row_number = input("Please enter a review row number: ")
    cleaned_text = clean_text(row_number, cleaned_text)
    
    # Exit the loop if the input is a valid integer
    if cleaned_text:
        break
sentiment_analysis(cleaned_text)


# Criteria 4: Check similarity
print("Criteria 4 Part 2: Check Similarity")
'''This code is to check the Similarity between 2 statements predefined in the code'''
cleaned_text_1 = ""
cleaned_text_2 = ""

# Select entries to compare
compare_1 = 250
compare_2 = 700

# Clean reviews
cleaned_text_1 = clean_text(compare_1,cleaned_text_1)
cleaned_text_2 = clean_text(compare_2,cleaned_text_2)

# Check similarity Calculation and return score
similarity = nlp(cleaned_text_1).similarity(nlp(cleaned_text_2))
print("Similarity Score:", similarity)
