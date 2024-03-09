# from aiogram import Bot, Dispatcher, types, executor
# from config import token
# import logging
import requests, os

# https://www.tiktok.com/@codex_kg/video/7327987700139691271
# https://www.tiktok.com/@ba7ile/video/7320840163859369222?is_from_webapp=1&sender_device=pc


input_url = input("URL: ").split("/")
# print(input_url)
current_id = input_url[5].split("?")[0]
# print(current_id)


if  current_id.isdigit():
    print("ID верный")
    video_api = requests.get(f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={current_id}").json()
    video_url = video_api['aweme_list'][0]['video']['play_addr']["url_list"][0]
    print(video_url)
    try:
        print("Greate file video")
        os.mkdir("video")
    except:
        pass
    try:
        with open(f"video/{current_id}.mp4", "wb") as video_file:
            video_file.write(requests.get(video_url).content)
        print(f"Successfully {current_id} dowland")
        os.system("cd explorer .")
    except Exception as error:
        print(f"Error: {error}")
else:
    print("ID неверный")
    
    
# bot = Bot(token=token)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)





