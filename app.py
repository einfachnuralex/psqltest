    import psycopg2
    import os
    
    from psycopg2 import Error
    try:
        connection = psycopg2.connect(user = os.environ['USER'],
                                      password = os.environ['PASS'],
                                      host = os.environ['HOST'],
                                      port = os.environ['PORT'],
                                      database = os.environ['DB'])
        cursor = connection.cursor()
        
        create_table_query = '''CREATE TABLE mobile
              (ID INT PRIMARY KEY     NOT NULL,
              MODEL           TEXT    NOT NULL,
              PRICE         REAL); '''
        
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL ")
    except (Exception, psycopg2.DatabaseError) as error :
        print ("Error while creating PostgreSQL table", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
