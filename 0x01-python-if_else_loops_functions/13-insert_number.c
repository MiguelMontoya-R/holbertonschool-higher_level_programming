#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *tmp = *head;
    listint_t *new_node;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    if (*head == NULL)
    {
        *head = new_node;
        new_node->n = number;
        new_node->next = tmp->next;
        return (new_node);
    }
    while (tmp)
    {
        if (tmp->next->n >= number)
        {
            new_node->n = number;
            new_node->next = tmp->next;
            tmp->next = new_node;
            break;
        }
        tmp = tmp->next;
    }
    return (new_node);
} 