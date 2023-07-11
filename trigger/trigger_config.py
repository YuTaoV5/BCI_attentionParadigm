from trigger.TriggerController import TriggerController


class TriggerConfig:
    # trigger类型
    EEG_TYPE = 'neuracle'
    # EEG_TYPE = 'neuroscan'

    # trigger串/并口
    # 采用串发送trigger(Neuracle/Neuroscan都支持)
    TRIGGER_HANDLE = 'serial'

    try:
        with open('port.txt', encoding='utf-8') as file:
            com_str = file.read()
            com_str = com_str.rstrip('\n')
            print("串口号读取成功")
    except:
        com_str = 'COM3'
        print("串口号读取失败")
    TRIGGER_PORT = com_str

    # 采用并口发送trigger(Neuracle/Neuroscan都支持)
    # TRIGGER_HANDLE = 'parallel'
    # TRIGGER_PORT = 16376

    trig_ctrl = TriggerController(EEG_TYPE, TRIGGER_HANDLE, TRIGGER_PORT)


