import requests
import pytest
import json



def test_bjlogin_01(login_fix):
    host = "http://www.bjszwhg.org.cn"
    api_path = "/login/user/pwd_login_v2"
    s = login_fix
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

    r = s.post(url=host+api_path, data=body)
    res =r.json()
    #print(res)
    assert res["data"]["mobile"] == "18670350686"
    assert res["success"] == True

def test_add_comment_01(login_fix):
    host = "http://www.bjszwhg.org.cn"
    api_path = "/common/user/add_comment"
    s = login_fix
    body = {
    "pubId": "8081",
    "Content": "%E7%9C%9F%E6%A3%92%EF%BC%81"
    }
    r = s.post(url=host+api_path, data= body)
    print(r.text)
    assert r.json()["code"] == 0



if __name__ == "__main__":
    pytest.main(["-v", "test_beijingcloud.py"])
