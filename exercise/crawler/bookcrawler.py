from bs4 import BeautifulSoup
import urllib.request as req
import requests
import json
import os
import time




def hot_book_img(book_ID_url):
    book_url = f'https://tclwebdata.s3.amazonaws.com/EBSRepos/EBSRepos/Images/cover450/{book_ID_url}.png'
    return book_url

def hot_book_total_url(book_ID):
    book_content = f'https://m.ebookservice.tw/api/3.00/ks/BookProfile/{book_ID}'
    return book_content

def hot_book(request,date_time=time.strftime(f'%Y/%m/%d', time.localtime()),book_number=50):
    if time.strptime(date_time, f"%Y/%m/%d"):
        hot_book_url = f'https://m.ebookservice.tw/api/3.00/kl;taipei;nt;ty;ml;ntc;cy;cyc;tn;ks;pt;ph;il;km;hc;hcc;ylc;ntl2;tt;tcl/TclPopularBook/?beginDate=2021/1/2&endDate=2021/1/2%2023:59:59&type=book&takeSize={book_number}'
        requests=req.Request(hot_book_url,headers={
            'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        })
        with req.urlopen(requests) as response:
            data = response.read().decode('utf8')

        datas = json.loads(data)
        datas =datas['List']
        book_ID_dic = {}
        # book_url_list= []
        book_flash = {}
        
        for date in datas:
            book_ID = date['TinyBook']['BookId']
            try_book = hot_book_img(book_ID)
            
            book_contents = hot_book_total_url(book_ID)
            book_contents =req.Request(book_contents,headers={
            'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
            })
            with req.urlopen(book_contents) as response:
                data = response.read().decode('utf8')
            book_contents = json.loads(data)

            book_flash.setdefault('book_img_url',hot_book_img(book_ID)) #圖片網址
            book_flash.setdefault('TitleCache',book_contents['TitleCache']) #標題
            book_flash.setdefault('Author',book_contents['Author']) #作者
            book_flash.setdefault('PublisherName',book_contents['PublisherName'])  # 出版社
            book_flash.setdefault('TotalPage',book_contents['TotalPage']) #總頁數
            book_flash.setdefault('UpdateDate',book_contents['UpdateDate']) #上傳時間
            book_flash.setdefault('Description',book_contents['Description']) #描述
            book_flash.setdefault('ISBN',book_contents['ISBN']) # 書本編號
            
            book_ID_dic.setdefault(book_ID,book_flash) # {ID:[img_url,TitleCache標題,Author作者,PublisherName出版社,TotalPage總頁數,UpdateDate上傳時間,Description描述,ISBN書本編號]}
            # book_url_list.append(hot_book_img(book_ID))   'book_url_list':book_url_list #GET圖片網址
            with open('try.txt','a',encoding='utf8') as f:
                f.write(str(book_ID_dic.keys))
                f.write('-----------------------------------------------------\n')
                f.write(str(book_ID_dic.values))
                f.write('-----------------------------------------------------\n')

        return print(date_time,book_ID_dic)


# https://m.ebookservice.tw/api/3.00/kl;taipei;nt;ty;ml;ntc;cy;cyc;tn;ks;pt;ph;il;km;hc;hcc;ylc;ntl2;tt;tcl/TclPopularBook/?beginDate=2021/1/1&endDate=2021/1/1%2023:59:59&type=book&takeSize=50
# https://m.ebookservice.tw/api/3.00/ks/BookProfile/7e229775-98a6-4ef3-9315-b594c122f6d5
#                                                   7e229775-98a6-4ef3-9315-b594c122f6d5
# https://tclwebdata.s3.amazonaws.com/EBSRepos/EBSRepos/Images/cover450/ 7e229775-98a6-4ef3-9315-b594c122f6d5.png
# https://tclwebdata.s3.amazonaws.com/EBSRepos/EBSRepos/Images/cover450/ 068dafa3-eef0-4b5c-8b37-fcd6bce61f63.png
hot_book(1)