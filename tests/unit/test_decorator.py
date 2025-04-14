import pytest
import pytest_asyncio
from src.garden.decorator import chainable


class ChainableTestClass:
    def __init__(self, value=0):
        self.value = value


class TestSyncMethods:
    @pytest.fixture
    def obj(self):
        class SyncClass(ChainableTestClass):
            @chainable
            def returns_self(self):
                self.value += 1
                return self

            @chainable
            def returns_none(self):
                self.value += 1
                return None

            @chainable
            def returns_value(self):
                self.value += 1
                return 42

            @chainable
            def returns_other(self):
                self.value += 1
                return 'other'

        return SyncClass()

    def test_sync_returns_self(self, obj):
        result = obj.returns_self()
        assert result is obj
        assert obj.value == 1

    def test_sync_returns_none(self, obj):
        result = obj.returns_none()
        assert result is obj
        assert obj.value == 1

    def test_sync_returns_value(self, obj):
        result = obj.returns_value()
        assert result == 42
        assert obj.value == 1

    def test_sync_returns_other(self, obj):
        result = obj.returns_other()
        assert result == 'other'
        assert obj.value == 1


class TestAsyncMethods:
    @pytest_asyncio.fixture
    async def obj(self):
        class AsyncClass(ChainableTestClass):
            @chainable
            async def returns_self(self):
                self.value += 1
                return self

            @chainable
            async def returns_none(self):
                self.value += 1
                return None

            @chainable
            async def returns_value(self):
                self.value += 1
                return 42

            @chainable
            async def returns_other(self):
                self.value += 1
                return 'other'

        return AsyncClass()

    @pytest.mark.asyncio
    async def test_async_returns_self(self, obj):
        result = await obj.returns_self()
        assert result is obj
        assert obj.value == 1

    @pytest.mark.asyncio
    async def test_async_returns_none(self, obj):
        result = await obj.returns_none()
        assert result is obj
        assert obj.value == 1

    @pytest.mark.asyncio
    async def test_async_returns_value(self, obj):
        result = await obj.returns_value()
        assert result == 42
        assert obj.value == 1

    @pytest.mark.asyncio
    async def test_async_returns_other(self, obj):
        result = await obj.returns_other()
        assert result == 'other'
        assert obj.value == 1


class TestEdgeCases:
    @pytest.mark.asyncio
    async def test_coroutine_return(self):
        '''return coroutine object'''

        class CoroutineClass(ChainableTestClass):
            @chainable
            def return_coroutine(self):
                async def coroutine():
                    return None

                return coroutine()

        obj = CoroutineClass()
        result = await obj.return_coroutine()
        assert result is obj

    def test_method_metadata(self):
        '''method metadata'''

        class MetaClass:
            @chainable
            def documented_method(self):
                '''test'''
                return self

        assert MetaClass.documented_method.__name__ == 'documented_method'
        assert MetaClass.documented_method.__doc__ == 'test'
