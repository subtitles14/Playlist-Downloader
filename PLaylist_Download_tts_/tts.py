import yt_dlp

def download_playlist(playlist_url, download_path, resolution):
    # Remove the "p" from resolution (e.g., "720p" -> "720")
    res_value = ''.join(filter(str.isdigit, resolution))

    ydl_opts = {
        "outtmpl": f"{download_path}/%(playlist_title)s/%(title)s.%(ext)s",  # Save inside playlist folder
        "format": f"bestvideo[height<={res_value}]+bestaudio/best[height<={res_value}]",
        "merge_output_format": "mp4",   # Always save as MP4
        "ignoreerrors": True,           # Skip failed videos
        "noplaylist": False,            # Ensure full playlist downloads
        "quiet": False,                 # Show progress
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading playlist from: {playlist_url}")
            ydl.download([playlist_url])
            print("✅ Playlist download complete!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    url = input("Enter playlist URL: ").strip()
    path = input("Enter download path: ").strip()
    res = input("Enter resolution (e.g., 720p): ").strip()

    download_playlist(url, path, res)
