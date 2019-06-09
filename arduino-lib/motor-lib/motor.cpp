#include "motor.h"

int Motor::counter = 2;

void Motor::setMotorDefinitions(unsigned char startAngle, unsigned char beginLimit, unsigned char endLimit){
  servo.attach(counter++);
  limitAngle[0] = beginLimit;
  limitAngle[1] = endLimit;
  servo.write(checkRange(startAngle));
}

void Motor::goTo(unsigned char angle){
  servo.write(int(checkRange(angle)));
}

unsigned char Motor::checkRange(unsigned char targetPos){
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
