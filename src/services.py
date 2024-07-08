from sqlalchemy import insert, select, Connection
from src.db import users_table
from src.dto import CreateUserDTO


def get_users(conn: Connection):
    query = select(users_table)
    rows = conn.execute(query).all()
    return map(lambda row: row._asdict(), rows)


def get_user(conn: Connection, user_id: str):
    query = select(users_table).where(users_table.c.id == user_id).limit(1)
    row = conn.execute(query).first()
    store = row._asdict() if row else None
    return store


def create_user(conn: Connection, data: CreateUserDTO):
    ut = users_table
    try:
        user_rows = conn.execute(
            (
                insert(ut)
                .values(
                    name=data.name,
                    email=data.email,
                )
                .returning(ut)
            )
        )
        conn.commit()
        return user_rows.first()._asdict()

    except Exception as e:
        conn.rollback()
        raise e


def delete_user(conn: Connection, user_id: str):
    try:
        print("user_id")

        conn.execute(users_table.delete().where(users_table.c.id == user_id))
        conn.commit()
    except Exception as e:
        print("error aqui")
        print(e)
        conn.rollback()
        raise e
