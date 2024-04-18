import random

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
url = "http://emo-vis.default.44.226.66.186.sslip.io"
headers = {
    "Content-Type": "application/json"
}
# # 读取请求体数据从文件
with open('./input.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

total_time = 0  # 记录总响应时间
successful_requests = 0  # 成功的请求次数

for i in range(5):  # 发送5次请求
    try:
        start = time.time()
        print(f"Sending request #{i + 1}...")
        response = requests.post(url, headers=headers, json=random.choice(data), timeout=24 * 60 * 60)
        end = time.time()

        request_time = end - start
        total_time += request_time  # 累加响应时间
        successful_requests += 1  # 增加成功的请求次数

        print("请求耗时：", request_time, "秒")
        print("服务器响应：", response.text)
        # 假设base64_to_image函数和其必要的参数已经定义
        # base64_to_image(json.loads(response.text)["instances"], "output.png")

        # if i < 4:  # 如果不是最后一次请求，等待45秒
        #     time.sleep(45)

    except requests.exceptions.Timeout:
        print("请求超时。服务器没有在预定时间内响应。")
    except requests.exceptions.RequestException as e:
        print("请求失败：", e)

if successful_requests > 0:
    average_time = total_time / successful_requests
    print("平均请求耗时：", average_time, "秒")
else:
    print("没有成功的请求。")
