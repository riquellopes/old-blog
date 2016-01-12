Title: Simples Flask App
Date: 2016-01-11 21:57
Tags: python, flask, dev
Category: developing
Slug: simples-flask-app
Author: Henrique Lopes


Já sentiu vontade de criar uma simples aplicação web, mas se sentiu preso? Pois quando você via o número de
configurações que eram necessárias para fazer a sua aplicação apenas dar um Hello World, você já sentia que ia
demorar? Pois bem, o Python não é uma bala de prata, mas ele possui n [frameworks](https://pt.wikipedia.org/wiki/Framework) e [microframeworks](https://en.wikipedia.org/wiki/Microframework) que vão fazer você sentir prazer em gerar um simples Hello World.

Hoje eu quero apresentar um microframework muito conhecido e já difundido na comunidade Python, o [Flask](http://flask.pocoo.org/) que pela sua simplicidade e robustez, merece ser o meu primeiro post hands on.
E, para adicionar mais baterias ao nosso App, vamos falar um pouco de [virtualenv](https://virtualenv.readthedocs.org/en/latest/).

##### Primeiro Passo - Montar o ambiente:
Se você usa [Linux](https://pt.wikipedia.org/wiki/Linux) ou [Macosx](https://pt.wikipedia.org/wiki/OS_X) seguir esse post será muito tranquilo. Se você usa [Windows](https://pt.wikipedia.org/wiki/Microsoft_Windows), eu vou escrever um outro post só para ajudar você.

Abra o terminal e siga os passos abaixo:
```bash
pip install virtualenv
```

Porque não instalar logo o Flask, e partir para o que realmente interessa? Se você teve a curiosidade de abrir o link do [virtualenv](https://virtualenv.readthedocs.org/en/latest/) e dar uma lida, você já sabe o porque e para que eu iniciei esse app instalando essa lib. O que eu quero fixar na sua mente de uma forma bem simples, é que no mundo real em uma empresa web ou de qualquer ramo da tecnologia, você vai ter a necessidade de trabalhar com várias versões de Python no seu dia a dia. Cada app ou projeto que você for trabalhar, vão possuir características que irão exigir que você possua várias versões de Python na sua máquina. O [virturalenv](https://virtualenv.readthedocs.org/en/latest/) vai permitir que você possua, para cada projeto, uma versão de Python diferente, sem precisar instalar nada no Python nativo do seu sistema. E sem deixar passar despercebido, eu estou usando o gerenciador de pacote do Python o [pip](https://docs.python.org/3.6/installing/index.html), com ele você irá instalar todos pacotes de python que o seu app precisa.

```bash
virtualenv /tmp/hello_world
source /tmp/hello_world/bin/activate

pip install flask
```

Eu não vou entrar no mérito dos comandos executados com o virtualenv, até porque a documentação explica muito bem isso. Mas logo logo eu escrevo um post, para te deixar a par.


#### Segundo passo - Escrever o app:

Após criar o nosso ambiente, vamos criar o nosso app. Geralmente eu crio uma pasta, então se quiser, pode fazer o mesmo. Comando executados [mkdir](http://www.linfo.org/mkdir.html), [cd](http://www.linfo.org/cd.html), [touch](http://www.linfo.org/touch.html) são comandos bem comuns para quem já do mundo opensource. Você pode clicar em cada uma deles para obter uma descrição melhor. O último comando executando o "atom" pode ser novidade para você, mais ele é um alias para o editor [Atom](https://atom.io/). Fique à vontade para usar o editor da sua preferência.

```bash
mkdir hello-world
cd hello-world
touch app.py
atom app.py
```

Quando eu escrevi essas linhas de código pela primeira vez, eu fiquei impressionado com a simplicidade que era para escrever uma aplicação. Cada linguagem tem o seu paradigma, mas o Python me surpreende com a sua simplicidade. Com apenas as 9 linhas de código abaixo a sua aplicação está pronta para ser executada.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HelloWorld"

if __name__ == "__main__":
    app.run()
```


```bash
python app.py
```

#### Terceiro passo:
Esse é o passo mais importante. Não pare de aprender e compartilhar.
