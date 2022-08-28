#include <Python.h>

/**
* print_python_list_info - Prints basic info about Python lists.
* @p: A PyObject list
*
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	int size, allocate, n;
	PyObject *obj;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (n = 0; n < size; n++)
	{
		printf("Element %d: ", n);

		obj = PyList_GetItem(p, n);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
