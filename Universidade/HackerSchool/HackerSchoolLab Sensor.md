***
Primeiro que tudo, é preciso um nome melhor para esta merda

> Este dispositivo tem o intuito de fornecer informações sobre  o estado do lab, como:
> - Presenças
> - Temperatura
> - Humidade
> - Fumos
> Dando assim display da informação remotamente.

# Componentes
## Micro-controlador
A minha ideia é ir com um micro-controlador Arduino Nano ou um [ESP32-C3](https://mauser.pt/catalog/product_info.php?products_id=095-1308), ambos têm baixos consumos e um tamanho razoável para meter dentro de um dispositivo pequeno.
Minha opinião é ser um ESP32-C3, são viáveis e super baratos para todas as funcionalidades que incluem.
## Temperatura/Humidade
Sensor de humidade/temperatura poderia ser um [DHT11](https://www.ptrobotics.com/atmosfericos/2333-dht11-basic-temperature-humidity-sensor.html) pois é fácil de calibrar com o único Downside de ter alguns segundos ter *sampling rate* (aproximadamente 2), limitando assim período de amostragem do dispositivo.
## Presença Humana
Fazendo alguma pesquisa, o []

