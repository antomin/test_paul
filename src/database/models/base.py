from datetime import datetime
from typing import Generic, Sequence, TypeVar

from sqlalchemy import BigInteger, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

T = TypeVar("T")


class Base(DeclarativeBase, Generic[T]):
    __abstract__ = True

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now(), server_default=func.now())
    modified_at: Mapped[datetime] = mapped_column(
        default=func.now(), server_default=func.now(), onupdate=func.now(), server_onupdate=func.now()
    )

    def __str__(self):
        return f"<{self.__class__.__name__}: {self.id}>"

    def __repr__(self):
        return self.__str__()

    async def create(self, session: AsyncSession) -> T:
        session.add(self)
        await session.commit()

        return self

    async def delete(self, session: AsyncSession) -> None:
        await session.delete(self)
        await session.commit()

    async def update(self, session: AsyncSession, **values) -> T:
        for key, value in values.items():
            if not hasattr(self, key):
                raise ValueError(f"Attribute '{key}' is not valid for {self.__class__.__name__}")
            setattr(self, key, value)

        session.add(self)
        await session.commit()

        return self

    @classmethod
    async def get_by_id(cls, id_: int, session: AsyncSession) -> T | None:
        stmt = select(cls).where(cls.id == id_)
        result = await session.execute(stmt)

        return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, session: AsyncSession) -> Sequence[T]:
        stmt = select(cls)
        result = await session.execute(stmt)

        return result.scalars().all()
