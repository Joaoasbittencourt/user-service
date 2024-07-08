from uuid import uuid4
from sqlalchemy import (
    MetaData,
    UUID,
    Column,
    Table,
    Text,
)

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
    Column("name", Text, nullable=False),
    Column("email", Text, nullable=False),
)
