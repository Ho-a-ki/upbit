import requests
import bs4
import json

# https://crix-api-endpoint.upbit.com/v1/crix/candles/기간타입/기간?code=CRIX.UPBIT.마켓-암호화폐기호&count=시세데이터수&to=최종시세데이터일시

# 기간타입: minutes, days, weeks, months (hours는 없으며 minutes로 대체)
# 기간: 1, 3, 5, 10, 15, 30, 60, 240 (기간타입 minutes만 해당)
# 마켓: KRW, BTC, ETH, USDT
# 암호화폐기호: BTC, ETH, XRP, STEEM, SBD 등 각 마켓의 지원 암호화폐
# 시세데이터수: 1(기본값), 2, 3, 4 등 원하는 시세 데이터 수 (최종시세데이터일시 기준)
# 최종시세데이터일시: 조회를 원하는 최종 시세 데이터 일시 (생략시 가장 최근 시세 데이터 일시, UTC 기준)

coinListtxt = open("coinList.txt", "r")
coinList = coinListtxt.readlines()
coinList = [i.strip() for i in coinList]


up = 0
down = 0

for i in coinList:
    url = 'https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/10?code=CRIX.UPBIT.KRW-' + str(i) + '&count=1'
#     print(url)
    r = requests.get(url)
    price_set = json.loads(r.text)
#     print(price_set)
    startprice = price_set[0]['openingPrice']
    endprice = price_set[0]['tradePrice']
    if startprice < endprice:
        up = up + 1
    else:
        down = down + 1

print('상승중인 코인 :', up , '하락중인 코인 :' , down)
