#include "lists.h"

/**
 * is_palindrome - function that checks if a singlyLL is a palindrome
 * @head: pointer to first element of LL
 *
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *middle_ptr;
	size_t len, n_len;
	int idx, idxx;

	if (!(*head) || !(*head)->next)
		return (1);

	middle_ptr = *head;
	len = listint_len(*head);
	n_len = (len / 2) + (len % 2);
	idx = n_len;

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


/**
 * listint_len - return the number of elements in a linked listint_t
 * @h: the head of the list
 *
 * Return: the number of nodes in the list
 */
size_t listint_len(const listint_t *h)
{
	unsigned int n_nodes;

	n_nodes = 0;

	if (h == NULL)
	{
		return (0);
	}

	else
	{
		do {
			n_nodes++;
			h = h->next;
		} while (h != NULL);
	}
	return (n_nodes);
}
