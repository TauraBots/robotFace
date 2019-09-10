#include "thread.h"

Thread::Thread(unsigned long msTimer) {
  _msTimer = msTimer;
  time = 0;
  logtime = 0;
}

void Thread::changeTimer(unsigned long new_msTimer) {
  _msTimer = new_msTimer;
}

boolean Thread::gotTime() {
  return (timer() == true) ? refreshTime() : false;
}

boolean Thread::timer() {
  return (time < millis()) ? true : false;
}
boolean Thread::refreshTime() {
  time = millis() + _msTimer;
  return true;
}
