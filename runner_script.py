import requests
from configs import *
import time
from random import randrange



created_logs = ['Started Whatsapp groups master process', 'Initialising API Credentials']
add_part_logs = []


def create_group(numbers, count):

    for i in range(count):
        wait_time = randrange(60, 500000)

        body = {
            'name' : f'Group Number {i}',
            'numbers' : numbers
        }

        url = INSTANCE_URL + "/" + PRODUCT_ID + "/" + PHONE_ID + "/createGroup"

        headers = {
            "Content-Type": "application/json",
            "x-maytapi-key": API_TOKEN,
        }
        response = requests.post(url, json=body, headers=headers)
        if response.json()["success"]:
            create_detail_log = response.json()["data"]
            print(f'Created Group ...Group Number {i} successfully......')


        time.sleep(wait_time)

    # print("Response", response.json())
    return response.json()




def get_groups(phone_id):

    url = INSTANCE_URL + "/" + PRODUCT_ID + "/" + PHONE_ID + "/getGroups"

    # endpoint = f"{INSTANCE_URL}/groups"
    headers = {
        "Content-Type": "application/json",
        "x-maytapi-key": API_TOKEN,
    }
    params = {
        "phone_id": phone_id,
        }

    response = requests.post(url, json=params, headers=headers)

    if response.status_code == 200:
        all_groups = response.json()["data"]
        group_names = []
        group_ids = []
        groups = {}

        for grp in all_groups:
            group_name = grp['name']#[:20]
            # new_name = group_name + '...'
            group_id = grp['id']


            group_names.append(group_name)
            group_ids.append(group_id)

            groups[f'{group_name}'] = group_id

            

        data = {
            'names': group_names,
            'ids' : group_ids,
            'groups' :groups
        }

    else:
        data = {
            'names' : '',
            'ids' : '',
        }
        print(f"Failed to retrieve groups. Status: {response.status_code}")
        

    return data



def add_participants(group_id, numbers):
    for num in numbers:
        wait_time = randrange(60, 500000)

        # add member to group
        url = INSTANCE_URL + "/" + PRODUCT_ID + "/" + PHONE_ID + "/group/add"

        headers = {
            "Content-Type": "application/json",
            "x-maytapi-key": API_TOKEN,
        }
        params = {
                "conversation_id": group_id,
                "number": num
        }

        response = requests.post(url, json=params, headers=headers)
        if response.json()["success"] == True:
            # create_detail_log = response.json()["data"]
            add_log = f'Added Participant ...{num} successfully to the group.....'
            print(add_log)
            print('wait for..', wait_time, 'seconds')
            time.sleep(wait_time)
        else:
            print(response.json())
        print(response.json())

    return


def get_group_id(group_name):
    all_groups = get_groups(PHONE_ID)['groups']
    # print(all_groups)

    if group_name in all_groups.keys():
        group = all_groups[f'{group_name}']
        # print(group)

    
    else:
        # print(f'no match... for {group_name} ')
        pass
    return group
