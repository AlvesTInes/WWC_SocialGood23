import pandas as pd
import numpy as np
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# Load dataset
# Replace 'your_dataset.csv' with the path to your dataset file
df = pd.read_csv(r'C:\Users\mmta9\Desktop\Food Waste Wizards - FoodWasteWizards.csv')

# Function to clean text data
def clean_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation, non-alphanumeric characters and digits
    text = ''.join([char for char in text if char.isalnum() or char.isspace() or char.isdigit()])
    return text

# Function to tokenize text
def tokenize_text(text):
    return word_tokenize(text)

# Function to remove stop words
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

# Function to lemmatize tokens
def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokens]

# Apply cleaning, tokenization, stop word removal, and lemmatization
df['clean_text'] = df['user_opinion'].apply(clean_text)
df['tokens'] = df['clean_text'].apply(tokenize_text)
df['tokens'] = df['tokens'].apply(remove_stopwords)
df['tokens'] = df['tokens'].apply(lemmatize_tokens)

# Create bag of words
all_words = [word for tokens in df['tokens'] for word in tokens]
word_freq = nltk.FreqDist(all_words)
top_ten=word_freq.most_common(10)
print(top_ten)
word_freq_df = pd.DataFrame({'word': list(word_freq.keys()), 'frequency': list(word_freq.values())})
word_freq_df=word_freq_df.sort_values("frequency", ascending=False)

pal=sns.color_palette('BuPu',10)
plt.rcParams['figure.dpi'] = 360
fig, ax = plt.subplots(figsize=(12,6))
sns.barplot(data=word_freq_df.head(10), 
            x='frequency',
            y='word',
            errorbar=None,
            palette=pal
            )
plt.xlabel('Words Frequency', size=12, color='#4f4e4e')
plt.ylabel('Words', size=12, color='#4f4e4e')
plt.title('Ten Most Common Words', size=14, color='#4f4e4e')
plt.xticks(size=10, color='#4f4e4e')
plt.yticks(size=10,color='#4f4e4e' )
sns.despine()
plt.savefig('word frequency.png')
plt.show()

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='BuPu').generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('worldcloud.png')
plt.show()

# Sentiment Analysis
sid = SentimentIntensityAnalyzer()

def calculate_compound(text):
    scores=sid.polarity_scores(text)['compound']
    return scores

df['compound_score']=df['clean_text'].apply(lambda text:calculate_compound(text))

# Function to perform sentiment analysis
def analyze_sentiment(text):
    sentiment_scores = sid.polarity_scores(text)
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis
df['sentiment'] = df['clean_text'].apply(analyze_sentiment)

def sentiment_score(row):
    if row.sentiment=='Positive' and row.rating >= 4: sentiment='Positive'
    elif row.sentiment=='Negative' and row.rating <= 2: sentiment='Negative'
    else: sentiment='Neutral'
    
    return sentiment
    
df['sentiment_score']=df.apply(sentiment_score, axis=1)

# Save the dataset with sentiment prediction as a new column
# Replace 'new_dataset.csv' with the desired path and file name
df.to_csv('new_dataset.csv', index=False)

print (df.head())

selected_columns = df[['score_1', 'score_2','score_3','score_4','score_5','score_6','score_7','score_8','score_9','score_10',
                       'score_11','score_12','score_13','score_14','score_15','score_16','score_17','score_18','score_19','score_20']]

# Transform the data from wide to long format
df_long = pd.melt(selected_columns, var_name='Score', value_name='Value')

# Save the transformed data to a new CSV file
df_long.to_csv('transformed_dataset.csv', index=False)