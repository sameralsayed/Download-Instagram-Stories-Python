from yt_dlp import YoutubeDL  # pip install yt-dlp

def download_instagram_story(url, output_path='./downloads'):
    """
    Download an Instagram Story (best quality MP4).
    
    Args:
    url (str): Instagram Story URL (e.g., 'https://www.instagram.com/stories/username/story_id/' or highlight link).
    output_path (str): Directory to save the Story (default: './downloads').
    
    Returns:
    dict: Info about the downloaded Story if successful, None otherwise.
    """
    try:
        # Configure options for Story download
        ydl_opts = {
            'format': 'best[ext=mp4]/best',  # Prefer MP4, fallback to best
            'outtmpl': f'{output_path}/%(uploader)s - Story %(id)s.%(ext)s',  # Output filename template (includes creator and ID)
            'noplaylist': False,  # Allow multiple if it's a series of stories
        }
        
        # Download the Story
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Story downloaded successfully to {output_path}!")
        return ydl.extract_info(url, download=False)  # Return metadata
        
    except Exception as e:
        print(f"Error downloading Story: {e}")
        return None

# Example usage
if __name__ == "__main__":
    STORY_URL = "https://www.instagram.com/stories/username/1234567890/"  # Replace with your public Instagram Story URL
    download_instagram_story(STORY_URL)