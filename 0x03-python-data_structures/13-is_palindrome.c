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
	static int pal[1024];
	int i, j;
	listint_t *current;

	if (!head || !*head)
		return (1);
	for (i = 0, current = *head; current != NULL; i++)
		current = current->next;
	for (j = 0, i -= 1, current = *head; current != NULL; j++, i--)
	{
		if (j <= i)
			pal[j] = current->n;
		else if (pal[i] != current->n)
			return (0);
		current = current->next;
	}
	return (1);
}
