from enum import Enum
from pydantic import BaseModel

class DarkMode(str, Enum):
    dark_mode = 'dark'
    light_mode = 'light'
    other = 'other'
    not_given = 'not_given'

class Settings(BaseModel):
    dark_mode: DarkMode
    music_id: str  # spotify tracklist