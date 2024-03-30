import openai
import pyttsx3
import os

def generate_fact(api_key, topic):
    openai.api_key = api_key

    prompt = f"Provide a fun fact about {topic}."

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None
    )

    return response.choices[0].text.strip()

def text_to_audio(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()

# Replace "YOUR_API_KEY" with your actual OpenAI API key
api_key = "#"
topic = input("Enter the topic for which you want a fun fact about: ")

fact = generate_fact(api_key, topic)
print("\nFun Fact:")
print(fact)

# Replace "OUTPUT_FOLDER" with the path where you want to save the audio file
output_folder = "C:/Users/sunai/Downloads/youtubeaudios"
output_path = os.path.join(output_folder, "fact.mp3")

text_to_audio(fact, output_path)

print(f"Audio file saved at: {output_path}")
