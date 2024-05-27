from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import time

app = Flask(__name__)

def generate_menu():
    return """
O que mais gostaria? 
1. Sobre Lucas Gomes
2. Link para seu LinkedIn
3. Link para seu currículo
4. Link para seu portfólio
5. Link para seu GitHub
Digite o número correspondente à opção desejada ou digite 'sair' para encerrar.
"""

@app.route('/bot', methods=['POST'])
def bot():
    incoming_message = request.values.get('Body', '').strip().lower()

    resp = MessagingResponse()

    if incoming_message == '':
        resp.message(generate_menu())
    elif incoming_message == '1':
        about_me_message = """Vivo no mundo da programação desde 2022, começando com desenvolvimento de API, onde me apaixonei pela tecnologia. 
Atualmente estou graduando Engenharia de Software no Instituto INFNET, no Rio de Janeiro, e estou em busca de um estágio.
- Skills: HTML, CSS (pré-processadores SASS), Javascript (React / ReactNative), C# em ambiente .NET, SQL, Python e Java (Springboot).
- Ferramentas: Visual Studio Code, Visual Studio, Git, Docker, Firebase, Azure, SQL Workbench, Google Colab, Looker Studio, Insomnia e pacote Office Microsoft.
- Projeto social extra: Projeto EcoSocial - Desenvolvedor de Aplicativo
- Amo a tecnologia, tenho curiosidade na área de cibersegurança.
- Sonho em trabalhar desenvolvendo APIs e softwares."""
        resp.message(about_me_message)
        time.sleep(1)
        resp.message(generate_menu())
    elif incoming_message == '2':
        resp.message("Link para meu LinkedIn: [https://www.linkedin.com/in/lucas-gomes-b78109240/]")
        time.sleep(1)
        resp.message(generate_menu())
    elif incoming_message == '3':
        resp.message("Link para meu currículo: [https://drive.google.com/file/d/1uCpI11DmFrOEKUE3nyfEAxhBMsMIo_s5/view?usp=sharing]")
        time.sleep(1)
        resp.message(generate_menu())
    elif incoming_message == '4':
        resp.message("Link para meu portfólio: [https://lucasportfolio-pi.vercel.app/]")
        time.sleep(1)
        resp.message(generate_menu())
    elif incoming_message == '5':
        resp.message("Link para meu GitHub: [https://github.com/LucasGAraujo]")
        time.sleep(1)
        resp.message(generate_menu())
    elif incoming_message == 'sair':
        resp.message("Obrigado por querer me conhecer, é um prazer. Meu telefone pessoal é +21999461157")
    else:
        resp.message("Olá, eu sou o bot do Lucas Gomes! A seguir, irei te informar sobre ele... número pessoal dele: +21999461157")
        time.sleep(1)
        resp.message(generate_menu())
    return str(resp)

@app.route('/')
def index():
    return "Está funcionando"

if __name__ == '__main__':
    app.run()
