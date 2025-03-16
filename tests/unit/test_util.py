import pytest
import asyncio
from src.garden.util import universal_execute


@pytest.mark.asyncio
async def test_sync_function_execution():
    '''execute sync function'''

    def func(r: str) -> str:
        return r

    result = await universal_execute(func, 'result')
    assert result == 'result'


@pytest.mark.asyncio
async def test_async_function_execution():
    '''execute async function'''

    async def func(r: str) -> str:
        await asyncio.sleep(0.01)
        return r

    result = await universal_execute(func, 'result')
    assert result == 'result'


@pytest.mark.asyncio
async def test_sync_argument_passing():
    '''sync function with arguments'''

    def func(a: int, b: int, c: int = 0) -> int:
        return a + b + c

    result = await universal_execute(func, 1, 2, c=3)
    assert result == 6


@pytest.mark.asyncio
async def test_async_argument_passing():
    '''async function with arguments'''

    async def func(a: int, b: int, c: int = 0) -> int:
        await asyncio.sleep(0.01)
        return a + b + c

    result = await universal_execute(func, 1, 2, c=3)
    assert result == 6


@pytest.mark.asyncio
async def test_invalid_function_type():
    '''invalid function type'''

    with pytest.raises(TypeError):
        await universal_execute("not_a_function")


@pytest.mark.asyncio
async def test_sync_exception_propagation():
    '''sync function exception propagation'''

    def func():
        raise ValueError("sync_error")

    with pytest.raises(ValueError) as exc_info:
        await universal_execute(func)

    assert "sync_error" in str(exc_info.value)


@pytest.mark.asyncio
async def test_async_exception_propagation():
    '''async function exception propagation'''

    async def func():
        raise ValueError("async_error")

    with pytest.raises(ValueError) as exc_info:
        await universal_execute(func)

    assert "async_error" in str(exc_info.value)
