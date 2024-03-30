import openai
import pandas as pd

def generate_quotes(api_key, topic, num_quotes):
    openai.api_key = api_key

    quotes = set()  # Use a set to store unique quotes
    prompt = f"Provide a quote about {topic}."

    while len(quotes) < num_quotes:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None
        )
        quote = response.choices[0].text.strip()
        quotes.add(quote)

    return list(quotes)

# Replace "YOUR_API_KEY" with your actual OpenAI API key
api_key = "#"
num_quotes = 10
topic = input("Enter the topic for which you want quotes about: ")

quotes = generate_quotes(api_key, topic, num_quotes)

# Specify the full path for saving the Excel file
file_path = r'C:\Users\sunai\OneDrive\Documents\YOUTUBE\data\quotes.xlsx'

# Save quotes to Excel with the specified path
df = pd.DataFrame({'Quotes': quotes})
df.to_excel(file_path, index=False)

print(f"\nQuotes saved to {file_path}:")
print(df)

