#!/usr/bin/python
#coding:utf-8
import urllib
import sys
import re

if len(sys.argv) == 1:	#û�е��ʾ���ʾ�÷�
	print "�÷�:./Dict.py Ҫ���ҵĵ���"
	sys.exit()

word = ""
for x in range(len(sys.argv) - 1): #���ҵĿ����Ƕ���м��пո���"join in",����ƴ�ӵ���
	word += " " + sys.argv[x + 1]
print "���ʣ�" + word

searchUrl = "http://dict.youdao.com/search?q=" + word + "&keyfrom=dict.index"	#���ҵĵ�ַ
response = urllib.urlopen(searchUrl).read() #��ò��ҵ�����ҳԴ��

#����ҳԴ����ȡ������������һ����
searchSuccess = re.search(r"(?s)<div class=\"trans-container\">\s*<ul>.*?</div>",response)

if searchSuccess:
	means = re.findall(r"(?m)<li>(.*?)</li>",searchSuccess.group()) #��ȡ��������ȡ�ĺ��ĵ�������
	print "���壺"
	for mean in means:
		print "\t" + mean.decode('utf-8').encode('gbk')	#�������
else:
	print "δ���ҵ�����."