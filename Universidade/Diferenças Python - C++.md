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