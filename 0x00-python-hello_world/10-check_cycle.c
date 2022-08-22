#include "lists.h"
#include <stdlib.h>

/**
* check_cycle - function that checks if a singly linked list has a cycle in it
* based on Floyd’s Cycle-Finding Algorithm
* @list: the head pointer
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = slow = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
