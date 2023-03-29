import json
import matplotlib.pyplot as plt

import requests
# Make an API call and store the response.
url = 'https://api.data.gov.in/resource/26a686fb-eff5-4b33-b5e9-7dd6f41fb870?api-key=579b464db66ec23bdd0000011c6bddee35f54a8e54f9b004e16182e7&format=json'
r = requests.get(url)
print(f"Status code: {r.status_code}")
# Store API response in a variable.
response_dict = r.json()
# Process results.
#print(response_dict['title'])
#print(response_dict)
#repo_dicts = response_dict.keys()
#repo_values = response_dict.values()
repo_dict = response_dict
#repo_dicts = list(keyss)
x = json.dumps(repo_dict, indent=4)
print(x)
# typenam , med = [],[]
# med.clear()
# typenam.clear()
# for n in range(len(repo_dict['records'])):
#     d = repo_dict['records'][n]
#
#     med.append(d['medicinename'])
#     typenam.append(d['typename'])
#     for key, value in d.items():
#         # srtr="=>"
#         print(f'{f"{key}":<40}{f"=>":<15}{f"{value}"}')
# # print(med)
# # print(typenam)
# x= [0,1,5,6,7,9,2,10]
# y= [0,4,5,8,7,5,3,10]
# fig,ax = plt.subplots()
# ax.plot(x,y)
# plt.style.use('seaborn')
# plt.show()



