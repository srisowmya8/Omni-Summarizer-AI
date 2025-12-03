from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    """Extract YouTube video ID from URL."""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    return None

def get_transcript(video_url, lang="en"):
    video_id = extract_video_id(video_url)
    if not video_id:
        return None

    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    full_text = " ".join([t["text"] for t in transcript])
    return full_text
