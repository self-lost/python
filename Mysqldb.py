import pymysql;

# 打开数据库连接
conn = pymysql.connect(
    host="localhost",
    user="root",password="2001",
    database="book",
    charset="utf8")
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
 

#使用 execute()  方法执行 SQL 查询 
#查询数据
sql="select * from books"
cursor.execute(sql)
for x in cursor.fetchall():
    #str=x[3].strftime('%Y-%m-%d')
    print("书本编号：%d，书本名称：%s，书本用户编号：%d，发布时间：%s"%(x))
# 使用 fetchone() 方法获取单条数据.
#data = cursor.fetchone()
#print ("Database version : %s " % data)


# 插入数据
# sql = "INSERT INTO books VALUES (%s,'%s', %d ,'%s' )"
# data = ("null","人性的弱点21",2,"2001-3-2")
# cursor.execute(sql % data)
# conn.commit()
# print('成功插入', cursor.rowcount, '条数据')


# 删除数据
# sql = "DELETE FROM books WHERE bId = %d or bName='%s'"
# data = (18, 'null')
# cursor.execute(sql % data)
# conn.commit()
# print('成功删除', cursor.rowcount, '条数据')
 
 
#修改数据
# sql="UPDATE  books SET bName='%s'  WHERE bId=%d";
# data=("人性的弱点",16)
# cursor.execute(sql % data)
# conn.commit();
# print('成功修改',cursor.rowcount,'条数据')
# 关闭数据库连接
conn.close()