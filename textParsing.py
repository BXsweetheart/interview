#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022-6-11 8:52
# @Author  : CBD
# @Site    : 
# @File    : textParsing.py
# @Software: PyCharm
import re
long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

result = {'name':0,'lei':0,'sub_fund':0}    # 解析结果初始化，字典类型
long_text = long_text.strip()   # 去掉首尾空字符
spl1 = long_text.split(sep='\n',maxsplit=2) # 以换行符分割两次，得到name和lei的值
result['name'] = spl1[0]    # 写入值
result['lei'] = spl1[1]

sub_fund = []   # 初始化sub_fund，形成一个list
spl2 = re.split('\n.*?. ',long_text)    # 用正则定位换行符和序号位置，分割出所有sub_fund形成一个list

spl2.pop(0) # 分割后的第一个str元素是已经获得的name和lei的值，删掉它们

for i in spl2:  # 遍历这个list，每个str元素包含一个sub_fund数组
    dic = {'title':0,'isin':0}  # 初始化用来保存sub_fund的字典
    spl3 = i.split(sep='\n')    # 再次用换行符分割，形成的list中第一个str元素是title的值，剩下的都是isin的值
    dic['title'] =spl3[0]   # 写入title值
    spl3.pop(0) # 用完的title不要留，剩下的都是isin
    dic['isin'] = spl3  # 写入sub_fund
    sub_fund.append(dic)    # 将完成的一个sub_fund数组添加到列表中
result['sub_fund'] = sub_fund   # 把列表写入result
print(result)