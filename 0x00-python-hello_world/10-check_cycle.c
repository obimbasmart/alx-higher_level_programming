#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: the hed node of the linked list
 *
 * Return: 1 if there's a cycle. 0 if not
 */
int check_cycle(listint_t *list)
{

	listint_t *fastptr, *slowptr;

	fastptr = slowptr = list;

	while (list && fastptr && slowptr)
	{
		slowptr = slowptr->next;
		fastptr = fastptr->next->next;

		if (slowptr == fastptr)
			return (1);
	}

	return (0);
}



