import requests
import time

# 定义请求的URL和数据
url = "http://diffusers-test.default.44.230.16.242.sslip.io/v1/models/sdxl-turbo:predict"
data = '{"instances":["a lobster"]}'
headers = {"Content-Type": "application/json"}

# 发送POST请求
# 设置一个非常长的超时时间，比如1天（24*60*60秒），以"一直等待"服务器响应

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

