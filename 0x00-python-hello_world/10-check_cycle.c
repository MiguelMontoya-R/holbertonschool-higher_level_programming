#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *aux = list;

	aux = aux->next;
	while (aux)
	{
		if (tmp == aux)
			return (1);
		aux = aux->next;
	}
	return (0);
}
