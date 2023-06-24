from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest

from config import load_config
from move_to import move_files_by_format, source_directory, destination_directory, file_extension, excluded_directories

config = load_config(".env")
post_limit = 10
CHANNEL_USERNAME = 'koyawaii' # Юзернейм без @


client = TelegramClient('session_name', config.tg_info.api_id, config.tg_info.api_hash)
client.start()


channel = client(GetFullChannelRequest(channel=CHANNEL_USERNAME))


messages = client(
    GetHistoryRequest(
        peer=CHANNEL_USERNAME,
        limit=post_limit,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    )
).messages


for message in messages:
    if message.media:
        if message.photo:
            # Если сообщение - фото
            caption = message.message or ''
            photo = message.photo
            file = client.download_media(photo)
            client.send_file(config.tg_info.chat_id, file, caption=caption)
            move_files_by_format(source_directory, destination_directory, file_extension, excluded_directories)
        elif message.document:
            # Если сообщение - документ
            caption = message.message or ''
            document = message.document
            file = client.download_media(document)
            client.send_file(config.tg_info.chat_id, file, caption=caption)
            move_files_by_format(source_directory, destination_directory, file_extension, excluded_directories)
        elif message.video:
            # Если сообщение - видео
            caption = message.message or ''
            video = message.video
            file = client.download_media(video)
            client.send_file(config.tg_info.chat_id, file, caption=caption)
            move_files_by_format(source_directory, destination_directory, file_extension, excluded_directories)
        elif message.audio:
            # Если сообщение - аудио
            caption = message.message or ''
            audio = message.audio
            file = client.download_media(audio)
            client.send_file(config.tg_info.chat_id, file, caption=caption)
            move_files_by_format(source_directory, destination_directory, file_extension, excluded_directories)
        elif message.voice:
            # Если сообщение - голосовое сообщение
            caption = message.message or ''
            voice = message.voice
            file = client.download_media(voice)
            client.send_file(config.tg_info.chat_id, file, caption=caption)
            move_files_by_format(source_directory, destination_directory, file_extension, excluded_directories)
        elif message.webpage:
            # Если сообщение - веб-страница
            caption = message.message or ''
            webpage = message.webpage
            client.send_message(config.tg_info.chat_id, f"{caption}\n{webpage.url}")
            move_files_by_format(source_directory, destination_directory, file_extension, excluded_directories)
    elif message.message:
        # Если сообщение содержит только текстовое сообщение
        caption = message.message
        client.send_message(config.tg_info.chat_id, caption)
        move_files_by_format(source_directory, destination_directory, file_extension, excluded_directories)


client.disconnect()
