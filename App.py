import random
import string
import customtkinter as ctk

# App.py
import tkinter.messagebox as msg

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Função para gerar senha
def gerar_senha():
    length = int(slider_length.get())
    sets = []
    if var_lower.get():
        sets.append(string.ascii_lowercase)
    if var_upper.get():
        sets.append(string.ascii_uppercase)
    if var_digits.get():
        sets.append(string.digits)
    if var_symbols.get():
        # remover espaços problemáticos se necessário
        symbols = "!@#$%^&*()-_=+[]{};:,.<>/?\\|"
        sets.append(symbols)

    if not sets:
        msg.showwarning("Aviso", "Selecione ao menos um tipo de caractere.")
        return

    # Garantir que haja pelo menos um caractere de cada conjunto selecionado
    senha_chars = [random.choice(s) for s in sets]

    all_chars = "".join(sets)
    remaining = length - len(senha_chars)
    if remaining > 0:
        senha_chars += [random.choice(all_chars) for _ in range(remaining)]

    random.shuffle(senha_chars)
    senha = "".join(senha_chars)

    entry_senha.configure(state="normal")
    entry_var.set(senha)
    entry_senha.configure(state="readonly")

def copiar_senha():
    pwd = entry_var.get()
    if not pwd:
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    root.update()  # garantir que o clipboard seja atualizado
    msg.showinfo("Copiado", "Senha copiada para a área de transferência.")

# Janela principal
root = ctk.CTk()
root.title("Gerador de Senhas")
root.geometry("560x360")
root.resizable(False, False)

# Frame principal
frame = ctk.CTkFrame(root, corner_radius=12)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Título
titulo_lbl = ctk.CTkLabel(frame, text="Gerador de Senhas", font=ctk.CTkFont(size=20, weight="bold"))
titulo_lbl.grid(row=0, column=0, columnspan=3, pady=(10, 15))

# Opções de caracteres
var_upper = ctk.BooleanVar(value=True)
var_lower = ctk.BooleanVar(value=True)
var_digits = ctk.BooleanVar(value=True)
var_symbols = ctk.BooleanVar(value=False)

chk_upper = ctk.CTkCheckBox(frame, text="Letras Maiúsculas", variable=var_upper)
chk_lower = ctk.CTkCheckBox(frame, text="Letras Minúsculas", variable=var_lower)
chk_digits = ctk.CTkCheckBox(frame, text="Números (0-9)", variable=var_digits)
chk_symbols = ctk.CTkCheckBox(frame, text="Símbolos (!@#...)", variable=var_symbols)

chk_upper.grid(row=1, column=0, sticky="w", padx=20, pady=5)
chk_lower.grid(row=1, column=1, sticky="w", padx=20, pady=5)
chk_digits.grid(row=2, column=0, sticky="w", padx=20, pady=5)
chk_symbols.grid(row=2, column=1, sticky="w", padx=20, pady=5)

# Slider de tamanho
comprimento_lbl = ctk.CTkLabel(frame, text="Tamanho da senha:")
comprimento_lbl.grid(row=3, column=0, pady=(15, 5), padx=20, sticky="w")

slider_length = ctk.CTkSlider(frame, from_=4, to=64, number_of_steps=60, command=lambda v: comprimento_lbl_val.configure(text=str(int(float(v)))))
slider_length.set(12)
slider_length.grid(row=3, column=1, columnspan=2, sticky="ew", padx=(0,20), pady=(15,5))

comprimento_lbl_val = ctk.CTkLabel(frame, text=str(int(slider_length.get())))
comprimento_lbl_val.grid(row=3, column=2, padx=10, sticky="w")

# Campo de senha gerada
entry_var = ctk.StringVar()
entry_senha = ctk.CTkEntry(frame, textvariable=entry_var, width=360, state="readonly", font=ctk.CTkFont(size=14))
entry_senha.grid(row=4, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="ew")

# Botões
btn_gerar = ctk.CTkButton(frame, text="Gerar Senha", command=gerar_senha, width=180, fg_color="#1f6feb")
btn_copiar = ctk.CTkButton(frame, text="Copiar", command=copiar_senha, width=120)

btn_gerar.grid(row=5, column=0, columnspan=2, padx=(20,10), pady=10, sticky="ew")
btn_copiar.grid(row=5, column=2, padx=(0,20), pady=10, sticky="ew")

# Rodapé com autor
autor_lbl = ctk.CTkLabel(frame, text="Autor: Willian Durães", font=ctk.CTkFont(size=12), anchor="w")
autor_lbl.grid(row=6, column=0, columnspan=3, sticky="w", padx=20, pady=(10,5))

# Ajustes de grid para responsividade simples
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=0)

root.mainloop()