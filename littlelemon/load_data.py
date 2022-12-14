data = [
    {
        'name': 'Greek salad',
        'price': '12',
        'description': 'Our famous Greek salad of crispy lettuce, peppers, olives, and our Chicago-style feta cheese. Garnished with crispy onion and salty capers.',
    },
    {
        'name': 'Grilled fish',
        'price': '9',
        'description': 'The fish is swiftly grilled over medium- or high-heat coals or over medium- or high-heat gas grill burners. Thinner fillets and steaks are grilled over direct fire.',
    },
    {
        'name': 'Bruschetta',
        'price': '11',
        'description': 'An Italian antipasto called bruschetta is made of grilled bread that has been smeared with garlic and seasoned with salt and olive oil. Toppings of tomato, veggies, beans, cured pork, or cheese are examples of variations. In Italy, a brustolina grill is frequently used to create bruschetta.',
    },
    {
        'name': 'Lemon dessert',
        'price': '7',
        'description': 'This cake is adored not only for its flavor but also for its texture and simplicity. A base of creamed butter and sugar, eggs, lemon, milk, and flour are among the most basic ingredients. We omitted the brown sugar and substituted extra granulated sugar instead.',
    },
]

from restaurant.models import Menu

Menu.objects.all().delete()

for menu in data:
    Menu(**menu).save()