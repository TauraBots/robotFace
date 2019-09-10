/*
   This is the SWIG interface for creating
   Python modules (and possibly other
   languages
*/
%define DOCSTRING
"The PyDynamixel module implements some low level
Dynamixel communication protocol functions"
%enddef

%module(docstring=DOCSTRING) pydynamixel

%typemap(in) int * {
  if (PyList_Check($input)) {
    int size = PyList_Size($input);
    int i = 0;
    $1 = (int *)malloc((size)*sizeof(int));
    for (i = 0 ; i < size ; i++) {
      PyObject *o = PyList_GetItem($input,i);
      if (PyInt_Check(o))
        $1[i] = (int)PyInt_AsLong(PyList_GetItem($input, i));
      else {
        PyErr_SetString(PyExc_TypeError, "list must contain integers");
        free($1);
        return NULL;
      }
    }
  } else {
    PyErr_SetString(PyExc_TypeError, "not a list");
    return NULL;
  }
}

%typemap(freearg) int * {
  free($1);
}


%feature("autodoc", "0");

%{

extern int initialize(char *dev_name, int baudnum);
extern void terminate(int socket);
extern void ping(int socket, int id);
extern int read_byte(int socket, int id, int address);
extern void write_byte(int socket, int id, int address, int value);
extern int read_word(int socket, int id, int address);
extern void write_word(int socket, int id, int address, int value);
extern void sync_write_word(int socket, int first_address,
                                int *ids, int *values, int total);
%}

%feature("docstring") initialize
"This method attempts to open dev_name with the
provided baudnum. Notice baudrate=2Mbps/(baudnum+1).
The return value is the socket number reference. The
socket number must be passed as an argument to the
subsequent communcation methods. If it fails to
open the socket then it returns 0"

%feature("docstring") terminate
"Closes the socket"

%feature("docstring") ping
"Implements the ping command"

%feature("docstring") read_byte
"Reads one byte from the servomotor"

%feature("docstring") write_byte
"Writes one byte to the servomotor"

%feature("docstring") read_word
"Reads a two byte word from the servomotor"

%feature("docstring") write_word
"Writes a two byte word to the servomotor"

%feature("docstring") sync_write_word
"Writes a two byte word to several servomotors
in synchronization. The argument ids should be
a list of integers representing the id of each
servomotor, and values should be a list of same
size with the respective values to be written.
The argument total is simply the length of the
list."

extern int initialize(char *dev_name, int baudnum);
extern void terminate(int socket);
extern void ping(int socket, int id);
extern int read_byte(int socket, int id, int address);
extern void write_byte(int socket, int id, int address, int value);
extern int read_word(int socket, int id, int address);
extern void write_word(int socket, int id, int address, int value);
extern void sync_write_word(int socket, int first_address,
                                int *ids, int *values, int total);

