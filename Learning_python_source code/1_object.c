The object.h file defined what a python object is and the source code is commented 
in a proper way to make it easy to read. intoobject.h showed int object.

	/* Nothing is actually declared to be a PyObject, but every pointer to
	* a Python object can be cast to a PyObject*.  This is inheritance built
	* by hand.  Similarly every pointer to a variable-size Python object can,
	* in addition, be cast to PyVarObject*.
	*/
	typedef struct _object {
		PyObject_HEAD
	} PyObject;
	
	/* PyObject_HEAD defines the initial segment of every PyObject. */
	#define PyObject_HEAD                   \
		_PyObject_HEAD_EXTRA                \
		Py_ssize_t ob_refcnt;               \
		struct _typeobject *ob_type;
	
	/* Define pointers to support a doubly-linked list of all live heap objects. */
	#define _PyObject_HEAD_EXTRA            \
		struct _object *_ob_next;           \
		struct _object *_ob_prev;
		
This structure is elementary block for all python object. PyObject is just a struct
contains PyObject_HEAD. PyVarObject is similar.

	typedef struct {
		PyObject_VAR_HEAD
	} PyVarObject;
	
	/* PyObject_VAR_HEAD defines the initial segment of all variable-size
	* container objects.  These end with a declaration of an array with 1
	* element, but enough space is malloc'ed so that the array actually
	* has room for ob_size elements.  Note that ob_size is an element count,
	* not necessarily a byte count.
	*/
	#define PyObject_VAR_HEAD               \
		PyObject_HEAD                       \
		Py_ssize_t ob_size; /* Number of items in variable part */
	#define Py_INVALID_SIZE (Py_ssize_t)-1
	
type pointer is the way to give type information of an object:

	typedef struct _typeobject {
		PyObject_VAR_HEAD
		const char *tp_name; /* For printing, in format "<module>.<name>" */
		Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */
	
		/* Methods to implement standard operations */
	
		destructor tp_dealloc;
		printfunc tp_print;
		getattrfunc tp_getattr;
		setattrfunc tp_setattr;
		cmpfunc tp_compare;
		reprfunc tp_repr;
	
		/* Method suites for standard classes */
	
		PyNumberMethods *tp_as_number;
		PySequenceMethods *tp_as_sequence;
		PyMappingMethods *tp_as_mapping;
	
		/* More standard operations (here for binary compatibility) */
	
		hashfunc tp_hash;
		ternaryfunc tp_call;
		reprfunc tp_str;
		getattrofunc tp_getattro;
		setattrofunc tp_setattro;
	
		/* Functions to access object as input/output buffer */
		PyBufferProcs *tp_as_buffer;
	
		/* Flags to define presence of optional/expanded features */
		long tp_flags;
	
		const char *tp_doc; /* Documentation string */
	
		/* Assigned meaning in release 2.0 */
		/* call function for all accessible objects */
		traverseproc tp_traverse;
	
		/* delete references to contained objects */
		inquiry tp_clear;
	
		/* Assigned meaning in release 2.1 */
		/* rich comparisons */
		richcmpfunc tp_richcompare;

		/* weak reference enabler */
		Py_ssize_t tp_weaklistoffset;
	
		/* Added in release 2.2 */
		/* Iterators */
		getiterfunc tp_iter;
		iternextfunc tp_iternext;
	
		/* Attribute descriptor and subclassing stuff */
		struct PyMethodDef *tp_methods;
		struct PyMemberDef *tp_members;
		struct PyGetSetDef *tp_getset;
		struct _typeobject *tp_base;
		PyObject *tp_dict;
		descrgetfunc tp_descr_get;
		descrsetfunc tp_descr_set;
		Py_ssize_t tp_dictoffset;
		initproc tp_init;
		allocfunc tp_alloc;
		newfunc tp_new;
		freefunc tp_free; /* Low-level free-memory routine */
		inquiry tp_is_gc; /* For PyObject_IS_GC */
		PyObject *tp_bases;
		PyObject *tp_mro; /* method resolution order */
		PyObject *tp_cache;
		PyObject *tp_subclasses;
		PyObject *tp_weaklist;
		destructor tp_del;
	
		/* Type attribute cache version tag. Added in version 2.6 */
		unsigned int tp_version_tag;
	
	#ifdef COUNT_ALLOCS
		/* these must be last and never explicitly initialized */
		Py_ssize_t tp_allocs;
		Py_ssize_t tp_frees;
		Py_ssize_t tp_maxalloc;
		struct _typeobject *tp_prev;
		struct _typeobject *tp_next;
	#endif
	} PyTypeObject;

A basic python object is a C struct variable that contains object reference count
and a pointer to indicate object type. And from definiton of Pytypeobject in 
object.h I thinke the type is just indicated by a name in type 'string'. I
think this is consistent with python's duck type as type is just a string and
all object has same method could be used as similar object.

If the object is a container of many element, PyObject_VAR_HEAD would be used
and it contains one more information(the size of the object). I think this 
is because no sting type or list which could contain arbitrary type in C and so
container object has to maintain the size information explicity.

An object has to include PyObject_HEAD and this is kind of inheritance. An
object also has to contain its own information. For example, the int object
in python:

	typedef struct {
		PyObject_HEAD
		long ob_ival;
	} PyIntObject;
	
It contains a long type variable and I guess it should be the value of this 
python int object. This explains why long in python is just a special case of
int. But I am not quite sure how some very large number could be stored in 
PyIntObject......

So, I know that why all python object is an instance of object(new style class)
now.



