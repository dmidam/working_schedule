import psycopg2 as pg2


def insert_availability(**kwargs):
    conn = None
    try:
        conn = pg2.connect(database='Work schedule', user='postgres', password='Damdamdam123!')
        cur = conn.cursor()

        start_date = kwargs.get('start_date', None)
        end_date = kwargs.get('end_date', None)
        start_work = kwargs.get('start_work', None)
        end_of_work = kwargs.get('end_of_work', None)
        day = kwargs.get('dat', None)
        if start_date == None:
            start_date = kwargs.get('start_date', 'null')
        else:
            start_date = f"'{start_date}'"

        if end_date == None:
            end_date = kwargs.get('end_date', 'null')
        else:
            end_date = f"'{end_date}'"

        if start_work == None:
            start_work = kwargs.get('start_work', 'null')
        else:
            start_work = f"'{start_work}'"

        if end_of_work == None:
            end_of_work = kwargs.get('end_of_work', 'null')
        else:
            end_of_work = f"'{end_of_work}'"

        if day == None:
            day = kwargs.get('day', 'null')
        else:
            day = f"'{day}'"

        cur.execute(
            f"INSERT INTO schedule(data_początkowa,data_końcowa,początek_pracy,koniec_pracy,dzień_tygodnia)"
            f"VALUES({start_date},{end_date},{start_work},{end_of_work},'{day}')")
        conn.commit()

        cur.execute("SELECT * FROM schedule")
        rows = cur.fetchall()

        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Data początkowa: {row[1]}")
            print(f"Data końcowa: {row[2]}")

    except(Exception, pg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


insert_availability(start_date='2022-02-01',
                    end_date="2022-03-01",
                    start_work='08:00',
                    end_of_work='10:00',
                    day='Monday')

# def insert_availability(start_date, end_date, start_hour, end_hour):
#     """ insert a new vendor into the vendors table """
#     sql = """INSERT INTO vendors(vendor_name)
#              VALUES(%s) RETURNING vendor_id;"""
#     conn = None
#     vendor_id = None
#     try:
#         # read database configuration
#         params = config()
#         # connect to the PostgreSQL database
#         conn = pg2.connect(database='Work schedule', user='postgres', password='Damdamdam123!')
#         # create a new cursor
#         cur = conn.cursor()
#         # execute the INSERT statement
#         cur.execute(sql, (start_date, end_date, start_hour, end_hour,))
#         # get the generated id back
#         vendor_id = cur.fetchone()[0]
#         # commit the changes to the database
#         conn.commit()
#         # close communication with the database
#         cur.close()
#     except (Exception, pg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#
#     return vendor_id
#
#
# if __name__ == '__main__':
#     # insert one vendor
#     insert_availability("2022-02-01", "2022-02-10", "08:00", "10:00")
