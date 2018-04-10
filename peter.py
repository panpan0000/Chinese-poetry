#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root", "poetry", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
fp = open('./popular.txt');
for line in fp.readlines():
    title,author = line.strip().split(',')
    print '----------'
    print author, title
    SQL="SELECT content from poems where author=\"" + author + "\" and title=\"" +  title + "\"";
    cursor.execute(SQL)

    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()
    if data is not None :
        content = data[0].encode('utf-8').strip();
        clines = content.split('\n');
        for c in clines:
            if '，' in c:
                segments = c.split('，')
                newLine =  segments[0]
                newLine += '，'
                for seg in segments[1:]:
                    seg = seg.replace("、","").replace("。","").replace(" ","").strip();
                    charCnt= len(seg)/3 # UTF-8 encode ,each Chinese Char is 3 bytes
                    for x in range(0, charCnt):
                        newLine += '*'
                    newLine += '，'
                print c
                print newLine

            else:
                print c
    #fo = open("/tmp/a.txt",'w');
    #for row in data:
    #        name = row[0].encode('utf-8').strip()
    #    nid = row[1]
    #        print "Authors : %s " % name, nid
 #   fo.write(  str(name) + ' ' +  str(nid) )

# 关闭数据库连接
db.close()
fp.close();
#fo.close()

#from googlesearch import search

