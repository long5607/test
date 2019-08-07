import json

import requests

from base.runmethod import RunMethod
from util.common_util import CommonUtil

# com = CommonUtil()
# # com.is_contain('123',123456)

res = requests.get(url="https://newhouseapi.apyfc.com/api/Selected/Index")
print(type(res))
print(res.content.decode("utf-8"))
print(res.text)
print(res.json())
# run=RunMethod()
# res=run.get_main(url="https://newhouse.apyfc.com/gpxq/20180606174804zn6a", data=None)
# print(res)
