from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    screen_size: int = 600


config = Config()
