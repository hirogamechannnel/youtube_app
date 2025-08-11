"""
SNS自動投稿機能
"""

class SNSPoster:
    def __init__(self):
        print("SNS投稿機能作成")
    
    def post_to_twitter(self, message):
        """Twitter投稿"""
        print(f"Twitter投稿: {message}")
    
    def post_to_instagram(self, image_path, caption):
        """Instagram投稿"""
        print(f"Instagram投稿: {caption}")
    
    def post_to_facebook(self, message):
        """Facebook投稿"""
        print(f"Facebook投稿: {message}")