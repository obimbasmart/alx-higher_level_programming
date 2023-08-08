#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to first node
 * @number: integer data for new node
 *
 * Return: address of the new nod or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *back_node, *new_node;

	back_node = *head;
	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	/**
	 * if linked list is empty or head's data is less than
	 * new element's data, then we add new node at the begening of list
	 */
	if (*head == NULL || (*head)->n > number)
	{
		free(new_node);
		new_node = NULL;
		return (add_nodeint(head, number));
	}

	while (back_node)
	{
		if (back_node->next && (back_node->next)->n > number)
		{
			new_node->next = back_node->next;
			back_node->next = new_node;
			return (new_node);
		}
		back_node = back_node->next;
	}

	/**
	 * add new node at the end of list if new node's data is the smallest
	 */
	if (back_node == NULL)
	{
		free(new_node);
		new_node = NULL;
	}
	return (add_nodeint_end(head, number));
}


/**
 * add_nodeint - function that adds a new node
 * at the beginning of a list_t list
 * @head: pointer to first element of LL
 * @n: starting point of linked list
 *
 * Return: the address of the new node
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}
