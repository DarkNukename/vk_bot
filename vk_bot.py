import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
import settings
import random


def load_photo(file_path):
    photo = upload.photo_messages(photos=open(file_path, "rb"))[0]
    attach = 'photo{}_{}'.format(photo['owner_id'], photo['id'])
    return attach

def send_message(user_id, message, attach = None):
     vk.messages.send(
                user_id=user_id,
                attachment=attach,
                keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                message=message,
                random_id=random.randint(1, 1000000))
    


# подключаемся к сообществу
vk = vk_api.VkApi(token=settings.TOKEN)

# Для получения сообщений и вложений
longpoll = VkLongPoll(vk)

# Для отправки вложений
upload = VkUpload(vk)

vk = vk.get_api()





for event in longpoll.listen():
    if event.to_me:
        print(dir(event))
        
        request = event.text
        if request == "Привет":
            photo = load_photo("./images/start_image.png")
            send_message(event.user_id, "12234", photo)



    