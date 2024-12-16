from db.database import Database
import gui.login.login_bankui as baseui


class login(baseui.Login_bankUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":  
    try:  
        Database.initialize()   
        app = login()      
        app.run()
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        Database.close_connection()
