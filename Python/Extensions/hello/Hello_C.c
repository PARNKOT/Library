#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include <math.h>
#include <stdio.h>


static PyObject* hello(PyObject* self) {
   return Py_BuildValue("s", "Hello, Python extensions!!");
}

static PyObject* test(PyObject* self, PyObject* args) {
   int n;
   double* arr;

   if(!PyArg_ParseTuple(args, "n", &n)) {
      return NULL;
   }

   arr = (double*)malloc(sizeof(double)*n);

   for(int i = 0; i < n; ++i) {
      double t = tan(i);
      arr[i] = t;
      //printf("tan(%d) : %f\n", i, t);
   }


   PyObject* ret = Py_BuildValue("(items)", arr);
   free(arr);
   return ret;

}

static char helloworld_docs[] =
   "hello( ): Any message you want to put here!!\n";

static PyMethodDef helloworld_funcs[] = {
   {"hello", (PyCFunction)hello, 
      METH_NOARGS, helloworld_docs},
   {"test", (PyCFunction)test, METH_VARARGS, "test(): just test ;)"},
   {NULL}
};

static struct PyModuleDef helloworldmodule = {
    PyModuleDef_HEAD_INIT,
    "helloworld",
    helloworld_docs,
    -1,
    helloworld_funcs
};

PyMODINIT_FUNC PyInit_helloworld(void) {
   return PyModule_Create(&helloworldmodule);
}
