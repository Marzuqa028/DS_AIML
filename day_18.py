import sqlite3
import pandas as pd
conn = sqlite3.connect("internship.db")
df = pd.read_sql_query("SELECT interns.name, mentors.mentor_name \
                       FROM interns \
                       INNER JOIN mentors \
                       ON interns.track = mentors.track;", conn)
print(df)