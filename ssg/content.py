import re
import load
from yaml import FullLoader
from collections.abc import Mapping

class Content:
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = regex.split(string, 2)
        load(fm, Loader=FullLoader)
        cls(metadata, content)

    