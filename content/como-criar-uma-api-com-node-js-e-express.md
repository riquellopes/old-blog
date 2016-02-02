Title: Como criar uma api com nodejs e express
Date: 2016-02-02 09:11
Tags: nodejs, express, api
Category: Dev
Slug: como-criar-uma-api-com-node-js-e-express
Author: Henrique Lopes

Eu sou uma pessoa que gosta de resolver problemas, não criar outros por causa de uma linguagem de programação. O [PO](http://www.desenvolvimentoagil.com.br/scrum/product_owner) na maioria das vezes não possui competências técnicas para distinguir qual seria a melhor linguagem ou arquitetura para o seu produto. Você que está entrando no mercado agora ou almeja entrar, deve ter esse tipo sapiência. Você também é parte do processo, software é feito por pessoas, e são elas que tomam as decisões. Por que eu quis iniciar esse post com essa pequena explanação? Eu sou um pythonista de coração, e adoro usar, quando tenho a possibilidade de resolver os problemas pythonicamente, mas no meu dia a dia, eu nem sempre o posso. Hoje na stack que temos no [hotelurbano](https://www.hotelurbano.com/), temos aplicações em [python](https://www.python.org), [nodejs](https://nodejs.org/en/), [scala](http://www.scala-lang.org/), [go](https://golang.org), [ruby](https://www.ruby-lang.org/pt/) e [php](https://secure.php.net/manual/pt_BR/index.php). As vezes é necessário desenvolver novas features nessas aplicações, para que elas possam se comunicar com outra aplicação.


#### Vamos ao que realmente interessa #nodejs.

Eu não tive muita dificuldade para entender [nodejs](https://nodejs.org/en/), eu já sabia javascript muito bem, então foi fácil para dar meus primeiros passos. A unica coisa que me atrapalhou um pouco nesse projeto foi montar a minha stack, o [nodejs](https://nodejs.org/en/) possui várias implementações para o que eu estava querendo fazer. Mas conversando com amigos mais fluentes em [nodejs](https://nodejs.org/en/) eu cheguei ao meu produto, uma api para me informar o valor dos proventos pagos por cada [fundo imobiliário](http://www.fundoimobiliario.com.br/). Se quiser já ir dando uma olhada o [link](https://github.com/riquellopes/fii) é esse. Eu vou explicar todo o processo, pode deixar. Vou te dar tudo no esquema.


Eu tentei encontrar alguma api que podesse me fornecer a informação que eu queria, mas não achei nada que fosse de graça. Então acabei criando um [scraping](https://pt.wikipedia.org/wiki/Data_scraping), que raspa essa informação de um outro site. Em python isso é muito tranquilo de se fazer. Com [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) e [requests](http://docs.python-requests.org/en/latest/), eu teria isso de forma simples. No [nodejs](https://nodejs.org/en/) eu utilizei o [scrap](https://www.npmjs.com/package/scrap), li vários posts que mencionavam ele, então resolvi usar. Para quem já usou jQuery, e sabe um pouco de [seletores](https://api.jquery.com/category/selectors/), não vai encontrar nenhuma dificuldade para utilizar.

```javascript
exports.scrap = function(request, response){
    scrap(config.endpoint.concat("/"), function(err, $) {
        var message = "Serviço indisponível."
          if( err ){
              return response.status(503).json({message:message});
          }

          var queue = async.queue(function(object, callback){
              return object.save(callback);
          }, 4);

          for(var i=1; i < $('tr','table').length; i++){
              var tr = $('tr','table').eq(i);
              var data = {
                  codigo: $("td", tr).eq(0).text(),
                  data_base: $("td", tr).eq(1).text(),
                  cotacao_base: $("td", tr).eq(2).text(),
                  data_pagamento: $("td", tr).eq(3).text(),
                  valor_rendimento: $("td", tr).eq(4).text(),
                  porcentagem_rendimento: $("td", tr).eq(5).text(),
                  observacao: $("td", tr).eq(6).text()
              }

              queue.push(new Fii(data), function(error, doc){
                  if(error){
                      queue.kill();
                      return response.status(500).json(
                          {message:"Erro ao importar as informações."});
                  }
              });
          }// for

          if(queue.length() == 0){
              return response.status(503).json({message:message});
          }

          queue.drain = function(){
              response.json(
                  {message: util.format(
                      "%s fii, foram copiados.", (i-1))});
          };
    });
}
```
Para acelerar um pouco mais o processo, eu utilizei um queue do módulo, [async](https://github.com/caolan/async). Eu não tinha tanta necessidade de fazer isso, mais como era um protótipo, resolvi adicionar essa fila, para que o meu processo fosse mais performático ainda. O módulo [async](https://github.com/caolan/async) possui várias features legais, da uma olhada depois na documentação do projeto.

#### Orm utilizado.

Para persistir esses dados, que não possuem uma estrutura muito bem definida eu resolvi utilizar o [mongodb](https://www.mongodb.org/)+[mongolab](https://mongolab.com/)+[mongoose](http://mongoosejs.com/).
Nas pesquisas que fiz o [mongoose](http://mongoosejs.com/) é muito difundido, então segui essa mesma linha. O [mongolab](https://mongolab.com/) é um MongoDB-as-a-Service que eu gosto muito, e como eu não queria pagar nada para ter uma máquina com [mongodb](https://www.mongodb.org/), adicionei mais esse ingrediente a minha stack.


```javascript
var FiiSchema = new Schema({
    codigo: {type: String, index: true, required: true, unique:true},
    data_base: String,
    cotacao_base: String,
    data_pagamento: String,
    valor_rendimento: String,
    porcentagem_rendimento: String,
    baixa_liquides: Boolean,
    investidor_qualificado: Boolean,
    observacao: String,
    created: {
        type: Date,
        default: Date.now
    }
});

var fii = module.exports = mongoose.model('Fii', FiiSchema);

FiiSchema.pre("save", function(next){
    this.investidor_qualificado = (this.codigo.indexOf("*IQ*") > -1);
    this.baixa_liquides = (this.codigo.indexOf("*BL*") > -1);
    this.codigo = this.codigo.split("*")[0];
    next();
})
```

Você pode perceber que utilizei um feature do mongoose, [pre save](http://mongoosejs.com/docs/middleware.html), pois antes que ele persiste a informação, eu precisava que algumas coisas fossem extraidas. Pra quem já usou o [django](https://www.djangoproject.com) alguma vez, já deve ter esbarrado com [signals](https://docs.djangoproject.com/en/1.9/ref/signals/).


#### Aplicação sem test não tem graça.

Uma das coisas que mais me auxiliam a criar aplicações, sem ter medo de errar, é sempre ter testes para
garantir que minha aplicacação vai fazer exatamente aquilo para qual ela foi criada. Para minha stack de teste eu utilizei,
[supertest](https://www.npmjs.com/package/supertest)+[assert](https://www.npmjs.com/package/assert)+[nock](https://www.npmjs.com/package/nock)+[mocha](https://github.com/mochajs/mocha).

```javascript
describe("SCRAP", function(){
    before(function(){
        Fii.remove({}, function(){});
    });

    it("should return {message:'94 fii, foram copiados.'}.", function(done){
        nock(config.endpoint).get("/").once()
            .reply(200, function(uri, requestBody, cb){
                fs.readFile(__dirname.concat("/index.html") , cb);
            });
        request(app)
            .get("/api/scrap")
            .expect(200)
            .end(function(error, res){
                if( error ) return done(error);

                assert.equal(res.body.message, "94 fii, foram copiados.");
                done();
            });
    });

    it("fii service return 404, scrap service should return message and status 503.", function(done){
        nock(config.endpoint).get("/").once().reply(404, "Fora");
        request(app)
            .get("/api/scrap")
            .expect(503)
            .end(function(error, res){
                assert.equal(res.body.message, "Serviço indisponível.");
                done();
            });
    });

    it("case html broken, scrap service should return status 503", function(done){
        nock(config.endpoint).get("/").once()
            .reply(200, function(uri, requestBody, cb){
                fs.readFile(__dirname.concat("/error.html") , cb);
            });
        request(app)
            .get("/api/scrap")
            .expect(503)
            .end(function(error, res){
                assert.equal(res.body.message, "Serviço indisponível.");
                done();
            });
    })
});
```

O [nock](https://www.npmjs.com/package/nock) só é necessário se você precisa [mockar](https://pt.wikipedia.org/wiki/Objeto_Mock) alguma resposta.
Para testes que dependem de recursos externernos a sua aplicação, é interessante você [mockar](https://pt.wikipedia.org/wiki/Objeto_Mock), para performar o tempo de resposta do seus testes.
Os testes foram escritos em [BDD](https://pt.wikipedia.org/wiki/Behavior_Driven_Development) utilizando o framework [mocha](https://github.com/mochajs/mocha), e para simular as chamadas ao serviço [supertest](https://www.npmjs.com/package/supertest). Para executar a stack de teste é bem simples.

```bash
make test
or
npm test
```

#### Desenvolvendo em ambientes seguros.

O último módulo é não menos importante que completou a minha stack, foi o [dotenv](https://www.npmjs.com/package/dotenv). Um site que eu indico para você ler, e ter uma melhor noção de boas práticas de software-as-a-service é [The Twelve-Factor APP](http://12factor.net). O tópico que ratifica
o uso desse módulo é o [III Config](http://12factor.net/config). O [dotenv](https://www.npmjs.com/package/dotenv) permite que você crie enviroments com as configurações que você precisa no seu ambiente local. Ele não é para ser utilizado em produção. Por default ele vai procurar na raiz
do seu projeto a variável de ambiente **.env**, caso você queira usar outro nome, você precisa passar o [path](https://www.npmjs.com/package/dotenv#path) para [dotenv](https://www.npmjs.com/package/dotenv), não é nenhum bicho de 7 cabeças.


#### Express em ação.

Criar uma aplicação com [express](http://expressjs.com/) é bem simples, ele não foge muito do
modelo que o [flask](http://flask.pocoo.org/) nos da. Eu queria que o meu app, ficasse isolado
do contexto geral, e que de certa forma eu pudesse desplugar ele rapidamente da minha app. Então
eu usei a feature *express.Router()* para me permitir fazer isso.

```javascript
var express = require("express");
var config = require("./config");
var mongoose = require('mongoose');
var api = require("./models/api.js");

var app = exports.app = express();
var port = process.env.PORT || 5000;
router = express.Router()

router.route("/").get(api.list);
router.route("/scrap").get(api.scrap);
router.route("/:codigo").get(api.filter);
app.set('json spaces', 2);
app.use("/api", router);

app.get("/", function(request, response){
    response.json({message:"Recupera informações sobre proventos dos fii"});
});

app.listen(port);
```

Para executar app, basta executar o commando abaixo.

```bash
make run
```

#### Conclusão.

Espero que tenha atendido as suas expectativas. Dúvidas ou sugestões é só comentar no post, que eu
estou sempre a disposição para ajudar. Não fique acanhado em fazer um [fork](https://help.github.com/articles/fork-a-repo/) e me mandar um [pull request](https://help.github.com/articles/using-pull-requests/) com uma melhoria no app.
