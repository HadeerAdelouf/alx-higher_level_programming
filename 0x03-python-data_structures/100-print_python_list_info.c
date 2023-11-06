#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 *
 */
void print_python_list_info(PyObject *p)
{
	int Size, alloc, i;
	PyObject *obj;

	Size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", Size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < Size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
