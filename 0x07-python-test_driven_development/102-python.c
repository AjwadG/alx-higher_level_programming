#include <Python.h>
#include <object.h>
#include <unicodeobject.h>



/**
 * print_python_string - prints info about python strings opject
 * @p: pointer to pyobject
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %lu\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}
