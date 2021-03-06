
def login(environ):
    with open("templates/login.html", "rb") as f:
        data = f.read()
    return data

from urllib.parse import parse_qs

def index(environ):
    with open("templates/index.html", "rb") as f:
        data = f.read()
    return data

def fav(environ):
    with open("templates/favicon.ico", "rb") as f:
        data = f.read()
    return data

def reg(environ):
    with open("templates/reg.html", "rb") as f:
        data = f.read()
    return data

def timer(environ):
    import datetime
    now = datetime.datetime.now().strftime("%y-%m-%d %X")
    return now.encode("utf-8")

def auth(request):
    try:
        request_body_size = int(request.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = request['wsgi.input'].read(request_body_size)
    data = parse_qs(request_body)

    user = data.get(b"user")[0].decode("utf8")
    pwd = data.get(b"pwd")[0].decode("utf8")

    # 连接数据库
    import pymysql
    conn = pymysql.connect(host='10.111.111.61', port=3306, user='root', passwd='123456', db='web_yuan')

    # 创建游标
    cur = conn.cursor()
    sql = "select * from userinfo WHERE user='%s' AND pwd ='%s'" %(user,pwd)
    cur.execute(sql)

    if cur.fetchone():
        f = open("templates/backend.html", "rb")
        data = f.read()
        data = data.decode("utf8")
        return data.encode("utf8")

    else:
        return b'user or pwd is wrong'
