import pytest
import requests

def test_qqtest_01():
    host = "http://japi.juhe.cn"
    path = "/qqevaluate/qq"

    bady = {
        "key": "eafe307fac13899b5c0c6ff6bc4e5f91",
        "qq": "704466925"
    }
    r = requests.post(url= host + path, data=bady)
    print(r.text)
    r.json()["reason"] == "seccess"

if __name__ == "__main__":
    pytest.main(["-v", "test_qqtest.py"])