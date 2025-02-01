import sys
import subprocess
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QScrollArea, QHBoxLayout, QSplitter, QListWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Dicionário com os dados de cada seção e suas subseções
SECTIONS_DATA = {
    "Introdução ao Python": [
        {
            "title": "O que é Python?",
            "content": "Python é uma linguagem simples e poderosa usada em diversas áreas.",
            "example": "print('Bem-vindo ao Python!')",
            "example_explanation": (
                "1. A função `print()` exibe mensagens no terminal.\n"
                "2. O texto entre aspas simples ou duplas é uma string.\n"
                "3. Este código imprime 'Bem-vindo ao Python!' no ecrã."
            ),
            "challenge": "Crie um programa que exiba 'Bem-vindo ao Python!'",
            "answer": "print('Bem-vindo ao Python!')"
        },
        {
            "title": "História do Python",
            "content": (
                "Python foi criado por Guido van Rossum em 1991.\n\n"
                "Desde então, diversas versões foram lançadas, "
                "adicionando melhorias e novas funcionalidades."
            ),
            "example": "",
            "example_explanation": "",
            "challenge": "Pesquise sobre as versões do Python e escreva um breve resumo.",
            "answer": "Versões do Python: 1.0, 2.x, 3.x, etc."
        }
    ],
    "Variáveis e Tipos de Dados": [
        {
            "title": "O que são variáveis?",
            "content": (
                "Variáveis armazenam informações em Python. Você pode criar quantas variáveis "
                "precisar, dando nomes que façam sentido."
            ),
            "example": "x = 10\nprint(x)",
            "example_explanation": (
                "1. `x = 10` cria uma variável chamada `x` e atribui o valor 10 a ela.\n"
                "2. `print(x)` exibe o valor armazenado na variável `x`."
            ),
            "challenge": "Crie variáveis para guardar seu nome e idade e imprima-os.",
            "answer": "nome = 'João'\nidade = 30\nprint(nome, idade)"
        },
        {
            "title": "Tipos de Dados",
            "content": (
                "Os principais tipos são:\n"
                "- int (inteiro)\n"
                "- float (decimal)\n"
                "- str (texto)\n"
                "- bool (booleano)."
            ),
            "example": "x = 3.14\nprint(type(x))",
            "example_explanation": (
                "1. `x = 3.14` cria uma variável do tipo `float`.\n"
                "2. `type(x)` retorna o tipo da variável, neste caso, `<class 'float'>`.\n"
                "3. O código exibe `<class 'float'>` no terminal."
            ),
            "challenge": "Descubra os tipos de dados em: 42, 3.14, 'Python' e True.",
            "answer": "print(type(42), type(3.14), type('Python'), type(True))"
        }
    ],
    "Estruturas Condicionais": [
        {
            "title": "If, Else",
            "content": (
                "O if/else permite tomar decisões no código, executando blocos diferentes "
                "conforme a condição."
            ),
            "example": "x = 10\nif x > 5:\n    print('Maior que 5')\nelse:\n    print('Menor ou igual a 5')",
            "example_explanation": (
                "1. `if x > 5:` verifica se `x` é maior que 5.\n"
                "2. Se a condição for verdadeira, `print('Maior que 5')` é executado.\n"
                "3. Caso contrário, `print('Menor ou igual a 5')` é executado."
            ),
            "challenge": "Crie um programa que avalie se um número é positivo ou negativo.",
            "answer": "x = -10\nif x >= 0:\n    print('Positivo')\nelse:\n    print('Negativo')"
        }
    ],
    "Ciclos e Repetição": [
        {
            "title": "Ciclo For",
            "content": (
                "O for permite iterar sobre itens de uma sequência ou usar o range "
                "para repetir um bloco de código."
            ),
            "example": "for i in range(5):\n    print(i)",
            "example_explanation": (
                "1. `range(5)` gera os números de 0 a 4.\n"
                "2. O laço `for` itera sobre esses números, atribuindo-os à variável `i`.\n"
                "3. `print(i)` exibe o valor de `i` em cada iteração."
            ),
            "challenge": "Imprima os números de 1 a 10 usando um ciclo 'for'.",
            "answer": "for i in range(1, 11):\n    print(i)"
        }
    ]
}

class PythonTutorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aprender Python - Tutor para Crianças")
        self.setGeometry(100, 100, 1200, 900)
        self.setStyleSheet("background-color: #2d2d2d; color: #ffffff;")
        self.init_ui()

    def init_ui(self):
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()

        self.title_label = QLabel("Aprender Python")
        self.title_label.setFont(QFont("Arial", 30, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        for section_name in SECTIONS_DATA.keys():
            button = QPushButton(section_name)
            button.setFont(QFont("Arial", 20))
            button.setStyleSheet(
                "background-color: #3e3e3e; color: #ffffff; border-radius: 10px; padding: 10px;"
            )
            button.clicked.connect(lambda checked, sn=section_name: self.show_section(sn))
            self.main_layout.addWidget(button)

        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def show_section(self, section_name):
        self.section_widget = QWidget()
        self.section_layout = QVBoxLayout()

        self.section_title = QLabel(section_name)
        self.section_title.setFont(QFont("Arial", 30, QFont.Bold))
        self.section_title.setAlignment(Qt.AlignCenter)
        self.section_layout.addWidget(self.section_title)

        for subsection in SECTIONS_DATA[section_name]:
            button = QPushButton(subsection["title"])
            button.setFont(QFont("Arial", 20))
            button.setStyleSheet(
                "background-color: #3e3e3e; color: #ffffff; border-radius: 10px; padding: 10px;"
            )
            button.clicked.connect(lambda checked, sb=subsection: self.show_subsection(section_name, sb))
            self.section_layout.addWidget(button)

        back_button = QPushButton("Página Inicial")
        back_button.setFont(QFont("Arial", 20))
        back_button.setStyleSheet(
            "background-color: #3e3e3e; color: #ffffff; border-radius: 10px; padding: 10px;"
        )
        back_button.clicked.connect(self.init_ui)
        self.section_layout.addWidget(back_button)

        self.section_widget.setLayout(self.section_layout)
        self.setCentralWidget(self.section_widget)

    def show_subsection(self, section_name, subsection):
        self.subsection_widget = QWidget()
        self.subsection_layout = QVBoxLayout()

        # Adiciona a explicação teórica acima da lista de desafios
        theory_label = QLabel(subsection["content"])
        theory_label.setFont(QFont("Courier", 14))
        theory_label.setWordWrap(True)
        theory_label.setStyleSheet("padding: 10px; background-color: #3e3e3e; color: #ffffff; border-radius: 10px;")
        self.subsection_layout.addWidget(theory_label)

        # Adiciona os exemplos e explicação passo-a-passo
        example_label = QLabel("Exemplo:")
        example_label.setFont(QFont("Arial", 18, QFont.Bold))
        example_label.setStyleSheet("margin-top: 15px; color: #ffffff;")
        self.subsection_layout.addWidget(example_label)

        example_code = QLabel(subsection["example"])
        example_code.setFont(QFont("Courier", 14))
        example_code.setStyleSheet("padding: 10px; background-color: #1e1e1e; color: #ffffff; border-radius: 10px;")
        example_code.setWordWrap(True)
        self.subsection_layout.addWidget(example_code)

        example_explanation = QLabel(subsection.get("example_explanation", "Explicação não disponível."))
        example_explanation.setFont(QFont("Courier", 14))
        example_explanation.setWordWrap(True)
        example_explanation.setStyleSheet("padding: 10px; background-color: #3e3e3e; color: #ffffff; border-radius: 10px;")
        self.subsection_layout.addWidget(example_explanation)

        self.splitter = QSplitter(Qt.Horizontal)
        self.subsection_layout.addWidget(self.splitter)

        # Lista de desafios
        self.challenge_list = QListWidget()
        for item in SECTIONS_DATA[section_name]:
            self.challenge_list.addItem(item["challenge"])
        self.challenge_list.currentRowChanged.connect(lambda index: self.select_challenge(index, section_name))
        self.splitter.addWidget(self.challenge_list)

        # Editor de código e saída
        editor_output_widget = QWidget()
        editor_output_layout = QVBoxLayout()

        self.code_editor = QTextEdit()
        self.code_editor.setFont(QFont("Courier", 14))
        self.code_editor.setStyleSheet(
            "background-color: #1e1e1e; color: #ffffff; border: 1px solid #555555;"
        )
        editor_output_layout.addWidget(self.code_editor)

        run_button = QPushButton("Executar Código")
        run_button.setFont(QFont("Arial", 15))
        run_button.setStyleSheet(
            "background-color: #3e3e3e; color: #ffffff; border-radius: 10px; padding: 10px;"
        )
        run_button.clicked.connect(self.run_code)
        editor_output_layout.addWidget(run_button)

        show_answer_button = QPushButton("Mostrar Resposta")
        show_answer_button.setFont(QFont("Arial", 15))
        show_answer_button.setStyleSheet(
            "background-color: #3e3e3e; color: #ffffff; border-radius: 10px; padding: 10px;"
        )
        show_answer_button.clicked.connect(lambda: self.show_answer(section_name))
        editor_output_layout.addWidget(show_answer_button)

        self.output_area = QTextEdit()
        self.output_area.setFont(QFont("Courier", 14))
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet(
            "background-color: #1e1e1e; color: #ffffff; border: 1px solid #555555;"
        )
        editor_output_layout.addWidget(self.output_area)

        editor_output_widget.setLayout(editor_output_layout)
        self.splitter.addWidget(editor_output_widget)

        back_button = QPushButton("← Voltar")
        back_button.setFont(QFont("Arial", 20))
        back_button.setStyleSheet(
            "background-color: #3e3e3e; color: #ffffff; border-radius: 10px; padding: 10px;"
        )
        back_button.clicked.connect(lambda: self.show_section(section_name))
        self.subsection_layout.addWidget(back_button)

        self.subsection_widget.setLayout(self.subsection_layout)
        self.setCentralWidget(self.subsection_widget)

    def select_challenge(self, index, section_name):
        self.selected_challenge_index = index

    def show_answer(self, section_name):
        if hasattr(self, 'selected_challenge_index') and self.selected_challenge_index >= 0:
            answer = SECTIONS_DATA[section_name][self.selected_challenge_index].get("answer", "Resposta não disponível.")
            self.code_editor.setPlainText(answer)

    def run_code(self):
        code = self.code_editor.toPlainText()
        temp_file = "temp_code.py"

        with open(temp_file, "w", encoding="utf-8") as file:
            file.write(code)

        try:
            result = subprocess.run(
                ["python", temp_file], capture_output=True, text=True
            )
            output = result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            output = str(e)

        self.output_area.setPlainText(output)

        os.remove(temp_file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = PythonTutorApp()
    main_window.show()
    sys.exit(app.exec_())
