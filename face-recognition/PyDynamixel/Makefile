all: _pydynamixel.so

_pydynamixel.so: dxl_hal.o dynamixel.o pydynamixel_wrap.o
	ld -shared dxl_hal.o dynamixel.o pydynamixel_wrap.o -o _pydynamixel.so

pydynamixel_wrap.c: pydynamixel.i
	swig -python pydynamixel.i

%.o: %.c
	gcc -fPIC -c $^ -I. -I/usr/include/python2.7

clean:
	rm -rf pydynamixel.py pydynamixel_wrap.c dxl_hal.o dynamixel.o pydynamixel_wrap.o _pydynamixel.so *.pyc

