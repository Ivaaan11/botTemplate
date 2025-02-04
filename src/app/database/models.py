from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='postgresql+asyncpg://user:password@postgres:5432/db')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(unique=True)

    tickets: Mapped[list["Ticket"]] = relationship(back_populates="creator")


class Ticket(Base):
    __tablename__ = 'tickets'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column()
    creator_username: Mapped[str] = mapped_column(ForeignKey('users.username'))

    creator: Mapped["User"] = relationship(back_populates="tickets")


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
