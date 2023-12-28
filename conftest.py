import sqlite3
import pytest
import time


@pytest.fixture()
def connect_data_base():
    connection = sqlite3.connect("test.db")
    print("Мы подключили БД")
    return connection


cursor = connect_data_base().cursor()
cursor.execute("SELECT *FROM employees")
cursor.fetchall()  # собери все записи и запринть
connect_data_base().close()   #закрывает БД


@pytest.fixture()
def connect_data_base(self):
    connection = sqlite3.connect("test.db")
    print("Мы подключили БД")
    return connection


# @pytest.fixture()
# def generate_data_way_2(request):
#
#     login = f"autotest_{time.time()}@ya.ru"
#     password = "123"
#     request.cls.login = login
#     request.cls.password = password
