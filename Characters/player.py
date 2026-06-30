from .character import Character
from .constants import *

class Player(Character):
    def __init__(self):
        super().__init__(
            None,
            PLAYER_BASE_HP,
            PLAYER_BASE_DAMAGE,
            PLAYER_BASE_WEAPON,
            PLAYER_BASE_AGILITY,
            PLAYER_BASE_STAMINA,
        )
        self.base_agility = PLAYER_BASE_AGILITY
        self.base_stamina = PLAYER_BASE_STAMINA