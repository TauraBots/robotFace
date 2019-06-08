#include <Arduino.h>
#include <Thread_Manager.h>
#include <Servo.h>

#ifndef Motor_h
#define Motor_h

class Motor{  
  public:
    void setMotorDefinitions( int startAngle, int beginLimit, int endLimit);
    void goTo(int angle);
    static void returnCount();
        
  private:
    static int counter;
    int checkRange(int targetPos);
    int limitAngle[2] = {5,175};
    Servo servo;
    
};

#endif

