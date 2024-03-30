mport moviepy.editor as mp
import speech_recognition as sr

def generate_subtitled_video(video_path, audio_path, output_path):
    # Load the video file
    video_clip = mp.VideoFileClip(video_path)

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    audio_clip = mp.AudioFileClip(audio_path)

    # Initialize subtitle list
    subtitles = []

    # Process audio in chunks and transcribe
    for chunk in range(0, int(audio_clip.duration), 10):  # 10 seconds chunks
        chunk_start = chunk
        chunk_end = min(chunk + 10, audio_clip.duration)

        # Recognize speech using Google Web Speech API
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source, offset=chunk_start, duration=chunk_end - chunk_start)
            try:
                text = recognizer.recognize_google(audio_data)
                subtitles.append((chunk_start, chunk_end, text))
            except sr.UnknownValueError:
                print("Google Web Speech API could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Web Speech API; {e}")

    # Add subtitles to the video
    for start_time, end_time, text in subtitles:
        subtitle_clip = mp.TextClip(text, fontsize=40, color='white', bg_color='black', size=(video_clip.size[0], '80%'))
        subtitle_clip = subtitle_clip.set_pos(('center', 'center')).set_start(start_time).set_end(end_time)
        video_clip = mp.CompositeVideoClip([video_clip, subtitle_clip])

    # Write the video with embedded subtitles
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', temp_audiofile='temp_audio.mp3', remove_temp=True)

    print("Subtitled video generated and saved successfully.")



if __name__ == "__main__":
    video_path = "video1.mp4"
    audio_path = "fact.mp3"  # Provide the path to your audio file
    output_path = "video.mp4"
    generate_subtitled_video(video_path, audio_path, output_path)
