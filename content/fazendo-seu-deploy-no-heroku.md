Title: Fazendo seu deploy do Heroku
Date: 2016-01-17 17:48
Tags: flask, python, heroku, deploy
Category: Vida
Slug: fazendo-seu-deploy-no-heroku
Author: Henrique Lopes

Semana passada eu mostrei como era simples você criar o seu primeiro app web com Python,
[simples flask app](http://blog.henriquelopes.com.br/simples-flask-app.html). Hoje eu quero ir além,
você já deve ter visto alguns posts em inglês ou em português, de como fazer o seu primeiro deploy no [Heroku](https://www.heroku.com/). É simples! Como o Flask é o meu coringa pra quando eu preciso desenvolver algo simples, o [Heroku](https://www.heroku.com/) é o meu parque de diversões. Onde eu posso simplesmente com um git push, ter a minha aplicação em produção. Com o tempo, fazendo a mesma coisa, eu resolvi criar uma extensão para o [Flask](http://flask.pocoo.org/): o [BootFlask](https://github.com/riquellopes/boot-flask). Com ele você cria uma aplicação simples, e ganha algum tempo para fazer o que realmente importa. Mas vamos ao que interessa.

#### Primeiro passo - Montar o ambiente:
No último post eu mostrei para vocês o benefício que você tem em usar a ferramenta [virtualenv](https://virtualenv.readthedocs.org/en/latest/), se tiver alguma duvida, volta lá no [post](http://blog.henriquelopes.com.br/simples-flask-app.html) e depois volte aqui. Dessa vez eu vou adicionar mais baterias nesse app eu vou usar o [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) para ficar mais fácil ainda. Qualquer duvida é só comentar que eu te explicarei. Mais básicamente o [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) cria uma camada em cima do [virtualenv](https://virtualenv.readthedocs.org/en/latest/) e cria novos comandos para facilitar o seu dia a dia.
Os comandos que eu vou utilizar abaixo, são comandos do [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/). Em breve vou escrever um novo post, para falar sobre isso.

```bash
mkvirtualenv hello-heroku
pip install https://github.com/riquellopes/boot-flask/tarball/master
```

#### Criando meu primeiro projeto com BootFlask:
Para criar um novo projeto com [BootFlask](https://github.com/riquellopes/boot-flask) você deve executar o bootflask com o argumento -p.
O -p é utilizado para informar o nome do projeto, após executar esse comando, a arquitetura básica de arquivos é criada.

```bash
bootflask -p hello-heroku
```

Ainda faltam alguns arquivos, um deles é o requirements.txt, esse arquivo é utilizado pelo [Heroku](https://www.heroku.com/) para indentificar quais pacotes do seu projeto Python, precisam ser instalados. O [freeze](https://pip.pypa.io/en/stable/reference/pip_freeze/#id4) é o comando do gerenciador de pacotes pip, para recuperar todos os pacotes que seu environment possui, quando você executar o comando pip freeze > requirements.txt, ele vai pegar todo o output e escrever no arquivo requirements.txt. Após criar o requirements.txt abra o arquivo, no editor de sua preferência, e remova o BootFlask==0.1 do arquivo, você não vai precisar dele no [Heroku](https://www.heroku.com/).


```bash
pip freeze

Flask==0.10.1
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
Werkzeug==0.11.3
wheel==0.24.0
```

Se você ainda não tiver iniciado o git para seu projeto, faça isso agora com o comando [git init](https://git-scm.com/docs/git-init), é bem simples. E você já pode fazer seu primeiro [commit](https://git-scm.com/docs/git-commit).

```bash
git init
git add -A
git commit -am "iniciando app."
```

#### Segundo passo - Criando a sua aplicação na interface do Heroku
A interface no Heroku é muito intuitiva e você não vai encontrar grandes problemas para criar um novo projeto.
Após sua autenticação no Heroku, basta você clicar em create app,
![alt text](http://blog.henriquelopes.com.br/imagens/create-new-app.png "Create new App")


Após você clicar em create app, você será encaminhado para a tela abaixo. o campo App Name não é obrigatório,
mas se você quiser dar um nome legal para a sua aplicação fique a vontade.
![alt text](http://blog.henriquelopes.com.br/imagens/create-app.png "Create App")


Depois dessa difícil tarefa, você será levado para a ultima tela, onde você receberá algumas instruções que você deve executar na sua máquina. Se você não possui o [Heroku ToolBelt](https://toolbelt.heroku.com/), esse é um bom momento para instalar.
![alt text](http://blog.henriquelopes.com.br/imagens/deploy-your-changes.png "Deploy you changes")


#### Terceiro passo - Configurando variáveis locais e fazendo seu primeiro deploy:
O [Heroku](https://www.heroku.com/) utiliza do [git push](https://git-scm.com/docs/git-push) para fazer o deploy da sua aplicação, não tem nada de complicado nisso, a única coisa que você precisa fazer é configurar o seu [remote](https://git-scm.com/docs/git-remote), o [Heroku ToolBelt](https://toolbelt.heroku.com/) possui um alias para isso, vamos executar esse comando agora.

```bash
heroku git:remote -a O_NOME_DO_APP_DEVE_SER_ADICIONADO_AQUI
```

Esse é o unico comando que precisa ser executado na sua máquina, para partir para o deploy. E vamos fazer isso agora mesmo!

```bash
git push
```

E num passe de mágica a sua aplicação está me produção. Acho que não poderia ter um jeito mais fácil de fazer isso. Como eu sempre preso pelo "show me the code", ai estão os meus:


* [Projeto em produção](http://mighty-stream-1291.herokuapp.com)
* [Código do projeto](https://github.com/riquellopes/hello-heroku)
