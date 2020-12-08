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
	listint_t *current;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
	{
		return (NULL);
	}
	if (*head == NULL)
	{
		*head = temp;
		temp->n = number;
		temp->next = NULL;
		return (temp);
	}
	current = *head;
	while (current != NULL && number > current->n)
	{
		if (current->next != NULL)
		{
			if (number < current->next->n)
				break;
			current = current->next;
		}
		else
			break;
	}
	temp->next = current->next;
	temp->n = number;
	current->next = temp;
	return (temp);
}
