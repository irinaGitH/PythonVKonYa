import  requests, json, time, os

VK_USER_ID = 529118130
VK_POLZ = int(input("Введите ид пользователя"))
VK_TOKEN = "vk1.a.G2grjCY6LAv1gZYKiWPAwRaNCCq8RNX3UdDD-ko5WGuimQZXY7SPCHjB7bzmRALShvxx7nl8Kyw9N13wtqa7MoZ9XR0l3vzu4-vSA6VvBZ3pBa3vKvgsHGfxOFKCnhx59kx1qNx-cn1H7AZiNbTRlRs5B4WdqJqAVRxh1HCZwNThKh4kfw_-10P-Dz7ZSctQVenfD7pPbH-jcf5uTzSe4w"

def get_foto_data(offset = 0, count = 50):
    api = requests.get("https://api.vk.com/method/photos.getAll", params={
        'owner_id': VK_POLZ,
        'access_token': VK_TOKEN,
        'offset': offset,
        'count': count,
        'extended': 1,
        'photo_sizes': 0,
        'v': 5.103
    })
    return json.loads(api.text)

a = get_foto_data(0,50)

for i in a['response']['items']:
    file_url = i["sizes"][-1]["url"]
    filename = str(i["likes"]["count"]) + ".jpg"
    api = requests.get(file_url)

    with open("images/%s" %filename, "wb") as file:
        file.write(api.content)


#https://oauth.vk.com/blank.html#access_token=vk1.a.G2grjCY6LAv1gZYKiWPAwRaNCCq8RNX3UdDD-ko5WGuimQZXY7SPCHjB7bzmRALShvxx7nl8Kyw9N13wtqa7MoZ9XR0l3vzu4-vSA6VvBZ3pBa3vKvgsHGfxOFKCnhx59kx1qNx-cn1H7AZiNbTRlRs5B4WdqJqAVRxh1HCZwNThKh4kfw_-10P-Dz7ZSctQVenfD7pPbH-jcf5uTzSe4w&expires_in=0&user_id=529118130&state=123456