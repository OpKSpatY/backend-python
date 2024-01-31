from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository
from sqlalchemy import text

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """Should insert and delete User"""

    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    # SQL
    new_user = user_repository.insert_user(name, password)

    connection = engine.connect()
    transaction = connection.begin()

    query = text("SELECT * FROM users WHERE id = :user_id")
    query_obj = query.bindparams(user_id=new_user.id)

    # Utilizando o objeto de texto do SQLAlchemy na execução da consulta
    result = connection.execute(query_obj)
    query_user = result.fetchone()

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password

    # Executando a exclusão
    delete_query = text("DELETE FROM users WHERE id = :user_id")
    delete_query_obj = delete_query.bindparams(user_id=query_user.id)
    result = connection.execute(delete_query_obj)

    transaction.commit()
    connection.close()


'''def test_select_user(): # teste c/ problema!
    """ Should select a user in Users table and compare it """

    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()
    data = UsersModel(id=user_id, name=name, password=password)

    engine = db_connection_handler.get_engine()
    with engine.connect() as conn:
        conn.execute(
            text(f"INSERT INTO users (id, name, password) VALUES ({user_id}, '{name}', '{password}')")
        )

    query_user1 = user_repository.select_user(user_id=user_id)
    query_user2 = user_repository.select_user(name=name)
    query_user3 = user_repository.select_user(user_id=user_id, name=name)

    assert data in query_user1

    with engine.connect() as conn:
        conn.execute(
        text(f"DELETE FROM users WHERE id='{user_id}';")
    )'''
