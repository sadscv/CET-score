#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import urllib
from urllib import parse

pre_url = 'http://cet.99sushe.com/getscore'

settings = {
    'school_number' : '610070', #学校代码。http://www.cha134.com/cetcode.asp
    'exam_code' : '1612',  #考试代码,四级为1611，六级是1612
    'c_number' : # classroom number
        {
            'start': 1,
            'end': 150,
        },
    's_number': #seat number
        {
            'start' : 1,
            'end' : 30
        },
    'name' : '张延' #姓名前两个字
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://cet.99sushe.com/',

}

cookies= {
    'score':'',
    'id': ''
}

postdata = {
    'id': '',
    'name':''
}

class Student(object):
    def __init__(self,**setting):
        self.pre_number = settings['school_number'] + settings['exam_code']
        self._name_ = settings['name']
        self.classroom = settings['c_number']
        self.seat = settings['s_number']
        self.cookies = cookies
        self.postdata = postdata
        self.headers = headers
        self.pre_url = pre_url
        self.session = requests.Session()

    def search(self,end_number):
        self.number = self.pre_number + str(end_number)
        self.cookies['id'] = self.number
        self.postdata['id'] = self.number
        self.postdata['name'] = self._name_
        self.url = self.pre_url + self.number
        self.str_data = parse.urlencode(self.postdata, encoding='gb2312')
        self.result = self.session.post(url=self.url,data=self.str_data,headers=self.headers,cookies=self.cookies)
        if self.result.text == '4':
            # pass
            print('number:%s time:%s' % (self.number, self.result.elapsed))
        else:
            print(self.result.text)


def next_end_number(c_start,c_end,s_start,s_end):
    for c in range(c_start,c_end):
        if c < 10:
            c = '00' + str(c)
        elif c < 100:
            c = '0' + str(c)
        else:
            c = str(c)
        for s in range(s_start,s_end):
            if s < 10:
                s = '0' + str(s)
            else:
                s = str(s)
            yield (c + s)

student = Student()
for i in next_end_number(settings['c_number']['start'],
                         settings['c_number']['end'],
                         settings['s_number']['start'],
                         settings['s_number']['end']):

    student.search(i)


