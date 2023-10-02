#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if the linked list have a cycle
 * @list: pointer to head of list
 * Return: 1 if cycle 0 otehr wise
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (list)
	{
		if (!list->next)
			break;
		list = list->next->next;
		tmp = tmp->next;
		if (tmp == list)
			return (1);
	}

	return (0);
}
