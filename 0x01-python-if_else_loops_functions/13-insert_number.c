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
    new_node->n = number;
    if (*head == NULL || tmp->n >= new_node->n)
    {
        *head = new_node;
        new_node->next = *head;
    }
    else
    {   
        while (tmp->next)
        {
            if (tmp->next->n >= new_node->n)
                break;
            tmp = tmp->next;
        }
        new_node->next = tmp->next;
        tmp->next = new_node;
    }
    return (new_node);
}