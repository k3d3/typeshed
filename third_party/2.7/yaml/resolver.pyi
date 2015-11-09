# Stubs for yaml.resolver (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from yaml.error import YAMLError

class ResolverError(YAMLError): ...

class BaseResolver:
    DEFAULT_SCALAR_TAG = ... # type: Any
    DEFAULT_SEQUENCE_TAG = ... # type: Any
    DEFAULT_MAPPING_TAG = ... # type: Any
    yaml_implicit_resolvers = ... # type: Any
    yaml_path_resolvers = ... # type: Any
    resolver_exact_paths = ... # type: Any
    resolver_prefix_paths = ... # type: Any
    def __init__(self) -> None: ...
    def add_implicit_resolver(cls, tag, regexp, first): ...
    def add_path_resolver(cls, tag, path, kind=None): ...
    def descend_resolver(self, current_node, current_index): ...
    def ascend_resolver(self): ...
    def check_resolver_prefix(self, depth, path, kind, current_node, current_index): ...
    def resolve(self, kind, value, implicit): ...

class Resolver(BaseResolver): ...
