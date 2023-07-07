import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from course import get_course


token = 'vk1.a.cw4w2nZgiZCDzCFodPiF4HS3Ho91-H76l5RRr6a5q-azzHmPZSQMTIPNoUYX2urDalC8AuPdFQVZ_57q6WRnWMxXR9ZW1YS5qLbDxgkaSFvP5rVDHz_jQ5UwKfQqK8v7KALo8Q4ppeeo_hDkwgRSwykxiHyWVUHj6a5gyJXbwd7LY8RHpqLGzdaMglBC7eVJQVyeRr48g6oKrmIQ8f13iQ'

while True:
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    random_id = random.randint(0, 10000000)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            print(event.text)
            msg = event.text
            user_id = event.user_id

            if msg == '-k доллар':
                response = f"{get_course('R01235')} рублей за 1 доллар"


            if msg == '-k евро':
                response = f"{get_course('R01239')}, рублей за 1 евро"

            if msg == '-k юани':
                response = f"{get_course('R01375')}, рублей за 10 юаней"

            if msg == '-k фунты':
                response = f"{get_course('R01035')} рублей за 1 фунт"

            if msg == '-k лиры':
                response = f"{get_course('R01700J')} рублей за 1 лир"

            if msg == '-k тенге':
                response = f"{get_course('R01335')} рублей за 100 тенге"

            else:
                response = 'Error'

            vk.messages.send(user_id=user_id, random_id=random_id, message=response)