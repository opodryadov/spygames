import requests
import time
from itertools import chain

TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
TIME = 1  # время задержки, сек
DEBUG = 0  # показывать сообщения в консоли


class VK_API:

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self, add_params: dict = None):
        params = {
            'access_token': TOKEN,
            'v': '5.107'
        }
        if add_params:
            params.update(add_params)
            pass
        return params

    def get_request(self, method, params):
        self.method = method
        response = requests.get(
            f'https://api.vk.com/method/{method}',
            params,
        )
        if 'error' in response.json():
            if DEBUG == 1:
                print('Error')
            return None
        else:
            return response.json()

    def get_groups(self):
        response = self.get_request(
            'groups.get',
            self.get_params({'user_id':self.user_id})
        )
        return response['response']['items']

    def get_friends(self):
        friends_list = []
        response = self.get_request(
            'friends.get',
            self.get_params({'user_id':self.user_id})
        )
        for user_id in response['response']['items']:
            friends_list.append(user_id)
        return friends_list

    def run(self):
        groups_list = []
        user_groups = set(self.get_groups())
        friends_ids = self.get_friends()
        for friend_id in friends_ids:
            try:
                self.user_id = friend_id
                groups = self.get_groups()
                groups_list.append(groups)
                print('.', end="")
            except:
                if DEBUG == 1:
                    print(f'id{friend_id} - закрытый профиль')
        friends_groups = set(list(chain.from_iterable(groups_list)))
        user_groups.difference_update(friends_groups)
        return user_groups

    def get_unique_groups(self):
        groups = self.run()
        time.sleep(TIME)
        groups_ids = ','.join(str(e) for e in groups)
        response = self.get_request(
            'groups.getById',
            self.get_params({'group_ids':groups_ids,
                            'fields':'members_count'})
        )
        return response['response']
