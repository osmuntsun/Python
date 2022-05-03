import bs4
import urllib.request as req
import requests
import json
import os


def vid(url,username,i):
    r = requests.get(url)
    with open('./%s/vid%s.mp4'%(username,i), "wb") as code:
        code.write(r.content)
def img(url,username,i):
    r = requests.get(url)
    with open('./%s/image%s.jpg'%(username,i), "wb") as code:
        code.write(r.content)

def next_url(url_key):
    url_key = url_key.replace('==','')
    next_url='https://www.instagram.com/graphql/query/?query_hash=003056d32c2554def87228bc3fd9668a&variables=%7B%22id%22%3A%22212843255%22%2C%22first%22%3A12%2C%22after%22%3A%22'+'%s'%url_key + '%3D%3D%22%7D'
    next_url = req.Request(next_url, headers={
        'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    })
    with req.urlopen(next_url) as response:
        next_url = response.read().decode('utf-8')
    next_url = json.loads(next_url)
    return next_url

def for_page(datas,sums,user):
    sums= sums
    for i in datas:
        TF = i['node']['__typename']
        if os.path.exists("./%s"%user):
            if TF == 'GraphSidecar':
                posts = i['node']['edge_sidecar_to_children']['edges']
                for post in posts:
                    if post['node']['is_video'] == True:
                        sums+=1
                        vid(post['node']['video_url'],user,sums)
                    else:
                        sums+=1
                        img(post['node']['display_url'],user,sums)
            elif TF == 'GraphVideo':
                sums+=1
                vid(i['node']['video_url'],user,sums)
            elif TF == 'GraphImage':
                sums+=1
                img(i['node']['display_url'],user,sums)
        else:
            os.mkdir("./%s"%user)
            if TF == 'GraphSidecar':
                posts = i['node']['edge_sidecar_to_children']['edges']
                for post in posts:
                    if post['node']['is_video'] == True:
                        sums+=1
                        vid(post['node']['video_url'],user,sums)
                    else:
                        sums+=1
                        img(post['node']['display_url'],user,sums)
            elif TF == 'GraphVideo':
                sums+=1
                vid(i['node']['video_url'],user,sums)
            elif TF == 'GraphImage':
                sums+=1
                img(i['node']['display_url'],user,sums)
    return sums

def igcrawler(user):
    url = 'https://www.instagram.com/%s/?__a=1'%user

    request = req.Request(url, headers={
        'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    })

    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')

    data = json.loads(data)
    datas = data['graphql']['user']['edge_owner_to_timeline_media']['edges']
    frist_determine = data['graphql']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
    frist_next_page = data['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']



    sums=0
    for i in datas:
        TF = i['node']['__typename']
        if os.path.exists("./%s"%user):
            if TF == 'GraphSidecar':
                posts = i['node']['edge_sidecar_to_children']['edges']
                for post in posts:
                    if post['node']['is_video'] == True:
                        sums+=1
                        vid(post['node']['video_url'],user,sums)
                    else:
                        sums+=1
                        img(post['node']['display_url'],user,sums)
            elif TF == 'GraphVideo':
                sums+=1
                vid(i['node']['video_url'],user,sums)
            elif TF == 'GraphImage':
                sums+=1
                img(i['node']['display_url'],user,sums)
        else:
            os.mkdir("./%s"%user)
            if TF == 'GraphSidecar':
                posts = i['node']['edge_sidecar_to_children']['edges']
                for post in posts:
                    if post['node']['is_video'] == True:
                        sums+=1
                        vid(post['node']['video_url'],user,sums)
                    else:
                        sums+=1
                        img(post['node']['display_url'],user,sums)
            elif TF == 'GraphVideo':
                sums+=1
                vid(i['node']['video_url'],user,sums)
            elif TF == 'GraphImage':
                sums+=1
                img(i['node']['display_url'],user,sums)


    if frist_determine == True:
        url = next_url(frist_next_page)
        next_page=url['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
        ws = url['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        rnage_total = 0
        while next_page:
            rnage_total += 1
            url = next_url(ws)
            sums = for_page(url['data']['user']['edge_owner_to_timeline_media']['edges'],sums,user)
            ws = url['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            next_page = url['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
            print('跑完%d'%rnage_total)

igcrawler(input("請輸入要抓取的IG名稱："))




# for i in datas:
#             TF = i['node']['__typename']
#             if TF == 'GraphSidecar':
#                 posts = i['node']['edge_sidecar_to_children']['edges']
#                 for post in posts:
#                     if post['node']['is_video'] == True:
#                         with open('video.txt', mode='a', encoding='utf-8') as vidata:
#                             vidata.write('影片:\n')
#                             vidata.write(str(post['node']['is_video']))
#                             vidata.write('\n')
#                             vidata.write(post['node']['video_url'])
#                             vidata.write('\n')
#                     else:
#                         with open('viphoto.txt', mode='a', encoding='utf-8') as photdata:
#                             photdata.write('照片:\n')
#                             photdata.write(post['node']['display_url'])
#                             photdata.write('\n')
#             elif TF == 'GraphVideo':
#                 with open('video.txt', mode='a', encoding='utf-8') as vidata:
#                     vidata.write('只有影片:\n')
#                     vidata.write(i['node']['video_url'])
#                     vidata.write('\n')
#             elif TF == 'GraphImage':
#                 with open('photo.txt', mode='a', encoding='utf-8') as photdata:
#                     photdata.write('只有照片:\n')
#                     photdata.write(i['node']['display_url'])
#                     photdata.write('\n')