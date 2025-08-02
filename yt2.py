import ssl

from pytube import YouTube # type: ignore

ssl._create_default_https_context = ssl._create_unverified_context

url = input("Enter the YouTube video URL: ")
yt = YouTube(url)

audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download()
print("Audio downloaded successfully!")
# print("Title:", yt.title)
# print("Length:", yt.length, "seconds")
# print("Views:", yt.views)
# print("Rating:", yt.rating)
# print("Description:", yt.description)
# print("Author:", yt.author)
# print("Publish Date:", yt.publish_date)
# print("Thumbnail URL:", yt.thumbnail_url)
# print("Audio Stream URL:", audio_stream.url)
# print("Audio Stream Type:", audio_stream.mime_type)
# print("Audio Stream Resolution:", audio_stream.resolution)
# print("Audio Stream Codec:", audio_stream.codecs)
# print("Audio Stream Bitrate:", audio_stream.bitrate)
# print("Audio Stream FPS:", audio_stream.fps)
# print("Audio Stream File Size:", audio_stream.filesize)
# print("Audio Stream File Size (MB):", audio_stream.filesize / (1024 * 1024))
# print("Audio Stream File Size (GB):", audio_stream.filesize / (1024 * 1024 * 1024))
# print("Audio Stream File Size (KB):", audio_stream.filesize / 1024)

