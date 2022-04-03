import sqlite3
import json

cnt = sqlite3.connect('student.db')
cursr = cnt.cursor()

# cursr.execute("INSERT INTO persons VALUES (?,?)",('Agg',None))

bw = cursr.execute("SELECT motto FROM persons WHERE name = 'Agg'").fetchone()[0]
print(type(bw))

# cursr.execute("CREATE TABLE persons (name text,motto null)")
cnt.commit()
cnt.close()