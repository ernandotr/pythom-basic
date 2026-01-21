from pytube import YouTube
from pytube.cli import on_progress

def download_youtube_video(url, output_path):
    """
    Download a YouTube video.

    :param url: The URL of the YouTube video.
    :param output_path: The path where the video will be saved.
    """
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Title: {yt.title}")
        print(f"Length: {yt.length} seconds")
        print(f"Views: {yt.views}")
        print(f"Rating: {yt.rating}")
        print(f"Description: {yt.description}")
        print(f"Author: {yt.author}")
        print(f"Publish Date: {yt.publish_date}")
        print(f"Thumbnail URL: {yt.thumbnail_url}")

        # Download the highest resolution stream
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path)
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_directory = input("Enter the output directory (default is current directory): ")
    if not output_directory:
        output_directory = "."
    download_youtube_video(video_url, output_directory)