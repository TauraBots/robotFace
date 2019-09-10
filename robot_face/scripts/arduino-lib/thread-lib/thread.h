#include <Arduino.h>
/*
  Thread_Manager.h - Library for use with multitasking simulation
*/

#ifndef Thread_h
#define Thread_h

class Thread {
  private:
    unsigned long time;
    unsigned long _msTimer;

  public:
    unsigned long logtime;

    Thread(unsigned long msTimer);
    void changeTimer(unsigned long new_msTimer);
    boolean gotTime();
    boolean timer();
    boolean refreshTime();
};

#endif
