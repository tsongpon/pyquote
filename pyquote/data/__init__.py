from psycopg2.pool import ThreadedConnectionPool
from contextlib import contextmanager
from psycopg2.extras import register_inet, Inet
import psycopg2

connection_pool = ThreadedConnectionPool(1, 20,
                                         database='testdb',
                                         user='tum',
                                         password='pingu123',
                                         host='localhost',
                                         port=5432,
                                         application_name='gaia',
                                         connect_timeout=10)

print 'connection pool created'


@contextmanager
def get_db_connection():
    """
    psycopg2 connection context manager.
    Fetch a connection from the connection pool and release it.
    """
    try:
        connection = connection_pool.getconn()
        yield connection
    finally:
        connection_pool.putconn(connection)


@contextmanager
def get_db_cursor(commit=False):
    """
    psycopg2 connection.cursor context manager.
    Creates a new cursor and closes it, commiting changes if specified.
    """
    with get_db_connection() as connection:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            yield cursor
            if commit:
                print 'commiting transection'
                connection.commit()
        finally:
            cursor.close()
