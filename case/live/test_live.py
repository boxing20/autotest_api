import pytest
import requests
import json
from case.common_function import login

def test_live_01(login_fix):
    url = "http://www.bjszwhg.org.cn/api/liveMark/add_mark?markType=1&userId=100024&deviceType=pc&liveId=276"
    s = login_fix
    userId = login(s)["data"]["id"]
    body ={
        "markType": "1",
        "userId": userId,
        "deviceType": "pc",
        "liveId": "276"
    }
    r = s.get(url,params=body)
    print(r.json())
    print(userId)
    assert r.json()["code"] == 0

if __name__ == "__main__":
    pytest.main()
