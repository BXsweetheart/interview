#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022-6-11 8:54
# @Author  : CBD
# @Site    : 
# @File    : SoupTest.py
# @Software: PyCharm
import re
import json
import csv
from bs4 import BeautifulSoup
soup=BeautifulSoup(open('interview.htm',encoding='utf-8'),'lxml')

#[0]转换数据类型从list到str  .*?是惰性匹配，第1个出现"["的地方，和跟着最近的出现"]"的地方

json_str=re.findall('"component":\[(.*)\],',str(soup))[0]
#将str类型的数据转换为dict类型
json_dict=json.loads(json_str)
#变为列表
caseList=json_dict['caseList']
with open('./soupData.csv', mode='a', encoding='utf-8', newline='') as fcsv:
    csv_writer = csv.writer(fcsv)
    csv_writer.writerow(('疫情地区','新增确诊','现有确诊','累计确诊','治愈','死亡'))
for case in caseList:
    area=case['area']#疫情地区
    confirmed=case['confirmed']#累计
    curConfirm=case['curConfirm']# 现有
    crued=case['crued']#治愈
    died=case['died']#死亡
    confirmedRelative=case['confirmedRelative'] # 新增确诊

    # print(area,confirmed,curConfirm,confirmedRelative,nativeRelative,overseasInputRelative, asymptomatic,asymptomaticRelative,crued,curedRelative,died,diedRelative)
    # 写入表格
    with open('./soupData.csv', mode='a', encoding='utf-8', newline='') as fcsv:
        csv_writer=csv.writer(fcsv)
        csv_writer.writerow([area,confirmedRelative,curConfirm,confirmed,crued,died])