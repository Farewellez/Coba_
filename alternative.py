import yt_dlp

def download_4k_video_without_audio():
    # Meminta URL video dari pengguna
    url = input("Masukkan URL YouTube: ")
    
    # Opsi untuk mendownload video dengan resolusi 4K
    ydl_opts = {
        'format': 'bestvideo[height<=2160][ext=mp4]',  # Resolusi 4K tanpa audio
        'outtmpl': 'video_4k.mp4'  # Nama file output
    }

    try:
        # Membuat objek yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Sedang mendownload video 4K (tanpa audio)...")
            ydl.download([url])
            print("Video 4K berhasil didownload!")
    except Exception as e:
        print("Terjadi kesalahan:", e)

# Panggil fungsi
download_4k_video_without_audio()
