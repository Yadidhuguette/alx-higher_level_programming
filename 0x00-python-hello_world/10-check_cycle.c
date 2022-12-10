#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: singly linked list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *li, *row;

	if (list == NULL || list->next == NULL)
		return (0);

	li = list->next;
	row = list->next->next;

	while (li && row && row->next)
	{
		if (li == row)
			return (1);

		li = li->next;
		row = row->next->next;
	}

	return (0);
}
