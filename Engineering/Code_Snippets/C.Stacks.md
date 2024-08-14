---
# Stack Simples (LIFO)

> [!important]  
> Complexidade Computacional: O(1) - Inserção e Retirada  
Com recurso ás listas, conseguimos criar uma nova estrutura de dados: as Stacks ou Pilhas, com uma organização LIFO - Last-In-First-Out. Para tal são criadas 5 novas funções, que nada mais são do que uma adaptação das funções declaradas em “linkedList.h”, como abaixo.

> Para o seguinte exemplo de construção e utilização de pilhas simples foram utilizados os recursos disponibilizados para gestão de listas simples em [[C.Lists]].
```C
\#include "linkedList.h"
\#include <stdio.h>
typedef List Stack;
Stack *createStack(){
    return (Stack*)createList();
}
void deleteStack(Stack *s, void (*freeItem)(Item i)){
    deleteList((List*)s, freeItem);
    return;
}
void push(Stack *s, Item i){
    appendStart((List*)s, i);
    return;
}
Item pop(Stack *s){
    return popHead((List*)s);
}
Item peek(Stack *s){
    //It's like a popHead, but without deleting the Node.
    return getItem(getHead((List*)s));
}
/**
 * In case the stack is empty, the peek and pop function return NULL
 */
void freeItem(){
    return;
}
int main(){
    int arr[7] = {1, 2, 3, 5, 7, 9, 11};
    Stack *st = createStack();
    for(int i = 0; i<sizeof(arr)/sizeof(int); i++){
        push(st, (Item)(arr+i));
    }
    pop(st);
    printf("%d ", *(int*)pop(st));
    printf("%d\n", *(int*)pop(st));
		//Output: 9 7
    deleteStack(st, freeItem);
    return 0;
}
```
Esta stack tem a capacidade de armazenar qualquer tipo de dados e uma complexidade de execução de O(1)!
O facto de ser realizada com listas permite que esta pilha não tenha dimensão limite, o que acontece com um vetor, contudo, estas limitações podem ser implementadas com código posterior. É de notar que caso a stack esteja vazia, o pop/peek retornam NULL (consultar [[C.Lists]]).