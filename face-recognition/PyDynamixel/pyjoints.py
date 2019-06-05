from math import pi
import sys

sys.path.append('/home/jio/workspace/PyDynamixel/dynamixel')
import dynamixel_functions as dxl

ADDR_MX_TORQUE_ENABLE = 0x18  # Address for torque enable
ADDR_MX_PRESENT_POSITION = 0x24 # Address for the current position
ADDR_MX_GOAL_POSITION = 0x1E # Address for goal position
MAXADDR_MX_TORQUE_ENABLE = 0x0E # Address for maximum torque
MAXTORQUELIMIT = 767 # Maximum torque possible

PROTOCOL_VERSION            = 1
COMM_SUCCESS                = 0                             # Communication Success result value
COMM_TX_FAIL                = -1001                         # Communication Tx Failed

BROADCAST_ID = 254

class DxlComm(object):
    ''' This class implements low level
    communication with the dynamixel
    protocol.
    '''

    commPort = None # path to default serial port
    baudnum = None # baudrate=2Mbps/(baudnum+1)
    baudRate = None
    socket = None # stores the socket number
    joints = [] # Database of attached joints
    joint_ids = [] # Database of servomotor ids
    total = 0 # Total number of attached joints

    def __init__(self, commPort="/dev/ttyUSB0", baudnum = 1):

        ''' The argument commPort should be
        the path to the serial device.
        The constructor optionally takes
        a baudnum argument:
           baudrate = 2Mbps / (baudnum + 1)
        If no baudnum is provided, then the
        default is 1, resulting 1Mbps
        '''

        self.commPort = commPort
        self.baudnum = baudnum
        self.baudRate = 2000000/(baudnum+1)
        self.socket = dxl.portHandler(self.commPort.encode('utf-8'))
        dxl.packetHandler()
        if dxl.openPort(self.socket):
            print("Port Open Success")
        if dxl.setBaudRate(self.socket, self.baudRate):
            print("Port Baud Set Success")

    def attachJoints(self, joints):

        ''' This method attaches several joints
        so that the communication can be
        handled by this class
        '''

        for joint in joints:
            self.attachJoint(joint)

    def attachJoint(self, joint):

        ''' This method attaches a joint so
        that the communication can be handled
        by this class
        '''

        # Registers the joint in the database
        # and sets its socket
        self.joints.append(joint)
        self.joint_ids.append(joint.servo_id)
        joint.setSocket(self.socket)
        self.total = self.total + 1

    def release(self):

        ''' This method should be called for
        the class to explicitly close the
        open socket
        '''

        dxl.closePort(self.socket)

    def sendGoalAngles(self):

        ''' Communicates the goal position for all
        servos connected to this port
        '''

        chJoints = [j for j in self.joints if j.changed is True]

        self._syncWrite(chJoints, ADDR_MX_GOAL_POSITION, 2)

        for i in chJoints:
            i.changed = False

    def sendMaxTorques(self, maxTorque = None):

        ''' Communicates the max torques for all
        servos connected to this port. Optionally
        the argument maxTorque can be provided.
        If provided, the same maxTorque will be
        set to all attached joints.
        '''

        if maxTorque:
            for j in self.joints:
                j.setMaxTorque(maxTorque)

        values = [j.maxTorque for j in self.joints]
        self._syncWrite(self.joints, MAXADDR_MX_TORQUE_ENABLE, 2, values)

    def _syncWrite(self, servos, addr, info_len, values=None):

        ''' this is an adaptation from dynamixel's sdk for
            the sync_write '''
        SW = dxl.groupSyncWrite(self.socket, PROTOCOL_VERSION, addr, info_len)
        for i, s in enumerate(servos):
            if(values is None):
                dxl.groupSyncWriteAddParam(SW, s.servo_id, s.goalValue, info_len)
            else:
                dxl.groupSyncWriteAddParam(SW, s.servo_id, values[i], info_len)

        dxl.groupSyncWriteTxPacket(SW) #does the sync write
        dxl.groupSyncWriteClearParam(SW) #clears buffer


    def enableTorques(self):

        ''' Enable torque for all motors connected
        in this port.
        '''
        dxl.write1ByteTxRx(self.socket, PROTOCOL_VERSION, BROADCAST_ID, \
                ADDR_MX_TORQUE_ENABLE, 1)

    def disableTorques(self):

        ''' Disables torque for all motors connected
        to this port
        '''

        dxl.write1ByteTxRx(self.socket, PROTOCOL_VERSION, BROADCAST_ID, \
                ADDR_MX_TORQUE_ENABLE, 0)


    def receiveCurrAngles(self):

        ''' This method read the current angle
        of all servos attached to this channel
        (This is sequential, not sync_read!)
        '''

        for joint in self.joints:
            joint.receiveCurrAngle()

class Joint(object):

    ''' This class represents a Dynamixel
    servo motor.
    '''

    servo_id = None # This is the servo id
    socket = None # This stores socket number
    goalAngle = 0.0
    goalValue = 0
    currAngle = 0.0
    currValue = 0
    centerValue = 0
    maxTorque = 767 # This is the maximum
    changed = False

    def __init__(self, servo_id, centerValue = 0):

        ''' The constructor takes the servo id
        as the argument. Argument centerValue
        can be set to calibrate the zero
        position of the servo.
        '''

        self.servo_id = servo_id
        self.centerValue = centerValue

    def setCenterValue(self, centerValue):

        ''' Sets the calibration of the zero
        for the joint. This can also be passed
        in the constructor.
        '''

        self.centerValue = centerValue

    def setSocket(self, socket):

        ''' Stores the socket number for later
        reference. This is called by DxlComm
        when the method attachJoint() is used
        '''

        self.socket = socket

    def setMaxTorque(self, maxTorque):

        ''' Sets the maximum torque (does not
        send it yet!). To send it the method
        sendMaxTorque() must be called.
        '''

        self.maxTorque = min(int(maxTorque), MAXTORQUELIMIT)

    def sendMaxTorque(self, maxTorque = None):

        ''' Sends a command to this specific
        servomotor to set its maximum torque.
        If the argument maxTorque is not
        provided, then it sends the last
        value set using setMaxTorque().
        '''

        if maxTorque:
            self.setMaxTorque(maxTorque)
        dxl.write2ByteTxRx(self.socket, PROTOCOL_VERSION, \
                self.servo_id, MAXADDR_MX_TORQUE_ENABLE, self.maxTorque)

    def setGoalAngle(self, angle):

        self.goalAngle = float(angle)
        self.goalValue = int(2048.0*angle/pi) \
                + self.centerValue
        self.changed = True

    def sendGoalAngle(self, goalAngle = None):
        ''' Sends a command to this specific
        servomotor to set its goal angle.
        If no parameter is passed then it
        sends the goal angle that was set
        via setGoalAngle()
        '''

        if goalAngle:
            self.setGoalAngle(goalAngle)
        dxl.write2ByteTxRx(self.socket, PROTOCOL_VERSION, self.servo_id, \
                ADDR_MX_GOAL_POSITION, self.goalValue)

    def receiveCurrAngle(self):

        ''' Reads the current position of this
        servomotor alone. The read position is
        stored and can be accessed via method
        getAngle()
        '''

        self.currValue = dxl.read2ByteTxRx(self.socket, PROTOCOL_VERSION, self.servo_id, \
                ADDR_MX_PRESENT_POSITION) - self.centerValue
        self.currAngle = pi*float(self.currValue)/2048.0
        return self.currAngle

    def getAngle(self):

        ''' Returns the current angle last read
        '''

        return self.currAngle

    def enableTorque(self):
        ''' Enables torque in this joint
        '''

        dxl.write1ByteTxRx(self.socket, PROTOCOL_VERSION, self.servo_id, \
                ADDR_MX_TORQUE_ENABLE, 1)

    def disableTorque(self):
        ''' Disables torque in this joint
        '''

        dxl.write1ByteTxRx(self.socket, PROTOCOL_VERSION, self.servo_id, \
                ADDR_MX_TORQUE_ENABLE, 0)



    '''These methods are for reading and writing directly from and to a specific address
        If possible, don't use these.
        They are intended to be used for changing servo addresses, and stuff like this.
        '''

    def readValue(self, address, size=1):
        if(size==1):
            v = dxl.read1ByteTxRx(self.socket, PROTOCOL_VERSION, self.servo_id, address)
        elif(size==2):
            v = dxl.read2ByteTxRx(self.socket, PROTOCOL_VERSION, self.servo_id, address)

        return v

    def writeValue(self, address, value, size=1):
        if(size==1):
            dxl.write1ByteTxRx(self.socket, PROTOCOL_VERSION, self.servo_id, \
                address, value)
        elif(size==2):
            dxl.write2ByteTxRx(self.socket, PROTOCOL_VERSION, self.servo_id, \
                address, value)
