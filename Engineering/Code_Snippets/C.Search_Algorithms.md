# Binary Search
---

> [!important]  
> Complexidade Computacional: O(log N)  
```C
int binSearch(int arr[], int alvo, int i, int f){
	  int m;  
		while(f >= i){
        m = (i+f)/2;
        if(alvo == arr[m]) return m;
        if(alvo < arr[m]) f = m-1;
        else i = m+1;
    }
    return -1;
}
```
- 📥 **Argumentos**
    
    - int arr[] - Vetor de inteiros **Ordenado(!)**
    - int alvo - Inteiro a procurar
    - int i - Índice do primeiro elemento de arr
    - int f - Índice do ultimo elemento de arr
    
      
    
- 📤 **Retorna**
    - -1 → O alvo não está no vetor.
    - m → Índice do alvo no vetor.

> De igual modo, podemos fazer o mesmo algoritmo de forma recursiva, contudo, a eficiência em memória é inferior:
- **Código Recursivo**
    
    ```C
    int recursiveBinSearch(int arr[], int alvo, int i, int f){
        int m;
    		if(f >= i){
            m = (i+f)/2;
    
            if(alvo == arr[m]) return m;
            if(alvo < arr[m])
                return recursiveBinSearch(arr, alvo, i, m-1);
            return recursiveBinSearch(arr, alvo, m+1, f);
        }
    		return -1;
    }
    ```
    
---

> Ou então um algoritmo para **strings**:
```C
int strBinSearch(char *arr[], char *alvo, int i, int f){
    int m;
    while( f >= i){
        m = (i+f)/2;
        if(strcmp(alvo, arr[m]) == 0) return m;
        if(strcmp(alvo, arr[m]) < 0) f = m-1;
        else i = m+1;
    }
    return -1;
}
```
- 📥 **Argumentos**
    
    - char *arr[] - Vetor de Strings **Ordenado(!)**
    - char *alvo - String a procurar
    - int i - Índice do primeiro elemento de arr
    - int f - Índice do ultimo elemento de arr
    
      
    
- 📤 **Retorna**
    - -1 → O alvo não está no vetor.
    - m → Índice do alvo no vetor.
---
# Linear Search
[https://tenor.com/view/we-dont-do-that-here-black-panther-tchalla-bruce-gif-16558003">We](https://tenor.com/view/we-dont-do-that-here-black-panther-tchalla-bruce-gif-16558003">We)