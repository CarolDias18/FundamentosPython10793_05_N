import customtkinter as ctk
import subprocess
import os

# Dicionário com os dados de cada seção e subseções
SECTIONS_DATA = {
    "Introdução ao Python": [
        {
            "title": "O que é Python?",
            "content": "Python é uma linguagem simples e poderosa usada em diversas áreas.",
            "example": "print('Bem-vindo ao Python!')",
            "challenge": "Crie um programa que exiba 'Bem-vindo ao Python!'"
        },
        # ... (demais subseções)
    ],
    "Variáveis e Tipos de Dados": [
        {
            "title": "O que são variáveis?",
            "content": (
                "Variáveis armazenam informações em Python. Você pode criar quantas variáveis "
                "precisar, dando nomes que façam sentido."
            ),
            "example": "x = 10\nprint(x)",
            "challenge": "Crie variáveis para guardar seu nome e idade e imprima-os."
        },
        # ... (demais subseções)
    ],
    # ... (demais seções)
}


class PythonTutorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprender Python - Tutor para Crianças")

        # Remove o tamanho fixo para deixar a janela livre para redimensionamento
        # self.root.geometry("1200x900")

        # Deixa a janela redimensionável (padrão é True, mas explicitamos)
        self.root.resizable(True, True)

        # Configura “peso” nas colunas e linhas da janela principal
        # para que os widgets possam expandir e ocupar o espaço disponível
        self.root.grid_rowconfigure(0, weight=1)   # Área principal
        self.root.grid_columnconfigure(0, weight=1)

        # Ajustes de tema do CustomTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_main_menu()

    def create_main_menu(self):
        # Limpa a janela
        self.clear_window()

        # Cria um frame que ocupará toda a área (row=0, col=0)
        main_frame = ctk.CTkFrame(self.root)
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Configura o “peso” para o layout dentro do main_frame
        main_frame.grid_rowconfigure(0, weight=0)  # Título
        main_frame.grid_rowconfigure(1, weight=1)  # Botões de seção
        main_frame.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            main_frame, text="Aprender Python", font=("Arial", 30, "bold")
        )
        title_label.grid(row=0, column=0, pady=20, sticky="n")

        # Frame para botões de seção
        buttons_frame = ctk.CTkFrame(main_frame)
        buttons_frame.grid(row=1, column=0, sticky="nsew")

        # Faz o frame de botões expandir verticalmente
        buttons_frame.grid_rowconfigure("all", weight=1)
        buttons_frame.grid_columnconfigure(0, weight=1)

        row_index = 0
        for section_name in SECTIONS_DATA.keys():
            button = ctk.CTkButton(
                buttons_frame,
                text=section_name,
                command=lambda sn=section_name: self.create_section_window(sn),
                font=("Arial", 20),
                height=50
            )
            button.grid(row=row_index, column=0, pady=10, padx=20, sticky="ew")
            row_index += 1

    def create_section_window(self, section_name):
        self.clear_window()

        # Frame principal da seção
        section_frame = ctk.CTkFrame(self.root)
        section_frame.grid(row=0, column=0, sticky="nsew")

        # Configura expansões dentro de section_frame
        section_frame.grid_rowconfigure(1, weight=1)  # Lista de subseções
        section_frame.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            section_frame, text=section_name, font=("Arial", 30, "bold")
        )
        title_label.grid(row=0, column=0, pady=20, sticky="n")

        # Frame para os botões de subseção
        subsections_frame = ctk.CTkFrame(section_frame)
        subsections_frame.grid(row=1, column=0, sticky="nsew", padx=20)

        subsections_frame.grid_rowconfigure("all", weight=1)
        subsections_frame.grid_columnconfigure(0, weight=1)

        subsections = SECTIONS_DATA.get(section_name, [])
        row_index = 0
        for subsection in subsections:
            button = ctk.CTkButton(
                subsections_frame,
                text=subsection["title"],
                command=lambda sb=subsection: self.display_content(section_name, sb),
                font=("Arial", 20),
                height=50,
            )
            button.grid(row=row_index, column=0, pady=10, sticky="ew")
            row_index += 1

        # Botão de voltar ao início
        back_button_main = ctk.CTkButton(
            section_frame,
            text="Página Inicial",
            command=self.create_main_menu,
            font=("Arial", 20),
            height=50,
            width=200
        )
        back_button_main.grid(row=2, column=0, pady=20)

    def display_content(self, section_name, subsection):
        self.clear_window()

        # Frame principal para o conteúdo
        content_frame = ctk.CTkFrame(self.root)
        content_frame.grid(row=0, column=0, sticky="nsew")

        # Define pesos para organização vertical:
        #   0: título e textos
        #   1: editor + saída (lado a lado)
        #   2: frame de navegação
        content_frame.grid_rowconfigure(0, weight=0)
        content_frame.grid_rowconfigure(1, weight=1)
        content_frame.grid_rowconfigure(2, weight=0)
        content_frame.grid_columnconfigure(0, weight=1)

        # ---------- Título e Textos ----------
        top_frame = ctk.CTkFrame(content_frame)
        top_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        title_label = ctk.CTkLabel(
            top_frame, text=subsection["title"], font=("Arial", 30, "bold")
        )
        title_label.pack(pady=5)

        content_label = ctk.CTkTextbox(
            top_frame, wrap="word", font=("Courier", 14), height=150
        )
        content_label.insert("1.0", subsection["content"])
        content_label.configure(state="disabled")
        content_label.pack(fill="x", pady=5)

        example_label = ctk.CTkTextbox(
            top_frame, wrap="word", font=("Courier", 14), height=80, fg_color="#1a3f3f"
        )
        example_label.insert("1.0", f"Exemplo:\n{subsection['example']}")
        example_label.configure(state="disabled")
        example_label.pack(fill="x", pady=5)

        challenge_label = ctk.CTkTextbox(
            top_frame, wrap="word", font=("Courier", 14), height=80, fg_color="#3f1a1a"
        )
        challenge_label.insert("1.0", f"Desafio:\n{subsection['challenge']}")
        challenge_label.configure(state="disabled")
        challenge_label.pack(fill="x", pady=5)

        # ---------- Frame do Editor + Saída (lado a lado) ----------
        middle_frame = ctk.CTkFrame(content_frame)
        middle_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Para “dividir” horizontalmente, configuramos 2 colunas
        middle_frame.grid_rowconfigure(0, weight=1)
        middle_frame.grid_columnconfigure(0, weight=1)  # editor
        middle_frame.grid_columnconfigure(1, weight=1)  # saída

        # ----- Editor (col=0) -----
        editor_frame = ctk.CTkFrame(middle_frame)
        editor_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        editor_frame.grid_rowconfigure(1, weight=1)  # caixa de texto cresce
        editor_frame.grid_columnconfigure(0, weight=1)

        editor_label = ctk.CTkLabel(
            editor_frame,
            text="Escreva e Teste o Seu Código",
            font=("Arial", 20, "bold")
        )
        editor_label.grid(row=0, column=0, pady=5, sticky="n")

        self.code_text = ctk.CTkTextbox(
            editor_frame, wrap="word", font=("Courier", 14)
        )
        self.code_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        run_button = ctk.CTkButton(
            editor_frame, text="Executar Código", command=self.run_code, font=("Arial", 15)
        )
        run_button.grid(row=2, column=0, pady=5, sticky="n")

        # ----- Saída (col=1) -----
        output_frame = ctk.CTkFrame(middle_frame)
        output_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        output_frame.grid_rowconfigure(1, weight=1)
        output_frame.grid_columnconfigure(0, weight=1)

        output_label = ctk.CTkLabel(
            output_frame,
            text="Saída do Código",
            font=("Arial", 20, "bold")
        )
        output_label.grid(row=0, column=0, pady=5, sticky="n")

        self.output_text = ctk.CTkTextbox(
            output_frame, wrap="word", font=("Courier", 14), fg_color="#262335"
        )
        self.output_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # ---------- Frame de Navegação ----------
        nav_frame = ctk.CTkFrame(content_frame)
        nav_frame.grid(row=2, column=0, pady=20, sticky="ew")

        back_button_subsections = ctk.CTkButton(
            nav_frame,
            text="Voltar",
            command=lambda: self.create_section_window(section_name),
            font=("Arial", 20),
            height=50,
            width=150
        )
        back_button_subsections.pack(side="left", padx=20)

        back_button_main = ctk.CTkButton(
            nav_frame,
            text="Main",
            command=self.create_main_menu,
            font=("Arial", 20),
            height=50,
            width=150
        )
        back_button_main.pack(side="left", padx=20)

    def run_code(self):
        code = self.code_text.get("1.0", "end-1c")
        temp_file = "temp_code.py"

        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(code)

        try:
            result = subprocess.run(
                ["python", temp_file],
                capture_output=True,
                text=True
            )
            output = result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            output = str(e)

        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", output)
        self.output_text.configure(state="disabled")

        os.remove(temp_file)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = ctk.CTk()
    app = PythonTutorApp(root)
    root.mainloop()
