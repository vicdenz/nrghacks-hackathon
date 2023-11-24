from django.contrib.auth.models import User
from dashboard.models import StockTransaction

from faker import Faker
from django.utils import timezone
import random
from .utils import round_value

fake = Faker()

def generate_stock_data(user, num_entries=10):
    for _ in range(num_entries):
        price = round_value(random.uniform(1, 1000), 2)
        quantity = random.randint(1, 100)
        fees = round_value(price * (random.randint(1, 10) / 10000), 2)
        total_cost = round_value(price * quantity - fees, 2)

        StockTransaction.objects.create(
            user=user,
            order_id=random.randint(1, 10000),
            timestamp=timezone.make_aware(fake.date_time_between(start_date="-30d", end_date="now")),
            symbol=fake.lexify(text="????").upper(),
            action=random.choice(['buy', 'sell']),
            price=price,
            quantity=quantity,
            fees=fees,
            total_cost=total_cost,
            outcome=round_value(random.uniform(-1, 1) * total_cost, 2),
        )