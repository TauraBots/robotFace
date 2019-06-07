#include "Motor.h"

int Motor::counter = 2;

void Motor::setMotorDefinitions(int startAngle, int beginLimit, int endLimit){
  servo.attach(counter++);
  limitAngle[0] = beginLimit; 
  limitAngle[1] = endLimit;
  servo.write(checkRange(angle));
  //spinTime();
  //servo.write(targetPos = checkRange(startAngle));
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

/*
void Motor::goToIn(int angle, unsigned long time){
  targetPos = checkRange(angle);
  unsigned long var= (servo.read()-angle > 0 ) ? servo.read()-angle : angle-servo.read();
  thread.changeTimer(time/var);
  spinTime();
}
boolean Motor::spinTime(){
  return thread.gotTime(); 
}
void Motor::spinMotor(){
  int aux = servo.read();
  if(aux < targetPos){
   aux++;
  }
  else if (aux > targetPos){
   aux--;
  }
  servo.write(aux);
  Serial.println(millis() - thread.logtime);
  thread.logtime = millis();
}
*/

void Motor::returnCount(){
  Serial.println(counter);
}
