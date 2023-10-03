#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	if (!head)
		return (NULL);
	tmp = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (new);

	new->n = number;

	if (*head == NULL || tmp->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (tmp->next != NULL && tmp->next->n < number)
			tmp = tmp->next;
		new->next = tmp->next;
		tmp->next = new;
	}

	return (new);
}
