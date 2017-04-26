from database.database_setup import session, Restaurant, MenuItem

spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print(spinach.restaurant.name)
session.delete(spinach)
session.commit()
print(spinach.restaurant.name)