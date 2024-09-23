***
# Casting

**Python**: Dinâmico, ou seja, você não precisa declarar o tipo das variáveis explicitamente. O tipo é inferido pelo valor.

```python
x = 10  # Python deduz que x é um inteiro
y = 5.5  # Python deduz que y é um float
```

**C++ (Arduino)**: Estático, ou seja, você precisa declarar o tipo da variável ao defini-la.

```Cpp
int x = 10;  // Declarando uma variável inteira
float y = 5.5;  // Declarando uma variável do tipo float
```

## Arrays

Vetores são uma grande parte da programação, em python quase qualquer variavel pode ser colocada numa lista, pois estas são dinamicas, que é naturalmente definida como:

```python
list = [var1, var2, 0, 1, 1.1, 9]

print(list) # Imprime a lista

list.append(17) # Acrescenta um elemento

for item in list:
	print(item)
```

Em C++, vetores (ou arrays) têm tamanho fixo, e todos os elementos devem ser do mesmo tipo de dado. Se precisar de uma coleção com tamanho dinâmico, é necessário usar bibliotecas adicionais como `std::vector`.

```Cpp
// Tamanho Fixo
// Criando um array com tamanho fixo de 5 elementos inteiros
int vetor[5] = {1, 2, 3, 4, 5};

// Acessando um elemento do array
Serial.println(vetor[2]);  // Saída: 3

// Iterando pelo array
for (int i = 0; i < 5; i++) {
    Serial.println(vetor[i]);
}
```

Com uso da biblioteca:
```Cpp
#include <vector>

std::vector<int> vetor = {1, 2, 3, 4, 5};

// Adicionando um elemento ao vetor
vetor.push_back(6);

// Acessando elementos
Serial.println(vetor[2]);  // Saída: 3

// Iterando pelo vetor
for (int i = 0; i < vetor.size(); i++) {
    Serial.println(vetor[i]);
}
```
---
# Estruturas de Controlo

#### **1. `if`, `elif`, `else` (Estruturas Condicionais)**

- **Python**: Em Python, blocos de código são delimitados por **indentação** e não são necessárias chaves `{}`. O Python utiliza `elif` no lugar de `else if`.
```python
x = 10
if x > 10:
    print("x é maior que 10")
elif x == 10:
    print("x é igual a 10")
else:
    print("x é menor que 10")
```

- **C++ (Arduino)**: Em C++, usamos chaves `{}` para definir os blocos de código. Além disso, usamos `else if` em vez de `elif`.
```Cpp
int x = 10;
if (x > 10) {
    Serial.println("x é maior que 10");
} else if (x == 10) {
    Serial.println("x é igual a 10");
} else {
    Serial.println("x é menor que 10");
}
```

#### **2. Loops `for`**

- **Python**: O `for` em Python é usado principalmente para iterar sobre sequências, como listas ou ranges.
**Exemplo com `range`:**
```python
for i in range(5):  # Itera de 0 a 4
	print(i)
```
**Exemplo com uma lista:**
```python
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)```

- **C++ (Arduino)**: O `for` em C++ é mais semelhante ao de outras linguagens de programação, onde você define o início, a condição de parada, e o incremento.
```Cpp
for (int i = 0; i < 5; i++) {
    Serial.println(i);  // Imprime de 0 a 4
}
```

#### **3. Loops `while`**

- **Python**: O loop `while` executa enquanto a condição é verdadeira. Como no `if`, a indentação delimita o bloco de código.
```python
i = 0
while i < 5:
    print(i)
    i += 1  # Incrementa i
```

- **C++ (Arduino)**: A sintaxe do `while` em C++ é similar à do Python, mas com o uso de chaves `{}` para delimitar o bloco de código.
```Cpp
int i = 0;
while (i < 5) {
    Serial.println(i);
    i++;  // Incrementa i
}
```

## Principais Diferenças

**Sintaxe e Delimitação de Blocos**:
- **Python**: Usa **indentação** para definir blocos de código. Isso torna o código visualmente mais limpo, mas também significa que a indentação incorreta pode causar erros.
- **C++**: Usa **chaves `{}`** para delimitar blocos de código, o que é mais explícito, mas também requer atenção para garantir que as chaves estejam corretamente alinhadas.

**Loops `for`**:
- Em **Python**, o `for` é frequentemente usado para iterar sobre sequências como listas e `range()`, simplificando o processo.
- Em **C++**, o `for` segue o modelo mais clássico, que requer inicialização, condição e incremento explícito.
---
# Funções
**Python**: As funções são definidas com `def` e podem retornar valores sem a necessidade de especificar o tipo de retorno.
```python
def soma(a, b):
    return a + b
```

**C++**: O tipo de retorno da função deve ser declarado explicitamente. As funções também podem ser void (sem retorno).
```Cpp
int soma(int a, int b) {
    return a + b;
}
```
---
# Exemplo

```python
valor = int(input("Digite um valor: "))
print("Você digitou:", valor)
```

```Cpp
int valor;

void setup() {
  Serial.begin(9600);  // Inicia a comunicação serial
}

void loop() {
  if (Serial.available() > 0) {
    valor = Serial.parseInt();  // Lê um valor inteiro
    Serial.print("Você digitou: ");
    Serial.println(valor);
  }
}
```