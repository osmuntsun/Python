import json
import requests
from bs4 import BeautifulSoup

igurl="https://www.instagram.com/crown_du/?hl=zh-tw"
prurl="gabrielfreiredev"
res=requests.get(f"{igurl}/{prurl}")
print(res.status_code)
if res.ok:
    html=res.text
    bshtml=BeautifulSoup(html)
    # print(res.text)
    scripts=bshtml.select("script[type='application/ld+json']")
    scripts_con=json.loads(scripts[0].text.strip())
    print(json.dumps(scripts_con,indent=4, sort_keys=True))
    main_entity_of_page=scripts_con['mainEntityofPage']
    inter=main_entity_of_page['interactionStatistic']
    follow=inter['userInteractionCount']
    print(follow)
    # print(len(scripts))