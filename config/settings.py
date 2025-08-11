"""
アプリケーション設定
"""

# デフォルト品質設定
DEFAULT_VIDEO_QUALITY = '1080p'
DEFAULT_AUDIO_QUALITY = '192'

# 出力先設定
OUTPUT_DIR = 'downloads'
AUDIO_DIR = 'downloads/audio'
VIDEO_DIR = 'downloads/video'

# yt-dlp設定
YT_DLP_OPTIONS = {
    'ignoreerrors': True,
    'retries': 3,
}