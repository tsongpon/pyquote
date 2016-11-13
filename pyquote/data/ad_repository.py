from pyquote.data import get_db_cursor


class QuoteRepository(object):

    def ping_db(self):
        with get_db_cursor(False) as cursor:
            cursor.execute("SELECT 1")
            data = cursor.fetchone()
            print data
