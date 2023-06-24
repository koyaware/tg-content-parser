from dataclasses import dataclass

from environs import Env


@dataclass
class TgInfo:
    api_id: int
    api_hash: str
    chat_id: int


@dataclass
class Config:
    tg_info: TgInfo


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_info=TgInfo(
            api_id=env.int('API_ID'),
            api_hash=env.str('API_HASH'),
            chat_id=env.int('CHAT_ID'),
        ),
    )