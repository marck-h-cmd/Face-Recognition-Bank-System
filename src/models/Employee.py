from pymongo.errors import DuplicateKeyError
from db.database import Database


class Employee:
    Database.initialize()
    collection = Database.get_db()["employees"]

    def __init__(self, emplcode, name,lastname,city,address, username, password):
        self.emplcode = emplcode
        self.name = name
        self.lastname = lastname
        self.city = city
        self.address = address
        self.username= username
        self.password=password

    @staticmethod
    def insert(code, name, lastname,city,address, username, password):
        return Employee.collection.insert_one({
            'emplcode': code,
            'name': name,
            'lastname':lastname,
            'city': city,
            'address': address,
            'username':username,
            'password':password
        })

    @classmethod
    def find_by_code(cls, code):
        empl_data = cls.collection.find_one({'code': code})
        return cls(empl_data['emplcode'], empl_data['name'],  empl_data['lastname'],empl_data['city'], empl_data['address'],empl_data['username',empl_data['password']]) if empl_data else None

    
    @classmethod
    def update(cls, code, **kwargs):
        update_data = {key: value for key, value in kwargs.items() if key in ['emplcode','name','lastname','city', 'address', 'username','password'] }
        return cls.collection.update_one({'code': code}, {'$set': update_data})


    def delete(self):
        return self.collection.delete_one({'code': self.emplcode})

  
    @classmethod
    def list_all(cls):
        employees = []
        for empl_data in cls.collection.find():
            employees.append(cls(empl_data['emplcode'], empl_data['name'],  empl_data['lastname'],empl_data['city'], empl_data['address'],empl_data['username',empl_data['password']]))
        return employees
