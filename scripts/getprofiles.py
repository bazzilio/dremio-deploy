import requests
import json
import datetime
import time
import urllib3
urllib3.disable_warnings()

dremio_url = 'https://dremio.common12p24.epaas.s7.aero'
user="v.romaneev"
pwd="ChangeMe"
path="."

def get_profiles():
    offset = 0
    all_jobs = json.loads(requests.get(dremio_url + '/apiv2/jobs/?limit=10000', headers = headers, verify=False).text)
    text_file = open(path +"/queries.json", "w")
    num_profiles_gotten = 0
    for job in all_jobs['jobs']:
        text_file.write(json.dumps(job))
        profile_response = requests.post(dremio_url + '/apiv2/support/' + job['id'] + '/download', headers = headers, verify=False)
        profile_file = bytearray(profile_response.content)
        with open(path + "/"+job['id'] + '.zip', 'wb') as prof_file:
            prof_file.write(profile_file)
        num_profiles_gotten += 1
        if num_profiles_gotten % 1000 == 0:
            print (str(datetime.datetime.now()) + 'gotten ' + str(num_profiles_gotten) + ' profiles')
    text_file.close()

headers = {'Content-Type': 'application/json'}
data = '{"userName": "'+ user + '","password": "'+pwd+'" }'

response = requests.post(dremio_url + '/apiv2/login', headers=headers, data=data, verify=False)
print(response.text)
token = response.json()['token'] # _dremio is prepended to the token
print(token)

headers = {'Content-Type': 'application/json', 'Authorization': '_dremio' + token}
print ('starting 10,000 ' + str(datetime.datetime.now()))

get_profiles()
print ('done ' + str(datetime.datetime.now()))
