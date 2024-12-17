from pymongo.errors import DuplicateKeyError
from db.database import Database
from datetime import datetime
import random
import timedelta
class Card:

    Database.initialize()
    collection = Database.get_db()["cards"]
    user_collection = Database.get_db()["users"] 
    
    def __init__(self, card_number, clcode, expiration_date, card_type, account_code):
        self.card_number = card_number
        self.clcode = clcode
        self.expiration_date = expiration_date
        self.card_type = card_type
        self.account_code = account_code
    
    @staticmethod
    def generate_card_number():
        """Genera un número de tarjeta aleatorio de 16 dígitos."""
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    @staticmethod
    def generate_expiration_date():
        """Genera una fecha de expiración a 3 años desde la fecha actual."""
        return datetime.now() + timedelta(days=3 * 365)

    @staticmethod
    def insert(clcode, card_type):
        user_data = Card.user_collection.find_one({"username": clcode})
        if not user_data:
            return None, "Usuario no encontrado."

        card_number = Card.generate_card_number()
        expiration_date = Card.generate_expiration_date()

        try:
            Card.collection.insert_one({
                "card_number": card_number,
                "clcode": clcode,
                "expiration_date": expiration_date,
                "card_type": card_type,
                "account_code": user_data.get("email", "")  
            })
            return card_number, "Tarjeta registrada exitosamente."
        except DuplicateKeyError:
            return None, "La tarjeta ya existe."

    @classmethod
    def find_by_card_number(cls, card_number):
        card_data = cls.collection.find_one({"card_number": card_number})
        if card_data:
            return cls(
                card_data["card_number"],
                card_data["clcode"],
                card_data["expiration_date"],
                card_data["card_type"],
                card_data["account_code"]
            )
        return None
    @classmethod
    def list_all(cls, user):
        collection = cls.get_collection()
        sellings = []
        for selling_data in collection.find({'user_name': user}):
            sellings.append(cls(selling_data['user_name'],selling_data['product_name'],selling_data['code'],selling_data['category'],selling_data['price'],selling_data['date']))
        return sellings

    @classmethod
    def list_by_customer(cls, clcode):
        collection = cls.get_collection()
        cards = []
        for card_data in collection.find({'clcode': clcode}):
            cards.append(cls(
                card_data['card_number'], card_data['clcode'], 
                datetime.strptime(card_data['expiration_date'], "%Y-%m-%d"),
                card_data['card_type'], card_data['account_code']
            ))
        return cards
    
    def deactivate(self):
        collection = self.get_collection()
        return collection.update_one({'card_number': self.card_number}, {'$set': {'status': 'inactive'}})

    def update_expiration_date(self, new_date):
        collection = self.get_collection()
        return collection.update_one({'card_number': self.card_number}, {'$set': {'expiration_date': new_date.strftime("%Y-%m-%d")}})
