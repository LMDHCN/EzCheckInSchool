import time
import json
import requests
import random
import datetime

sckey = input()

# 时间判断
now = time.localtime().tm_hour + 8
if (now >= 6) & (now < 8):
    templateid = "clockSign1"
    customerAppTypeRuleId = 146
elif (now >= 12) & (now < 14):
    templateid = "clockSign2"
    customerAppTypeRuleId = 147
elif (now >= 21) & (now< 22):
    templateid = "clockSign3"
    customerAppTypeRuleId = 148
else:
    print("现在是%d点%d分，打卡时间将自动打卡" %(now,time.localtime().tm_min))
    exit(0)

sign_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

jsons = {"businessType":"epmpics","method":"submitUpInfoSchool","jsonData":{"deptStr":{"deptid":226923,"text":"信息工程学院-计算机系-计20-1"},"areaStr":"{\"streetNumber\":\"\",\"street\":\"\",\"district\":\"土默特左旗\",\"city\":\"呼和浩特市\",\"province\":\"内蒙古自治区\",\"town\":\"\",\"pois\":\"北苑公寓\",\"lng\":111.56171499999668,\"lat\":40.80133098122903,\"address\":\"土默特左旗北苑公寓\",\"text\":\"内蒙古自治区-呼和浩特市\",\"code\":\"\"}","reportdate":1601302136827,"customerid":533,"deptid":226923,"source":"app","templateid":"clockSign2","stuNo":"202010201028","username":"高沛暄","userid":24660130,"updatainfo":[{"propertyname":"temperature","value":"36.3"},{"propertyname":"symptom","value":"无症状"}],"customerAppTypeRuleId":customerAppTyperRuleId,"clockState":0},"token":"90003e35-9bbc-4bd1-8eca-eb8a5e950677"},
# 提交打卡
response = requests.post(sign_url, json=jsons)
utcTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
cstTime = utcTime.strftime("%H时%M分%S秒")
print(response.text)
# 结果判定
if response.json()["msg"] == '成功':
    msg = cstTime + "打卡成功"
else:
    msg = cstTime + "打卡异常"
print(msg)
# 微信通知

title = msg
result = json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
content = f"""
```
{result}
```

"""
data = {
    "text": title,
    "desp": content
}
req = requests.post(sckey, data=data)
