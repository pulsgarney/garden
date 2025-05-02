from __future__ import annotations
from typing import (
    Awaitable,
    Callable,
    ParamSpec,
    TypeVar,
    Union,
    overload,
    cast,
    Concatenate,
)
import functools
import inspect


P = ParamSpec('P')
R = TypeVar('R')
SelfT = TypeVar('SelfT')


@overload
def chainable(
    func: Callable[Concatenate[SelfT, P], R],
) -> Callable[Concatenate[SelfT, P], Union[R, SelfT, None]]: ...


@overload
def chainable(
    func: Callable[Concatenate[SelfT, P], Awaitable[R]],
) -> Callable[Concatenate[SelfT, P], Awaitable[Union[R, SelfT, None]]]: ...


@overload
def chainable(
    func: Callable[Concatenate[SelfT, P], Union[R, Awaitable[R]]],
) -> Callable[
    Concatenate[SelfT, P], Union[Union[R, SelfT], Awaitable[Union[R, SelfT]]]
]: ...


def chainable(func):
    @functools.wraps(func)
    def wrapper(
        self: SelfT, *args: P.args, **kwargs: P.kwargs
    ) -> Union[R, SelfT, Awaitable[Union[R, SelfT]]]:
        result = func(self, *args, **kwargs)

        if inspect.isawaitable(result):

            async def async_wrapper() -> Union[R, SelfT]:
                res = await cast(Awaitable[Union[R, SelfT]], result)
                return self if res is None or res is self else cast(R, res)

            return async_wrapper()
        else:
            return (
                self if result is None or result is self else cast(R, result)
            )

    return wrapper
