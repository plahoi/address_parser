import datetime

STREET: str = 'street'
HOUSE_NUMBER: str = 'housenumber'
ADDRESS_SEP: str = ' '
SPECIAL_CHARACTERS_TO_AVOID = r'[,#]'
NOT_AVAILABLE_VALUE: str = 'NA'
PATTERN_NONR = rf'(?P<{STREET}>.+\d+)\s(?P<{HOUSE_NUMBER}>(?:No|Nr|no|nr)\.?\s?\d+\s?[a-zA-Z]?)'
DATETIME_LOG_STR: str = f'[{datetime.datetime.utcnow()}]'
