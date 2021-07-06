import pymysql
from sshtunnel import SSHTunnelForwarder

# ssh远程连接服务器
# with SSHTunnelForwarder(
#     ("192.168.56.102", 22), #ssh IP和port
#     ssh_password = "so6626329",#ssh 密码
#     ssh_username = "root",#ssh账号
#     remote_bind_address = ("192.168.56.102", 3306)) as server: #数据库所在的IP和端口

# 连接数据库
db = pymysql.connect(host="192.168.56.102", port=3306, user="root",
                  passwd="6626329",db="mysql")

# 使用cursor()方法创建一个游标对象
cursor = db.cursor()

sql = "select * from user"

# 查看行数
cursor.execute(sql)
print("%d 行"% (cursor.rowcount))

# 查看表内容
for i in cursor.fetchall():
    print(i)

# 关闭数据库连接db.close()
db.close()

