import mysql.connector as MySQLdb

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'neelima_2012',
    'database': 'movies',
}

class SqlConnection(object):
# MySQL Configuration

    def __init__(self, db_config):
        self.db_config = db_config
        try:
            self.connection = MySQLdb.connect(**self.db_config)
            self.cursor = self.connection.cursor(dictionary=True)
        except Exception as e:
            self.connection.close()
            
    def get_num_of_visitors(self,movie_id):
    
        try:
        # Fetching the number of visitors for the given movie ID from the database
            query = "SELECT SUM(visits) FROM visitors WHERE movie_id = %s"
            self.cursor.execute(query, (movie_id,))
            result = self.cursor.fetchone()

            if result is not None:
                num_of_visitors = result[0]
                return num_of_visitors
            else:
                return 0  
        
        except Exception as e:
            print(f'Error{e}')

        finally:
            self.cursor.close()
            self.connection.close()


   