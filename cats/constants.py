from enum import Enum


class ColorState(Enum):
    GRAY = "gray"
    BLACK = "black"
    WHITE = "white"
    GINGER = "ginger"
    MIXED = "mixed"


COLOR_CHOICES = (
    (ColorState.GRAY.value, "Серый"),
    (ColorState.BLACK.value, "Черный"),
    (ColorState.WHITE.value, "Белый"),
    (ColorState.GINGER.value, "Рыжий"),
    (ColorState.GINGER.value, "Рыжий"),
    (ColorState.MIXED.value, "Смешанный"),
)
