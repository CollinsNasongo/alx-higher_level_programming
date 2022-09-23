#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - insert number in sorted linked list
 *
 * head: pointer to pointer to the head of list
 * number: the number
 *
 * Return: address of new node or NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *next_val = (*head)->next;
	listint_t *current = *head;

	if (new == NULL || head == NULL)
		return (NULL);

	while (*head != NULL)
	{
		if (next_val->n < number)
		{
			current = current->next;
			next_val = next_val->next;
		}
		else
		{
			new->n = number;
			new->next = next_val;
			current->next = new;
			return (new);
		}
	}
	return (NULL);
}

