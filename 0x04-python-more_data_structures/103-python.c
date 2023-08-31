#include "Python.h"

void print_python_bytes(PyObject *p)
{
	size_t b_size, idx;

	PyBytesObject *byte_obj = (PyBytesObject *)p;
	b_size = byte_obj->ob_base.ob_size;

	printf("[.] bytes object info\n");
	printf("  size: %lu\n", b_size);
	printf("  trying string: %s\n", byte_obj->ob_sval);

	printf("  first %lu bytes: ", (b_size > 9) ? 10 : b_size + 1);
	for (idx = 0; idx < b_size; idx++)
	{
		if (idx > 8)
			break;

		printf("%02x ", byte_obj->ob_sval[idx]);
	}
	printf("%02x\n", byte_obj->ob_sval[idx]);

}

void print_python_list(PyObject *p)
{
	size_t l_size, idx;
	char *tp_name;

	PyListObject *list_obj = (PyListObject *)p;
	l_size = list_obj->ob_base.ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", l_size);
	printf("[*] Allocated = %lu\n", list_obj->allocated);

	for (idx = 0; idx < l_size; idx++)
	{
		tp_name = (char *) list_obj->ob_item[idx]->ob_type->tp_name;
		printf("Element %lu: %s\n", idx, tp_name);

		if (strcmp("bytes", tp_name) == 0)
			print_python_bytes(list_obj->ob_item[idx]);
	}
}

