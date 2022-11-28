#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 * @list: Linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *first = list;

	if (!list)
		return (0);

	while (slow && first && first->next)
	{
		slow = slow->next;
		first = first->next->next;
		if (slow == first)
			return (1);
	}

	return (0);
}
