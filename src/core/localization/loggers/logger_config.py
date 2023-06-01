import sys
from loguru import logger


CONFIG = {
    'handlers': [
        {'sink': sys.stdout,
         'level': 'DEBUG',
         'format': '<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | <blue>{level}</blue> | {message}',
         'colorize': True,
         }
    ]
}

Logger = logger
Logger.configure(**CONFIG)
