import textwrap;
import google.generativeai as gnai

import markdown
from markdown_it import MarkdownIt
from mdit_plain.renderer import RendererPlain

GOOGLE_API_KEY="YOUR_API_KEY"
gnai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "candidate_count":1,
    "temperature": 0.5,
}

model = gnai.GenerativeModel(model_name="gemini-1.0-pro")

def menu():
    menu = """\n
    ============ MENU ============
    [A]\tResumo
    [B]\tAtividades
    [C]\tNovo Assunto e Área
    [D]\tFim
    => """
    return input(textwrap.dedent(menu)) 

def conhecimento(escolaridade, assunto, area,nivel):
    response = model.generate_content(f"Sou um aluno do ensino {escolaridade} quero estudar sobre {assunto} na area de {area} na dificuldade {nivel}. faça um resumo")
    markdowit(response)

def atividades(escolaridade, assunto, area,nivel):
    response = model.generate_content(f"faça 5 questões do ensino {escolaridade} sobre {assunto} na area de {area} na dificuldade {nivel}.")
    markdowit(response)

    resposta=input("ver respostas ? s/n ")
    if(resposta == "s"):
        questoes = model.generate_content(f"quais são as respostas dessas questões {response}?")
        markdowit(questoes)

def markdowit(value):
    parser = MarkdownIt(renderer_cls=RendererPlain)
    Markdown= markdown.markdown(value.text)
    text = parser.render(Markdown)
    return print(text)

def main():
    escolaridade = str(input("nível de ensino: Fundamental, médio, superior ou profissionalizante: "))
    area = str(input("qual área specífica você vai focar? (ex: matemática, história...): "))
    assunto = str(input("qual assunto dessa área você quer? "))
    nivel = str(input("Qual nivel você deseja: fácil, médio, difícil: "))

    while True:
        opcao = menu()
        if opcao == "A" or opcao == "a":
            conhecimento(escolaridade, assunto, area,nivel)
        if opcao == "B" or opcao == "b":
            atividades(escolaridade, assunto, area,nivel)
        if opcao == "C" or opcao == "c":
            area = str(input("qual área specífica você vai focar ? (ex: matemática, história...): "))
            assunto = str(input("qual assunto dessa área você que ?:  "))
            nivel = str(input("Qual nivel você deseja: fácil, médio, difícil: "))
        if opcao == "D" or opcao == "d": 
            break
main()