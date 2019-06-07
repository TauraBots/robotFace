#include <Arduino.h>
#include <Thread_Manager.h>
#include <Servo.h>

/*
  Motor_Manager.h - Library for use with motor behaviour
*/

#ifndef Motor_h
#define Motor_h

class Motor{  
  public:
    void setMotorDefinitions( int startAngle, int beginLimit, int endLimit);
    void goTo(int angle);
    //void goToIn(int angle, unsigned long time);
    //boolean spinTime();
    //void spinMotor();
    static void returnCount();
        
  private:
    static int counter;
    int checkRange(int targetPos);
    int limitAngle[2] = {5,175};
    //int targetPos;
    //Thread thread = Thread(0);
    Servo servo;
    
};

#endif

