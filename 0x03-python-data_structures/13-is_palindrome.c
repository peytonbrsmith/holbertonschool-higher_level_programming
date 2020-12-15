#include "lists.h"
/**
 * is_palindrome - detects palindromic singly linked lists
 * @head: head of the list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *cmpcpy;
	listint_t *cpy;
	unsigned int len, i;

	if (head == NULL)
		return (1);
	cpy = *head;
	cmpcpy = *head;
	for (len = 0; cmpcpy->next != NULL; len++)
		cmpcpy = cmpcpy->next;
	while (len > 0)
	{
		if (cpy->n == cmpcpy->n)
		{
			len--;
			cpy = cpy->next;
			cmpcpy = *head;
			for (i = len; i > 0; i--)
				cmpcpy = cmpcpy->next;
		}
		else
			break;
	}
	if (cpy->n == cmpcpy->n)
		return (1);
	return (0);
}
