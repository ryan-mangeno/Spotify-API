import urllib.request
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
ua = UserAgent()

from selenium import webdriver
import time

video_url_list = []
video_title_list = []
video_requests = []

with open("songs.txt", "r") as file:
    for line in file:
        video_requests.append(line)

# Set up the Chrome driver (you can use other browsers as well)
driver = webdriver.Chrome()
for video_request in video_requests:
    try:
    #Navigate to the YouTube search page
        driver.get(f'https://www.youtube.com/results?search_query={video_request}')
        time.sleep(5)
    # Get the page source (fully rendered content)
        page_source = driver.page_source

        soup = bs(page_source, 'html.parser')
        video_title_elements = soup.find_all('a', {'class': 'yt-simple-endpoint'})
        for video_title_element in video_title_elements:
            # Extract the title
            title = video_title_element.get('title', '')
            # Extract the video URL doing 'href','', '' serves as a default is none type is found
            video_url = 'https://www.youtube.com' + video_title_element.get('href', '')

            # this acts as another error check, if a non type is found an is defaulted to '', then 'watch' wouldnt be in the .get
            if title and 'watch' in video_title_element.get('href', ''):
                print(video_url,'\n', title)
                sub_video_list = video_url.split('&')
                print(f"Title: {title}")
                print(f"Video URL: {sub_video_list[0]}")
                video_title_list.append(title)
                video_url_list.append(sub_video_list[0])
                break
    except Exception as e:
        print(f'Error: {e}')

driver.quit()

import youtube_dl
from pytube import YouTube
import os


def download_and_convert_to_audio(video_url, output_path,titles):
    #make output path if doesnt exist
    os.makedirs(output_path,exist_ok=True)
    os.chdir(output_path)

    for song,url in zip(titles,video_url):
        try:
            song_search_pre = f"{song}.mp4"
            song_search = song_search_pre.replace("'","")

            if song_search in os.listdir(output_path):
                continue
            # Download the YouTube video

            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=False, file_extension='mp4').first()
            stream.download(output_path)
            print("Downloaded")

        except Exception as e:
            print(f"error {e}")

        
output_path = os.path.join(os.path.expanduser("~"), "Music",)
download_and_convert_to_audio(video_url_list,output_path, video_title_list)



def download(url_list):
    output_path = os.path.join(os.path.expanduser("~"), "Music", "%(title)s.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',  # Select the best audio format available
        'outtmpl': output_path,  # Set the output path template
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download(url_list)

download(video_url_list)
