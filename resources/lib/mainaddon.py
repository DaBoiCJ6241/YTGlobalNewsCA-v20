import requests
import re
from bs4 import BeautifulSoup

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
get_soup1("https://www.youtube.com/feeds/videos.xml?channel_id=UChLtXXpo4Ge1ReTEboVvTDg")

def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
get_soup2("https://www.youtube.com/feeds/videos.xml?channel_id=UCkiP0kvvwqUWlttRLCq88gw")

def get_soup3(url3):
    page = requests.get(url3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup3))
    return soup3
get_soup3("https://www.youtube.com/feeds/videos.xml?channel_id=UCxUD8G1jO8T-Ef2tuADCZOA")

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('media:content')
            link = link.get('url')
            print("\n\nLink: ", link)
            thumbnail = content.find('media:thumbnail')
            thumbnail = thumbnail.get('url')
            title = content.find('media:title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('media:content')
            link = link.get('url')
            print("\n\nLink: ", link)
            thumbnail = content.find('media:thumbnail')
            thumbnail = thumbnail.get('url')
            title = content.find('media:title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast3(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('media:content')
            link = link.get('url')
            print("\n\nLink: ", link)
            thumbnail = content.find('media:thumbnail')
            thumbnail = thumbnail.get('url')
            title = content.find('media:title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
