YouTuberAI
YouTuberAI is a project aimed at assisting content creators by generating quotes, fun facts, and subtitled videos automatically using the power of artificial intelligence. This project leverages OpenAI's GPT-3.5 model to generate content based on user-provided topics.

Features
1. Generate Quotes
Function: generate_quotes(api_key, topic, num_quotes)
Description: This function generates quotes related to a given topic using OpenAI's GPT-3.5 model. The quotes are saved to an Excel file.
2. Generate Fun Facts
Function: generate_fact(api_key, topic)
Description: This function generates a fun fact related to a given topic using OpenAI's GPT-3.5 model.
3. Text-to-Audio Conversion
Function: text_to_audio(text, output_path)
Description: This function converts text to audio using the pyttsx3 library and saves the audio file to the specified output path.
4. Create Video with Text Overlay
Function: create_video_with_text_overlay(background_folder, audio_file, output_location, topic, fact)
Description: This function creates a video with text overlay using background videos from a specified folder. It overlays a fun fact text on each background video and combines them into a single video with audio.
5. Generate Subtitled Video
Function: generate_subtitled_video(video_path, audio_path, output_path)
Description: This function generates a subtitled video by transcribing the audio of a video file and adding subtitles to it.
6. Create Video
Function: create_video(background_folder, audio_file, output_location)
Description: This function creates a video by combining background videos with audio.

Usage
API Key Setup: Replace "YOUR_API_KEY" with your actual OpenAI API key.
Topic Input: Enter the topic for which you want to generate quotes, fun facts, or videos.
File Paths: Specify the necessary file paths for input and output files.
Run the Functions: Run the respective functions based on your requirements.

Dependencies
openai
pandas
pyttsx3
moviepy
speech_recognition

Installation
You can install the required dependencies using pip:
pip install openai pandas pyttsx3 moviepy SpeechRecognition
