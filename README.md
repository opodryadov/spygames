# VK Spy Games
![](http://www.oko.by/uploads/posts/2018-08/thumbs/1534242655_2.jpg)

**VK Spy Games** - программа, которая выводит список групп в ВК в которых состоит пользователь, но никто не состоит из его друзей.

## Запуск программы
Для того, чтобы скачать и запустить данную программу выполните следующие шаги:
1. Если у Вас не установлен Git, установите его по [этой инструкции](https://github.com/netology-code/guides/tree/master/git);

2. Склонируйте с помощью Git данный репозиторий следующей командой:
   
   ```git clone https://github.com/opodryadov/spygames.git```
3. Если у Вас не установлен Python, установите его по данным инструкциям:
   - [Инструкция по установке и настройке Python в Windows](https://github.com/netology-code/guides/blob/master/python/python_windows.md)
   - [Инструкция по установке и настройке Python в Mac](https://github.com/netology-code/guides/blob/master/python/python_mac.md)
   - [Инструкция по установке и настройке Python в Linux](https://github.com/netology-code/guides/blob/master/python/python_linux.md)
   
4. Для установки всех зависимостей запустите командную строку от имени администратора и выполните следующую команду:
   
   ```pip install -r 'путь до файла requirements.txt'```
5. Запустите IDLE (Python), откройте файл diploma.py ;
6. В переменную USER_ID вставьте свой ID ВКонтакте;
7. Запустите программу, нажав на клавишу F5.

### Выходные данные
Файл groups.json в папке с программой в формате:
```
[
    {
    “name”: “Название группы”, 
    “gid”: “идентификатор группы”, 
    “members_count”: количество_участников_сообщества
    ...
    },
    {
    …
    }
]
```