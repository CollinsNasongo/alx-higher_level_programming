#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle
 *
 * list: the list
 *
 * Return: 0 if there is no cycle and 1 otherwise
 */
int check_cycle(listint_t *list)
{
	const listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
