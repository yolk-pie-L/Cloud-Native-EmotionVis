import requests
import time
import json

# 设置请求的 URL 和 headers
url = "http://a0f7b28e656044459aac52ac80b27226-1279278232.us-west-2.elb.amazonaws.com/v1/models/sdxl-turbo:predict"
headers = {
    "Content-Type": "application/json",
    "Host": "diffusers-test.default.example.com"
}
# # 读取请求体数据从文件
with open('./input.json', 'r') as file:
    data = json.load(file)
    data = json.dumps(data)

# 发送POST请求
# 设置一个非常长的超时时间，比如1天（24*60*60秒），以"一直等待"服务器响应
a=time.time()
try:
    start = time.time()
    print("sending request...")
    response = requests.post(url, headers=headers, data=data, timeout=24*60*60)
    end = time.time()
    print("请求耗时：", end - start, "秒")
    print("服务器响应：", response.text)
except requests.exceptions.Timeout:
    print("请求超时。服务器没有在预定时间内响应。")
except requests.exceptions.RequestException as e:
    print("请求失败：", e)
b=time.time()
print("总耗时：", b - a, "秒")
