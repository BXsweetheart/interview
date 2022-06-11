#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022-6-11 8:53
# @Author  : CBD
# @Site    : 
# @File    : baidu_EpidemicSituation.py
# @Software: PyCharm
#加载模块
import requests
import re
import json
import csv

headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
        }

#请求地址
url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'
#发送请求
response=requests.get(url=url,headers=headers)
#数据解析
content=response.text
with open('interview.htm','w',encoding='utf-8') as fp:
    fp.write(content)

# 【0】转换数据类型从list到str  .*?是惰性匹配，第1个出现"["的地方，和跟着最近的出现"]"的地方
json_str=re.findall('"component":\[(.*)\],',content)[0]
#将str类型的数据转换为dict类型
json_dict=json.loads(json_str)
#变为列表
caseList=json_dict['caseList']
with open('./onlineData.csv', mode='a', encoding='utf-8', newline='') as fcsv:
    csv_writer = csv.writer(fcsv)
    csv_writer.writerow(('疫情地区','新增确诊','现有确诊','累计确诊','治愈','死亡'))
for case in caseList:
    area=case['area']#疫情地区
    confirmed=case['confirmed']#累计
    curConfirm=case['curConfirm']# 现有
    crued=case['crued']#治愈
    died=case['died']#死亡
    confirmedRelative=case['confirmedRelative'] # 新增确诊

    # 写入表格
    with open('./onlineData.csv', mode='a', encoding='utf-8', newline='') as fcsv:
        csv_writer=csv.writer(fcsv)
        csv_writer.writerow([area,confirmedRelative,curConfirm,confirmed,crued,died])