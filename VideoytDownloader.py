import pytube
import re
from pytube import YouTube
from pytube.cli import on_progress

# Fungsi untuk memperbaiki bug di pytube
def patch_pytube():
    yt_extractor = pytube.extract
    if not hasattr(yt_extractor, '_js_initial_function_patched'):
        yt_extractor._js_initial_function_patched = True
        yt_extractor.initial_function = re.compile(r"function\([^)]*\)\s*{.*?return.*?;}", re.DOTALL)

# Panggil fungsi patch sebelum membuat objek YouTube
patch_pytube()

# Fungsi utama untuk mendownload video 4K tanpa audio
def download_4k_video_without_audio():
    # Meminta input URL dari pengguna
    url = input("Masukkan URL YouTube: ")
    
    try:
        # Membuat objek YouTube
        yt = YouTube(url)
        
        # Menampilkan judul video
        print("Judul Video: ", yt.title)
        
        # Mendapatkan stream video dengan resolusi 4K (video-only)
        video_stream = yt.streams.filter(res="2160p", file_extension="mp4", progressive=False).first()
        
        # Jika video 4K tidak ditemukan
        if not video_stream:
            print("Video dengan resolusi 4K tidak tersedia.")
            return
        
        # Menampilkan info video
        print("Resolusi yang akan didownload: ", video_stream.resolution)
        
        # Mendownload video
        print("Sedang mendownload video 4K (tanpa audio)...")
        video_stream.download(output_path="./", filename="video_4k.mp4")
        print("Video 4K berhasil didownload!")

    except Exception as e:
        print("Terjadi kesalahan:", e)

# Panggil fungsi download
download_4k_video_without_audio()
