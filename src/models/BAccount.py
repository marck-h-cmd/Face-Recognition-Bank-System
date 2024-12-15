
from db.database import Database


class BAccount:
    collection = Database.get_db()["bank_accounts"]

    def __init__(self, acctcode,face_id, clcode,  created_at, amount,state, mov_cont,acc_pass):
        self.acctcode = acctcode
        self.face_id=face_id
        self.clcode = clcode
        self.created_at = created_at
        self.amount = amount
        self.state = state
        self.mov_cont = mov_cont
        self.acc_pass = acc_pass
        

    @staticmethod
    def insert( acctcode, face_id, clcode,created_at,amount, state, mov_cont,acc_pass):

        return BAccount.collection.insert_one({
           
            'acctcode': acctcode,
            'face_id':face_id,
            'clcode': clcode,
            'created_at': created_at,
            'amount': amount,
            'state': state,
            'mov_cont':mov_cont,
            'acc_pass':acc_pass
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

    @staticmethod
    def delete_account(acctcode):
        BAccount.card_collection.delete_many({'linked_acctcode': acctcode})  
        return BAccount.collection.delete_one({'acctcode': acctcode})

        