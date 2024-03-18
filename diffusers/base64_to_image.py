import base64
from PIL import Image
import io

# 文件路径
base64_file_path = 'output'

# 从文件中读取Base64编码的字符串
with open(base64_file_path, 'r') as file:
    base64_string = file.read()

# 解码Base64字符串
image_data = base64.b64decode(base64_string)

# 将字节数据转换成图片
image = Image.open(io.BytesIO(image_data))

# 保存图片
image.save("output.png")
