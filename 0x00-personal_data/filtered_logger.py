#!/usr/bin/env python3
"""
A module that defines a function filter_datum
"""
import re
import logging
import mysql.connector
from os import environ
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """Create a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.propagate = False
    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()
    sh.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(sh)

    return logger


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate fileds inside a message"""
    field = '|'.join(fields)
    return re.sub(fr'({field})=[^{separator}]*', fr'\1={redaction}', message)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to secure database"""
    user = environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host = environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db = environ.get('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connection.MySQLConnection(
      host=host,
      user=user,
      password=password,
      database=db
    )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats a LogRecord object"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
