#include "lists.h"

/**
 *Check_cycke - checks if a singly linked list has a cycle in it.
 *@list: listin_t
 *Return: boolean
 *
 */


int check_cycle(listint_t *list)
{

	listint_t *ptr;

	if (list)
	{
		while (list != NULL)
		{
			ptr = list;
			list = list->next;
			if (ptr <= list)
				return (1);
		}
		return (0);
	}
	return (0);

}
