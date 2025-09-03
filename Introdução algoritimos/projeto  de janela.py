import customtkinter as ctk 

# configurar a aparecnia 

ctk. set_appearance_mode('dark')

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

# Verificar se o usuario é caio e senha 12345
    if usuario =='caio' or 'Caio' and senha == '12345':
        resultado_login.configure(text= 'Login permitido', text_color='green')
    else:
        resultado_login.configure(text= 'Login incorreto', text_color='red')


# criação da jenla principal 

app= ctk.CTk()
app.title('Sitema de login')
app.geometry('300x300')

#criação de campos
# Label
label_usuario =ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)
# Entry
campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

# Label
label_senha =ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)
# Entry
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

# Button
login = ctk.CTkButton(app, text= 'Login', command=validar_login)
login.pack(pady=10)
#campo feedback de login
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

# criação das funções 

# inicializar a aplicação 

app.mainloop()