import requests

"""公共函数"""

def login(s):
    host = "http://www.bjszwhg.org.cn"
    api_path = "/login/user/pwd_login_v2"
    # s = requests.Session()
    userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Geck" \
                "o) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3870.400 QQBrowser/10.8.4405.400"
    # headers = {
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     "Referer": "http://www.bjszwhg.org.cn/login",
    #     "Accept-Encoding": "gzip, deflate",
    #     "Accept-Language": "zh-CN,zh;q=0.9"
    # }

    body = {
        "username": "18670350686",
        "pwd": "570cd045046840b86fa061edc4cbd1e7"
    }

    r = s.post(url=host + api_path, data=body)
    print(r.json())
    return r.json()
