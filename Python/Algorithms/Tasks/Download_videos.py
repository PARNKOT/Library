from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=0ph1dIHXEVE&list=LL&index=2"

try:
    video_obj = YouTube(video_url)
    filters = video_obj.streams.filter(progressive=True, file_extension="mp4")

    filters.get_highest_resolution().download()
    print("Video is downloaded successfully")
except Excepttion as e:
    print(e)
