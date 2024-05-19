class CPU:
    def freeze(self):
        return 'CPU is freezing '
    def jump(self,position):
        return 'CPU is jumping to {}'.format(position)
    def execute(self):
        return 'CPU is executing'
    
class Memory:
    def load(self,data,position):
        return 'Memory loading {} to {}'.format(data,position)
    
class HardDrive:
    def read(self,size,lba):
        return 'reading data {} bytes from {} '.format(size,lba)
    
class computerFacade:
    def __init__(self):
        self.cpu=CPU()
        self.memory=Memory()
        self.hard_drive=HardDrive()
    def start(self):
        operations=[
            self.cpu.freeze,
            self.memory.load,
            self.cpu.jump,
            self.cpu.execute
        ]
        return '\n'.join(operations() for operation in operations )
    def shutDown(self):
        return ' computer is shutting down'
    def read_data(self,size,lba):
        return self.hard_drive.read(100,1024)
    
def main():
    computer=computerFacade()
    print("computer is starting")
    print(computer.start())
    print("computer is reading ")
    print(computer.read_data())
    print("computer is shutting down")
    print(computer.shutDown())

if __name__=="__main__":
    main()