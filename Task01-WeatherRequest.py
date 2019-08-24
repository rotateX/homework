# -*- coding: utf-8 -*-

import requests
import time
import re


while True:
    city = input('请输入城市，回车退出：\n')
    if '\u4e00'<= city <= '\u9fff':
        req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
        req.encoding = 'utf8'
        status = req.json()['status']
        desc = req.json()['desc']
        if status == 1000:
            wt_dict = req.json()['data']
            cityname = wt_dict['city']
            yesterday = wt_dict['yesterday']
            forecast = wt_dict['forecast']
            ganmao = wt_dict['ganmao']
            wendu = wt_dict['wendu']
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            pattern = r'\d?[<|-]\d'
            print('%s天气，查询时间%s\n' % (cityname, now))
            for i in forecast:
                print(
                    '%s,'% i['date'] + '%s,'% i['type'] + '\n'
                    '最%s,'% i['high'] + '最%s,'%i['low'] + '\n'
                    '风力：%s级,'% re.findall(pattern, i['fengli'])[0] + '风向：%s,'% i['fengxiang'] + '\n'
                )
        else:
            print('查询失败，状态码：%s，' % str(status) + '原因：%s' % desc)
    elif not city:
        break
    else:
        print('输入有误')
