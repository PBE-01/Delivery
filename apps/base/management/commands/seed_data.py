import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

from django.contrib.auth import get_user_model
from apps.products.models import Category, Product
from apps.products.models import Order, OrderItem
from apps.products.chaoices import OrderStatus

User = get_user_model()


class Command(BaseCommand):
    help = "Test ma'lumotlarini database'ga qo'shadi"

    @transaction.atomic
    def handle(self, *args, **options):

        self.stdout.write(
            self.style.WARNING(
                "Database test ma'lumotlari bilan to'ldirilmoqda..."
            )
        )

        # =====================================================
        # USERS
        # =====================================================

        users = []

        for i in range(1, 11):

            user, created = User.objects.get_or_create(
                username=f"user{i}",
                defaults={
                    "email": f"user{i}@gmail.com",
                    "first_name": f"User{i}",
                    "last_name": "Test",
                    "phone": f"+9989012345{i:02d}",
                }
            )

            if created:
                user.set_password("12345678")
                user.save()

            users.append(user)

        self.stdout.write(
            self.style.SUCCESS(
                f"✓ {len(users)} ta user tayyor"
            )
        )

        # =====================================================
        # CATEGORIES
        # =====================================================

        category_names = [
            "Fast Food",
            "Pizza",
            "Burger",
            "Ichimliklar",
            "Shirinliklar",
        ]

        categories = {}

        for name in category_names:

            category, _ = Category.objects.get_or_create(
                name=name
            )

            categories[name] = category

        self.stdout.write(
            self.style.SUCCESS(
                f"✓ {len(categories)} ta category tayyor"
            )
        )

        # =====================================================
        # PRODUCTS
        # =====================================================

        products_data = [
            # Burger
            {
                "name": "Classic Burger",
                "description": "Mol go'shtidan tayyorlangan klassik burger",
                "price": Decimal("25000.00"),
                "category": "Burger",
            },
            {
                "name": "Cheese Burger",
                "description": "Pishloqli mazali burger",
                "price": Decimal("30000.00"),
                "category": "Burger",
            },
            {
                "name": "Double Burger",
                "description": "Ikki qavatli go'shtli burger",
                "price": Decimal("40000.00"),
                "category": "Burger",
            },
            {
                "name": "Chicken Burger",
                "description": "Tovuqli burger",
                "price": Decimal("28000.00"),
                "category": "Burger",
            },

            # Pizza
            {
                "name": "Margherita Pizza",
                "description": "Pomidor va pishloqli pizza",
                "price": Decimal("45000.00"),
                "category": "Pizza",
            },
            {
                "name": "Pepperoni Pizza",
                "description": "Pepperoni va pishloqli pizza",
                "price": Decimal("55000.00"),
                "category": "Pizza",
            },
            {
                "name": "Chicken Pizza",
                "description": "Tovuqli pizza",
                "price": Decimal("60000.00"),
                "category": "Pizza",
            },
            {
                "name": "Mushroom Pizza",
                "description": "Qo'ziqorinli pizza",
                "price": Decimal("50000.00"),
                "category": "Pizza",
            },

            # Fast Food
            {
                "name": "Lavash",
                "description": "Mol go'shtli lavash",
                "price": Decimal("30000.00"),
                "category": "Fast Food",
            },
            {
                "name": "Chicken Lavash",
                "description": "Tovuqli lavash",
                "price": Decimal("28000.00"),
                "category": "Fast Food",
            },
            {
                "name": "Hot Dog",
                "description": "Klassik hot dog",
                "price": Decimal("20000.00"),
                "category": "Fast Food",
            },
            {
                "name": "Doner",
                "description": "Mazali doner",
                "price": Decimal("32000.00"),
                "category": "Fast Food",
            },

            # Drinks
            {
                "name": "Coca Cola",
                "description": "Coca Cola 0.5L",
                "price": Decimal("10000.00"),
                "category": "Ichimliklar",
            },
            {
                "name": "Pepsi",
                "description": "Pepsi 0.5L",
                "price": Decimal("10000.00"),
                "category": "Ichimliklar",
            },
            {
                "name": "Fanta",
                "description": "Fanta 0.5L",
                "price": Decimal("10000.00"),
                "category": "Ichimliklar",
            },
            {
                "name": "Mineral Water",
                "description": "Mineral suv 0.5L",
                "price": Decimal("5000.00"),
                "category": "Ichimliklar",
            },

            # Desserts
            {
                "name": "Chocolate Cake",
                "description": "Shokoladli tort",
                "price": Decimal("35000.00"),
                "category": "Shirinliklar",
            },
            {
                "name": "Cheesecake",
                "description": "Klassik cheesecake",
                "price": Decimal("40000.00"),
                "category": "Shirinliklar",
            },
            {
                "name": "Donut",
                "description": "Shirin donut",
                "price": Decimal("12000.00"),
                "category": "Shirinliklar",
            },
            {
                "name": "Ice Cream",
                "description": "Muzqaymoq",
                "price": Decimal("15000.00"),
                "category": "Shirinliklar",
            },
        ]

        products = []

        for data in products_data:

            product, _ = Product.objects.get_or_create(
                name=data["name"],
                defaults={
                    "description": data["description"],
                    "price": data["price"],
                    "category": categories[data["category"]],
                }
            )

            products.append(product)

        self.stdout.write(
            self.style.SUCCESS(
                f"✓ {len(products)} ta product tayyor"
            )
        )

        # =====================================================
        # ORDERS
        # =====================================================

        # Har safar command ishlaganda yangi 20 ta order
        # yaratamiz.

        orders = []

        statuses = [
            OrderStatus.PENDING,
            OrderStatus.CONFIRMED,
            OrderStatus.DELIVERING,
            OrderStatus.COMPLETED,
        ]

        for _ in range(20):

            user = random.choice(users)

            order = Order.objects.create(
                user=user,
                status=random.choice(statuses)
            )

            orders.append(order)

        self.stdout.write(
            self.style.SUCCESS(
                f"✓ {len(orders)} ta order yaratildi"
            )
        )

        # =====================================================
        # ORDER ITEMS
        # =====================================================

        total_items = 0

        for order in orders:

            # Har bir orderga 2-4 ta har xil product
            item_count = random.randint(2, 4)

            selected_products = random.sample(
                products,
                item_count
            )

            for product in selected_products:

                quantity = random.randint(1, 5)

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price
                )

                total_items += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"✓ {total_items} ta order item yaratildi"
            )
        )

        # =====================================================
        # TEST
        # =====================================================

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "======================================"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "DATABASE MUVAFFAQIYATLI TO'LDIRILDI"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "======================================"
            )
        )

        self.stdout.write(
            f"Users:      {User.objects.count()}"
        )

        self.stdout.write(
            f"Categories: {Category.objects.count()}"
        )

        self.stdout.write(
            f"Products:   {Product.objects.count()}"
        )

        self.stdout.write(
            f"Orders:     {Order.objects.count()}"
        )

        self.stdout.write(
            f"OrderItems: {OrderItem.objects.count()}"
        )

        # Birinchi orderning totalini ko'rsatamiz
        if orders:
            first_order = orders[0]

            self.stdout.write(
                self.style.SUCCESS(
                    f"Order #{first_order.id} total: "
                    f"{first_order.total_price}"
                )
            )