# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from gensim.utils import simple_preprocess

# Load the data from the CSV file
df = pd.read_csv('D:\\College Work\\UTSA\\Spring 2023\\Large Scale Data Management\\Project csv files\\Fake.csv')

print(df.columns)

# Convert the date column to a datetime object
df['date'] = pd.to_datetime(df['date'], format='%d-%b-%y')

# Define the preprocessing function
def preprocess(text):
    if not isinstance(text, str):
        return ''
    return [token for token in simple_preprocess(text)]

# Apply the preprocessing function to the 'text' column and store the results in a new 'tokens' column
df['tokens'] = df['text'].apply(preprocess)

# Define a function to create a wordcloud for a given year
def create_wordcloud(year):
    # Select the rows for the given year
    year_df = df[df['date'].dt.year == year]

    # Concatenate the tokens for all rows into a single string
    year_tokens = ' '.join([token for tokens in year_df['tokens'] for token in tokens])


    # Generate a wordcloud from the concatenated string of tokens
    wordcloud = WordCloud(background_color='white').generate(year_tokens)

    # Display the wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Year " + str(year))
    plt.show()

# Create a wordcloud for each year in the dataset
for year in df['date'].dt.year.unique():
    create_wordcloud(year)