import requests
from urllib import parse

pre_url = 'http://cet.99sushe.com/getscore'
pre_number = '3600121612'
classroom_number = '116'
number = pre_number
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'

headers = {
    'User-Agent': agent,
    'Content-Type': 'application/x-www-form-urlencoded',
    'charset':'GB2312',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Origin': 'http://cet.99sushe.com',
    'Referer': 'http://cet.99sushe.com/',
    'Host': 'cet.99sushe.com',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Upgrade-Insecure-Requests':'1',
    'Cache-Control': 'max-age=0',

}
cookies= {
    'score':'',
    'id': number
}

postdata = {
    'id': number,
    'name':'付广'
}


def get_result(classroom_number,seat_number):
    number = pre_number + classroom_number + seat_number
    cookies['id'] = number
    postdata['id'] = number
    str_data = parse.urlencode(postdata, encoding='gb2312')
    url = pre_url + classroom_number + number
    result = session.post(url=url, data=str_data, headers=headers, cookies=cookies)
    if result.text == '4':
        print('number:%s time:%s' %(number,result.elapsed))
    else:
        print(result.text)



session = requests.Session()



for i in range(10, 14):
    for j in range(1, 30):
        if i < 100:
            classroom_number = '0' + str(i)
        else:
            classroom_number = str(i)
        if j < 10:
            seat_number = '0' + str(j)
        else:
            seat_number = str(j)
        get_result(classroom_number, seat_number)



