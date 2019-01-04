'''
NOTES:-
Cluster Labeling 0.0.1
Threat Detection Model
To Analyse Computer Log Data for Threat Detection
Dev : Manu Gupta
Cyber-Shield

'''


class Threat:

    def __init__(self, PID, cpu_usage, ram_usage, sent_data, received_data, disk_read, disk_write, file_priority, file_permission, type_access):
        self.PID = PID
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.sent_data = sent_data
        self.received_data = received_data
        self.disk_read = disk_read
        self.disk_write = disk_write
        self.file_priority = file_priority
        self.file_permission = file_permission
        self.type_access = type_access


class Threat_Level:
    