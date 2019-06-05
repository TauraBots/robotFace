#ifndef _DYNAMIXEL_HEADER
#define _DYNAMIXEL_HEADER

#ifdef __cplusplus
extern "C" {
#endif


///////////// device control methods ////////////////////////
int initialize(char* dev_name, int baudnum);
void terminate(int jointSocket);


///////////// set/get packet methods //////////////////////////
#define MAXNUM_TXPARAM		(150)
#define MAXNUM_RXPARAM		(60)

void set_txpacket_id(int id);
#define BROADCAST_ID		(254)

void set_txpacket_instruction(int instruction);
#define INST_PING			(1)
#define INST_READ			(2)
#define INST_WRITE			(3)
#define INST_REG_WRITE		(4)
#define INST_ACTION			(5)
#define INST_RESET			(6)
#define INST_SYNC_WRITE		(131)

void set_txpacket_parameter(int index, int value);
void set_txpacket_length(int length);

int get_rxpacket_error(int errbit);
#define ERRBIT_VOLTAGE		(1)
#define ERRBIT_ANGLE		(2)
#define ERRBIT_OVERHEAT		(4)
#define ERRBIT_RANGE		(8)
#define ERRBIT_CHECKSUM		(16)
#define ERRBIT_OVERLOAD		(32)
#define ERRBIT_INSTRUCTION	(64)

int get_rxpacket_length(void);
int get_rxpacket_parameter(int index);


// utility for value
int makeword(int lowbyte, int highbyte);
int get_lowbyte(int word);
int get_highbyte(int word);


////////// packet communication methods ///////////////////////
void tx_packet(int);
void rx_packet(int);
void txrx_packet(int);

int get_result(void);
#define	COMM_TXSUCCESS		(0)
#define COMM_RXSUCCESS		(1)
#define COMM_TXFAIL		(2)
#define COMM_RXFAIL		(3)
#define COMM_TXERROR		(4)
#define COMM_RXWAITING		(5)
#define COMM_RXTIMEOUT		(6)
#define COMM_RXCORRUPT		(7)


//////////// high communication methods ///////////////////////
void ping(int jointSocket, int id);
int read_byte(int jointSocket, int id, int address);
void write_byte(int jointSocket, int id, int address, int value);
int read_word(int jointSocket, int id, int address);
void write_word(int jointSocket, int id, int address, int value);
void sync_write_word(int jointSocket, int first_address, int *ids, int *values, int total);

#ifdef __cplusplus
}
#endif

#endif
