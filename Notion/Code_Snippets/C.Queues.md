---
# Fila Simples (FIFO)

## Summary
> [!important]  
> Complexidade Computacional: O(1) - Inserção e Retirada  
Com recurso ás listas duplamente ligadas, conseguimos criar uma nova estrutura de dados: as Queues ou Filas, com uma organização FIFO - First-In-First-Out. Para tal são criadas 5 novas funções, que nada mais são do que uma adaptação das funções declaradas em “doubleLinkedList.h”, como abaixo.

> Para o seguinte exemplo de construção e utilização de filas simples foram utilizados os recursos disponibilizados para gestão de listas duplamente ligadas em [[C.Lists]].
## Code
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
# Priority Queue w/ Hash Table
## Summary

### Time Complexities:
- **Insertion**: O(log n)
- **Extraction**: O(log n)
- **Priority Change**: O(log n)
- **Hash Table Operations**: O(1)
### Memory Complexities:
- **Binary Heap**: O(n)
- **Hash Table**: O(m)
- **Total Memory**: O(n + m)
### Pros:
- Efficient insertions and deletions.
- O(1) priority changes due to hash table.
- Flexible and dynamic resizing.
- Generic pointer storage.
### Cons:
- Additional memory overhead.
- Increased complexity in implementation.
- Potential for hash collisions.
- Higher memory usage for large hash table sizes.

This implementation is suitable for scenarios where efficient priority changes are crucial and the additional memory overhead is acceptable.

## Code
```C
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct {
    void *data;
    int priority;
} HeapNode;

typedef struct {
    void *data;
    int index;
} HashEntry;

typedef struct {
    HeapNode *nodes;
    int capacity;
    int size;
    HashEntry **hashTable;
    int hashTableSize;
} BinaryHeap;

BinaryHeap* createHeap(int capacity, int hashTableSize) {
    BinaryHeap *heap = (BinaryHeap *)malloc(sizeof(BinaryHeap));
    if (!heap) return NULL;
    heap->capacity = capacity;
    heap->size = 0;
    heap->nodes = (HeapNode *)malloc(sizeof(HeapNode) * capacity);
    if (!heap->nodes) {
        free(heap);
        return NULL;
    }
    heap->hashTableSize = hashTableSize;
    heap->hashTable = (HashEntry **)calloc(hashTableSize, sizeof(HashEntry *));
    if (!heap->hashTable) {
        free(heap->nodes);
        free(heap);
        return NULL;
    }
    return heap;
}

int hashFunction(void *data, int hashTableSize) {
    return ((uintptr_t)data) % hashTableSize;
}

void insertHashEntry(BinaryHeap *heap, void *data, int index) {
    int hashIndex = hashFunction(data, heap->hashTableSize);
    HashEntry *entry = (HashEntry *)malloc(sizeof(HashEntry));
    entry->data = data;
    entry->index = index;
    heap->hashTable[hashIndex] = entry;
}

void removeHashEntry(BinaryHeap *heap, void *data) {
    int hashIndex = hashFunction(data, heap->hashTableSize);
    free(heap->hashTable[hashIndex]);
    heap->hashTable[hashIndex] = NULL;
}

int getHashIndex(BinaryHeap *heap, void *data) {
    int hashIndex = hashFunction(data, heap->hashTableSize);
    if (heap->hashTable[hashIndex] && heap->hashTable[hashIndex]->data == data) {
        return heap->hashTable[hashIndex]->index;
    }
    return -1; // Not found
}

void heapifyUp(BinaryHeap *heap, int index) {
    int parentIndex = (index - 1) / 2;
    while (index > 0 && heap->nodes[index].priority > heap->nodes[parentIndex].priority) {
        HeapNode temp = heap->nodes[index];
        heap->nodes[index] = heap->nodes[parentIndex];
        heap->nodes[parentIndex] = temp;

        insertHashEntry(heap, heap->nodes[index].data, index);
        insertHashEntry(heap, heap->nodes[parentIndex].data, parentIndex);

        index = parentIndex;
        parentIndex = (index - 1) / 2;
    }
}

void insert(BinaryHeap *heap, void *data, int priority) {
    if (heap->size == heap->capacity) {
        heap->capacity *= 2;
        heap->nodes = (HeapNode *)realloc(heap->nodes, sizeof(HeapNode) * heap->capacity);
        if (!heap->nodes) return;
    }

    int index = heap->size++;
    heap->nodes[index].data = data;
    heap->nodes[index].priority = priority;

    insertHashEntry(heap, data, index);
    heapifyUp(heap, index);
}

void heapifyDown(BinaryHeap *heap, int index) {
    int leftChild = 2 * index + 1;
    int rightChild = 2 * index + 2;
    int largest = index;

    if (leftChild < heap->size && heap->nodes[leftChild].priority > heap->nodes[largest].priority) {
        largest = leftChild;
    }

    if (rightChild < heap->size && heap->nodes[rightChild].priority > heap->nodes[largest].priority) {
        largest = rightChild;
    }

    if (largest != index) {
        HeapNode temp = heap->nodes[index];
        heap->nodes[index] = heap->nodes[largest];
        heap->nodes[largest] = temp;

        insertHashEntry(heap, heap->nodes[index].data, index);
        insertHashEntry(heap, heap->nodes[largest].data, largest);

        heapifyDown(heap, largest);
    }
}

void* extractMax(BinaryHeap *heap) {
    if (heap->size == 0) return NULL;

    void *maxData = heap->nodes[0].data;

    removeHashEntry(heap, maxData);

    heap->nodes[0] = heap->nodes[--heap->size];

    insertHashEntry(heap, heap->nodes[0].data, 0);

    heapifyDown(heap, 0);

    return maxData;
}

void changePriority(BinaryHeap *heap, void *data, int newPriority) {
    int index = getHashIndex(heap, data);
    if (index == -1) return;

    int oldPriority = heap->nodes[index].priority;
    heap->nodes[index].priority = newPriority;

    if (newPriority > oldPriority) {
        heapifyUp(heap, index);
    } else {
        heapifyDown(heap, index);
    }
}

int main() {
    BinaryHeap *heap = createHeap(10, 20);

    int data1 = 5, data2 = 10, data3 = 3;
    insert(heap, &data1, 2);
    insert(heap, &data2, 5);
    insert(heap, &data3, 1);

    printf("Change priority of data3 (3) to 6\n");
    changePriority(heap, &data3, 6);

    int *maxData = (int *)extractMax(heap);
    printf("Max data: %d\n", *maxData);

    maxData = (int *)extractMax(heap);
    printf("Max data: %d\n", *maxData);

    maxData = (int *)extractMax(heap);
    printf("Max data: %d\n", *maxData);

    free(heap->nodes);
    for (int i = 0; i < heap->hashTableSize; i++) {
        if (heap->hashTable[i]) free(heap->hashTable[i]);
    }
    free(heap->hashTable);
    free(heap);

    return 0;
}

```