import json
import time
import urllib


import requests
import sys

from plyer import notification




def vaccinate():
    print('...vaccination center appointmnet...')
    kannur_id = 297
    r = requests.get(
        f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={kannur_id}&date=01-05-2021')
    data = r.json()

    print(data['centers'])
    center = []
    if data['centers']:
        print('availabe at')
        for value in data['centers']:
            center.append(value['name'])

        for j in center:

            print(j)
            title = 'cowin'

            notification.notify(title=title, message=j)
        sys.exit()

    else:
        print('currenty not available')
        time.sleep(3)
    vaccinate()

def districts():

    district_data = requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/districts/17')
    d=district_data.json()
    for i in d['districts']:
        print(i)

if __name__ == '__main__':

    districts()
    vaccinate()