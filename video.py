from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
import os
def create_video(background_folder, audio_file, output_location):
    # Get a list of all video files in the background folder
    background_videos = [f"{background_folder}/{file}" for file in os.listdir(background_folder) if file.endswith(('.mp4', '.avi', '.mkv'))]

    if not background_videos:
        print("No background videos found in the specified folder.")
        return

    # Load the audio file
    audio_clip = AudioFileClip(audio_file)

    # Create a list to store video clips with the background videos
    video_clips = []

    for background_video in background_videos:
        # Load each background video
        background_clip = VideoFileClip(background_video)

        # Set the audio of the background video to the given audio file
        video_with_audio = background_clip.set_audio(audio_clip)

        # Append the video with audio to the list
        video_clips.append(video_with_audio)

    # Concatenate all video clips into a single video
    final_video = CompositeVideoClip(video_clips)

    # Write the final video to the specified output location
    final_video.write_videofile(output_location, codec='libx264', audio_codec='aac')

    print(f"Video created successfully at: {output_location}")

# Example usage
background_folder = "backgroundvideos"
audio_file = "fact.mp3"
output_location = "video1.mp4"

create_video(background_folder, audio_file, output_location)
