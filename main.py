from enum import Enum
from typing import Optional

import psycopg2
from fastapi import FastAPI, Query

from model import Phone

app = FastAPI()

FILE_PATH = 'phone.csv'


def get_conn():
    return psycopg2.connect(dbname='postgres', user='postgres', password='s71456')


def get_phone_list():
    sql = 'select * from phone'
    with get_conn() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
    phones = [Phone(id=row[0], name=row[1], description=row[2], price=row[3]) for row in rows]
    return phones


class PhoneEnum(str, Enum):
    iphone = 'IPhone'
    htc = 'HTC'
    samsung = 'Samsung'


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Path parameter

# # 1 path
# @app.get('/phone/{phone_id}')
# async def get_phone_id(phone_id: int):
#     phone_list = get_phone_list()
#     phone: Phone
#     for phone in phone_list:
#         if phone.id == phone_id:
#             return {'name': phone.name, 'description': phone.description, 'price': phone.price}
#     return {'Phone not found'}
#
#
# # 2 return list
# @app.get('/iphone')
# async def get_iphone():
#     phone_list = get_phone_list()
#     phone: Phone
#     result = []
#     for phone in phone_list:
#         if phone.name == 'IPhone':
#             result.append(phone)
#     return {'result': result}
#
#
# # 3 enum
# @app.get('/phone_name/{phone_name}')
# async def get_phone(phone_name: PhoneEnum):
#     if phone_name == PhoneEnum.samsung:
#         return {'Phone name': phone_name}
#
#     if phone_name.value == 'htc':
#         return {'Phone name': phone_name}
#
#     return {'Phone name': phone_name}

# query parameter

# # 1 path and query
# @app.get('/phone/{phone_id}')
# async def get_phone_id(phone_id: int, tax_pct: Optional[float] = None):
#     phone_list = get_phone_list()
#     for phone in phone_list:
#         if phone.id == phone_id:
#             if tax_pct:
#                 phone = phone.dict()
#                 phone['tax'] = phone['price'] * tax_pct
#                 return phone
#             else:
#                 return phone
#
#     return {'Phone not found'}
#
#
# # 2 任意給訂參數
# @app.get('/phone')
# async def get_phone(name: str, price: Optional[int] = None):
#     phone_list = get_phone_list()
#     phone: Phone
#     for phone in phone_list:
#         if phone.name == name:
#             price = price or phone.price
#             return {'name': phone.name, 'price': price}
#     return {'Phone not found'}

# request body
# 1
@app.post('/create_phone/')
async def create_phone(phone: Phone):
    with get_conn() as conn:
        with conn.cursor() as cursor:
            sql = '''
            insert into phone (name, description, price) values (%s, %s, %s)
            '''
            values = (phone.name, phone.description, phone.price)
            cursor.execute(sql, values)
        conn.commit()
    return phone


# Query: string validation
# ... make it required
@app.get('/phone')
async def get_phone(name: Optional[str] = Query(None, max_length=5)):
    phone_list = get_phone_list()
    phone: Phone
    result = []
    for phone in phone_list:
        if phone.name == name:
            result.append(phone)
    return result


# Path: number validation
