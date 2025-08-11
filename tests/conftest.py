"""
pytest共通設定とフィクスチャ
"""
import pytest
import os
import tempfile
import shutil

@pytest.fixture
def temp_output_dir():
    """テスト用一時出力ディレクトリ"""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

@pytest.fixture
def sample_youtube_url():
    """テスト用YouTube URL"""
    return "https://youtube.com/watch?v=dQw4w9WgXcQ"

@pytest.fixture
def mock_video_info():
    """モック動画情報"""
    return {
        'title': 'Test Video',
        'duration': 180,  # 3分
        'formats': [
            {'height': 1080, 'abr': 192},
            {'height': 720, 'abr': 128},
            {'height': 480, 'abr': 96}
        ]
    }