from pymongo.errors import DuplicateKeyError
from db.database import Database
from datetime import datetime

class Card:
    @staticmethod
    def get_collection():
        return Database.get_db()["cards"]
    
    def __init__(self, card_number,clcode, expiration_date, card_type, account_code):
        self.card_number = card_number
        self.clcode = clcode
        self.expiration_date = expiration_date
        self.card_type = card_type
        self. account_code =  account_code
    
    @staticmethod
    def insert(card_number, clcode, expiration_date, card_type, account_code):
        collection = Card.get_collection()
        try:  
             return collection.insert_one({
                'card_number': card_number,
                'clcode': clcode,
                'expiration_date': expiration_date.strftime("%Y-%m-%d"),
                'card_type': card_type,
                'account_code': account_code
            })
        except DuplicateKeyError:
            print("Error: Duplicate entry.")
            return None

    @classmethod
    def find_by_card_number(cls, card_number):
        collection = cls.get_collection()
        card_data = collection.find_one({'card_number': card_number})
        return cls(
            card_data['card_number'],  card_data['clcode'], 
            datetime.strptime(card_data['expiration_date'], "%Y-%m-%d"),
            card_data['card_type'], card_data['account_code']
        ) if card_data else None

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
