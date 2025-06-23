import requests  #pip install requests
from bs4 import BeautifulSoup  #pip install beautifulsoup4, html5lib
import re
import time
import os

novel_name = '轉生後想要在田園過慢生活'
os.chdir('content')
if not os.path.exists(novel_name):
    os.mkdir(novel_name)
    os.mkdir(f'content/{novel_name}/img')
    os.mkdir(f'content/{novel_name}/txt')
# url = 'https://tw.linovelib.com/novel/3139/159069.html'
url = 'https://tw.linovelib.com/novel/3139/276114.html'
last_title = '0'

headers = {
    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language':
    'zh-TW,zh;q=0.9',
    'cache-control':
    'no-cache',
    'pragma':
    'no-cache',
    'priority':
    'u=0, i',
    'sec-ch-ua':
    '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Windows"',
    'sec-fetch-dest':
    'document',
    'sec-fetch-mode':
    'navigate',
    'sec-fetch-site':
    'none',
    'sec-fetch-user':
    '?1',
    'upgrade-insecure-requests':
    '1',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

cookies = {
        'night':
        '0',
        '_ga':
        'GA1.1.858433580.1740736270',
        'Hm_lvt_1251eb70bc6856bd02196c68e198ee56':
        '1740736292',
        'HMACCOUNT':
        '8BA7214072928503',
        'cf_clearance':
        'hSIMyDbQVA5kxCW0I9bg5gi.fGVX1HgEa7B5SuYPtLQ-1740737284-1.2.1.1-DXxrnXKGpOknt3YCB0xcsKY1CywTxwzap_IxHK8TxiSSMiDUO0VWTXZtHsdr5ZOAFoKGPDAx5FT.kDdnxMq5EimgHIfVxrB1HXxfS_l1DHgM3.nGRnAGbSC1E6Hi6Rh.xTR67tSu_QET62ogqB.QZmzfVPfMiHJa1_Cz4yUpQ.E_cTl7Rrs.86MPXdE1bSXksSho8egWpSI5nUQtrXUUtFX.053CYaMxj47H4F54KsIJtHqnJyNvUlqdL65uiD.f5HGuLb9RWSWZU2NcFLzxxXRghrhjdTQNZUxvlrrFEas',
        '__gads':
        'ID=28b11837f9361c7c:T=1740736353:RT=1740737284:S=ALNI_MbeLb7vF0IR-QpiPBywKP3QgyZNjA',
        '__gpi':
        'UID=0000104e0081caf1:T=1740736353:RT=1740737284:S=ALNI_Mbbj-l5DyId6x2eRnmgDnd32aa6dA',
        '__eoi':
        'ID=96dde09a29d7d84c:T=1740736353:RT=1740737284:S=AA-AfjYSdS4zoJuD8xfQe4Bwy3B_',
        'jieqiRecentRead':
        '3095.154933.0.1.1740737288.0',
        '_ga_NG72YQN6TX':
        'GS1.1.1740736270.1.1.1740737289.0.0.0',
        'Hm_lpvt_1251eb70bc6856bd02196c68e198ee56':
        '1740737290',
        'FCNEC':
        '%5B%5B%22AKsRol8K90u22_760XILll97A0Z2PjjiAKwe_dKYM85RyT3T7KyI7_rrety0UH6lZasVeQNTWHT99Yd8oq6e-Yj8QxSgFIDtQsadgRKNooT6OMnfMpwScUiabH4ZerH8z2fsDJ-SNqfwYLFp5xXJfk2ZVlsYhrBZqA%3D%3D%22%5D%5D',
    }

def do():
    global url, last_title
    response = requests.get(url=url, headers=headers, cookies=cookies)
    with open('demo.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    pattern = 'nextpage="(.*?)"'
    next_page = re.search(pattern, response.text)
    soup = BeautifulSoup(response.text, 'html5lib')
    title = soup.find('h1').text.strip()
    title = re.sub(r'[<>:"/\\|?*]', '', title).strip()
    exp = soup.find('h3').text.strip()
    content = soup.find('div', id='acontent')
    text = content.text.strip()
    text = text.split('zation()')[0]
    '''
    print(title)
    print(exp)
    print(text)
    '''
    pic_headers = {
        'accept':
        'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language':
        'zh-TW,zh;q=0.9',
        'cache-control':
        'no-cache',
        'pragma':
        'no-cache',
        'priority':
        'i',
        'referer':
        'https://tw.linovelib.com/',
        'sec-ch-ua':
        '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'image',
        'sec-fetch-mode':
        'no-cors',
        'sec-fetch-site':
        'cross-site',
        'sec-fetch-storage-access':
        'none',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    }

    for i in content:
        if i.name == 'img':
            try:
                img_url = i['data-src']
            except:
                img_url = i['src']
            resp = requests.get(img_url, headers=pic_headers)
            with open(f'content/{novel_name}/img/{img_url.split("/")[-1]}', 'wb') as f:
                f.write(resp.content)
    if last_title in title:
        with open(f'content/{novel_name}/txt/{last_title}.txt', 'a', encoding='utf-8') as f:
            f.write('\n' + text)
    else:
        with open(f'content/{novel_name}/txt/{title}.txt', 'w', encoding='utf-8') as f:
            f.write(title + '\n' + exp + '\n' + text)
    print(title)   
    last_title = title
    url = 'https://tw.linovelib.com' + next_page.group(1)
    time.sleep(3)
    
for i in range(10):
    for j in range(40):
        do()
    time.sleep(60)  # 每10次後休息1分鐘