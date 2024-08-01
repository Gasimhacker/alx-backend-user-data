#!/usr/bin/env python3
"""
A module that defines a function filter_datum
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """Obfuscate fileds inside a message"""
    field = '|'.join(fields)
    pattern = fr'({field})=[^{separator}]*'
    return re.sub(pattern, r'\1=' + redaction, message)
