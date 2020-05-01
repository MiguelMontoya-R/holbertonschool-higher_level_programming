#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if there's a cycle in linked list
 * @list: the list to check
 * Return: 1 if cycle = true/ 0 if cycle = false
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *aux = list;

	aux = aux->next;
	while (aux && tmp && aux->next)
	{
		if (tmp == aux)
			return (1);
		aux = aux->next;
	}
	return (0);
}
