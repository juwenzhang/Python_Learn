import pymysql

def connect_db():
    """
    查看数据库版本
    :return:
    """
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="451674",
        charset="utf8"
    )

    # 我们后期需要进行操作数据库的对象，指针
    cursor = db.cursor()
    cursor.execute("select version();")  # 实现的是显示数据库的版本号

    data = cursor.fetchall()  # 实现的获取我们的数据库中的所有的数据
    print(f"数据库版本为: {data}")

    # 关闭数据库
    cursor.close()
    db.close()

def create_db():
    """
    创建数据库
    :return:
    """
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="451674",
        charset="utf8"
    )

    # 我们后期需要进行操作数据库的对象，指针
    cursor = db.cursor()
    cursor.execute("""create database if not exists demo """)  # 实现的是显示数据库的版本号

    data = cursor.fetchall()  # 实现的获取我们的数据库中的所有的数据
    print(f"数据库版本为: {data}")

    # 关闭数据库
    cursor.close()
    db.close()

def create_table():
    """
    创建数据库表
    :return:
    """
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        database="demo",
        password="451674",
        charset="utf8"
    )

    # 我们后期需要进行操作数据库的对象，指针
    cursor = db.cursor()
    cursor.execute("""create table if not exists demo_table (
        username varchar(32)
    )""")  # 实现的是显示数据库的版本号

    data = cursor.fetchall()  # 实现的获取我们的数据库中的所有的数据
    print(f"数据库版本为: {data}")

    # 关闭数据库
    cursor.close()
    db.close()

def insert_db():
    """
    想数据库表中插入数据
    :return:
    """
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        database="demo",
        password="451674",
        charset="utf8"
    )
    cursor = db.cursor()

    cursor.execute("insert into demo_table (username) values ('%s')" % "juwenzhang")

    db.commit()  # 实现手动提交数据库事务

    cursor.close()
    db.close()


def get_data():
    """
    获取数据
    :return:
    """
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        database="demo",
        password="451674",
        charset="utf8"
    )
    cursor = db.cursor()

    sql = """select * from demo_table"""
    cursor.execute(sql)
    print("{}".format(cursor.fetchall()))

    cursor.close()
    db.close()

def update_data():
    """
    更新数据
    :return:
    """
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        database="demo",
        password="451674",
        charset="utf8"
    )
    cursor = db.cursor()

    sql = """update demo_table set username='%s' where username like 'juwenzhang'""" % ("水逆信封")
    cursor.execute(sql)

    db.commit()
    cursor.close()
    db.close()

def delete_data():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        database="demo",
        password="451674",
        charset="utf8"
    )
    cursor = db.cursor()

    sql = """delete from demo_table where username = 'juwenzhang'"""
    cursor.execute(sql)

    db.commit()
    cursor.close()
    db.close()

if __name__ == "__main__":
    connect_db()
    create_db()
    create_table()
    insert_db()
    get_data()
    update_data()
    get_data()
    delete_data()
    get_data()