# Stubs for kazoo.recipe.watchers (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

log = ... # type: Any

class DataWatch:
    def __init__(self, client, path, func=None, *args, **kwargs) -> None: ...
    def __call__(self, func): ...

class ChildrenWatch:
    def __init__(self, client, path, func=None, allow_session_lost=True, send_event=False) -> None: ...
    def __call__(self, func): ...

class PatientChildrenWatch:
    client = ... # type: Any
    path = ... # type: Any
    children = ... # type: Any
    time_boundary = ... # type: Any
    children_changed = ... # type: Any
    def __init__(self, client, path, time_boundary=30) -> None: ...
    asy = ... # type: Any
    def start(self): ...
