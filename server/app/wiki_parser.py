import json
import requests
import os


INDO_PLANTS= ['suweg', 'zodia', 'nilan' ]

def get_raw_intro_text(title):
    response = requests.get(
        'https://en.wikipedia.org/w/api.php',
        params={
            'action': 'query',
            'format': 'json',
            'titles': title,
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True
        },
        allow_redirects=True,
        ).json()
    page = next(iter(response['query']['pages'].values()))
    result=""
    try:
        result = page['extract']
    except:
        result= 'No wikipedia content'
    return result


def get_image_urls(title):
    response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
        'action': 'query',
        'format': 'json',
        'titles': title,
        'prop': 'imageinfo',
        'iiprop': 'url',
        'generator':'images',
    },
    allow_redirects=True
    ).json()
    try:
        image_urls = [response['query']['pages']['-3']['imageinfo'][0]['url'],response['query']['pages']['-2']['imageinfo'][0]['url']]
    except:
        image_urls = ['./asset/image/noImage.jpg', './asset/image/noImage.jpg']
    return image_urls


def get_result(title):
    PATH=f"cache/{title}.json"
    if os.path.exists(PATH):
        file = open(PATH)
        result= json.loads(file.read())
    else:
        result=None
        if title in INDO_PLANTS:
            result = {
                'title': title,
                'text': 'There is no content in English wikipedia',
                'url_1': '#',
                'url_2': '#',
                'link': f'https://id.wikipedia.org/wiki/{title}',
            }
        else:
            image_urls = get_image_urls(title)
            result={
                'title': title,
                'text': get_raw_intro_text(title),
                'url_1': image_urls[0],
                'url_2': image_urls[1],
                'link': f'https://en.wikipedia.org/wiki/{title}',
            }
        result = json.dumps(result)
        with open(PATH,"w", encoding='utf-8') as file:
            file.write(result)
    return result