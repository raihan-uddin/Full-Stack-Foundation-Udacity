from database.database_setup import session, Restaurant, MenuItem

firstResult = session.query(Restaurant).first()
# print(session.query(MenuItem).all())

items = session.query(MenuItem).all()
for item in items:
    print(item.name)