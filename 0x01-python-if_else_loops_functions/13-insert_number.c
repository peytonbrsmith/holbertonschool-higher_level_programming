#include "lists.h"
/**
 * insert_node - inserts a node in order of integer value
 * @head: pointer to the head
 * @number: integer
 *
 * Return: pointer to new node or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *current = *head;
	int notbeg = 0; /* checks if it needs to be the head */

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = temp;
		temp->n = number;
		temp->next = NULL;
		return (temp);
	}
	while (current != NULL && number > current->n)
	{
		notbeg = 1;
		if (current->next != NULL)
		{
			if (number < current->next->n)
				break;
			current = current->next;
		}
		else
			break;
	}
	temp->n = number;
	if (notbeg == 1)
	{
		temp->next = current->next;
		current->next = temp;
	}
	else
	{
		temp->next = current;
		*head = temp;
	}
	return (temp);
}
