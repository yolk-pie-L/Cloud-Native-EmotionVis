import matplotlib.pyplot as plt
import matplotlib

import yaml
from datetime import datetime
import re

def extract_deployment_name(full_name):
    # 提取 "0000" 前面的部分
    index_0000 = full_name.find("-0000")
    if index_0000 != -1:
        before_0000 = full_name[:index_0000]
        return before_0000



with open('logs/Started1.yaml', 'r', encoding='utf-16') as stream:
    try:
        started_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

with open('logs/Killing1.yaml', 'r', encoding='utf-16') as stream:
    try:
        killing_data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


deploy_time = {}
started_podset = set()
killing_podset = set()

# 遍历 items 并打印每个 Pod 的名称和创建时间
first_pod_time = None

items = started_data['items'] + killing_data['items']
items.sort(key=lambda x: x['metadata']['creationTimestamp'])

for item in items:
    pod_name = item['involvedObject']['name']
    creation_time_str = item['metadata']['creationTimestamp']
    creation_time = datetime.strptime(creation_time_str, "%Y-%m-%dT%H:%M:%SZ")

    if first_pod_time is None:
        first_pod_time = creation_time
        time_diff = 0  # 第一个 Pod 的时间差是 0
    else:
        time_diff = (creation_time - first_pod_time).total_seconds()  # 计算时间差（秒）

    deploy_name = extract_deployment_name(pod_name)
    if deploy_name not in deploy_time:
        deploy_time[deploy_name] = {}
        deploy_time[deploy_name]['count'] = 1
        deploy_time[deploy_name][0] = 1
    if item['reason'] == 'Killing':
        deploy_time[deploy_name]['count'] -= 0.5
    else:
        deploy_time[deploy_name]['count'] += 0.5
    deploy_time[deploy_name][time_diff] = deploy_time[deploy_name]['count']

result = {}
# 打印每个 Deployment 的创建和删除时间
for deploy_name, deploy_data in deploy_time.items():
    result[deploy_name] = deploy_data
    result[deploy_name].pop('count')

print(result)

# 定义每个 Deployment 的 Timeline 数据
deployments = result

matplotlib.use('Agg')
# 设置图表
plt.figure(figsize=(10, 8))

# 为每个 Deployment 绘制一个时间线
for deployment, timeline in deployments.items():
    times = list(map(float, timeline.keys()))  # 转换时间点为浮点数
    counts = list(timeline.values())
    plt.plot(times, counts, marker='o', label=deployment)

# 设置图表标题和图例
plt.title('Replica Count Over Time for Various Deployments')
plt.xlabel('Time (seconds)')
plt.ylabel('Replica Count')
plt.legend()

# 显示图表
plt.grid(True)
plt.savefig('replica_count_over_time_n500_c10.png')