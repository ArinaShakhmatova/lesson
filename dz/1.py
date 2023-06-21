import vk_api
import requests
import random
token = 'vk1.a.CdXwQ2KwyYcwn5oaP2TQwkfQggDLfT9E3EMGa8dpfTW2Fig89ZYWMy1PkA9IvR_hd24KsDOp0jdS19zX5IolBrCOupbRJxiMt4PMcmsofWM8CWF8FyC6eutUKmlMSfc4Cm5IogkZAL0iokcA3wBTpgpadENXYkUS8adiWyuIi6VKzjj3EdVzPMDprSZsRrtrpOjNacbLhI7ceWhPZGKvWw'

vk = vk_api.VkApi(token=token)
vk._auth_token()
while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] >= 1:
        print(messages)
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']
        if message_text.lower() == 'корабли':

            def get_starship(url):
                global num
                global max_speed
                global max_speed_ship
                num += 1

                response = requests.get(f'{url}{num}/').json()

                if response.get('detail') == 'Not found' or response['max_atmosphering_speed'] == 'n/a':
                    get_starship(url_starships)
                else:
                    ship_name = response['name']
                    ship_speed = response['max_atmosphering_speed']
                    if ship_speed[-2:] == 'km':
                        ship_speed = ship_speed[:-2]
                    if int(ship_speed) > max_speed:
                        max_speed = int(ship_speed)
                        max_speed_ship = ship_name


            url_starships = 'https://swapi.dev/api/starships/'
            num = 0
            max_speed = 0

            for _ in range(10):
                get_starship(url_starships)

            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': {max_speed_ship}})

        if message_text.lower() == 'планеты':

            def get_starship(url):
                global num
                global max_diameter
                global max_diameter_ship
                num += 1

                response = requests.get(f'{url}{num}/').json()

                if response.get('detail') == 'Not found' or response['diameter'] == 'n/a':
                    get_starship(url_starships)
                else:
                    ship_name = response['name']
                    ship_diameter = response['diameter']
                    if ship_diameter[-2:] == 'km':
                        ship_diameter = ship_diameter[:-2]
                    if int(ship_diameter) > max_diameter:
                        max_diameter = int(ship_diameter)
                        max_diameter_ship = ship_name


            url_starships = 'https://swapi.dev/api/planets/'
            num = 0
            max_diameter = 0

            for _ in range(10):
                get_starship(url_starships)

            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': {max_diameter_ship}})



        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Error'})