#include "dxl_hal.h"
#include "dynamixel.h"
#include <stdio.h>

#define ID				(2)
#define LENGTH				(3)
#define INSTRUCTION			(4)
#define ERRBIT				(4)
#define PARAMETER			(5)
#define DEFAULT_BAUDNUMBER	        (1)

unsigned char gbInstructionPacket[MAXNUM_TXPARAM+10] = {0};
unsigned char gbStatusPacket[MAXNUM_RXPARAM+10] = {0};
unsigned char gbRxPacketLength = 0;
unsigned char gbRxGetLength = 0;
int gbCommStatus = COMM_RXSUCCESS;
int giBusUsing = 0;

int initialize(char *dev_name, int baudnum)
{
        int jointSocket;
	float baudrate;
	baudrate = 2000000.0f / (float)(baudnum + 1);

	if( dxl_hal_open(&jointSocket, dev_name, baudrate) == 0 )
		return 0;

	gbCommStatus = COMM_RXSUCCESS;
	giBusUsing = 0;
	return jointSocket;
}

void terminate(int socket)
{
	dxl_hal_close(&socket);
}

void tx_packet(int jointSocket)
{
	unsigned char i;
	unsigned char TxNumByte, RealTxNumByte;
	unsigned char checksum = 0;

	if( giBusUsing == 1 )
		return;

	giBusUsing = 1;

	if( gbInstructionPacket[LENGTH] > (MAXNUM_TXPARAM+2) )
	{
		gbCommStatus = COMM_TXERROR;
		giBusUsing = 0;
		return;
	}

	if( gbInstructionPacket[INSTRUCTION] != INST_PING
		&& gbInstructionPacket[INSTRUCTION] != INST_READ
		&& gbInstructionPacket[INSTRUCTION] != INST_WRITE
		&& gbInstructionPacket[INSTRUCTION] != INST_REG_WRITE
		&& gbInstructionPacket[INSTRUCTION] != INST_ACTION
		&& gbInstructionPacket[INSTRUCTION] != INST_RESET
		&& gbInstructionPacket[INSTRUCTION] != INST_SYNC_WRITE )
	{
		gbCommStatus = COMM_TXERROR;
		giBusUsing = 0;
		return;
	}

	gbInstructionPacket[0] = 0xff;
	gbInstructionPacket[1] = 0xff;
	for( i=0; i<(gbInstructionPacket[LENGTH]+1); i++ )
		checksum += gbInstructionPacket[i+2];
	gbInstructionPacket[gbInstructionPacket[LENGTH]+3] = ~checksum;

	if( gbCommStatus == COMM_RXTIMEOUT || gbCommStatus == COMM_RXCORRUPT )
		dxl_hal_clear(jointSocket);

	TxNumByte = gbInstructionPacket[LENGTH] + 4;
	RealTxNumByte = dxl_hal_tx(jointSocket,  (unsigned char*)gbInstructionPacket, TxNumByte );

	if( TxNumByte != RealTxNumByte )
	{
		gbCommStatus = COMM_TXFAIL;
		giBusUsing = 0;
		return;
	}

        // Dimitri
	if( gbInstructionPacket[INSTRUCTION] == INST_READ )
		dxl_hal_set_timeout( gbInstructionPacket[PARAMETER+1] + 6 ); //6 );
	else
		dxl_hal_set_timeout( 6 ); //6 );

	gbCommStatus = COMM_TXSUCCESS;
}

void rx_packet(int jointSocket)
{
	unsigned char i, j, nRead;
	unsigned char checksum = 0;

	if( giBusUsing == 0 )
		return;

	if( gbInstructionPacket[ID] == BROADCAST_ID )
	{
		gbCommStatus = COMM_RXSUCCESS;
		giBusUsing = 0;
		return;
	}

	if( gbCommStatus == COMM_TXSUCCESS )
	{
		gbRxGetLength = 0;
		gbRxPacketLength = 6;
	}

	nRead = dxl_hal_rx(jointSocket, (unsigned char*)&gbStatusPacket[gbRxGetLength], gbRxPacketLength - gbRxGetLength); //was );
	gbRxGetLength += nRead;
	if( gbRxGetLength < gbRxPacketLength )
	{
		if( dxl_hal_timeout() == 1 )
		{
			if(gbRxGetLength == 0)
                        {
                                //printf("COMM_RXTIMEOUT\n");
				gbCommStatus = COMM_RXTIMEOUT;
                        }
			else
                        {
                                //printf("COMM_RXCORRUPT\n");
				gbCommStatus = COMM_RXCORRUPT;
                        }
			giBusUsing = 0;
			return;
		}
	}

	// Find packet header
	for( i=0; i<(gbRxGetLength-1); i++ )
	{
		if( gbStatusPacket[i] == 0xff && gbStatusPacket[i+1] == 0xff )
		{
			break;
		}
		else if( i == gbRxGetLength-2 && gbStatusPacket[gbRxGetLength-1] == 0xff )
		{
			break;
		}
	}
	if( i > 0 )
	{
		for( j=0; j<(gbRxGetLength-i); j++ )
			gbStatusPacket[j] = gbStatusPacket[j + i];

		gbRxGetLength -= i;
	}

	if( gbRxGetLength < gbRxPacketLength )
	{
		gbCommStatus = COMM_RXWAITING;
		return;
	}

	// Check id pairing
	if( gbInstructionPacket[ID] != gbStatusPacket[ID])
	{
                //printf("Pairing id problem\n");
		gbCommStatus = COMM_RXCORRUPT;
		giBusUsing = 0;
		return;
	}

	gbRxPacketLength = gbStatusPacket[LENGTH] + 4;
	if( gbRxGetLength < gbRxPacketLength )
	{
		nRead = dxl_hal_rx(jointSocket, (unsigned char*)&gbStatusPacket[gbRxGetLength], gbRxPacketLength - gbRxGetLength );
		gbRxGetLength += nRead;
		if( gbRxGetLength < gbRxPacketLength )
		{
			gbCommStatus = COMM_RXWAITING;
			return;
		}
	}

	// Check checksum
	for( i=0; i<(gbStatusPacket[LENGTH]+1); i++ )
		checksum += gbStatusPacket[i+2];
	checksum = ~checksum;

	if( gbStatusPacket[gbStatusPacket[LENGTH]+3] != checksum )
	{
                //printf("Checksum problem\n");
		gbCommStatus = COMM_RXCORRUPT;
		giBusUsing = 0;
		return;
	}

	gbCommStatus = COMM_RXSUCCESS;
	giBusUsing = 0;
}

void txrx_packet(int jointSocket)
{
	tx_packet(jointSocket);

	if( gbCommStatus != COMM_TXSUCCESS )
		return;

        int i = 0;
	do{
		rx_packet(jointSocket);
                i++;
	}while( gbCommStatus == COMM_RXWAITING );
        //printf("Waited:%d ",i);
}

int get_result(void)
{
	return gbCommStatus;
}

void set_txpacket_id( int id )
{
	gbInstructionPacket[ID] = (unsigned char)id;
}

void set_txpacket_instruction( int instruction )
{
	gbInstructionPacket[INSTRUCTION] = (unsigned char)instruction;
}

void set_txpacket_parameter( int index, int value )
{
	gbInstructionPacket[PARAMETER+index] = (unsigned char)value;
}

void set_txpacket_length( int length )
{
	gbInstructionPacket[LENGTH] = (unsigned char)length;
}

int get_rxpacket_error( int errbit )
{
	if( gbStatusPacket[ERRBIT] & (unsigned char)errbit )
		return 1;

	return 0;
}

int get_rxpacket_length(void)
{
	return (int)gbStatusPacket[LENGTH];
}

int get_rxpacket_parameter( int index )
{
	return (int)gbStatusPacket[PARAMETER+index];
}

int makeword( int lowbyte, int highbyte )
{
	unsigned short word;

	word = highbyte;
	word = word << 8;
	word = word + lowbyte;
	return (int)word;
}

int get_lowbyte( int word )
{
	unsigned short temp;

	temp = word & 0xff;
	return (int)temp;
}

int get_highbyte( int word )
{
	unsigned short temp;

	temp = word & 0xff00;
	temp = temp >> 8;
	return (int)temp;
}

void ping( int jointSocket, int id )
{
	while(giBusUsing);

	gbInstructionPacket[ID] = (unsigned char)id;
	gbInstructionPacket[INSTRUCTION] = INST_PING;
	gbInstructionPacket[LENGTH] = 2;

	txrx_packet(jointSocket);
}

int read_byte(int jointSocket, int id, int address )
{
	while(giBusUsing);

	gbInstructionPacket[ID] = (unsigned char)id;
	gbInstructionPacket[INSTRUCTION] = INST_READ;
	gbInstructionPacket[PARAMETER] = (unsigned char)address;
	gbInstructionPacket[PARAMETER+1] = 1;
	gbInstructionPacket[LENGTH] = 4;

	txrx_packet(jointSocket);

	return (int)gbStatusPacket[PARAMETER];
}

void write_byte(int jointSocket, int id, int address, int value )
{
	while(giBusUsing);

	gbInstructionPacket[ID] = (unsigned char)id;
	gbInstructionPacket[INSTRUCTION] = INST_WRITE;
	gbInstructionPacket[PARAMETER] = (unsigned char)address;
	gbInstructionPacket[PARAMETER+1] = (unsigned char)value;
	gbInstructionPacket[LENGTH] = 4;

	txrx_packet(jointSocket);
}

int read_word(int jointSocket, int id, int address )
{
	while(giBusUsing);

	gbInstructionPacket[ID] = (unsigned char)id;
	gbInstructionPacket[INSTRUCTION] = INST_READ;
	gbInstructionPacket[PARAMETER] = (unsigned char)address;
	gbInstructionPacket[PARAMETER+1] = 2;
	gbInstructionPacket[LENGTH] = 4;

	txrx_packet(jointSocket);

        if (get_result() != 1)
        {
          return -1;
        } else {
          return makeword((int)gbStatusPacket[PARAMETER], (int)gbStatusPacket[PARAMETER+1]);
        }
}

void write_word(int jointSocket, int id, int address, int value )
{
	while(giBusUsing);

	gbInstructionPacket[ID] = (unsigned char)id;
	gbInstructionPacket[INSTRUCTION] = INST_WRITE;
	gbInstructionPacket[PARAMETER] = (unsigned char)address;
	gbInstructionPacket[PARAMETER+1] = (unsigned char)get_lowbyte(value);
	gbInstructionPacket[PARAMETER+2] = (unsigned char)get_highbyte(value);
	gbInstructionPacket[LENGTH] = 5;

	txrx_packet(jointSocket);
}

void sync_write_word(int jointSocket, int first_address,
                    int *ids, int *values, int total)
{
	while(giBusUsing);

	gbInstructionPacket[ID] = (unsigned char)0xFE;
	gbInstructionPacket[INSTRUCTION] = INST_SYNC_WRITE;

	gbInstructionPacket[PARAMETER] = (unsigned char)first_address;
	gbInstructionPacket[PARAMETER+1] = (unsigned char)2;
	short i;
	for(i = 0; i<total; i++){
		gbInstructionPacket[PARAMETER+i*3+2] = (unsigned char)ids[i];
		gbInstructionPacket[PARAMETER+i*3+3] = (unsigned char)get_lowbyte(values[i]);
		gbInstructionPacket[PARAMETER+i*3+4] = (unsigned char)get_highbyte(values[i]);
		//printf("%d:%d, ", ids[i], values[i]);
	}
	//printf("\n");
        // Comprimento calculato a partir de total
	//(L+1) *N + 4
        gbInstructionPacket[LENGTH] = 3 * total + 4;
	//for (i = 0 ; i < 3*total+7 ; i++)
	//{
	//	printf("%d ", gbInstructionPacket[i]);
	//}
	//printf("\n");
	txrx_packet(jointSocket);
}

