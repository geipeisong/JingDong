# -*- coding:utf-8 -*-
#https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main
#https://list.jd.com/list.html?cat=9987,653,655&page=2&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main
#https://list.jd.com/list.html?cat=9987,653,655&page=3&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main
from mobliePhone import mobliePhone
page=input("请输入你要抓取的页数（小于60页):")
for i in range(int(page)):
    html = "https://list.jd.com/list.html?cat=9987,653,655&page=" +str(i+1)+ "&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main";
    a=mobliePhone(html,i+1)
    a.printInfo()
