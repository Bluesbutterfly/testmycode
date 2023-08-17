# 引入requests库
import requests
import plotly.express as px
# 执行API并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept":"application/vnd.github.v3+json"}
r = requests.get(url,headers=headers)
print(f"Status code: {r.status_code}")
# 将响应转换为字典
response_dict = r.json()
# 处理结果
# print(response_dict.keys())
print(f"incomplete_results:{not response_dict['incomplete_results']}")
print(f"total_count:{response_dict['total_count']}")
repo_dicts = response_dict['items']
repo_names,stars,hover_texts = [],[],[]
for repo_dict in repo_dicts:
  # 创建悬停文本
  owner = repo_dict['owner']['login']
  description = repo_dict['description']
  hovertext = f"{owner}<br />{description}"
  hover_texts.append(hovertext)
  repo_names.append(repo_dict['name'])
  stars.append(repo_dict['stargazers_count'])
title = "github 网站收藏数排名"
label = {'x':'代码仓库','y':'收藏数'}
fig = px.bar(x=repo_names, y=stars,title=title, labels=label,hover_name=hover_texts)
# 修改和样式有关的东西
fig.update_layout(title_font_size=28,xaxis_title_font_size=20,yaxis_title_font_size=20)
fig.show()