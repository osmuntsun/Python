import urllib.request as req

urls='https://www.instagram.com/graphql/query/?query_hash=5b71e1f0e14e2ce11199f10da87357ec&variables=%7B%22only_stories%22%3Atrue%2C%22stories_prefetch%22%3Afalse%2C%22stories_video_dash_manifest%22%3Afalse%7D'

request=req.Request(urls,headers={
    'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

import json
data=json.loads(data)
data_list=data['data']['user']['feed_reels_tray']['edge_reels_tray_to_reel']['edges']
sums=0
for key in data_list:
    key=key['node']['user']
    sums+=1
    print(key['username'],sums)