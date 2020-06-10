import requests
import time
from itertools import chain

TOKEN = 'a180756acd7bed622871623f37d94932a75083403b1542ac21539edeaf16f32e3085da79166e3dc86c36d'
TIME = 1 # время задержки, сек
DEBUG = 0 # показывать сообщения в консоли

class VK_API:

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self, user_id, groups_ids='', fields=''):
        return {
            'access_token': TOKEN,
            'user_id': user_id,
            'v': '5.107',
            'group_ids': groups_ids,
            'fields': fields,
        }

    def get_request(self, method, params):
        self.method = method
        response = requests.get(
            f'https://api.vk.com/method/{method}',
            params,
        )
        return response.json()

    def get_groups(self):
        response = self.get_request(
            'groups.get',
            self.get_params(self.user_id)
        )
        return response['response']['items']

    def get_friends(self):
        friends_list = []
        response = self.get_request(
            'friends.get',
            self.get_params(self.user_id)
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
        return list(user_groups)

    def get_unique_groups(self, user_id):
        groups = self.run()
        time.sleep(TIME)
        groups_ids = ','.join(str(e) for e in groups)
        response = self.get_request(
            'groups.getById',
            self.get_params(user_id, groups_ids, 'members_count')
        )
        return response['response']