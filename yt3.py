import yt_dlp

def list_formats(video_url):
    ydl_opts = {
        'listformats': True  # Lists all available formats
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(video_url, download=False)

def download_youtube_video(video_url, format_code):
    ydl_opts = {
        'format': format_code  # Uses specified format
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Request video URL from user
video_url = input("Please enter the full URL of the YouTube video: ")

# List available formats
list_formats(video_url)

# Request format code
format_code = input("Please enter the format code to be downloaded (e.g. 137+140): ")


try:
    print(f"Download video in format {format_code}...")
    download_youtube_video(video_url, format_code)
    print("Download completed successfully.")
except ValueError as e:
    print(e)
   
    

