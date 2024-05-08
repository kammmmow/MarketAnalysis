'''
URLは https://market-analysis.r.chuo-u.ac.jp/public/html/index1.html
index1, index2...といったようにページ数に応じてURLが変わる。
レビューが書かれている部分はすべて、
    reviews というid名がついた div というタグの中にある、
    comment というclass名がついた　p　というタグの中にある
レビューは全部で 1000 個
'''

import requests, bs4, time

url_base = 'https://market-analysis.r.chuo-u.ac.jp/public/html/index'

txt = ''

for i in range(20):
    target = f'{url_base}{i+1}.html'
    html = requests.get(target)
    
    time.sleep(10)
    
    soup = bs4.BeautifulSoup(html.content, 'html.parser')
    array = soup.select('div#reviews p.comment')

    for val in array:
        txt += val.get_text(strip=True) + '\n'
    print(f'{i+1}ページ目の処理が終わりました。')
    
with open('extract.txt', mode='w', encoding='utf-8') as f:
	f.write(txt)
    
print('extract.txtを作成しました。')