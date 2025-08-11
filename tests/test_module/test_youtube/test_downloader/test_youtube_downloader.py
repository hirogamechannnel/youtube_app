"""
YoutubeDownloaderのテスト
"""
import pytest
from unittest.mock import Mock, patch
from module.youtube.downloader.youtube_downloader import YoutubeDownloader

class TestYoutubeDownloader:
    def test_init(self):
        """初期化テスト"""
        with patch('module.youtube.downloader.youtube_downloader.AudioDownloader') as mock_audio, \
             patch('module.youtube.downloader.youtube_downloader.VideoDownloader') as mock_video:
            
            downloader = YoutubeDownloader()
            
            mock_audio.assert_called_once_with('192')
            mock_video.assert_called_once_with('1080p')
    
    def test_init_with_custom_quality(self):
        """カスタム品質での初期化テスト"""
        with patch('module.youtube.downloader.youtube_downloader.AudioDownloader') as mock_audio, \
             patch('module.youtube.downloader.youtube_downloader.VideoDownloader') as mock_video:
            
            downloader = YoutubeDownloader('720p', '256')
            
            mock_audio.assert_called_once_with('256')
            mock_video.assert_called_once_with('720p')
    
    def test_download_mp3(self, sample_youtube_url):
        """MP3ダウンロードテスト"""
        with patch('module.youtube.downloader.youtube_downloader.AudioDownloader') as mock_audio_class:
            mock_audio = Mock()
            mock_audio_class.return_value = mock_audio
            
            downloader = YoutubeDownloader()
            downloader.download_mp3(sample_youtube_url, "test_output/")
            
            mock_audio.download.assert_called_once_with(sample_youtube_url, "test_output/")
    
    def test_download_mp4(self, sample_youtube_url):
        """MP4ダウンロードテスト"""
        with patch('module.youtube.downloader.youtube_downloader.VideoDownloader') as mock_video_class:
            mock_video = Mock()
            mock_video_class.return_value = mock_video
            
            downloader = YoutubeDownloader()
            downloader.download_mp4(sample_youtube_url, "test_output/")
            
            mock_video.download.assert_called_once_with(sample_youtube_url, "test_output/")