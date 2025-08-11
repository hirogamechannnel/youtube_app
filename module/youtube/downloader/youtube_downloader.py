"""
YouTubeダウンローダー統合インターフェース
"""
from .audio.audio_downloader import AudioDownloader
from .video.video_downloader import VideoDownloader

class YoutubeDownloader:
    def __init__(self, video_quality='1080p', audio_quality='192'):
        self.audio_downloader = AudioDownloader(audio_quality)
        self.video_downloader = VideoDownloader(video_quality)
    
    def download_mp3(self, url, output_path="downloads/audio/"):
        """動画をMP3形式でダウンロード"""
        self.audio_downloader.download(url, output_path)
    
    def download_mp4(self, url, output_path="downloads/video/"):
        """自動品質選択でMP4ダウンロード"""
        self.video_downloader.download(url, output_path)