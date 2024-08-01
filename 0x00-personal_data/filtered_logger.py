#!/usr/bin/env python3
"""
A module that defines a function filter_datum
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate fileds inside a message"""
    field = '|'.join(fields)
    return re.sub(fr'({field})=[^{separator}]*', fr'\1={redaction}', message)
