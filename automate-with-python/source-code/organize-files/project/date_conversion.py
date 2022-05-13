# This program renames Files with American-Style Dates to European-Style Dates
import re
import os
import shutil

datePattern = re.compile(r"""
                         ^(.*?)
                         ((0|1)?\d)-
                         ((0|1|2|3)?\d)-
                         ((19|20)\d\d)
                         (.*?)$
                         """, re.VERBOSE)
