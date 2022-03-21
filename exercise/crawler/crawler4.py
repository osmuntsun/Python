import urllib.request as req
import json
import bs4
def username():
    urls='https://www.instagram.com/p/BffDq3njKUP1Ruh8aqIGbmXLCP2THhm40ZgUGY0/?__a=1'

    request=req.Request(urls,headers={
        'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    })
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')

   
    data=json.loads(data)
    
    print(data['graphql']['shortcode_media']['display_url'])
    
    # data_list=data['graphql']['user']['edge_owner_to_timeline_media']['edges']
    # total_url_list,total_url_img=list(),list()
    # vid_url_list,img_url_list=list(),list()
    # total_vig,total_img=list(),list()

    # for key in data_list:
    #     bool_key=key['node']['__typename']
    #     if bool_key == 'GraphImage':
    #         img_url_list.append(key['shortcode_media']['video_url'])
    #     elif bool_key == 'GraphVideo':
    #         vid_url_list.append(key['shortcode_media']['video_url'])
        
    #     elif bool_key == 'GraphSidecar':
    #         total_url_list.append(key['node']['edge_sidecar_to_children']['edges'])
    #         for img_key in total_url_list:
    #             if img_key['node']['is_video'] == False:
    #                 total_url_img.append(img_key['node']['display_url'])
    #             else:
    #                 total_vig.append(img_key['node']['video_url'])
    #                 total_img.append(str(img_key['node']['video_view_count']))
    # print(total_vig)
    # print(total_img)
    # print(vid_url_list)
    # print(img_url_list)
            
            

username()