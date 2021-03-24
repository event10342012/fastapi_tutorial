import sqlite3


def create_table():
    with sqlite3.connect('sqlite.db') as conn:
        cursor = conn.cursor()
        sql = '''
            create table phone
            (
                id          serial,
                name        varchar(20),
                description varchar(100),
                price       numeric(9, 2),
                primary key (id)
            )
            '''
        cursor.execute(sql)


def insert_values():
    with sqlite3.connect('sqlite.db') as conn:
        cursor = conn.cursor()
        sql = '''
            insert into phone (id, name, description, price)
            values (1, 'IPhone', 'IPhone6', 100),
                   (2, 'Samsung', 'Samsung', 80),
                   (3, '小米', '小米手機', 50)

            '''
        cursor.execute(sql)
    conn.commit()


if __name__ == '__main__':
    create_table()
    insert_values()
