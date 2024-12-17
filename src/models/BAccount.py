
from db.database import Database
from functions.utils import decode_hash_function,encode_hash_function
from models import Transaction
import datetime

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
    
    @classmethod
    def retirar_dinero(self, cantidad):
        #Debe ser implementada en la gui estas verificaciones
        #if cantidad <= 0:
        #    raise ValueError("La cantidad a retirar debe ser mayor a 0")
        #if cantidad > self.amount:
        #    raise ValueError("Saldo insuficiente")
        nuevo_saldo = self.amount - cantidad
        BAccount.collection.update_one({'acctcode': self.acctcode}, {'$set': {'amount': nuevo_saldo}})
        # Registro de la transacción
        Transaction.insert(
            transaction_id=f"TR-{self.mov_cont + 1}", 
            from_account=self.acctcode, 
            to_account=None, 
            amount=cantidad, 
            date=datetime.now(), 
            trans_type='retiro'
        )
        return nuevo_saldo
    @classmethod
    def transferir_dinero(self, destinatario_acctcode, cantidad):
        #Debe ser implementada en la gui estas verificaciones
        #if cantidad <= 0:
        #    raise ValueError("La cantidad a transferir debe ser mayor a 0")
        #if cantidad > self.amount:
        #    raise ValueError("Saldo insuficiente")
        nuevo_saldo_origen = self.amount - cantidad
        BAccount.collection.update_one({'acctcode': self.acctcode}, {'$set': {'amount': nuevo_saldo_origen}})
        
        # Registro de la transacción en la cuenta de origen
        Transaction.insert(
            transaction_id=f"TR-{self.mov_cont + 1}", 
            from_account=self.acctcode, 
            to_account=destinatario_acctcode, 
            amount=cantidad, 
            date=datetime.now(), 
            trans_type='transferencia'
        )

        # Registro de la transacción en la cuenta de destino
        destinatario = BAccount.find_baccount(destinatario_acctcode)
        if destinatario:
            nuevo_saldo_destino = destinatario.amount + cantidad
            BAccount.collection.update_one({'acctcode': destinatario.acctcode}, {'$set': {'amount': nuevo_saldo_destino}})
            Transaction.insert(
                transaction_id=f"TR-{destinatario.mov_cont + 1}", 
                from_account=None, 
                to_account=destinatario_acctcode, 
                amount=cantidad, 
                date=datetime.now(), 
                trans_type='transferencia'
            )
    @classmethod
    def actualizar_cuenta(self, **kwargs):
        update_data = {key: value for key, value in kwargs.items()
                       if key in ['username', 'face_id', 'clcode', 'created_at', 'amount', 'state', 'mov_cont']}
        return BAccount.collection.update_one({'acctcode': self.acctcode}, {'$set': update_data})

    def obtener_saldo(self):
        return self.amount

    @classmethod
    def listar_cuentas(cls):
        cuentas = []
        for cuenta_data in cls.collection.find():
            cuentas.append(cls(
                cuenta_data['acctcode'], cuenta_data['username'], cuenta_data['face_id'],
                cuenta_data['clcode'], cuenta_data['created_at'], cuenta_data['amount'],
                cuenta_data['state'], cuenta_data['mov_cont'], cuenta_data['acc_pass']
            ))
        return cuentas    

        