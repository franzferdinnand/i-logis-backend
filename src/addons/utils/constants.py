import enum


class Roles(enum.IntEnum):
    ADMIN = 1
    CLIENT = 2
    DRIVER = 3

HELP_TEXT_ROLES = "1: ADMIN, 2: CLIENT, 3: DRIVER"

class Statuses(enum.IntEnum):
    PENDING = 1
    ACCEPTED = 2
    ON_THE_WAY = 3
    DELIVERED = 4

HELP_TEXT_STATUS = "1: PENDING, 2: ACCEPTED, 3: ON_THE_WAY, 4: DELIVERED"
