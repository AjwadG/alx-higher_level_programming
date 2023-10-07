#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if the list is a palindrome.
 * @head: pointer to head of list
 * Return: 1 if palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int *pal, i, j;
	listint_t *current;

	if (!head || !*head)
		return (1);
	for (i = 0, current = *head; current->next != NULL; i++)
		current = current->next;
	pal = malloc(sizeof(int) * i + 1);
	for (i = 0, current = *head; current != NULL; i++)
	{
		pal[i] = current->n;
		current = current->next;
	}
	for (j = 0, i -= 1; i >= j; j++, i--)
	{
		if (pal[i] != pal[j])
		{
			free(pal);
			return (0);
		}
	}
	free(pal);
	return (1);
}
