from enum import IntEnum


class Role(IntEnum):
    ADMIN = 1
    TRANSPORT_OWNER = 2
    CARGO_OWNER = 3

HELP_TEXT_ROLES = "1: ADMIN, 2: TRANSPORT_OWNER, 3: CARGO_OWNER"
