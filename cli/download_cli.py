"""
動画ダウンロード専用CLI

使用例:
    # 基本使用（MP4、自動品質選択）
    py -m cli.download_cli "https://youtube.com/watch?v=dQw4w9WgXcQ"
    
    # MP3ダウンロード（自動音質選択）
    py -m cli.download_cli "https://youtube.com/watch?v=dQw4w9WgXcQ" -f mp3
    
    # ヘルプ表示
    py -m cli.download_cli --help
"""
import argparse
import os
from module.youtube.downloader.youtube_downloader import YoutubeDownloader

def main():
    parser = argparse.ArgumentParser(
        description='YouTube動画ダウンロード（自動品質選択）',
        epilog='例: py -m cli.download_cli "https://youtube.com/watch?v=xxx" -f mp3'
    )
    parser.add_argument('url', help='YouTube URL')
    parser.add_argument('-f', '--format', choices=['mp3', 'mp4'], default='mp4', help='形式')
    
    args = parser.parse_args()
    
    try:
        # インスタンス作成
        downloader = YoutubeDownloader()
        
        # 形式に応じて保存先を設定
        if args.format == 'mp3':
            output_path = 'downloads/audio/'
            os.makedirs(output_path, exist_ok=True)
            
            print(f"ダウンロード開始: {args.url}")
            print(f"形式: {args.format}")
            print(f"品質: 自動選択")
            print(f"保存先: {output_path}")
            
            downloader.download_mp3(args.url, output_path)
            print("MP3ダウンロード完了")
        else:
            output_path = 'downloads/video/'
            os.makedirs(output_path, exist_ok=True)
            
            print(f"ダウンロード開始: {args.url}")
            print(f"形式: {args.format}")
            print(f"品質: 自動選択")
            print(f"保存先: {output_path}")
            
            downloader.download_mp4(args.url, output_path)
            print("MP4ダウンロード完了")
            
    except KeyboardInterrupt:
        print("\nダウンロードが中断されました")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == '__main__':
    main()