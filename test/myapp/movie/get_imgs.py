import requests
from pymongo import MongoClient

def get_url():
    client = MongoClient()
    db = client['dytt']
    col = db['zuixindianying']
    items = col.find({'海报大图': {'$ne': None}})
    for item in items[:30]:
        # print(item)
        url = item.get('海报大图')
        try:
            save_img(url[0])
        except:
            print('failed')
            continue


def save_img(url):
    print('start')
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    img = requests.get(url, headers=headers, timeout=3)
    name = url[-9: -4]
    f = open('./static/movie/img/' + name + '.jpg', 'ab')
    f.write(img.content)
    f.close()
    print('saved')

if __name__ == '__main__':
    get_url()