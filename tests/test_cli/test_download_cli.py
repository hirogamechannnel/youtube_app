"""
download_cliのテスト
"""
import pytest
from unittest.mock import Mock, patch, call
import sys
from io import StringIO
from cli.download_cli import main

class TestDownloadCli:
    def test_help_display(self):
        """ヘルプ表示テスト"""
        with patch('sys.argv', ['download_cli.py', '--help']):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 0
    
    @patch('cli.download_cli.YoutubeDownloader')
    @patch('cli.download_cli.os.makedirs')
    def test_mp4_download(self, mock_makedirs, mock_downloader_class, sample_youtube_url):
        """MP4ダウンロードテスト"""
        mock_downloader = Mock()
        mock_downloader_class.return_value = mock_downloader
        
        with patch('sys.argv', ['download_cli.py', sample_youtube_url]):
            main()
        
        mock_makedirs.assert_called_once_with('downloads/video/', exist_ok=True)
        mock_downloader.download_mp4.assert_called_once_with(sample_youtube_url, 'downloads/video/')
    
    @patch('cli.download_cli.YoutubeDownloader')
    @patch('cli.download_cli.os.makedirs')
    def test_mp3_download(self, mock_makedirs, mock_downloader_class, sample_youtube_url):
        """MP3ダウンロードテスト"""
        mock_downloader = Mock()
        mock_downloader_class.return_value = mock_downloader
        
        with patch('sys.argv', ['download_cli.py', sample_youtube_url, '-f', 'mp3']):
            main()
        
        mock_makedirs.assert_called_once_with('downloads/audio/', exist_ok=True)
        mock_downloader.download_mp3.assert_called_once_with(sample_youtube_url, 'downloads/audio/')
    
    @patch('cli.download_cli.YoutubeDownloader')
    def test_keyboard_interrupt(self, mock_downloader_class, sample_youtube_url, capsys):
        """キーボード中断テスト"""
        mock_downloader = Mock()
        mock_downloader_class.return_value = mock_downloader
        mock_downloader.download_mp4.side_effect = KeyboardInterrupt()
        
        with patch('sys.argv', ['download_cli.py', sample_youtube_url]):
            main()
        
        captured = capsys.readouterr()
        assert "ダウンロードが中断されました" in captured.out