import tkinter as tk
from tkinter import messagebox
import random
import os

class JoKenPoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JoKenPo Elite - Python Edition")
        self.root.geometry("600x550")
        self.root.configure(bg="#0d0d12")
        
        self.user_score = 0
        self.cpu_score = 0
        
        # Colors
        self.bg_color = "#0d0d12"
        self.card_bg = "#1a1a24"
        self.accent_color = "#7000ff"
        self.text_color = "#ffffff"
        
        # Load Images
        try:
            self.rock_img = tk.PhotoImage(file="rock.png").subsample(4, 4)
            self.paper_img = tk.PhotoImage(file="paper.png").subsample(4, 4)
            self.scissors_img = tk.PhotoImage(file="scissors.png").subsample(4, 4)
        except Exception as e:
            print(f"Erro ao carregar imagens: {e}")
            # Fallback if images fail
            self.rock_img = None
            self.paper_img = None
            self.scissors_img = None

        self.setup_ui()

    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.bg_color, pady=20)
        header_frame.pack(fill="x")
        
        self.title_label = tk.Label(header_frame, text="JO KEN PO", font=("Outfit", 36, "bold"), 
                                   fg=self.accent_color, bg=self.bg_color)
        self.title_label.pack()
        
        # Score Board
        score_frame = tk.Frame(self.root, bg=self.bg_color)
        score_frame.pack(pady=20)
        
        self.user_score_label = tk.Label(score_frame, text=f"VOCÊ: {self.user_score}", 
                                        font=("Outfit", 18), fg="#00f2ff", bg=self.card_bg, 
                                        padx=20, pady=10, width=10)
        self.user_score_label.grid(row=0, column=0, padx=10)
        
        self.cpu_score_label = tk.Label(score_frame, text=f"CPU: {self.cpu_score}", 
                                       font=("Outfit", 18), fg="#ff00ea", bg=self.card_bg, 
                                       padx=20, pady=10, width=10)
        self.cpu_score_label.grid(row=0, column=1, padx=10)
        
        # Result Status
        self.status_label = tk.Label(self.root, text="Escolha sua jogada!", 
                                    font=("Outfit", 14), fg=self.text_color, bg=self.bg_color, pady=20)
        self.status_label.pack()
        
        # Battlefield (Images display)
        battle_frame = tk.Frame(self.root, bg=self.bg_color)
        battle_frame.pack(pady=10)
        
        self.user_move_label = tk.Label(battle_frame, bg=self.bg_color)
        self.user_move_label.grid(row=0, column=0, padx=40)
        
        tk.Label(battle_frame, text="VS", font=("Outfit", 24, "italic bold"), 
                 fg=self.accent_color, bg=self.bg_color).grid(row=0, column=1)
        
        self.cpu_move_label = tk.Label(battle_frame, bg=self.bg_color)
        self.cpu_move_label.grid(row=0, column=2, padx=40)
        
        # Choices Buttons
        choices_frame = tk.Frame(self.root, bg=self.bg_color)
        choices_frame.pack(pady=30)
        
        btn_config = {"bg": self.card_bg, "activebackground": "#2a2a3a", "bd": 0, "cursor": "hand2"}
        
        self.rock_btn = tk.Button(choices_frame, image=self.rock_img, text="PEDRA", compound="top",
                                 fg=self.text_color, font=("Outfit", 10, "bold"), 
                                 command=lambda: self.play("rock"), **btn_config)
        self.rock_btn.grid(row=0, column=0, padx=15)
        
        self.paper_btn = tk.Button(choices_frame, image=self.paper_img, text="PAPEL", compound="top",
                                  fg=self.text_color, font=("Outfit", 10, "bold"), 
                                  command=lambda: self.play("paper"), **btn_config)
        self.paper_btn.grid(row=0, column=1, padx=15)
        
        self.scissors_btn = tk.Button(choices_frame, image=self.scissors_img, text="TESOURA", compound="top",
                                     fg=self.text_color, font=("Outfit", 10, "bold"), 
                                     command=lambda: self.play("scissors"), **btn_config)
        self.scissors_btn.grid(row=0, column=2, padx=15)

    def play(self, user_choice):
        options = ["rock", "paper", "scissors"]
        cpu_choice = random.choice(options)
        
        # Update images
        imgs = {"rock": self.rock_img, "paper": self.paper_img, "scissors": self.scissors_img}
        self.user_move_label.config(image=imgs[user_choice])
        self.cpu_move_label.config(image=imgs[cpu_choice])
        
        # Logic
        if user_choice == cpu_choice:
            result = "EMPATE!"
            color = self.text_color
        elif (user_choice == "rock" and cpu_choice == "scissors") or \
             (user_choice == "paper" and cpu_choice == "rock") or \
             (user_choice == "scissors" and cpu_choice == "paper"):
            result = "VOCÊ VENCEU! 🎉"
            color = "#00ff88"
            self.user_score += 1
        else:
            result = "CPU VENCEU! 😢"
            color = "#ff3c3c"
            self.cpu_score += 1
            
        # Update labels
        self.status_label.config(text=result, fg=color)
        self.user_score_label.config(text=f"VOCÊ: {self.user_score}")
        self.cpu_score_label.config(text=f"CPU: {self.cpu_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = JoKenPoGUI(root)
    root.mainloop()
