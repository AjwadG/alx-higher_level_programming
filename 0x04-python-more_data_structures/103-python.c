#define PY_SSIZE_T_CLEAN
#include "Python.h"


/**
 * print_python_bytes - prints info about Python lists.
 * @p: pointer to head of list
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *list = (PyBytesObject *) p;
	long int i, size = list->ob_base.ob_size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", list->ob_sval);
	size = size < 10 ? size + 1 : 10;
	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
	{
		printf(" %2.2x", list->ob_sval[i] & 0xff);
	}
	putchar('\n');
}



/**
 * print_python_list - prints info about Python lists.
 * @p: pointer to head of list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	long int i, count = list->ob_base.ob_size;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", count);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < count; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (PyBytes_Check((PyObject *) list->ob_item[i]))
			print_python_bytes((PyObject *) list->ob_item[i]);
	}
}

