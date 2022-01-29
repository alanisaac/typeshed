import sys
from _typeshed import Self
from typing import Any, Container, Generic, Iterable, Iterator, SupportsInt, TypeVar, overload

# Undocumented length constants
IPV4LENGTH: int
IPV6LENGTH: int

_A = TypeVar("_A", IPv4Address, IPv6Address)
_N = TypeVar("_N", IPv4Network, IPv6Network)

def ip_address(address: object) -> IPv4Address | IPv6Address: ...
def ip_network(address: object, strict: bool = ...) -> IPv4Network | IPv6Network: ...
def ip_interface(address: object) -> IPv4Interface | IPv6Interface: ...

class _IPAddressBase:
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self: Self, other: Self) -> bool: ...
    def __gt__(self: Self, other: Self) -> bool: ...
    def __le__(self: Self, other: Self) -> bool: ...
    def __lt__(self: Self, other: Self) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def compressed(self) -> str: ...
    @property
    def exploded(self) -> str: ...
    @property
    def reverse_pointer(self) -> str: ...
    @property
    def version(self) -> int: ...

class _BaseAddress(_IPAddressBase, SupportsInt):
    def __init__(self, address: object) -> None: ...
    def __add__(self: Self, other: int) -> Self: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __sub__(self: Self, other: int) -> Self: ...
    @property
    def is_global(self) -> bool: ...
    @property
    def is_link_local(self) -> bool: ...
    @property
    def is_loopback(self) -> bool: ...
    @property
    def is_multicast(self) -> bool: ...
    @property
    def is_private(self) -> bool: ...
    @property
    def is_reserved(self) -> bool: ...
    @property
    def is_unspecified(self) -> bool: ...
    @property
    def max_prefixlen(self) -> int: ...
    @property
    def packed(self) -> bytes: ...

class _BaseNetwork(_IPAddressBase, Container[_A], Iterable[_A], Generic[_A]):
    network_address: _A
    netmask: _A
    def __init__(self, address: object, strict: bool = ...) -> None: ...
    def __contains__(self, other: Any) -> bool: ...
    def __getitem__(self, n: int) -> _A: ...
    def __iter__(self) -> Iterator[_A]: ...
    def address_exclude(self: Self, other: Self) -> Iterator[Self]: ...
    @property
    def broadcast_address(self) -> _A: ...
    def compare_networks(self: Self, other: Self) -> int: ...
    def hosts(self) -> Iterator[_A]: ...
    @property
    def is_global(self) -> bool: ...
    @property
    def is_link_local(self) -> bool: ...
    @property
    def is_loopback(self) -> bool: ...
    @property
    def is_multicast(self) -> bool: ...
    @property
    def is_private(self) -> bool: ...
    @property
    def is_reserved(self) -> bool: ...
    @property
    def is_unspecified(self) -> bool: ...
    @property
    def max_prefixlen(self) -> int: ...
    @property
    def num_addresses(self) -> int: ...
    def overlaps(self, other: _BaseNetwork[_A]) -> bool: ...
    @property
    def prefixlen(self) -> int: ...
    if sys.version_info >= (3, 7):
        def subnet_of(self: Self, other: Self) -> bool: ...
        def supernet_of(self: Self, other: Self) -> bool: ...
    def subnets(self: Self, prefixlen_diff: int = ..., new_prefix: int | None = ...) -> Iterator[Self]: ...
    def supernet(self: Self, prefixlen_diff: int = ..., new_prefix: int | None = ...) -> Self: ...
    @property
    def with_hostmask(self) -> str: ...
    @property
    def with_netmask(self) -> str: ...
    @property
    def with_prefixlen(self) -> str: ...
    @property
    def hostmask(self) -> _A: ...

class _BaseInterface(_BaseAddress, Generic[_A, _N]):
    hostmask: _A
    netmask: _A
    network: _N
    @property
    def ip(self) -> _A: ...
    @property
    def with_hostmask(self) -> str: ...
    @property
    def with_netmask(self) -> str: ...
    @property
    def with_prefixlen(self) -> str: ...

class IPv4Address(_BaseAddress): ...
class IPv4Network(_BaseNetwork[IPv4Address]): ...
class IPv4Interface(IPv4Address, _BaseInterface[IPv4Address, IPv4Network]): ...

class IPv6Address(_BaseAddress):
    @property
    def ipv4_mapped(self) -> IPv4Address | None: ...
    @property
    def is_site_local(self) -> bool: ...
    @property
    def sixtofour(self) -> IPv4Address | None: ...
    @property
    def teredo(self) -> tuple[IPv4Address, IPv4Address] | None: ...
    if sys.version_info >= (3, 9):
        @property
        def scope_id(self) -> str | None: ...

class IPv6Network(_BaseNetwork[IPv6Address]):
    @property
    def is_site_local(self) -> bool: ...

class IPv6Interface(IPv6Address, _BaseInterface[IPv6Address, IPv6Network]): ...

def v4_int_to_packed(address: int) -> bytes: ...
def v6_int_to_packed(address: int) -> bytes: ...

# Third overload is technically incorrect, but convenient when first and last are return values of ip_address()
@overload
def summarize_address_range(first: IPv4Address, last: IPv4Address) -> Iterator[IPv4Network]: ...
@overload
def summarize_address_range(first: IPv6Address, last: IPv6Address) -> Iterator[IPv6Network]: ...
@overload
def summarize_address_range(
    first: IPv4Address | IPv6Address, last: IPv4Address | IPv6Address
) -> Iterator[IPv4Network] | Iterator[IPv6Network]: ...
def collapse_addresses(addresses: Iterable[_N]) -> Iterator[_N]: ...
@overload
def get_mixed_type_key(obj: _A) -> tuple[int, _A]: ...
@overload
def get_mixed_type_key(obj: IPv4Network) -> tuple[int, IPv4Address, IPv4Address]: ...
@overload
def get_mixed_type_key(obj: IPv6Network) -> tuple[int, IPv6Address, IPv6Address]: ...

class AddressValueError(ValueError): ...
class NetmaskValueError(ValueError): ...
