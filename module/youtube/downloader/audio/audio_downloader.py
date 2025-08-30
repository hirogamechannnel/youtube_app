"""
音声ダウンロード機能
"""
import yt_dlp
import shutil
from .audio_quality_selector import AudioQualitySelector

try:
    import imageio_ffmpeg as ffmpeg
    FFMPEG_PATH = ffmpeg.get_ffmpeg_exe()
except ImportError:
    FFMPEG_PATH = None

class AudioDownloader:
    def __init__(self, default_quality='192'):
        self.default_quality = default_quality
        self.has_ffmpeg = FFMPEG_PATH is not None or shutil.which('ffmpeg') is not None
    
    def download(self, url, output_path):
        """自動音質選択でMP3ダウンロード"""
        print(f"MP3ダウンロード開始: {url}")
        
        # 自動音質選択
        auto_quality = AudioQualitySelector.auto_select_audio_quality(url, self.default_quality)
        
        # 基本設定（YouTube制限回避）
        base_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'ignoreerrors': True,
            'retries': 3,
            'extractor_args': {
                'youtube': {
                    'player_client': ['android', 'web'],
                    'player_skip': ['webpage']
                }
            },
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        }
        
        # FFmpegの有無に応じた設定
        if self.has_ffmpeg:
            # FFmpeg利用可能な場合はMP3変換
            ydl_opts = {
                **base_opts,
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': auto_quality,
                }]
            }
            # imageio-ffmpegのパスを指定
            if FFMPEG_PATH:
                ydl_opts['ffmpeg_location'] = FFMPEG_PATH
        else:
            # FFmpeg未インストール時はm4aで保存
            print("警告: FFmpegが見つかりません。m4a形式で保存します")
            ydl_opts = {
                **base_opts,
                'format': 'bestaudio[ext=m4a]/bestaudio/best'
            }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            format_name = "MP3" if self.has_ffmpeg else "M4A"
            print(f"{format_name}ダウンロード完了 (選択音質: {auto_quality}kbps)")
        except Exception as e:
            print(f"エラー: {e}")