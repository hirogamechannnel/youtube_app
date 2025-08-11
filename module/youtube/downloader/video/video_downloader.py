"""
動画ダウンロード機能
"""
import yt_dlp
from .video_quality_selector import VideoQualitySelector

class VideoDownloader:
    def __init__(self, default_quality='1080p'):
        self.default_quality = default_quality
    
    def download(self, url, output_path):
        """自動品質選択でMP4ダウンロード"""
        print(f"MP4自動ダウンロード開始: {url}")
        
        # 自動品質選択
        auto_quality = VideoQualitySelector.auto_select_quality(url, self.default_quality)
        
        # 選択された品質でダウンロード
        ydl_opts = {
            'format': VideoQualitySelector.get_quality_format(auto_quality),
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'ignoreerrors': True,
            'retries': 3,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"MP4自動ダウンロード完了 (選択品質: {auto_quality})")
        except Exception as e:
            print(f"エラー: {e}")