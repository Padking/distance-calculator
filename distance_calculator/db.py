'''
Создаёт, наполняет, перезаписывает таблицу БД

'''

import sqlite3

from graph import get_shortest_distance_table


TABLE_NAME = 'distances'


def get_connection(table_name=TABLE_NAME):
    table_name_tmpl = '{}.sqlite'
    conn = sqlite3.connect(table_name_tmpl.format(table_name))

    return conn


def get_shortest_distance(conn, table_name=TABLE_NAME, from_city=1, to_city=2):
    cursor = conn.cursor()

    shortest_distance_ = cursor.execute(
        """
        SELECT dist_with_city_{}
        FROM {}
        WHERE city_id = {}""".format(from_city, table_name, to_city)).fetchall()

    shortest_distance = shortest_distance_[0][0]

    conn.close()

    return shortest_distance


if __name__ == '__main__':

    shortest_distance_table = get_shortest_distance_table()
    conn = get_connection(TABLE_NAME)
    shortest_distance_table.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
