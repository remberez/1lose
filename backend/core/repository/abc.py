from abc import ABC, abstractmethod


class AbstractRepository[ModelORM](ABC):
    """
    Интерфейс репозитория для работы с моделью.
    Основное назначение инкапсулировать логику работы с данными.
    """

    @abstractmethod
    async def get(self, *args, **kwargs) -> ModelORM:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, **data) -> ModelORM | None:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, model_id: int, **data) -> ModelORM | None:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, model_id: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def list(self, *args, **kwargs) -> list[ModelORM]:
        raise NotImplementedError()
