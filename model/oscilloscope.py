from serial import Serial, SerialException
from model.sensors import Sensor

class oscilloscope(Sensor):
    def __init__(self, port= None):
        self.port = port
        super(oscilloscope,self).__init__(port)
    
    def checkcomm(self):
        self.putdata("*IDN?")
        data = self.getdata()
        if data.find("HIOKI") is not -1:
            return True
        else:
            return False

    def start(self):
        self.putdata(":START")

    def stop(self):
        self.putdata(":STOP")

    def abort(self):
        self.putdata(":ABORT")

    def auto(self):
        self.putdata(":AUTO")

    def measure(self,t,ch,no=1):
        if t == 'rms':
            self.putdata(":CALCulate:MEASSet NO%d,RMS,CH%d"%(ch,no))
        elif t == 'peak':
            self.putdata(":CALCulate:MEASSet NO%d,PP,CH%d"%(ch,no))
        elif t == 'max':
            self.putdata(":CALCulate:MEASSet NO%d,MAX,CH%d"%(ch,no))
        elif t == 'min':
            self.putdata(":CALCulate:MEASSet NO%d,MIN,CH%d"%(ch,no))
    
    def getMeasurement(self,no=1):
        data = self.getdata(":CALCulate:ANSWer? NO%d"%(no))
        data = data.split(',')[-1]
        data = 0 if data == '' else data
        data = float(data)
        return data


if __name__ == "__main__":

    osc = oscilloscope('COM3')
    while(True):
        data = input('>> ')
        if(data.find('meas ') != -1):
            _ , t, ch = data.split(' ')
            osc.measure(t,int(ch))
        elif(data == 'start'):
            osc.start()
        elif(data == 'stop'):
            osc.stop()
        elif(data.find('ans ') != -1):
            _, ch= data.split(' ')
            print(osc.getMeasurement(int(ch)))
