---
# Fila Simples (FIFO)

> [!important]  
> Complexidade Computacional: O(1) - Inserção e Retirada  
Com recurso ás listas duplamente ligadas, conseguimos criar uma nova estrutura de dados: as Queues ou Filas, com uma organização FIFO - First-In-First-Out. Para tal são criadas 5 novas funções, que nada mais são do que uma adaptação das funções declaradas em “doubleLinkedList.h”, como abaixo.

> Para o seguinte exemplo de construção e utilização de filas simples foram utilizados os recursos disponibilizados para gestão de listas duplamente ligadas em [[C.Lists]].

```C
\#include "doubleLinkedList.h"
\#include <stdio.h>
typedef DList Queue;
Queue *createQueue(){
    return (Queue*)createDoubleList();
}
void deleteQueue(Queue *q, void (*freeItem)(Item i)){
    /**
     * When deleting the queue, the function freeItem
     * will free all the allocated memory of the Item,
     * you can also just set it as a simple enter and return
     * so that you don't free any of the Items!
    */
    deleteDoubleList((DList*)q, freeItem);
}
void push(Queue* q, Item i){
    D_appendStart((DList*)q, i);
}
/**
 * The following funtions return NULL if the queue is empty!
*/
Item pop(Queue* q){
    return D_popTail((DList*)q);
}
Item peek(Queue *q){
    return D_getItem(D_getTail((DList*)q));
}
/**
 * In this case, the data that we are sending are int*
 * (static) so we don't need to free them.
*/
void freeItem(Item i){
    return;
}
int main(){
    Queue *queue = createQueue();
    int arr[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    for(int i = 0; i<8; i+=2){
        push(queue, (Item)(arr+i+1));
        push(queue, (Item)(arr+i));
    }
    for(int i = 0; i<8; i++){
        printf("%d\n", *(int*)pop(queue));
    }
    deleteQueue(queue, freeItem);
    return 0;
}
```

Esta queue tem a capacidade de armazenar qualquer tipo de dados e uma complexidade de execução de O(1)!
O facto de ser realizada com listas permite que esta fila não tenha dimensão limite, o que acontece com um vetor, contudo, estas limitações podem ser implementadas com código posterior. É de notar que caso a queue esteja vazia, o pop/peek retornam NULL (consultar [[C.Lists]]).
***
# Priority Queue
