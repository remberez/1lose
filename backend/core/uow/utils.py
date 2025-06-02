def with_uow(method):
    async def wrapper(self, *args, **kwargs):
        async with self._uow_factory() as uow:
            return await method(self, *args, uow=uow, **kwargs)
    return wrapper
