import pytest
import requests

#def test_qqtest_01():
host = "http://japi.juhe.cn"
path = "/qqevaluate/qq"
headers = {
    "Content-Type": "application/json;charset=UTF-8"
}
bady = {
    "key": "eafe307fac13899b5c0c6ff6bc4e5f91",
    "qq": "704466925"
}
r = requests.post(url= host + path, data=bady)
# print(r.text)
r.json()["reason"] == []