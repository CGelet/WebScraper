import json
import re
from tabulate import tabulate
from subprocess import call


mailTxt = ""
# Formatting the email
f = open('article_dict.json')
ArticleDict = json.load(f)

f = open('Platforms.json')
PlatformList = json.load(f)


for Platform in PlatformList:
     print(Platform)
     PlatformSpot = PlatformList.index(Platform)
     print(PlatformSpot)
     mailTxt = mailTxt + '<b>'+Platform+' Articles</b>\n\n'
     for Article in ArticleDict[PlatformSpot][Platform+' Articles']:
          ArticleName = Article['Article_Name']
          ArticleLink = Article['Article_Link']
          mailTxt = mailTxt + ArticleName+'\n'
          mailTxt = mailTxt + ArticleLink+'\n\n'


#print(mailTxt)
i = 0
table_format = ''
for Platform in PlatformList:
     print(Platform)
     PlatformSpot = PlatformList.index(Platform)
     print(PlatformSpot)
     mailTxt = mailTxt + '<b>'+Platform+' Articles</b>\n\n'
     table_format = table_format + '<tr>\n<th colspan="3">\n' + Platform +' Articles \n</th>\n</tr> \n'
     table_format = table_format + '<tr> \n'
     for Article in ArticleDict[PlatformSpot][Platform+' Articles']:
          ArticleName = Article['Article_Name']
          ArticleLink = Article['Article_Link']
          if i != 3:
               table_format = table_format + '<td>\n<a href='+ArticleLink+'>\n'+ArticleName+'\n</a>\n' + '</td> \n'
          else: 
               table_format = table_format + '</tr> \n' + '<tr> \n'
               table_format = table_format + '<td>\n<a href='+ArticleLink+'>\n'+ArticleName+'\n</a>\n' + '</td> \n'
               i = 0

          i = i + 1
          
     if i != 0:
          table_format = table_format + '</tr> \n'
          i = 0

html_style = '''<style>
tr {
  border-bottom: 1px solid #ddd;
}
</style>'''

html_table = html_style + '<font size="3">\n<table cellspacing="5" border="1" width="100%"> \n' + '<tbody>\n' + table_format + '</tbody>\n' + '</table>'

print(html_table)

with open('Email_Message.txt', 'w') as Email_Message:
    Email_Message.write(html_table)

call(["python","Email_Service.py"])