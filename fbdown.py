import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import wget

def get_video_url(url):
    if 'www' in url:
        url = url.replace('www', 'm')

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'xml')
    for a in soup.find_all("a"):
        try:
            hrefOfA = a['href']
        except:
            continue
        else:
            if '.mp4' in hrefOfA:
                    videoUrl = hrefOfA.split('src=')[-1]
                    decodedVideoUrl = unquote(videoUrl)
                    return decodedVideoUrl

def download_video(url, fileLoc=''):
    print("[>>>] Downloading...")
    wget.download(url, fileLoc)
    print("[>>>] Success")

    return


if __name__ == "__main__":
    urlTarget = "https://www.facebook.com/watch?v=1469537626825571"
    videoUrl = get_video_url(urlTarget)
    print(videoUrl)
    download_video(videoUrl)