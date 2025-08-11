"""
動画品質選択ロジック
"""
import yt_dlp

class VideoQualitySelector:
    @staticmethod
    def get_video_info(url):
        """動画情報を取得"""
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except Exception as e:
            print(f"動画情報取得エラー: {e}")
            return None
    
    @staticmethod
    def auto_select_quality(url, default_quality):
        """動画に最適な品質を自動選択"""
        print(f"動画情報を取得中...")
        info = VideoQualitySelector.get_video_info(url)
        
        if not info:
            print("情報取得失敗、デフォルト品質を使用")
            return default_quality
        
        # 利用可能な最高解像度を取得
        max_height = 0
        duration = info.get('duration', 0)
        
        for fmt in info.get('formats', []):
            height = fmt.get('height', 0)
            if height and height > max_height:
                max_height = height
        
        print(f"動画情報: 最高解像度={max_height}p, 長さ={duration//60}分{duration%60}秒")
        
        # 自動選択ロジック
        if max_height >= 2160:  # 4K対応
            if duration > 3600:  # 1時間以上の長時間動画
                selected = '1080p'  # ファイルサイズ考慮
                reason = "長時間動画のためファイルサイズを考慮"
            else:
                selected = '4k'
                reason = "4K品質対応"
        elif max_height >= 1440:  # 1440p対応
            selected = '1440p'
            reason = "1440p品質対応"
        elif max_height >= 1080:  # 1080p対応
            selected = '1080p'
            reason = "1080p品質対応"
        elif max_height >= 720:   # 720p対応
            selected = '720p'
            reason = "720p品質対応"
        else:  # 低解像度
            selected = '480p'
            reason = "低解像度動画"
        
        print(f"自動選択結果: {selected} ({reason})")
        return selected
    
    @staticmethod
    def get_quality_format(quality):
        """品質設定をyt-dlpフォーマット文字列に変換"""
        quality_map = {
            'highest': 'best',
            '4k': 'best[height<=2160]',
            '1440p': 'best[height<=1440]',
            '1080p': 'best[height<=1080]',
            '720p': 'best[height<=720]',
            '480p': 'best[height<=480]',
            'h264_1080p': 'best[height<=1080][vcodec^=avc1]/best[height<=1080]',
            'h265_1080p': 'best[height<=1080][vcodec*=hev1]/best[height<=1080]',
            'h264_720p': 'best[height<=720][vcodec^=avc1]/best[height<=720]',
            'h265_720p': 'best[height<=720][vcodec*=hev1]/best[height<=720]',
            'medium': 'best[height<=720][ext=mp4]',
            'small': 'best[height<=360][filesize<50M]',
            'balanced': 'best[height<=720]/best[height<=480]/best',
            'compatible': 'best[height<=1080][vcodec^=avc1][ext=mp4]/best[height<=1080][ext=mp4]',
        }
        return quality_map.get(quality, 'best[height<=1080]')