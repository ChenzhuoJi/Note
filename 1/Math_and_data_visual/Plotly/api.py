import requests
import plotly.express as px
url='https://api.github.com/search/repositories'
url+='?q=language:python+sort:stars+stars:>10000'

headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
#print(f"Status code:{r.status_code}")
response_dict=r.json()
#print(response_dict.keys())

repo_dicts=response_dict['items']
repo_names,stars=[],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
labels={'x':'Respositories','y':'Stars'}
fig=px.bar(x=repo_names,y=stars,labels=labels)
fig.show()