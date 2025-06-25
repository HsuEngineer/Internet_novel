import requests
from bs4 import BeautifulSoup
import re
import time
import os
from fpdf import FPDF
import textwrap  # pip install textwrap3

# ========== 工具函數 ==========

def file_name_reduce(file_name):
    match = re.search(r'(\d+)', file_name)
    if not match:
        return file_name
    number_str = match.group(1)
    padded_number = f"{int(number_str):03}"
    return file_name.replace(number_str, padded_number)

def clean_line(line):
    return re.sub(r'[\u200b-\u200f\u202a-\u202e]', '', line)

def wrap_text(text, max_width, pdf):
    avg_char_width = pdf.get_string_width('一') or 5
    est_chars = max(1, int(max_width / avg_char_width))
    if pdf.get_string_width(text) > max_width:
        return textwrap.wrap(text, width=est_chars)
    else:
        return [text]

def safe_output_text(text, pdf, max_width):
    for paragraph in text.split('\n'):
        clean = clean_line(paragraph.strip())
        if not clean:
            pdf.ln(6)  # 小段空格感更自然
            continue
        wrapped = wrap_text(clean, max_width, pdf)
        for wline in wrapped:
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(max_width, 10, wline, align='L')
        pdf.ln(4)  # 段與段之間補點空隙更舒服

def txt_to_pdf(txt_path, pdf_path, font_path='fonts/NotoSansTC-Regular.ttf'):
    pdf = FPDF(format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.add_font('CustomFont', '', font_path)
    pdf.set_font('CustomFont', size=12)

    max_width = pdf.w - 2 * pdf.l_margin

    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            for line in file:
                safe_output_text(line, pdf, max_width)
    except UnicodeDecodeError:
        with open(txt_path, 'r', encoding='big5') as file:
            for line in file:
                safe_output_text(line, pdf, max_width)

    pdf.output(pdf_path)

# ========== 網頁下載函數 ==========

def download_novel(url, headers, cookies, pic_headers, novel_path, last_title, is_pdf):    
    response = requests.get(url=url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html5lib')
    title = soup.find('h1').text.strip()
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    title = file_name_reduce(title)
    exp = soup.find('h3').text.strip()
    content = soup.find('div', id='acontent')
    text = content.text.strip().split('zation()')[0]

    for i in content:
        if i.name == 'img':
            img_url = i.get('data-src', i.get('src'))
            resp = requests.get(img_url, headers=pic_headers)
            img_name = img_url.split("/")[-1]
            with open(f'{novel_path}/img/{exp}-{img_name}', 'wb') as f:
                f.write(resp.content)
                
    title = last_title if last_title in title else title
                
    txt_filename = f'{novel_path}/txt/{exp}-{title}.txt'
    if last_title in title:
        with open(txt_filename, 'a', encoding='utf-8') as f:
            f.write('\n' + text)
    else:
        with open(txt_filename, 'w', encoding='utf-8') as f:
            f.write(title + '\n' + exp + '\n' + text)

    if is_pdf:
        pdf_filename = f'{novel_path}/pdf/{exp}-{title}.pdf'
        txt_to_pdf(txt_filename, pdf_filename)

    pattern = 'nextpage="(.*?)"'
    next_page = re.search(pattern, response.text)
    
    last_title = last_title if last_title in title else title
    
    if not next_page:
        return None, title

    next_url = 'https://tw.linovelib.com' + next_page.group(1)
    return next_url, title

def download_novels(novel_path, url, is_pdf=False):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'accept-language': 'zh-TW,zh;q=0.9',
    }
    cookies = {
        'night': '0',
    }
    pic_headers = {
        'referer': 'https://tw.linovelib.com/',
        'user-agent': headers['user-agent'],
    }

    last_title = '0'

    while url and 'catalog' not in url:
        url, last_title = download_novel(url, headers, cookies, pic_headers, novel_path,  last_title, is_pdf)
        time.sleep(5)

    print('下載完成!')

# ========== 主程式 ==========

if __name__ == '__main__':
    
    # 小說名稱
    # novel_name = '轉生後想要在田園過慢生活'
    novel_name = input('請輸入小說名稱:')
    
    # 小說網址(第一章)
    # url = 'https://tw.linovelib.com/novel/3139/159069.html'
    url = input('小說網址(第一章):')

    novel_path = f'content/{novel_name}'

    # 創建目錄
    os.makedirs(novel_path, exist_ok=True)
    os.makedirs(f'{novel_path}/img', exist_ok=True)
    os.makedirs(f'{novel_path}/txt', exist_ok=True)
        
    if input('是否開始下載? (y/n): ') == 'y':
        is_pdf = input('是否轉成PDF檔? (y/n): ') == 'y'
        if is_pdf:
            os.makedirs(f'{novel_path}/pdf', exist_ok=True)
        download_novels(novel_path, url, is_pdf)
