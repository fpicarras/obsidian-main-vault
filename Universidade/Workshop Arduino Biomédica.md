***
# Porque um Arduino

O Arduino é amplamente utilizado na prototipagem e desenvolvimento de dispositivos eletrónicos pela sua simplicidade, flexibilidade e acessibilidade. Para alunos de engenharia biomédica, ele oferece um meio rápido e eficiente de testar e desenvolver soluções tecnológicas na área da saúde. O Arduino permite controlar uma grande variedade de sensores e dispositivos de maneira integrada, sendo ideal para projetos que envolvem monitorização de sinais vitais, reabilitação, próteses e instrumentação médica.

## Vantagens para a Engenharia Biomédica:

- **Fácil Integração com Sensores Biomédicos**: Compatível com sensores de ECG, temperatura, frequência cardíaca, oxímetro, entre outros.
- **Custo Acessível**: Uma opção de baixo custo em comparação com outros microcontroladores e sistemas embarcados.
- **Plataforma Aberta e Extensível**: O ambiente de código aberto permite o uso e personalização de bibliotecas para diferentes aplicações médicas.
- **Prototipagem Rápida**: Permite testar e desenvolver rapidamente novos dispositivos e ideias, algo essencial na inovação biomédica.

---

## **Exemplos práticos**

- **Monitorização de Sinais Vitais**: Projetos que utilizam sensores de frequência cardíaca, temperatura corporal e oxímetros de pulso para criar sistemas de monitoramento de pacientes.
- **Próteses Ativas**: Controle de servomotores para simular o funcionamento de membros protéticos baseados em comandos provenientes de sensores musculares (EMG).
- **Sistemas de Reabilitação**: Dispositivos que auxiliam em terapias físicas, monitorizando e ajustando o movimento através de sensores de posição e força.
- **Desfibrilador Simulado**: Simulações em laboratório de protótipos de desfibriladores para prática e pesquisa, usando Arduino para controlar e monitorar as correntes e pulsos.
- **Dispositivos de Medição para Pesquisa**: Utilização de sensores para coletar dados experimentais, como análise de stress físico através de sensores de pressão.

---
# Introdução ao dispositivo

O Arduino é uma plataforma de hardware e software de código aberto composta por um microcontrolador (geralmente da linha Atmel AVR) e um ambiente de desenvolvimento simples (Arduino IDE). Ele oferece uma interface de fácil uso para iniciantes e uma vasta gama de recursos para usuários avançados.

## Core Features

- **Microcontrolador**: Atmega328 (para Arduino Uno), responsável pelo processamento.
- **Memória Flash**: 32 KB no Arduino Uno (para armazenar o programa).
- **Memória SRAM**: 2 KB para dados temporários.
- **EEPROM**: 1 KB de armazenamento permanente.
- **Velocidade de Clock**: 16 MHz, permitindo execução eficiente de tarefas de controle e leitura de sensores.
- **Interface USB**: Permite comunicação com o computador e carregamento de programas.
- **Entrada de alimentação externa**: Pode ser alimentado por fonte externa (7-12V).


## Alimentação

O Arduino pode ser alimentado de várias maneiras, o que o torna muito flexível para diferentes aplicações:

- **USB**: Alimentação de 5V a partir de um computador ou carregador USB.
- **Alimentação Externa (Jack)**: Entre 7V e 12V através de um adaptador DC ou baterias.
- **Pinos de Alimentação**: A placa também disponibiliza pinos de 5V e 3.3V para fornecer energia a sensores e atuadores.


## **IO's (Entradas e Saídas)**

O Arduino Uno possui pinos dedicados para entradas e saídas digitais e analógicas que permitem interagir com o mundo exterior.

#### **Alimentação**

- **5V e 3.3V**: Pinos que fornecem alimentação para sensores e outros periféricos.
- **GND (Ground)**: Pino de referência para o sistema de alimentação e circuito externo.

---

#### **Pinos Digitais**

- **Entrada e Saída Digital**: O Arduino Uno possui 14 pinos digitais (0 a 13), usados para ler e enviar sinais digitais (0V ou 5V, ou seja, HIGH ou LOW).
- **PWM (Pulse Width Modulation)**: 6 desses pinos podem gerar sinais PWM, essenciais para controle de velocidade de motores ou brilho de LEDs.

---

#### **Pinos Analógicos**

- **Entradas Analógicas**: O Arduino Uno tem 6 entradas analógicas (A0 a A5), que podem ser usadas para ler valores de sensores analógicos como sensores de temperatura, potenciómetros ou sensores de pressão. Estes pinos leem valores de 0 a 5V e os convertem para um valor digital (entre 0 e 1023) através do conversor ADC (Analógico para Digital).

---

#### **Extras (Tx/Rx, etc.)**

- **Pinos Tx/Rx**: Pinos 0 (Rx) e 1 (Tx) são usados para comunicação serial com outros dispositivos ou com o computador.
- **I2C**: Pinos A4 e A5, que também são usados para comunicação I2C (Serial Clock e Serial Data).
- **SPI (Serial Peripheral Interface)**: Pinos 10 (SS), 11 (MOSI), 12 (MISO) e 13 (SCK) são usados para comunicação SPI com dispositivos como cartões SD, displays e outros módulos.

---

# Programação

> Antes de tudo, abordar [[Diferenças Python - C++]].

O Arduino é programado utilizando uma linguagem baseada em C/C++, através do IDE Arduino. A programação é feita com dois blocos principais:

### **Estrutura básica de um programa (Sketch)**

- **setup()**: Função chamada uma vez, no início do programa. Utilizada para inicializar pinos, configurar a comunicação serial e preparar o Arduino para a execução do programa.
- **loop()**: Função chamada repetidamente após o setup, onde a lógica do programa é implementada. O código dentro de `loop()` será executado de forma contínua.

```Cpp
void setup() {
  pinMode(13, OUTPUT);  // Configura o pino 13 como saída
  Serial.begin(9600);   // Inicia a comunicação serial
}

void loop() {
  digitalWrite(13, HIGH);  // Liga o LED no pino 13
  delay(1000);             // Espera 1 segundo
  digitalWrite(13, LOW);   // Desliga o LED no pino 13
  delay(1000);             // Espera 1 segundo
}
```

### **Funções Comuns**

- **digitalWrite(pino, valor)**: Define o estado de um pino digital (HIGH ou LOW).
- **digitalRead(pino)**: Lê o estado de um pino digital (HIGH ou LOW).
- **analogWrite(pino, valor)**: Escreve um valor PWM em um pino digital (0-255).
- **analogRead(pino)**: Lê um valor analógico de um pino analógico (0-1023).

### **Bibliotecas**

O Arduino possui uma vasta gama de bibliotecas que facilitam a programação de sensores e módulos específicos. Exemplo: **Servo.h** para controlar motores servo ou **Wire.h** para comunicação I2C.