Title: Como testar a velocidade da sua internet com Python
Date: 2016-01-21 09:00
Modified: 2016-01-21 09:30
Tags: python, ferramenta
Category: Dev
Slug: como-testar-a-velocidade-da-sua-internet-com-python
Author: Henrique Lopes

Python sempre me surpreende por sua versatilidade e sua usabilidade. Resolvi buscar no [google](https://www.google.com.br/) alguma lib python que eu pudesse utilizar para medir a velocidade da
internet da minha casa. E logo na primeira tacada me deparei com esse post: [Measuring Internet Speed In Python Using Speedtest-cli](http://www.raspberrypi-spy.co.uk/2015/03/measuring-internet-speed-in-python-using-speedtest-cli/).

Matt Martz que é o autor do projeto, criou uma [interface cli](https://www.techopedia.com/definition/3337/command-line-interface-cli), utilizando o serviço [speedtest.net](http://www.speedtest.net).

#### Instalando

```bash
pip install speedtest-cli
```

#### Executando SpeedTest

```bash
speedtest
```

Esse foi o meu resultado.

![ScreeShot](//res.cloudinary.com/madeinhouse/image/upload/c_scale,w_680/v1453418830/screen-shot_m1pgrn.png)

O speedtest possui um feature bem legal, na qual você pode passar o parâmetro -share para o programa,
e ele vai criar uma imagem online do seu resultado, que você pode compartilhar com seus amigos.

No [github do projeto](https://github.com/sivel/speedtest-cli) você vai encontrar mais informações sobre
como você pode utilizar.
