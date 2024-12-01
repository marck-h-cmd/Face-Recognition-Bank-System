from pymongo.errors import DuplicateKeyError
from db.database import Database


class Customer:
    collection = Database.get_db()["customers"]

    def __init__(self, clcode, name, lastname, city, dni, phone, email):
        self.clcode = clcode
        self.name = name
        self.lastname = lastname
        self.city = city
        self.dni = dni
        self.phone = phone
        self.email = email

    @staticmethod
    def insert(clcode, name, lastname, city, dni, phone, email):

        return Customer.collection.insert_one({
            'clcode': clcode,
            'name': name,
            'lastname': lastname,
            'city': city,
            'dni': dni,
            'phone': phone,
            'email': email
        })

    @classmethod
    def find_by_code(cls, clcode):

        customer_data = cls.collection.find_one({'clcode': clcode})
        if customer_data:
            return cls(
                customer_data['clcode'],
                customer_data['name'],
                customer_data['lastname'],
                customer_data['city'],
                customer_data['dni'],
                customer_data['phone'],
                customer_data['email']
            )
        return None

    @classmethod
    def update(cls, clcode, **kwargs):

        update_data = {key: value for key, value in kwargs.items()
                       if key in ['name', 'lastname', 'city', 'dni', 'phone', 'email']}
        return cls.collection.update_one({'clcode': clcode}, {'$set': update_data})

    def delete(self):

        return self.collection.delete_one({'clcode': self.clcode})

    @classmethod
    def list_all(cls):

        customers = []
        for customer_data in cls.collection.find():
            customers.append(cls(
                customer_data['clcode'],
                customer_data['name'],
                customer_data['lastname'],
                customer_data['city'],
                customer_data['dni'],
                customer_data['phone'],
                customer_data['email']
            ))
        return customers
