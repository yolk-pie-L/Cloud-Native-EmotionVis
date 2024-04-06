import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import json
import seaborn as sns
from datetime import datetime
from collections import Counter

matplotlib.use('Agg')  # Use the Anti-Grain Geometry (Agg) backend

# Define the URL, headers, and data for the request
url = "http://emo-vis.default.34.214.162.76.sslip.io"
headers = {"Content-Type": "application/json"}

# Assuming input.json is a JSON file with the request payload
# Ensure to have this JSON file in the same directory as your script
with open("input.json", "r", encoding='utf-8') as file:
    data = json.load(file)


# Function to send a single POST request and measure response time
def send_request(url, headers, data):
    start_time = time.time()
    try:
        response = requests.post(url, headers=headers, json=data)
        response_time = time.time() - start_time
        return response_time, str(response.status_code)
    except requests.exceptions.RequestException as e:  # 捕获请求相关的异常
        response_time = time.time() - start_time
        return response_time, str(e)  # 返回异常信息


def send_requests_concurrently(url, headers, data, num_requests=20, num_workers=5):
    response_times = []
    statuses_or_errors = []  # List to collect both statuses and error messages
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(send_request, url, headers, data) for _ in range(num_requests)]
        for future in as_completed(futures):
            response_time, status_or_error = future.result()  # Unpack returned tuple
            response_times.append(response_time)
            statuses_or_errors.append(status_or_error)  # Collect status code or error message
    return response_times, statuses_or_errors  # Return both lists


# Plotting the CDF of response times
def plot_cdf(data):
    data_sorted = np.sort(data)
    yvals = np.arange(len(data_sorted)) / float(len(data_sorted) - 1)
    plt.plot(data_sorted, yvals)
    plt.xlabel('Response Time (seconds)')
    plt.ylabel('CDF')
    plt.title('Cumulative Distribution Function of Response Times')
    plt.grid(True)
    # 获取当前时间戳
    plt.savefig(formatted_time + 'response_time_cdf.png')  # Save the plot as a PNG file


def plot_pdf(data):
    plt.figure(figsize=(10, 6))  # 设置图像大小
    sns.histplot(data, kde=True, color='blue', bins=30)  # 绘制带有KDE的直方图
    plt.xlabel('Response Time (seconds)')  # 设置x轴标签
    plt.ylabel('Density')  # 设置y轴标签
    plt.title('Probability Density Function of Response Times')  # 设置标题
    plt.grid(True)  # 显示网格
    filename = str(formatted_time + '_response_time_pdf.png')  # 使用当前时间戳生成文件名
    plt.savefig(filename)  # 保存图像
    plt.close()  # 关闭图像，释放资源


def plot_histogram(data):
    plt.figure(figsize=(10, 6))  # 设置图像大小
    plt.hist(data, bins=30, color='blue', edgecolor='black')  # 绘制直方图
    plt.xlabel('Response Time (seconds)')  # 设置x轴标签
    plt.ylabel('Frequency')  # 设置y轴标签
    plt.title('Histogram of Response Times')  # 设置标题
    plt.grid(True)  # 显示网格
    filename = str(formatted_time) + '_response_time_histogram.png'  # 使用当前时间戳生成文件名
    plt.savefig(filename)  # 保存图像
    plt.close()  # 关闭图像，释放资源


def count_responses(statuses_or_errors):
    # 使用Counter计算每种响应的出现次数
    response_counts = Counter(statuses_or_errors)

    return response_counts


# Send the requests and plot the CDF
response_times, statuses_or_errors = send_requests_concurrently(url, headers, data)
current_timestamp = time.time()
formatted_time = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d %H_%M_%S')

plot_cdf(response_times)
plot_pdf(response_times)
mean_response_time = np.mean(response_times)
median_response_time = np.median(response_times)
percentile_25 = np.percentile(response_times, 25)
percentile_50 = np.percentile(response_times, 50)  # 与中位数相同
percentile_75 = np.percentile(response_times, 75)
percentile_90 = np.percentile(response_times, 90)
percentile_95 = np.percentile(response_times, 95)
percentile_99 = np.percentile(response_times, 99)

response_counts = count_responses(statuses_or_errors)
for response, count in response_counts.items():
    print(f"{response}: {count} times")
# 打印统计信息
print(f"Mean Response Time: {mean_response_time} seconds")
print(f"Median Response Time: {median_response_time} seconds")
print(f"25th Percentile: {percentile_25} seconds")
print(f"50th Percentile: {percentile_50} seconds")
print(f"75th Percentile: {percentile_75} seconds")
print(f"90th Percentile: {percentile_90} seconds")
print(f"95th Percentile: {percentile_95} seconds")
print(f"99th Percentile: {percentile_99} seconds")
