---
- **Conectividade para inteiros (.h e .c):**> [!important]  
    > Complexidade Computacional: O(log* N) (por ligação)  
    
    > Ficheiros com código para a conectividade de N números inteiros, que tem por base o algoritmo Compressed Weighted Union.
    
    ![[Connectivity_cs.zip]]
    
**Algoritmos Presentes:**
Quick Find
Quick Union
Weighted Union
Compressed Weighted Union
# Quick Find
---

> [!important]  
> Complexidade Computacional: O(N) (por ligação)  
```C
\#include <stdio.h>
\#define N 10000
int main(){
    int num1, num2, temp, id[N];
    //Initialize the id array
    for(int i = 0; i<N; i++) id[i] = i;
    //While the user is inputing data
    while(scanf("%d %d", &num1, &num2) == 2){
        if(id[num1] == id[num2]) continue;
        
        temp = id[num1];
        for(int i = 0; i < N; i++)
            if(id[i] == temp) id[i] = id[num2];
        printf("\t%d %d\n", num1, num2);
    }
    //Union is Slow -> O(N)
    //But to find if two numbers are connected
    //All we have to do is check if id[num1] == id[num2]
```
![[Untitled.png]]

> Embora a procura seja consideravelmente rápida, a união é realizada com um algoritmo linear rudimentar, que força o programa a ler todo o vetor de conexões por nó unido…

> Ora assim temos que se quisermos unir todos os N nós, o algoritmo vai ter uma complexidade temporal de **O(N²)**!
# Quick Union
---

> [!important]  
> Complexidade Computacional: O(N) (por ligação)  
```C
\#include <stdio.h>
\#define N 10000
int main(){
    int num1, num2, temp1, temp2, id[N];
    //Initialize the id array
    for(int i = 0; i<N; i++) id[i] = i;
    //While the user is inputing data
    while(scanf("%d %d", &num1, &num2) == 2){
        temp1 = num1; temp2 = num2;
        while(temp1 != id[temp1]) temp1 = id[temp1];
        while(temp2 != id[temp2]) temp2 = id[temp2];
        if(temp1 == temp2) continue;
        id[temp1] = temp2;
        printf("\t%d %d\n", num1, num2);
    }
    //Union is Faster -> O(1)
    //But to find if two numbers are connected
    //We have to find if they have the same root
}
```
![[Untitled 1.png]]

> A estrutura de dados formada é agora uma árvore.

> Quando dois nós tiverem a mesma raiz esses estão ligados. Assim temos que em grafos com maior verticalidade a complexidade temporal aproxima-se de **O(N)**!
# Weighted Union
---

> [!important]  
> Complexidade Computacional: O(log N) (por ligação)  
```C
\#include <stdio.h>
\#define N 10000
int main(){
    int num1, num2, temp1, temp2, id[N], sz[N];
    //Initialize the id array
    for(int i = 0; i<N; i++){
        id[i] = i;
        sz[i] = 1;
    }
    //While the user is inputing data
    while(scanf("%d %d", &num1, &num2) == 2){
        temp1 = num1; temp2 = num2;
        while(temp1 != id[temp1]) temp1 = id[temp1];
        while(temp2 != id[temp2]) temp2 = id[temp2];
        if(temp1 == temp2) continue;
        if(sz[temp1] < sz[temp2]){
            id[temp1] = temp2; sz[temp2] += sz[temp1];
        }else {
            id[temp2] = temp1; sz[temp1] += sz[temp2];
        }
        printf("\t%d %d\n", num1, num2);
    }
}
```
![[Untitled 2.png]]

> As estruturas de dados mantém-se, contudo, na ligação a árvore mais pequena é ligada à maior.

> Evita-se assim um crescimento demasiado rápido ao custo de mais código para a decisão.
# Compressed Weighted Union
---

> [!important]  
> Complexidade Computacional: O(log* N) (por ligação)  
```C
\#include <stdio.h>
\#define N 10000
int main(){
    int num1, num2, temp1, temp2, t, x, id[N], sz[N];
    //Initialize the id array
    for(int i = 0; i<N; i++){
        id[i] = i;
        sz[i] = 1;
    }
    //While the user is inputing data
    while(scanf("%d %d", &num1, &num2) == 2){
        temp1 = num1; temp2 = num2;
        while(temp1 != id[temp1]) temp1 = id[temp1];
        while(temp2 != id[temp2]) temp2 = id[temp2];
        if(temp1 == temp2) continue;
        if(sz[temp1] < sz[temp2]){
            id[temp1] = temp2; sz[temp2] += sz[temp1]; t = temp2;
        }else {
            id[temp2] = temp1; sz[temp1] += sz[temp2]; t = temp1;
        }
        //Now each vertice will point to the root
        for(temp1 = num1; temp1 != id[temp1]; temp1 = x){
            x = id[temp1]; id[temp1] = t;
        }
        for(temp2 = num2; temp2 != id[temp2]; temp2 = x){
            x = id[temp2]; id[temp2] = t;
        }
        printf("\t%d %d\n", num1, num2);
    }
}
```

> O algoritmo agora será responsável por percorrer a árvore desde os nós unidos até à raiz e colocar todos os vértices encontrados pelo caminho a apontar para a raiz.

> Assim garantimos que nenhuma árvore tem um crescimento considerável, diminuindo a complexidade temporal para o tempo de procura.

> O custo de execução do algoritmo está apenas a um fator constante do custo (inevitável) de leitura dos dados → No pior caso, custo de ligação ≈ 5!