#ifndef LISTS_H
#define LISTS_H

/**
* struct listint_s - singly linked list
* @n: integer variable
* @next: pointer to the next node
*
* Description: structure for singly linked list node
*/
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;


int check_cycle(listint_t *list);

#endif
