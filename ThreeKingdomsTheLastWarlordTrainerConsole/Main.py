import pymem
from pymem.ptypes import RemotePointer
def GetProc():
    pm = pymem.Pymem("threekingdoms.exe")
    return pm
def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(GetProc().process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(GetProc().process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset
def Main():
    addr = GetProc().base_address + 0x01AE4D60
    remote_ptr_trainingtoken = [0x18, 0x160]
    tr = GetProc().read_int(getPointerAddress(addr, offsets=remote_ptr_trainingtoken))
    print(tr)
    GetProc().write_int(getPointerAddress(addr, offsets=remote_ptr_trainingtoken), 6000)
if __name__ == "__main__":
    Main()