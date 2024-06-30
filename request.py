import requests

url1 = 'http://localhost:5000/soilpredict_api'
url2 = 'http://localhost:5000/fertilizerpredict_api'
url3 = 'http://localhost:5000/yieldpredict_api'


r1 = requests.post(url1,json={'experience':2, 'test_score':9, 'interview_score':6})
r2 = requests.post(url2,json={'experience':2, 'test_score':9, 'interview_score':6})
r3 = requests.post(url3,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r1.json())
print(r2.json())
print(r3.json())