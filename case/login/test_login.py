import pytest
import os
import requests
import urllib3


def test_login_1():
    host = "http://api.nnzhp.cn"
    login_path = "/api/user/login"
    bady = {
        "username": "niuhanyang",
        "passwd": "aA123456"
    }
    r = requests.post(url=host+login_path,data=bady)
    error_code = r.json().get('error_code')
    userId = r.json().get('login_info')["userId"]   #.get('userId')也可以
    assert error_code == 0
    assert userId == 1





if __name__ == "__main__":
    pytest.main()
