"""
音質選択ロジック
"""
import yt_dlp

class AudioQualitySelector:
    @staticmethod
    def get_audio_info(url):
        """音声情報を取得"""
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
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
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info
        except Exception as e:
            print(f"音声情報取得エラー: {e}")
            return None
    
    @staticmethod
    def auto_select_audio_quality(url, default_quality):
        """動画に最適な音質を自動選択"""
        print(f"音声情報を取得中...")
        info = AudioQualitySelector.get_audio_info(url)
        
        if not info:
            print("情報取得失敗、デフォルト音質を使用")
            return default_quality
        
        # 利用可能な最高音質を取得
        max_abr = 0
        duration = info.get('duration', 0)
        
        for fmt in info.get('formats', []):
            abr = fmt.get('abr', 0)
            if abr and abr > max_abr:
                max_abr = abr
        
        print(f"音声情報: 最高音質={max_abr}kbps, 長さ={duration//60}分{duration%60}秒")
        
        # 自動選択ロジック
        if max_abr >= 320:  # 高音質対応
            selected = '320'
            reason = "高音質対応"
        elif max_abr >= 256:  # 中高音質
            selected = '256'
            reason = "中高音質対応"
        elif max_abr >= 192:  # 標準音質
            selected = '192'
            reason = "標準音質対応"
        elif max_abr >= 128:  # 低音質
            selected = '128'
            reason = "低音質対応"
        else:  # 最低音質
            selected = '96'
            reason = "最低音質"
        
        print(f"自動選択結果: {selected}kbps ({reason})")
        return selected