from pypika import Query, Table, Field
from connection import cursor

q = Query.from_('passwords').select('hash')

def get_all_hashs():
  q = Query.from_('passwords').select('hash')
  cursor.execute(str(q))
  result = cursor.fetchall()
  [result] = result
  result = list(result)
  return result


print(get_all_hashs())