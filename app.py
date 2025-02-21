


import pandas as pd
from fpdf import FPDF



dados = pd.read_csv("dados.csv")

titulo =    "CERTIFICADO DE PARTICIPAÇÃO"
subtitulo = "Este certificado comprova que o aluno concluiu com êxito"
texto2 = "o curso GRATUITO DE PYTHON ministrado por"
texto3 = " PROF. SAUER entre 23/08/2024 e 28/08/2024,"
texto4 = "com carga horária de 08 horas."

for nomecompleto in  dados['nomecompleto']:

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', size = 15)
    pdf.image("template.png", x=0, y=0)
    pdf.set_text_color(33, 24, 136)

    pdf.text(65, 95, titulo)
    pdf.text(72, 120, nomecompleto)
    pdf.text(35, 145, subtitulo)
    pdf.text(50, 155, texto2)
    pdf.text(50, 165, texto3)
    pdf.text(70, 175, texto4)

    pdf.output(f"cerrtificado_{nomecompleto}.pdf")