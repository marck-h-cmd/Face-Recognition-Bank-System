#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import bank_cardui as baseui


class Bank_card(baseui.Bank_cardUI):
  def __init__(self, master=None):
        super().__init__(master)
        self.generate_button.configure(command=self.generate_card)

    def generate_card(self):
        """Maneja la generación de tarjetas desde la interfaz."""
        clcode = self.clcode_entry.get()  
        card_type = self.card_type_combobox.get()  

        if not clcode or not card_type:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        card_number, message = Card.insert(clcode, card_type)

        if card_number:
            self.card_number_label.configure(text=f"Tarjeta: {card_number}")
            self.expiration_label.configure(text="Fecha de expiración: 3 años desde hoy")
        else:
            messagebox.showerror("Error", message)

if __name__ == "__main__":
    app = Bank_card()
    app.run()
