import vk_module
import json

USER_ID = '171691064' # сюда необходимо вписать id 'жертвы'

with open('groups.json', 'w', encoding='utf-8') as output:
    func = vk_module.VK_API(USER_ID).get_unique_groups(USER_ID)
    json.dump(func, output, ensure_ascii=False, indent=2)
    print('\nРезультат записан в файл groups.json')