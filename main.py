from pytube import YouTube
import subprocess

def download_video(link, path):
    try:
        vid = YouTube(link)
        stream = vid.streams.first()
        stream.download(path)
        return stream.title
    except:
        print("Invalid YouTube link.")
        return False

def change_to_audio(title, path):
    process = subprocess.run(["ffmpeg", "-i", f"{path}{title}.mp4", "-vn", "-sn", "-c:a", "mp3", "-ab", "192k", f"../../Downloads/{title}.mp3"], capture_output=True)
    print("Audio download complete.")

def delete_mp4(title, path):
    process = subprocess.run(["rm", f"{path}{title}.mp4"])
    process = subprocess.run(["rmdir", "./tmp"])


link = input("Enter YouTube link: ")
download_format = input("Would you like audio or video format? ")

if download_format == "video":
    path = "../../Downloads"
    cont = download_video(link, path)
    if cont:
        print("Video download complete.")

elif download_format == "audio":
    path = "./tmp/"
    print("Checking video link...")
    title = download_video(link, path).replace("'", "")
    print("\nThis may take a while.. please be patient.\n")
    change_to_audio(title, path)
    delete_mp4(title, path)
