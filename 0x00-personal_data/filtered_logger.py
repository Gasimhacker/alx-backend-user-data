#!/usr/bin/env python3
"""
A module that defines a function filter_datum
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """Obfuscate fileds inside a message"""
    for field in fields:
        message = re.sub(fr'{field}=[^{separator}]*',
                         fr'{field}={redaction}', message)
    return message
