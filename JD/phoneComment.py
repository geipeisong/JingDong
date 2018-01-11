# -*- coding: utf-8 -*-
#https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv131228&productId=2967929&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1
import urllib.request as req
from bs4 import BeautifulSoup
import re
class phoneComment:
    def __init__(self,commentUrl):
        self.commentUrl=commentUrl

    def Comment(url):
        try:
            html=req.Request("https:"+url)
            content=req.urlopen(html).read()
            return content
        except Exception:
            print('url报错'+"https:"+url)
            print(Exception)
            return None
    def printComment(self):
        htmlContent=phoneComment.Comment(self.commentUrl)
        if htmlContent:
            file=open('comment.html','w',encoding='gbk')
            file.write(htmlContent.decode('gbk','ignore'))
            file.flush()
            file.close()
            file=open('comment.html','r',encoding='gbk')
            soup=BeautifulSoup(file.read(),'html.parser')
            try:
                comments=soup.find('div',id='hidcomment').find_all('div',class_='comment-content')
            except:
                comments=None
            file.close()
            return comments
        else:
            return None
    

    
    
