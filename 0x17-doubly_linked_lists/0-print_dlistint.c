#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * print_dlistint - print all elements of list
 * @h: pointer to head of linked list
 * Return: Number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *ptr = h;
	size_t counter = 0;

	while (ptr)
	{
		printf("%d\n", ptr->n);
		ptr = ptr->next;
		counter++;
	}
	return (counter);
}
