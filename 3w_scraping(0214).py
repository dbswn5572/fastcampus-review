import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo',headers=headers)

# 네이버 한국 야구 순위 가져오기 웹 스크랩핑
soup = BeautifulSoup(data.text, 'html.parser')

teams = soup.select('#regularTeamRecordList_table > tr')
#print(teams)

for team in teams:
    record = team.select_one('th > strong').text
    name = team.select_one('td.tm > div > span').text
    win = team.select_one('td:nth-child(7) > strong').text
    if float(win) > 0.5:
        print (record, name, win)