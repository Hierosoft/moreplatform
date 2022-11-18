#!/usr/bin/env python
'''
Get platform-specific special folders. This module doesn't use
pathlib, so you can use it without requiring Python 3.4+.

To use it, place morefolders.py in your module and then import it such
as via:

from .morefolders import (
    HOME,
    getUnique,  # replaced by: from hierosoft import get_unique_path
)

Examples:

# To get unique directories for a program named "world_clock":
MY_LUID = "world_clock"  # formerly myDirName
myShare = get_unique_path(MY_LUID, key="Share:Unique")
dtPath = get_unique_path(MY_LUID, key="Desktop:Unique")


Known issues:
- [Consider splitting morefolders into a separate repo and require it.
  #5](https://github.com/poikilos/blnk/issues/5)
'''
from __future__ import print_function
raise NotImplementedError(
    "This module is deprecated. Instead you can use"
    " <https://github.com/Hierosoft/hierosoft>."
)
