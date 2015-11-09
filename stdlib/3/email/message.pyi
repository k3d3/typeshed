# Stubs for email.message (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Message:
    policy = ...  # type: Any
    preamble = ...  # type: Any
    defects = ...  # type: Any
    def __init__(self, policy=...) -> None: ...
    def as_string(self, unixfrom=False, maxheaderlen=0, policy=None): ...
    def __bytes__(self): ...
    def as_bytes(self, unixfrom=False, policy=None): ...
    def is_multipart(self): ...
    def set_unixfrom(self, unixfrom): ...
    def get_unixfrom(self): ...
    def attach(self, payload): ...
    def get_payload(self, i=None, decode=False): ...
    def set_payload(self, payload, charset=None): ...
    def set_charset(self, charset): ...
    def get_charset(self): ...
    def __len__(self): ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, val): ...
    def __delitem__(self, name): ...
    def __contains__(self, name): ...
    def __iter__(self): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def get(self, name, failobj=None): ...
    def set_raw(self, name, value): ...
    def raw_items(self): ...
    def get_all(self, name, failobj=None): ...
    def add_header(self, _name, _value, **_params): ...
    def replace_header(self, _name, _value): ...
    def get_content_type(self): ...
    def get_content_maintype(self): ...
    def get_content_subtype(self): ...
    def get_default_type(self): ...
    def set_default_type(self, ctype): ...
    def get_params(self, failobj=None, header='', unquote=True): ...
    def get_param(self, param, failobj=None, header='', unquote=True): ...
    def set_param(self, param, value, header='', requote=True, charset=None, language='',
                  replace=False): ...
    def del_param(self, param, header='', requote=True): ...
    def set_type(self, type, header='', requote=True): ...
    def get_filename(self, failobj=None): ...
    def get_boundary(self, failobj=None): ...
    def set_boundary(self, boundary): ...
    def get_content_charset(self, failobj=None): ...
    def get_charsets(self, failobj=None): ...

class MIMEPart(Message):
    def __init__(self, policy=None) -> None: ...
    @property
    def is_attachment(self): ...
    def get_body(self, preferencelist=...): ...
    def iter_attachments(self): ...
    def iter_parts(self): ...
    def get_content(self, *args, *, content_manager=None, **kw): ...
    def set_content(self, *args, *, content_manager=None, **kw): ...
    def make_related(self, boundary=None): ...
    def make_alternative(self, boundary=None): ...
    def make_mixed(self, boundary=None): ...
    def add_related(self, *args, **kw): ...
    def add_alternative(self, *args, **kw): ...
    def add_attachment(self, *args, **kw): ...
    def clear(self): ...
    def clear_content(self): ...

class EmailMessage(MIMEPart):
    def set_content(self, *args, **kw): ...
