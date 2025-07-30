import customtkinter as ctk
import customtkinter


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x300")
app.title("лаунчер гри")
def  run_game():
    name = name_imyinput.get()
    host = name_adresinput.get()
    port = name_portinput.get()
    if name and host and part:
        app.destray()
        star_game(imyinput, adresinput, portinput)





name_lbl = ctk.CTkLabel(app, text= "Імя гравя")
name_lbl.pack(pady=7)

name_imyinput = ctk.CTkEntry(app)
name_imyinput.pack()

name_adres = ctk.CTkLabel(app, text= "Адрес сервера")
name_adres.pack(pady=7)
host_entry.insert(0, "2,tcp.eu.ngrok.io")
host_entry.pack()

name_adresinput = ctk.CTkEntry(app)
name_adresinput.pack()

name_port = ctk.CTkLabel(app, text= "Порт")
name_port.pack(pady=7)

name_portinput = ctk.CTkEntry(app)
name_portinput.pack()

button = customtkinter.CTkButton(master=app, text="запустити гру")
button.pack(pady=13)

app.mainloop()