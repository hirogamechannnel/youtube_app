# YouTube App

YouTube動画ダウンロードアプリケーション（自動品質選択機能付き）

## 特徴

- **完全自動品質選択**: 動画の解像度や音質を自動で最適化
- **シンプルCLI**: URLと形式だけ指定で簡単ダウンロード
- **PEP 8準拠**: Python標準の命名規則に完全準拠
- **モジュラー設計**: 機能別に整理された構成
- **エラーハンドリング**: 適切なエラー処理とリトライ機能

## プロジェクト構成

```
youtube_app/
├── cli/
│   └── download_cli.py           # CLIインターフェース
├── config/
│   └── settings.py              # 設定ファイル
├── module/
│   ├── youtube/
│   │   └── downloader/          # YouTubeダウンロード機能
│   │       ├── audio/           # 音声ダウンロードモジュール
│   │       │   ├── audio_downloader.py
│   │       │   └── audio_quality_selector.py
│   │       ├── video/           # 動画ダウンロードモジュール
│   │       │   ├── video_downloader.py
│   │       │   └── video_quality_selector.py
│   │       └── youtube_downloader.py # 統合インターフェース
│   └── sns/                     # SNS機能（将来拡張用）
│       └── poster.py
├── utils/                       # 共通ユーティリティ
├── requirements.txt              # 依存ライブラリ
└── README.md                    # このファイル
```

## セットアップ

```cmd
# 依存関係インストール
pip install -r requirements.txt
```

## 使用方法

### CLIツール

```cmd
# 基本使用（MP4、自動品質選択）
py -m cli.download_cli "https://youtube.com/watch?v=dQw4w9WgXcQ"

# MP3ダウンロード（自動音質選択）
py -m cli.download_cli "https://youtube.com/watch?v=dQw4w9WgXcQ" -f mp3

# ヘルプ表示
py -m cli.download_cli --help
```

### プログラムからの使用

```python
from module.youtube.downloader.youtube_downloader import YoutubeDownloader

# ダウンローダー作成（自動品質選択）
downloader = YoutubeDownloader()

# MP4ダウンロード（自動品質選択）
downloader.download_mp4("https://youtube.com/watch?v=xxx")

# MP3ダウンロード（自動音質選択）
downloader.download_mp3("https://youtube.com/watch?v=xxx")
```

## 機能

### 自動品質選択

- **動画品質**: 動画の最高解像度に応じて4K/1440p/1080p/720p/480pから自動選択
- **音声品質**: 音声の最高音質に応じて320/256/192/128/96kbpsから自動選択
- **長時間動画**: ファイルサイズを考慮して品質調整
- **フォールバック**: 情報取得失敗時はデフォルト品質を使用
- **保存先**: MP3は`downloads/audio/`、MP4は`downloads/video/`に自動保存

### サポート形式

- **MP4**: 動画ファイル（H.264/H.265コーデック対応）
- **MP3**: 音声ファイル（可変ビットレート）

### エラーハンドリング

- ネットワークエラーの自動リトライ（3回）
- キーボード中断（Ctrl+C）対応
- 適切なエラーメッセージ表示

## 自動品質選択の仕組み

### 動画品質選択ロジック

1. 動画情報を取得
2. 利用可能な最高解像度を確認
3. 動画の長さを考慮
4. 最適な品質を自動選択

```
利用可能解像度 → 選択される品質
4K (2160p)以上 → 4K または 1080p（長時間動画の場合）
1440p以上     → 1440p
1080p以上     → 1080p
720p以上      → 720p
それ以下      → 480p
```

### 音声品質選択ロジック

```
利用可能音質 → 選択される音質
320kbps以上 → 320kbps（高音質）
256kbps以上 → 256kbps（中高音質）
192kbps以上 → 192kbps（標準音質）
128kbps以上 → 128kbps（低音質）
それ以下   → 96kbps（最低音質）
```

## 技術仕様

- **Python**: 3.7+
- **依存ライブラリ**: yt-dlp, requests
- **命名規則**: PEP 8準拠
- **アーキテクチャ**: モジュラー設計
- **外部ツール**: FFmpeg（音声変換用）

## ファイル出力

```
downloads/
├── audio/          # MP3ファイル
│   └── *.mp3
└── video/          # MP4ファイル
    └── *.mp4
```

## ライセンス

個人使用のみ。YouTubeの利用規約を遵守してください。