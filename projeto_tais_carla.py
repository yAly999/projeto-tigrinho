<<<<<<< HEAD
import tkinter as tk
import random

#config

simbolos = ["🍆", "🥒", "🪵", "🐥", "📏"]
saldo = 20.0
custo_giro = 2

#função girar():

def girar():
    global saldo

    if saldo < custo_giro:
        resultado_label.config(text="Saldo insuficiente!", fg="red")
        return

    saldo -= custo_giro

    # Sorteio
    resultado = [random.choice(simbolos) for _ in range(3)]

    # Atualiza slots
    slot1.config(text=resultado[0])
    slot2.config(text=resultado[1])
    slot3.config(text=resultado[2])

    # Verifica vitória
    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20
        saldo += premio
        resultado_label.config(text=f"🎉 JACKPOT! +R$ {premio}", fg="green")
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        premio = 2.5
        saldo += premio
        resultado_label.config(text=f"✨ Quase! +R$ {premio}", fg="blue")
    else:
        resultado_label.config(text="😕 Tente novamente...", fg="black")

    # Atualiza saldo
    saldo_label.config(text=f"Saldo: R$ {saldo:.2f}")

# ---------------- INTERFACE ----------------
janela = tk.Tk()
janela.title("🎰 Caça-Níquel")
janela.geometry("350x300")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="🎰 Caça-Níquel", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

# Slots
frame_slots = tk.Frame(janela)
frame_slots.pack(pady=10)

slot1 = tk.Label(frame_slots, text="❔", font=("Arial", 30))
slot1.pack(side="left", padx=10)

slot2 = tk.Label(frame_slots, text="❔", font=("Arial", 30))
slot2.pack(side="left", padx=10)

slot3 = tk.Label(frame_slots, text="❔", font=("Arial", 30))
slot3.pack(side="left", padx=10)

# Resultado
resultado_label = tk.Label(janela, text="Clique em girar!", font=("Arial", 12))
resultado_label.pack(pady=10)

# Saldo
saldo_label = tk.Label(janela, text=f"Saldo: R$ {saldo:.2f}", font=("Arial", 12, "bold"))
saldo_label.pack(pady=5)

# Botão
botao_girar = tk.Button(janela, text="🎲 Girar", font=("Arial", 12), command=girar)
botao_girar.pack(pady=10)

# ---------------- RODAR ----------------
=======
import tkinter as tk
import random

#config

simbolos = ["🍆", "🥒", "🪵", "🐥", "📏"]
saldo = 20.0
custo_giro = 2

#função girar():

def girar():
    global saldo

    if saldo < custo_giro:
        resultado_label.config(text="Saldo insuficiente!", fg="red")
        return

    saldo -= custo_giro

    # Sorteio
    resultado = [random.choice(simbolos) for _ in range(3)]

    # Atualiza slots
    slot1.config(text=resultado[0])
    slot2.config(text=resultado[1])
    slot3.config(text=resultado[2])

    # Verifica vitória
    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20
        saldo += premio
        resultado_label.config(text=f"🎉 JACKPOT! +R$ {premio}", fg="green")
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        premio = 2.5
        saldo += premio
        resultado_label.config(text=f"✨ Quase! +R$ {premio}", fg="blue")
    else:
        resultado_label.config(text="😕 Tente novamente...", fg="black")

    # Atualiza saldo
    saldo_label.config(text=f"Saldo: R$ {saldo:.2f}")

# ---------------- INTERFACE ----------------
janela = tk.Tk()
janela.title("🎰 Caça-Níquel")
janela.geometry("350x300")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="🎰 Caça-Níquel", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

# Slots
frame_slots = tk.Frame(janela)
frame_slots.pack(pady=10)

slot1 = tk.Label(frame_slots, text="❔", font=("Arial", 30))
slot1.pack(side="left", padx=10)

slot2 = tk.Label(frame_slots, text="❔", font=("Arial", 30))
slot2.pack(side="left", padx=10)

slot3 = tk.Label(frame_slots, text="❔", font=("Arial", 30))
slot3.pack(side="left", padx=10)

# Resultado
resultado_label = tk.Label(janela, text="Clique em girar!", font=("Arial", 12))
resultado_label.pack(pady=10)

# Saldo
saldo_label = tk.Label(janela, text=f"Saldo: R$ {saldo:.2f}", font=("Arial", 12, "bold"))
saldo_label.pack(pady=5)

# Botão
botao_girar = tk.Button(janela, text="🎲 Girar", font=("Arial", 12), command=girar)
botao_girar.pack(pady=10)

# ---------------- RODAR ----------------
>>>>>>> 7ffe1764cb2e13331d2974a4632bb4b889971ce6
janela.mainloop()