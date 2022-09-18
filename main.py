import psycopg2 as pg2
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

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
            f"INSERT INTO availability(date_1,date_2,start_work,end_work,day_of_the_week)"
            f"VALUES({start_date},{end_date},{start_work},{end_of_work},'{day}')")
        conn.commit()

        cur.execute("SELECT * FROM availability")
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


def date_from():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()


def date_to():
    def print_sel():
        print(cal.get_date())
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)
    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)
    ttk.Button(top, text="ok", command=print_sel).pack()

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Date from', command=date_from).grid(column=0, row=0)
ttk.Button(root, text='Date to', command=date_to).grid(column=0, row=1)

root.mainloop()




# insert_availability(start_date='2022-02-01',
#                     end_date="2022-03-01",
#                     start_work='08:00',
#                     end_of_work='10:00',
#                     day='Monday')

