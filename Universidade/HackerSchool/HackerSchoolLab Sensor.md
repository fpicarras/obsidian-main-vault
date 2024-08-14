***
Primeiro que tudo, é preciso um nome melhor para esta merda

> Este dispositivo tem o intuito de fornecer informações sobre  o estado do lab, como:
> - Presenças
> - Temperatura
> - Humidade
> - Qualidade do AR
>
 Dando assim display da informação remotamente.

# Componentes
## Micro-controlador
A minha ideia é ir com um micro-controlador Arduino Nano ou um [ESP32-C3](https://mauser.pt/catalog/product_info.php?products_id=095-1308), ambos têm baixos consumos e um tamanho razoável para meter dentro de um dispositivo pequeno.
Minha opinião é ser um ESP32-C3, são viáveis e super baratos para todas as funcionalidades que incluem.
## Temperatura/Humidade
Sensor de humidade/temperatura poderia ser um [DHT11](https://www.ptrobotics.com/atmosfericos/2333-dht11-basic-temperature-humidity-sensor.html) pois é fácil de calibrar com o único Downside de ter alguns segundos ter *sampling rate* (aproximadamente 2), limitando assim período de amostragem do dispositivo.
## Presença Humana
Fazendo alguma pesquisa, o [XIAO - Seeed 101010001](https://mauser.pt/catalog/product_info.php?products_id=095-3163) parece ser o que precisamos, tem a capacidade de detectar presença humana até 5m de distância com um precisão de 0.75m, medindo também se há movimentos.
Contudo, apenas utilizaríamos a funcionalidade de detecção de presença. que funciona com uma amplitude de 60º:

![Diagrama de funcionamento | center](https://storage.googleapis.com/mauser-public-images/prod_description_image%2F2024%2F45%2F10f4239f132430559cd730af7b6d0882_image.png)
## Qualidade do Ar

***
# Comunicação e Exposição
Seria por POST em HTTP, para um servidor externo. Idealmente, a mensagem era enviada para o server com o site na HackerSchool, onde era disposta a informação recolhida.
O site também ter a opção de devolver essa informação era porreiro, pois assim conseguia-se criar aplicações com base nisso. Tipo um simples display à entrada do lab que dizia se havia gente ou não.

# Alimentação
Não vejo a necessidade de utilizar baterias, acho que é bastante prático apenas ligar o USB-C do controlador a um transformador eficiente e está resolvido.

# Posicionamento
A sala tem aproximadamente 3m (desde a porta até ás janelas), a melhor opção pelo que estou a ver seria colocar o sensor na parede da janela em cima da mesma. Deste modo, garante-se que existe cobertura suficiente na sala toda e também bloqueia o sensor de medir a presença de pessoas no lab aberto.
