#include <Motor.h>

#include <DynamixelProtocol.h>
#include <string.h>
#include <stdint.h>
#include <Servo.h>
#include <Thread_Manager.h>
#define ID 128
#define BAUDRATE 1000000

enum motors : byte {
  EYEBROW_HEIGHT_RIGHT, EYEBROW_HEIGHT_LEFT, EYEBROW_ANGLE_RIGHT, EYEBROW_ANGLE_LEFT,
  EYELID_UP_RIGHT, EYELID_UP_LEFT, EYELID_DOWN_RIGHT, EYELID_DOWN_LEFT,
  EYE_HORIZONTAL, EYE_VERTICAL,
  JAW_CLOCKWISE, JAW_ANTICLOCKWISE
};

enum anim : byte {
  BLINK, PANIC, SUSPICIOUS, SLEEPY, DISGUSTED  
};

Motor motor[12];


DynamixelProtocol dxl(BAUDRATE, ID);

uint32_t angle;
int adress;
int lenght;

void setup() {

  dxl.init();
  Serial.begin(BAUDRATE);
  Serial.flush();
  
  motor[EYEBROW_ANGLE_RIGHT].setMotorDefinitions(180, 0, 150);
  motor[EYEBROW_ANGLE_LEFT].setMotorDefinitions(180, 0, 150);  
  //Configurado
  motor[EYEBROW_HEIGHT_RIGHT].setMotorDefinitions(180, 0, 150);
  motor[EYEBROW_HEIGHT_LEFT].setMotorDefinitions(180, 0, 150);
  motor[EYELID_UP_RIGHT].setMotorDefinitions(0, 5, 175);
  motor[EYELID_UP_LEFT].setMotorDefinitions(0, 5, 175);
  motor[EYELID_DOWN_RIGHT].setMotorDefinitions(0, 5, 175);
  motor[EYELID_DOWN_LEFT].setMotorDefinitions(0, 5, 175);  
  motor[EYE_HORIZONTAL].setMotorDefinitions(0, 55, 125);
  motor[EYE_VERTICAL].setMotorDefinitions(0, 55, 125);
  motor[JAW_CLOCKWISE].setMotorDefinitions(180, 0, 150);
  motor[JAW_ANTICLOCKWISE].setMotorDefinitions(180-180, 0, 150);
  
}

void loop(){
  uint32_t angle = 0;

  dxl.checkMessages();
  if(dxl.instruction != DXL_NO_DATA){
    switch(dxl.instruction){
      case DXL_READ_DATA:
        break;

      case DXL_WRITE_DATA:
        lenght = dxl.total_parameters;

        //Debug
        for(int i=0; i< lenght; i++){
          Serial.print("valor: ");
          Serial.println(dxl.parameters[i]); 
        }
        
        //that's working... but only if the adress is in the dxl.parameters[0]
        //and the angle is in the dxl.parameters[1]
        
        for(int i = 0; i< lenght; i++){
          if(i < 1){
            adress = dxl.parameters[i];
          }else{
            angle = angle<<8 | dxl.parameters[i];
            //angle = dxl.parameters[i] | angle>>8;  
          }
        }
        
        switch(adress){
          case EYEBROW_HEIGHT_RIGHT:
            motor[EYEBROW_HEIGHT_RIGHT].goTo(angle);
            break;
          case EYEBROW_HEIGHT_LEFT:
            motor[EYEBROW_HEIGHT_LEFT].goTo(angle);
            break;
          case EYEBROW_ANGLE_RIGHT:
            motor[EYEBROW_ANGLE_RIGHT].goTo(angle);
            break;
          case EYEBROW_ANGLE_LEFT:
            motor[EYEBROW_ANGLE_LEFT].goTo(angle);
            break;
          case EYELID_UP_RIGHT:
            motor[EYELID_UP_RIGHT].goTo(angle);
            break;
          case EYELID_UP_LEFT:
            motor[EYELID_UP_LEFT].goTo(angle);
            break;
          case EYELID_DOWN_RIGHT:
            motor[EYELID_DOWN_RIGHT].goTo(angle);
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
        
        break;
    } 
  }
}
