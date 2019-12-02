# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 01:17:38 2019

@author: zsl
"""

import pymysql
import pandas as pd

# 打开数据库
db = pymysql.connect(host='localhost',port =3306,user='root',passwd='zsl123',db='subgraph_nodes_data',charset='utf8' )

#使用cursor()方法获取操作游标
cursor = db.cursor()

cursor.execute( "CREATE DATABASE `subgraph_nodes_data`")

cursor.execute("DROP TABLE IF EXISTS `node_data`")
cursor.execute("""CREATE TABLE `node_data` (
  `nodes` varchar(32) NOT NULL,
  `path` varchar(32) NOT NULL,
  PRIMARY KEY (`nodes`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;
""")
#插入语句
insert_sql = "insert into node_data values (%s,%s);"
nodes_info = pd.read_csv('./words_list_data.csv')
for i in range(len(nodes_info)):
      nodes   = str(nodes_info.iloc[i,0])
      values = (nodes,'')
      cursor.execute(insert_sql, values)
cursor.connection.commit()  

#查询更新语句
#x_node=""
#path=""
#query_path_sql ="select path from node_data where nodes=%s"%(x_node)
#update_path_sql = "update node_data set path=%s where nodes=%s"%(path,x_node)
#if cursor.execute(query_path_sql)=='':
#    cursor.execute(update_path_sql)
#else:
#    =