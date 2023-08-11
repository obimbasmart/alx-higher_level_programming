#include "lists.h"

/**
 * is_palindrome - function that checks if a singlyLL is a palindrome
 * @head: pointer to first element of LL
 *
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *middle_node;
	size_t node_count, middle_index;
	int idx;

	if (!(*head) || !(*head)->next)
		return (1);

	node_count = get_number_of_nodes(*head);
	middle_node = get_middle_node(*head);

	ptr = middle_node; /* used for looping */
	middle_index = (node_count / 2) + (node_count % 2); /* from 1 not 0 */

	while (middle_index--)
	{
		idx = middle_index;
		while (idx--)
			ptr = ptr->next; /* take ptr to last node */

		if ((*head)->n != ptr->n) /* then compare with first node (head) */
			return (0);

		ptr = middle_node; /* update ptr */
		*head = (*head)->next; /* shift head point to next node */
	}

	return (1);
}


/**
 * get_middle_node - return the middle node of a linked listint_t
 * @head: the head of the list
 *
 * Return: middle nod of listint_t *h
 */
listint_t *get_middle_node(const listint_t *head)
{
	int node_count, middle_index;
	listint_t *middle_node;

	middle_node = (listint_t *)head;
	if (!head)
		return (NULL);

	node_count = get_number_of_nodes(head);
	middle_index = node_count / 2;

	while (middle_index--)
		middle_node = middle_node->next;

	return (middle_node);
}


/**
 * get_number_of_nodes - returns the number of nodes in Linked list(LL)
 * @head: pointer to head of LL
 *
 * Return: int
 */
size_t get_number_of_nodes(const listint_t *head)
{
	size_t node_count = 0;
	listint_t *head_copy = (listint_t *)head;

	while (head_copy != NULL)
	{
		node_count++;
		head_copy = head_copy->next;
	}
	return (node_count);
}
