import os
import pyttsx3
import openai
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def generate_fact(api_key, topic):
    try:
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

    except Exception as e:
        print(f"Error generating fact: {e}")
        return None

def text_to_audio(text, output_path):
    try:
        engine = pyttsx3.init()
        engine.save_to_file(text, output_path)
        engine.runAndWait()
    except Exception as e:
        print(f"Error converting text to audio: {e}")

import os
import pyttsx3
import openai
from moviepy.editor import VideoFileClip, TextClip, concatenate_videoclips, AudioFileClip  # Add AudioFileClip import

# ... (the rest of your code)

def create_video_with_text_overlay(background_folder, audio_file, output_location, topic, fact):
    # Get a list of all video files in the background folder
    background_videos = [f"{background_folder}/{file}" for file in os.listdir(background_folder) if file.endswith(('.mp4', '.avi', '.mkv'))]

    if not background_videos:
        print("No background videos found in the specified folder.")
        return

    video_clips = []
    for background_video in background_videos:
        # Load each background video
        background_clip = VideoFileClip(background_video)

        # Add text overlay to the background clip
        txt_clip = TextClip(fact, fontsize=70, color='white', bg_color='black', size=(1920, 1080)).set_pos(('center', 'center')).set_duration(background_clip.duration)
        video_clip = concatenate_videoclips([background_clip, txt_clip])

        video_clips.append(video_clip)

    # Concatenate video clips
    final_clip = concatenate_videoclips(video_clips)

    # Load the audio file separately
    audio_clip = AudioFileClip(audio_file)

    # Set audio for the final clip
    final_clip = final_clip.set_audio(audio_clip)

    # Write the final clip to the output video
    final_clip.write_videofile(output_location, codec='libx264', audio_codec='aac', temp_audiofile='temp_audio.m4a', remove_temp=True)

    print(f"Video created successfully at: {output_location}")



# Replace "YOUR_API_KEY" with your actual OpenAI API key
api_key = ""
topic = input("Enter the topic for which you want a fun fact about: ")

# Generate fact and convert it to audio
fact = generate_fact(api_key, topic)
text_to_audio(fact, "fun_fact.mp3")

# Paths
background_folder = ""
audio_file = ""
output_location = f"..../{topic}_video.mp4"

# Create video with text overlay using moviepy
create_video_with_text_overlay(background_folder, audio_file, output_location, topic, fact)
