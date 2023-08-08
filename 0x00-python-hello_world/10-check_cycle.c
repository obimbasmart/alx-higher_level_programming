#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle
 * @list: the head node of the linked list
 *
 * Return: 1 if there's a cycle. 0 if not
 */
int check_cycle(listint_t *list)
{

	listint_t *fastptr, *slowptr;

	if (!list)
		return (0);

	slowptr = fastptr = list;
	if (!slowptr->next)
		return (0);

	slowptr = slowptr->next;

	while (fastptr && (fastptr = fastptr->next))
	{
		fastptr = fastptr->next; /* move fastptr again */

		if (slowptr == fastptr) /* check for convergence */
			return (1);

		slowptr = slowptr->next;
	}
	return (0);
}



