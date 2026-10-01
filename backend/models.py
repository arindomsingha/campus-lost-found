from sqlalchemy import String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from .database import Base


class LostItem(Base):
    __tablename__ = "lost_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    item_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    location: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    date_lost: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )


class FoundItem(Base):
    __tablename__ = "found_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    item_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    location: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    date_found: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )