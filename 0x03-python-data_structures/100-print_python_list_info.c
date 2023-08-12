#include <stdio.h>
#include <python3.4/Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @py_obj: a python object of type PyObject, to be casted to PyListObject
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *py_obj)
{
	int id;

	PyListObject *list = (PyListObject *)py_obj;

	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (id = 0; id < list->ob_base.ob_size; id++)
	{
		printf("Element %d: %s\n", id, list->ob_item[id]->ob_type->tp_name);
	}
}

