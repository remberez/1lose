from abc import ABC, abstractmethod


class AbstractReadRepository[ModelORM](ABC):
    """
    Интерфейс репозитория для чтения данных.
    Основное назначение инкапсулировать логику работы с базой данных.
    """

    @abstractmethod
    async def get(self, *args, **kwargs) -> ModelORM:
        raise NotImplementedError()

    @abstractmethod
    async def list(self, *args, **kwargs) -> list[ModelORM]:
        raise NotImplementedError()

    @abstractmethod
    async def is_exists(self, model_id: int) -> bool:
        raise NotImplementedError()

class AbstractWriteRepository[ModelORM](ABC):
    """
    Интерфейс репозитория для изменения данных.
    Основное назначение инкапсулировать логику работы с базой данных.
    """

    @abstractmethod
    async def create(self, **data) -> ModelORM | None:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, model_id: int, **data) -> ModelORM | None:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, model_id: int) -> None:
        raise NotImplementedError()
