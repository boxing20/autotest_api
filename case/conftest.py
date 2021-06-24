import pytest
import requests
import json
from case.common_function import login

@pytest.fixture(scope="module")
def login_fix():
    '''自定义一个前置的操作'''
    print("先登陆")
    s = requests.session()
    login(s)
    return s

@pytest.fixture(scope="function")
def unlogin_fix():
    '''自定义一个前置的操作'''
    print("不登陆")
    s = requests.session()
    s.headers.update({"localToken": "5754516a-be78-4339-842a-53d2f3d0c811xxx"})
    return s
