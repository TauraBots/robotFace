#include "motor.h"

int Motor::counter = 2;

void Motor::setMotorDefinitions(int startAngle, int beginLimit, int endLimit){
  servo.attach(counter++);
  limitAngle[0] = beginLimit;
  limitAngle[1] = endLimit;
  servo.write(checkRange(startAngle));
}

void Motor::goTo(int angle){
  servo.write(checkRange(angle));
}

int Motor::checkRange(int targetPos){
 if (targetPos <  limitAngle[0]){
   return limitAngle[0];
 }
 else if ( targetPos > limitAngle[1]){
   return limitAngle[1];
 }
 else return targetPos;
}

void Motor::returnCount(){
  Serial.println(counter);
}
