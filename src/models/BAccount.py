
from db.database import Database
from functions.utils import decode_hash_function,encode_hash_function

class BAccount:
    Database.initialize()
    collection = Database.get_db()["bank_accounts"]

    def __init__(self, acctcode, username,face_id, clcode,  created_at, amount,state, mov_cont,acc_pass):
        self.acctcode = acctcode
        self.username=username
        self.face_id=face_id
        self.clcode = clcode
        self.created_at = created_at
        self.amount = amount
        self.state = state
        self.mov_cont = mov_cont
        self.acc_pass = acc_pass
        

    @staticmethod
    def insert( acctcode,username, face_id, clcode,created_at,amount, state, mov_cont,acc_pass):

        password = encode_hash_function(acc_pass)  
        return BAccount.collection.insert_one({
           
            'acctcode': acctcode,
            'face_id':face_id,
            'username': username,
            'clcode': clcode,
            'created_at': created_at,
            'amount': amount,
            'state': state,
            'mov_cont':mov_cont,
            'acc_pass': password
        })
        
    def add_card(self, card):
      
       pass

    def display_cards(self,acctcode):
   
        return [card.card_number for card in self.cards]
    
    def close_account(acctcode):
    
        return BAccount.collection.update_one(
            {'acctcode': acctcode},
            {'$set': {'state': 'inactive'}}
        )
        
    def find_baccount(cls,username):
        user_data =  cls.collection.find_one({'username': username})
        
        return cls(user_data['acctcode'], user_data['face_id'], user_data['clcode'], 
                   user_data['created_at'], user_data['amount'],user_data['state'],
                   user_data['mov_cont'],user_data['acc_pass']) if user_data else None

    @staticmethod
    def delete_account(acctcode):
        BAccount.card_collection.delete_many({'linked_acctcode': acctcode})  
        return BAccount.collection.delete_one({'acctcode': acctcode})

        