#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if singly linked list is a palindrome
 *
 * @head: double pointer to the list
 *
 * Return: 1 if true and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = get_len(*head);
	int mid = len / 2;
	int front_idx = 0;
	int back_idx = len - 1;

	while (front_idx != (mid + 1))
	{
		if (get_num(*head, front_idx) != get_num(*head, back_idx))
			return (0);
		front_idx++;
		back_idx--;
	}
	return (1);
}

/**
 * get_len - Get number of elements in a list
 *
 * @h: pointer to first element on list
 *
 * Return: Length of list
 */
int get_len(const listint_t *h)
{
	int len = 0;

	while (h != NULL)
	{
		len++;
		h = h->next;
	}
	return (len);
}

/**
 * get_num - Get the number at a given index (from 0)
 *
 * @h: pointer to the head
 * @idx: the index
 *
 * Return: the number at the index
 */
int get_num(listint_t *h, int idx)
{
	listint_t *current = h;
	int len = get_len(h);
	int count = 0;

	if (idx > (len - 1))
		return (0);
	while (h)
	{
		if (idx == count)
			return (current->n);
		count++;
		current = current->next;
	}
	return (0);
}
