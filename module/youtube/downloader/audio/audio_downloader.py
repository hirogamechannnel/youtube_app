"""
音声ダウンロード機能
"""
import yt_dlp
from .audio_quality_selector import AudioQualitySelector

class AudioDownloader:
    def __init__(self, default_quality='192'):
        self.default_quality = default_quality
    
    def download(self, url, output_path):
        """自動音質選択でMP3ダウンロード"""
        print(f"MP3ダウンロード開始: {url}")
        
        # 自動音質選択
        auto_quality = AudioQualitySelector.auto_select_audio_quality(url, self.default_quality)
        
        # yt-dlp設定
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': auto_quality,
            }],
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'ignoreerrors': True,
            'retries': 3,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"MP3ダウンロード完了 (選択音質: {auto_quality}kbps)")
        except Exception as e:
            print(f"エラー: {e}")