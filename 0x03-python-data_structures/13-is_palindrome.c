#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - function that checks if a singlyLL is a palindrome
 * @head: pointer to first element of LL
 *
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *middle_ptr;
	int len, idx, idxx, n_len;

	if (!(*head) || !(*head)->next)
		return (1);

	middle_ptr = *head;
	len = listint_len(*head);
	n_len = idx = (len / 2) + (len % 2);

	/* get the middle node */
	while (idx--)
		middle_ptr = middle_ptr->next;

	ptr = middle_ptr;
	idx = n_len;

	while (idx--)
	{
		idxx = idx;
		while (idxx--)
			ptr = ptr->next;

		if ((*head)->n != ptr->n)
			return (0);

		ptr = middle_ptr;
		*head = (*head)->next;
	}

	return (1);
}
