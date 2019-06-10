#include <motor.h>
#include <thread.h>
#include <DynamixelProtocol.h>
#include <Servo.h>

#define ID 128
#define BAUDRATE 1000000

enum motors : byte {
  EYEBROW_HEIGHT_RIGHT, EYEBROW_HEIGHT_LEFT, EYEBROW_ANGLE_RIGHT, EYEBROW_ANGLE_LEFT,
  EYELID_UP_RIGHT, EYELID_UP_LEFT, EYELID_DOWN_RIGHT, EYELID_DOWN_LEFT,
  EYE_HORIZONTAL, EYE_VERTICAL,
  JAW_CLOCKWISE, JAW_ANTICLOCKWISE
};

Motor motor[12];
DynamixelProtocol dxl(BAUDRATE, ID);
unsigned char adress;
unsigned char angle;

void setup() {
  dxl.init();
  Serial.begin(BAUDRATE);
  Serial.flush();
  motor[EYEBROW_HEIGHT_RIGHT].setMotorDefinitions(0, 20, 115);
  motor[EYEBROW_HEIGHT_LEFT].setMotorDefinitions(180-0, 65, 160);
  motor[EYEBROW_ANGLE_RIGHT].setMotorDefinitions(90, 60, 120);
  motor[EYEBROW_ANGLE_LEFT].setMotorDefinitions(180-90, 60, 120);
  motor[EYELID_UP_RIGHT].setMotorDefinitions(0, 20, 80);
  motor[EYELID_UP_LEFT].setMotorDefinitions(180-0, 100, 160);
  motor[EYELID_DOWN_RIGHT].setMotorDefinitions(180-0, 100, 160);
  motor[EYELID_DOWN_LEFT].setMotorDefinitions(0, 20, 80);
  motor[EYE_HORIZONTAL].setMotorDefinitions(90, 55, 125);
  motor[EYE_VERTICAL].setMotorDefinitions(100, 85, 130);  
  motor[JAW_CLOCKWISE].setMotorDefinitions(180, 0, 150);
  motor[JAW_ANTICLOCKWISE].setMotorDefinitions(180-180, 0, 150);
}

void loop(){
  dxl.checkMessages();
  if(dxl.instruction != DXL_NO_DATA && dxl.id == ID){
    switch(dxl.instruction){
      case DXL_WRITE_DATA:
        adress = dxl.parameters[0];
        angle = dxl.parameters[1];
        switch(adress){
          case EYEBROW_HEIGHT_RIGHT:
            motor[EYEBROW_HEIGHT_RIGHT].goTo(angle);
            break;
          case EYEBROW_HEIGHT_LEFT:
            motor[EYEBROW_HEIGHT_LEFT].goTo(180-angle);
            break;
          case EYEBROW_ANGLE_RIGHT:
            motor[EYEBROW_ANGLE_RIGHT].goTo(angle);
            break;
          case EYEBROW_ANGLE_LEFT:
            motor[EYEBROW_ANGLE_LEFT].goTo(180-angle);
            break;
          case EYELID_UP_RIGHT:
            motor[EYELID_UP_RIGHT].goTo(angle);
            break;
          case EYELID_UP_LEFT:
            motor[EYELID_UP_LEFT].goTo(180-angle);
            break;
          case EYELID_DOWN_RIGHT:
            motor[EYELID_DOWN_RIGHT].goTo(180-angle);
            break;
          case EYELID_DOWN_LEFT:
            motor[EYELID_DOWN_LEFT].goTo(angle);
            break;
          case EYE_HORIZONTAL:
            motor[EYE_HORIZONTAL].goTo(angle);
            break;
          case EYE_VERTICAL:
            motor[EYE_VERTICAL].goTo(angle);
            break;
          case JAW_CLOCKWISE:
            motor[JAW_CLOCKWISE].goTo(angle);
            motor[JAW_ANTICLOCKWISE].goTo(180-angle);            
            break;
          default:
            break;
        }
      default:
        break;
    }   
  }
}