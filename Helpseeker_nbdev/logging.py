# AUTOGENERATED! DO NOT EDIT! File to edit: logging.ipynb (unless otherwise specified).

__all__ = ['add_timestamp', 'logging_setup']

# Comes from core.ipynb, cell
import datetime
import logging
import sys
from structlog import wrap_logger
from structlog.processors import JSONRenderer
from structlog.stdlib import filter_by_level

def add_timestamp(_, __, event_dict):
    """
    Add timestamp to a structlog entry
    Args:
        event_dict: structlog event_dict

    Returns:
        event_dict: modified structlog event_dict, now includes a timestamp
    """
    event_dict["timestamp"] = datetime.datetime.utcnow()
    return event_dict


def logging_setup(log_level='INFO'):
    """
    Set up standard structlog logger
    Args:
        log_level: string, defined the logging level. Can be: 'INFO', 'WARNING'

    Returns:
        logger: instantiated logger
    """

    #     logging setup. Import log level from config.json

    logging.basicConfig(stream=sys.stdout,format="%(message)s", level=log_level)
    logger = wrap_logger(
        logging.getLogger(__name__),
        processors=[
            filter_by_level,
            add_timestamp,
            JSONRenderer(indent=1, sort_keys=True)
        ]
    )

    return logger