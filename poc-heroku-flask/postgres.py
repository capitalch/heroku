from psycopg2 import pool
from psycopg2.extras import RealDictCursor

poolStore = {}
def getFromHerokuPostgres():
    out = None
    connection = None
    try:
        connection, cursor, pool = getConnectionCursor(dbName='d52l5d6nmpv2ak', autoCommitMode=False)
        cursor.execute('select * from "test"')
        try:
            out = cursor.fetchall()
        except (Exception) as err:
            out = None
            print('Sql execution error')
            connection.commit()
    except (Exception) as error:
        if connection:
            connection.rollback()
        print("Sql execution failure")
    finally:
        if connection:
            cursor.close()
            connection.close()
    return out
    

def getConnectionCursor(dbName, autoCommitMode=False):
    pool = getPool(dbName)
    connection = pool.getconn()
    if autoCommitMode:
        connection.autocommit = True
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    return connection, cursor, pool

def getPool(dbName):
    # dbName = 'd52l5d6nmpv2ak'
    if not dbName in poolStore:
        poolStore[dbName] = pool.ThreadedConnectionPool(
            1,500,user='hrdjzvzaplwrfi', password='18a00536ca50fff504699104e6b21644f7fcd25cf106a0adec1dd99a1f1f0076', host='ec2-34-200-205-45.compute-1.amazonaws.com', port='5432', database='d52l5d6nmpv2ak'
        )
    return poolStore[dbName]