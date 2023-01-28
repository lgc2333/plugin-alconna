from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar

from arclet.alconna import Arparma, command_manager
from arclet.alconna.core import T_Duplication

T = TypeVar("T")


@dataclass
class Match(Generic[T]):
    """
    匹配项，表示参数是否存在于 `all_matched_args` 内
    result (T): 匹配结果
    available (bool): 匹配状态
    """

    result: T
    available: bool


class Query(Generic[T]):
    """
    查询项，表示参数是否可由 `Arparma.query` 查询并获得结果

    result (T): 查询结果

    available (bool): 查询状态

    path (str): 查询路径
    """
    result: T
    available: bool
    path: str

    def __init__(self, path: str, default: T | None = None):
        self.path = path
        self.result = default
        self.available = False

    def __repr__(self):
        return f"Query({self.path}, {self.result})"


@dataclass(frozen=True)
class CommandResult:
    token: int
    output: str | None = field(default=None)
    duplication_type: type[T_Duplication] | None = field(default=None)

    @property
    def result(self) -> Arparma:
        return command_manager.get_record(self.token)  # type: ignore

    @property
    def matched(self) -> bool:
        return self.result.matched

    @property
    def duplication(self) -> T_Duplication:
        return self.result.get_duplication(self.duplication_type)
