import abc

from src.shared.domain.enums.gender import GENDER

class Criminal(abc):
    name: str
    description: str
    gender: GENDER
    common_attack_region: str