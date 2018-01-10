# -*- coding:utf-8 -*-
import urllib.request as req
import sys
from bs4 import BeautifulSoup
from phoneComment import phoneComment
import re
class mobliePhone:
    def __init__(self,phoneUrl,page):
        self.phoneUrl=phoneUrl
        self.page=page

    def ok(self):
        print('ok')

    def findMoblie(url):
        try:
            html=req.Request(url)
            content=req.urlopen(html).read()
            return content.decode('utf-8','ignore')
        except:
            print('url报错'+url)
            return "url报错";

    #def phoneComment(url):
    #    try:
    #        html=req.Request(url)
    #        content=req.urlopen(url).read()
    #    except:
    #        print('url报错'+url)
    #        return "url报错";
            
    def printInfo(self):    
        htmlContent=mobliePhone.findMoblie(self.phoneUrl)
        file=open('jingdong.html','w',encoding='utf-8')
        file.write(htmlContent)
        file.flush()
        file.close()
        file=open('jingdong.html','r',encoding='utf-8')
        soup = BeautifulSoup(file.read(),"html.parser")
        a=soup.find('div',id='plist').find_all('div',class_='p-name')
        count=0
        file2=open("page/"+str(self.page)+'.txt','a')
        for phoneName in a:
            count=count+1
            name=phoneName.find('em').string
            #print("手机名字:"+name.strip())
            href=phoneName.a['href']
            file2.write("第"+str(count)+"部手机："+name.strip())
            file2.write("\n")
            file2.write("\n")
            print(href)
            comm=phoneComment(href)
            comments=comm.printComment()
            commentNum=0;
            for comment in comments:
                commentNum=commentNum+1;
                comm="第"+str(commentNum)+"条评论："+comment.string
                try:
                    file2.write(str(comm.strip()))
                except:
                    file2.write("第"+str(commentNum)+"条评论："+"数据出错")
                file2.write("\n")
                print(comm)
                print("")
            file2.flush()
            file2.write("\n")
            file2.write("\n")
            file2.write("\n")
                
            #print(type(href))
            #phoneComment("https:"+href)
        print(count)
        file.close()
    
