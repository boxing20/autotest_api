import pytest
import requests
import json

def test_collect_01(login_fix):
    url = "http://www.bjszwhg.org.cn/common/res/collect"
    s = login_fix
    data = {
        "pubId": "8042"
    }
    r = s.post(url, data=data)
    print(r.text)

    assert r.json()["isCollect"] == "yes"
    assert r.json()["collectNum"] == 1

if __name__ == "__main__":
    pytest.main(["-v","test_collect.py"])
