import requests
import time
import json
import base64
from PIL import Image
import io

def base64_to_image(base64_string, output_path):
    # 解码Base64字符串
    image_data = base64.b64decode(base64_string)

    # 将字节数据转换成图片
    image = Image.open(io.BytesIO(image_data))

    # 保存图片
    image.save(output_path)

# 设置请求的 URL 和 headers
url = "http://ensemble.default.52.32.2.254.sslip.io"
headers = {
    "Content-Type": "application/json"
}
# # 读取请求体数据从文件
with open('./input.json', 'r', encoding='utf-8') as file:
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
    base64_to_image(json.loads(response.text)["instances"], "output.png")

except requests.exceptions.Timeout:
    print("请求超时。服务器没有在预定时间内响应。")
except requests.exceptions.RequestException as e:
    print("请求失败：", e)
b=time.time()
print("总耗时：", b - a, "秒")
