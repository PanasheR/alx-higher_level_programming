#include "lists.h"

/**
 * check_cylce - a function that checks if a singly linked list has a
 * cycle in it
 * @list: the list to check
 *
 * Return: 1, if a cycle is present or 0, if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *made = list;
	listint_t *hide = list;

	while (hide && made && made->next)
	{
		hide = hide->next;
		made = made->next->next;

		if (made == hide)
			return (1);
	}

	return (0);
}
