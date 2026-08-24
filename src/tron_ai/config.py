from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    screen_size: int = 400


config = Config()
