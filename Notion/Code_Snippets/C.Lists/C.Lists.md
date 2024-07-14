**Estruturas apresentadas:**
Simple Linked Lists
Exemplo
Definição
Criação
Destruição
Acrescentar ao inicio/fim
Retirar Cabeça
Ponteiro para a Cabeça/Cauda
Próximo Nó
Ver Conteúdo
Trocar Conteúdo
Double Linked Lists
---
# Simple Linked Lists
**Download dos ficheiros** 📥**:**
![[linkedList_cs.zip]]
Código para listas simplesmente ligadas, apresentado abaixo.

> Listas simplesmente ligadas são estruturas de dados que contem conteúdo e estão ligadas umas ás outras através de um apontador.
![[Images/Untitled 3.png|Untitled 3.png]]

> Uma enorme vantagem desta estrutura é o facto de conseguirmos inserir dados (na cabeça ou cauda) sem sabermos o numero total de dados que teremos de inserir, pois basta concatenar nós à frente uns dos outros.
---
## Exemplo
```C
#include <string.h>
#include <stdio.h>
#include "linkedList.h"
//Compiling: gcc -o lists_example lists_example.c linkedList.c
/**
 * Item is a typedef for a void* (8B).
 * To convert other values to an Item you simply cast it: (Item)var.
 * To return to it's original type, you just cast it back! 
 * This allows this data structures not to be limited to a single datatype,
 * instead you can use the same .h file to store multiple different values.
 */
/**
 * This function is used to be parsed when deleting a list,
 * Since we are using the list as a strings list,
 * what this will do is simply free said string pointer
 * when an Item is parsed to it.
 */
void freeItem(Item i){
    free((char*)i);
}
int main(){
    //Initialization of the strings (to be used as example)
    char *str1 = (char*)malloc(50*sizeof(char));
    strcpy(str1, "Back in Time");
    char *str2 = (char*)malloc(50*sizeof(char));
    strcpy(str2, "Somewhere");
    //Creation of a list named Test
    List *test = createList();
    /**
     * Append the two strings at the end and start of the list,
		 * making it "look" like this:
     *                  (head) Somewhere <-> Back in Time (tail)
     */
    appendEnd(test, (Item)str1);
    appendStart(test, (Item)str2);
    /**
     * Using the popHead we get the content in the head node and delete said node
     * This Item was a string, so we have to free the allocated memory.
     */
    free(popHead(test));
    /** 
     * Now let's print the last string on the list.
     * Again we use the getHead function to get the pointer to the head node,
     * using that pointer we get it's content with the D_getItem,
		 * now all we have to do is cast the returned value back to a string (char*)
     */
    printf("%s\n", (char*)getItem(getHead(test)));
    //Deleting the list and freeing the allocated memory
    deleteList(test, freeItem);
    return 0;
}
```
---
## Definição
  
Esta estrutura de dados é composta por dois segmentos: a estrutura List, que nada mais é que o tipo de dados que irá albergar os ponteiros para a cabeça e causa da lista, e Node, que será cada nó individual da lista como se observa na imagem acima.
```C
typedef struct _node{
    Item content;
    struct _node *next;
}Node;
typedef struct _linkedList{
    struct _node *head;
    struct _node *tail;
}List;
```
---
```C
List *createList(){
    List *new = (List*)calloc(1, sizeof(List));
    if(new == NULL) return NULL;
    new->head = NULL; new->tail = NULL;
    return new;
}
```
## Criação
  
Inicia a estrutura da lista e retorna um apontador para a mesma. O conteúdo (cabeça da lista e cauda) é iniciado a NULL.
---
## Destruição
  
Função responsável pela libertação da memória, é esperado que uma função seja passada nos argumentos para libertar a memória alocada pelos dados guardados em cada nó.
```C
void deleteList(List *l, void (*freeItem)(Item i)){
    Node *aux1 = NULL, *aux2 = NULL;
    aux1 = l->head;
    while(aux1 != NULL){
        freeItem(aux1->content);
        aux2 = aux1;
        aux1 = aux1->next;
        free(aux2); aux2 = NULL;
    }
    free(l);
}
```
---
```C
void appendStart(List *l, Item i){
    Node *aux = NULL;
    if(l->head == NULL){
        l->head = createNode(i);
        l->tail = l->head;
        return;
    }else {
        aux = createNode(i);
        aux->next = l->head;
        l->head = aux;
        return;
    }
}
void appendEnd(List *l, Item i){
    Node *aux = NULL;
    if(l->head == NULL){
        l->head = createNode(i);
        l->tail = l->head;
        return;
    }else {
        aux = createNode(i);
        l->tail->next = aux;
        return;
    }
}
```
## Acrescentar ao inicio/fim
  
Junta um nó ao inicio ou fim da lista, respetivamente, colocando cada um dos novos nós como cabeça/cauda da lista. O conteúdo a acrescentar é um tipo de dados abstrato Item (void*).
  
É de notar, que caso a lista esteja vazia em qualquer um dos casos, é criado o primeiro nó, que será a cabeça e cauda.
---
## Retirar Cabeça
  
Retorna o conteúdo na cabeça da lista, eliminando o nó da mesma. Assim a nova cabeça passa a ser o nó seguinte.
```C
Item popHead(List *l){
    Node *node_aux = NULL;
    Item item_aux = NULL;
    if(l->head == NULL) return NULL;
    node_aux = l->head; item_aux = node_aux->content;
    l->head = l->head->next;
    free(node_aux); node_aux = NULL;
    //Does not free the head's content!!!
    return(item_aux);
}
```
---
```C
Node *getHead(List *l){
    if(l == NULL) return NULL;
    return l->head;
}
Node *getTail(List *l){
    if(l == NULL) return NULL;
    return l->tail;
}
```
## Ponteiro para a Cabeça/Cauda
  
Dada uma lista, retorna o ponteiro para a cabeça/cauda da mesma (Node*), em caso da lista estar vazia retorna NULL.
---
## Próximo Nó
  
Dado um Nó, retorna um ponteiro para o próximo nó.
```C
Node *getNext(Node *n){
    if(n == NULL) return NULL;
    return n->next;
}
```
---
```C
Item getItem(Node *n){
    if(n == NULL) return NULL;
    return n->content;
}
```
## Ver Conteúdo
  
Dado um nó retorna o seu conteúdo.
---
## Trocar Conteúdo
  
Dado um nó e novos dados, estes são trocados pelo conteúdo antigo que é retornado à saída da função.
```C
Item replaceItem(Node *n, Item i){
    Item aux = NULL;
    if(n == NULL) return NULL;
    aux = n->content;
    n->content = i;
    return aux;
}
```
---

> **Aviso à navegação:** A única vez que a memória ocupada pelos dados é libertada é quando eliminamos a lista por completo, assim as funções **replaceItem** e **popHead** não libertam esse conteúdo! Essa gestão de memória fica a cargo do utilizador.
- Código .h e .c completo
    
    ```C
    #ifndef _H_LINKEDLIST
    #define _H_LINKEDLIST
    
    /** @file linkedList.h
     *  @brief Icludes all the functions to create and manage a Simple Linked List Data Structure
     *  
     *      The lists created are linked to the next node and have a poointer to a void* (Item datatype),
     *      the lists have a pointer to the head and tail.
     *      This file incorporates the functions necessary to manage this data structure, listed bellow:
     * 
     *      # createList -------> Creates a Simple Linked List
     *      # deleteList -------> Deletes the list, freeing the allocated memory for the list aswell as for the Items
     *      # appendStart ------> Appends Item at the start of a list
     *      # appendEnd --------> Appends Item at the end of a list
     *      # popHead ----------> Return the content of the head of the list, deleting said node
     *      # getHead ----------> Returns a pointer to the Head Node
     *      # getTail ----------> Returns a pointer to the Tail Node
     *      # getNext ----------> Given a Node, returns the linked next one
     *      # getItem ----------> Returns the content in a Node
     * 
     *      The ability to append and remove Items at the start of the list allows this structure to be used as stack.
     *
     *  @author Filipe Piçarra (fpicarra)
     *  @bug No known bugs.
     */
    
    \#include <stdlib.h>
    
    typedef void* Item;
    
    typedef struct _linkedList List;
    
    typedef struct _node Node;
    
    /** @brief Creates a new List structure. 
     *
     *  The allocation of the structure is followed by it's initialization.
     *
     *  @return Pointer to a Simple Linked List Structure
     */
    List *createList();
    
    /** @brief Deletes a given list, freeing it's allocated memory. 
     *
     *  The content in each node is also freed!! This happens parsing a function that frres the Items stored in the list,
     *  if you don't want this to happen, simply parse a function that returns on entry.
     *
     *  @param l Pointer to list to be freed.
     *  @param freeItem Function that recieves an Item and frees the memory allocated by it, no matter the type, returns void.
     *  @return NONE
     */
    void deleteList(List *l, void (*freeItem)(Item i));
    
    /** @brief Appends an Item to the start of a list. This Item will be the new head.
     *
     *  @param l Pointer to list to be inserted an Item.
     *  @param i Item to be inserted.
     *  @return NONE
     */
    void appendStart(List *l, Item i);
    
    /** @brief Appends an Item to the end of a list. This Item will be the new tail.
     *
     *  @param l Pointer to list to be inserted an Item.
     *  @param i Item to be inserted.
     *  @return NONE
     */
    void appendEnd(List *l, Item i);
    
    /** @brief Removes the head Node, and returns it's content.
     * 
     *  The node following the head will be the new head.
     *
     *  @param l Pointer to list.
     *  @return Item in the head of the list, NULL if there is no head.
     */
    Item popHead(List *l);
    
    /** @brief Returns a pointer to the head node.
     *
     *  @param l Pointer to list.
     *  @return Pointer to the head of the list (*Node), NULL if there is no head.
     */
    Node *getHead(List *l);
    
    /** @brief Returns a pointer to the tail node.
     *
     *  @param l Pointer to list.
     *  @return Pointer to the tail of the list (*Node), NULL if there is no tail.
     */
    Node *getTail(List *l);
    
    /** @brief Given a node pointer, return a pointer to the next Node
     *
     *  @param n Pointer to Node.
     *  @return Pointer to the node following the one parsed, NULL if there is no next Node.
     */
    Node *getNext(Node *n);
    
    /** @brief Returns the content in a Node.
     *
     *  @param n Pointer to node.
     *  @return Content in the Node (Item)
     */
    Item getItem(Node *n);
    
    \#endif
    ```
    
    ```C
    \#include "linkedList.h"
    
    typedef struct _node{
        Item content;
        struct _node *next;
    }Node;
    
    typedef struct _linkedList{
        struct _node *head;
        struct _node *tail;
    }List;
    
    List *createList(){
        List *new = (List*)calloc(1, sizeof(List));
        if(new == NULL) return NULL;
    
        new->head = NULL; new->tail = NULL;
        return new;
    }
    
    void deleteList(List *l, void (*freeItem)(Item i)){
        Node *aux1 = NULL, *aux2 = NULL;
        aux1 = l->head;
        while(aux1 != NULL){
            freeItem(aux1->content);
            aux2 = aux1;
            aux1 = aux1->next;
            free(aux2); aux2 = NULL;
        }
        free(l);
    }
    
    Node *createNode(Item i){
        Node *new = (Node*)calloc(1, sizeof(Node));
        if(new != NULL){
            new->content = i;
            return new;
        }
        return NULL;
    }
    
    void appendStart(List *l, Item i){
        Node *aux = NULL;
        if(l->head == NULL){
            l->head = createNode(i);
            l->tail = l->head;
            return;
        }else {
            aux = createNode(i);
            aux->next = l->head;
            l->head = aux;
            return;
        }
    }
    
    void appendEnd(List *l, Item i){
        Node *aux = NULL;
        if(l->head == NULL){
            l->head = createNode(i);
            l->tail = l->head;
            return;
        }else {
            aux = createNode(i);
            l->tail->next = aux;
            return;
        }
    }
    
    Item popHead(List *l){
        Node *node_aux = NULL;
        Item item_aux = NULL;
    
        if(l->head == NULL) return NULL;
    
        node_aux = l->head; item_aux = node_aux->content;
        l->head = l->head->next;
        free(node_aux); node_aux = NULL;
        //Does not free the head's content!!!
        return(item_aux);
    }
    
    Node *getHead(List *l){
        if(l == NULL) return NULL;
        return l->head;
    }
    
    Node *getTail(List *l){
        if(l == NULL) return NULL;
        return l->tail;
    }
    
    Node *getNext(Node *n){
        if(n == NULL) return NULL;
        return n->next;
    }
    
    Item getItem(Node *n){
        if(n == NULL) return NULL;
        return n->content;
    }
    
    Item replaceItem(Node *n, Item i){
        Item aux = NULL;
        if(n == NULL) return NULL;
        aux = n->content;
        n->content = i;
        return aux;
    }
    ```
    
---
# Double Linked Lists
**Download dos ficheiros** 📥**:**
![[doubleLinkedList_cs.zip]]
Código para listas duplamente ligadas.
- Discrição e Funções
    
    nothing yet :(