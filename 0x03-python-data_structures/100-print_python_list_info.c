#define PY_SSIZE_T_CLEAN
#include "Python.h"

/**
 * print_python_list_info - prints info about Python lists.
 * @p: pointer to head of list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	long int i, count = list->ob_base.ob_size;
	const char *type;

	printf("[*] Size of the Python List = %ld\n", count);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < count; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}
