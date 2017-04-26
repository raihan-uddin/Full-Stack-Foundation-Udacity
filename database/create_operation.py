from database.database_setup import session, Restaurant, MenuItem

myFirstRestaurant = Restaurant(name="Pizza palace")
session.add(myFirstRestaurant)
session.commit()

print(session.query(Restaurant).all())

cheesepizza = MenuItem(name="Cheese Pizza", description="Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
print(session.query(MenuItem).all())