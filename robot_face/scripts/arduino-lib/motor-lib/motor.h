#include <Arduino.h>
#include <thread.h>
#include <Servo.h>

#ifndef Motor_h
#define Motor_h

class Motor{  
  public:
    void setMotorDefinitions( unsigned char startAngle, unsigned char beginLimit, unsigned char endLimit);
    void goTo(unsigned char angle);
    static void returnCount();
        
  private:
    static int counter;
    unsigned char checkRange(unsigned char targetPos);
    unsigned char limitAngle[2] = {5,175};
    Servo servo;
    
};

#endif

