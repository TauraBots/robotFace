#ifndef _DYNAMIXEL_HAL_HEADER
#define _DYNAMIXEL_HAL_HEADER


#ifdef __cplusplus
extern "C" {
#endif


int dxl_hal_open(int *jointSocket, char* dev_name, float baudrate);
void dxl_hal_close(int *socket);
int dxl_hal_set_baud( int socket, float baudrate );
void dxl_hal_clear(int socket);
int dxl_hal_tx(int socket, unsigned char *pPacket, int numPacket );
int dxl_hal_rx(int socket, unsigned char *pPacket, int numPacket );
void dxl_hal_set_timeout( int NumRcvByte );
int dxl_hal_timeout();



#ifdef __cplusplus
}
#endif

#endif
