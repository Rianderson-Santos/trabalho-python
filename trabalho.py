import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

dados_educacao = pd.read_csv('PDA_Dados_Cursos_Graduacao_Brasil.csv')

municipios_uni = pd.read_csv('PDA_Dados_Cursos_Graduacao_Brasil.csv')

municipio = dados_educacao['MUNICIPIO'].value_counts()

contagem_situacao_curso = dados_educacao['UF'].value_counts()

municipios = municipios_uni.groupby('MUNICIPIO').size().reset_index(name='media')
municipios

universidades = dados_educacao.groupby('NOME_IES').size().reset_index(name='media')
universidades

lista_de_municipios = municipios.nlargest(5, 'media')
lista_de_municipios

maiores_universidades = universidades.nlargest(5, 'media')
maiores_universidades

plt.figure(figsize=(12, 6))
plt.figure(figsize=(12, 6))

maiores_universidades.plot(kind='bar', color='skyblue',x='NOME_IES',y='media', title = 'Maiores Universidades\nBaseado no IES\nInstituição de Ensino Superior, ou apenas IES,\né uma unidade autônoma que oferece serviços\nde educação superior, como cursos de graduação,\npós-graduação e de extensão')
plt.savefig('graficos_desigualdade.png', bbox_inches='tight')

lista_de_municipios.plot(kind='bar', color='skyblue',x='MUNICIPIO',y='media', title = ' Média estadual\nMostra a média de entidades de ensino superior\ncom base no município/estado.\nO estado de São Paulo sai disparado na frente.')
plt.savefig('media_municipal', bbox_inches='tight'

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório - Media quantidade universidades nos maiores centros', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()
pdf.chapter_title('Media estadual:')
pdf.chapter_body('')

pdf = FPDF('P', 'mm', 'A4')

pdf.add_page()
# b, i, u
pdf.set_font('Arial', '', 10)

pdf.cell(w=0, h=16, txt='',  ln=True, align='c')
# align = r: direita , l: esquerda, c: center, j: justificado
text = 'Esses dois graficos a seguir analisa maiores universidades baseado no IES e media dos estados onde tem a maior concentração de universidades com ensino de qualidade São da região sul ou sudeste, fonte com as 10 melhores universidades privadas do brasil https://portalmaratimba.com.br/10-melhores-universidades-privadas-do-brasil/, como podemos analisar regiões mais afastadas como no caso do norte e nordeste não tem um ensino de tanta qualidade em comparação aos outros estados. '

pdf.multi_cell(w=0,h=10, align='c', txt=text)

pdf.image('graficos_desigualdade.png')
pdf.image('media_municipal.png', )

pdf.output('pdf1.pdf')