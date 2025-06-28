from commands import Commands
from files import Files
from general import General
from globalEnv import GlobalEnv
import dns.resolver


class PortScanning:
    def __init__(self):
        pass

    __record_types = [
        "A",
        "AAAA",
        "CNAME",
        "MX",
        "NS",
        "TXT",
        "SOA",
        "PTR",
        "SRV",
        "CAA",
        "NAPTR",
        "DNSKEY",
        "RRSIG",
        "DS",
        "HINFO",
        "SPF",
        "TLSA",
    ]

    def __prepare(self):
        if (Files.IsFileExists(GlobalEnv.GetEnhancedHttpx()) and Files.IsFileEmpty(GlobalEnv.GetEnhancedHttpx())) or not Files.IsFileExists(GlobalEnv.GetEnhancedHttpx()):
            Files.WriteToFile(GlobalEnv.GetPortScanningTargetDomains(), "a", GlobalEnv.GetDomain())
        else:
            Files.CopyFromTo(GlobalEnv.GetEnhancedHttpx(), GlobalEnv.GetPortScanningTargetDomains())
        Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTargetDomains())

    def __Masscan(self):
        commands = Commands.MasscanCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetMasscan(), False, True)

    def __Nmap(self):
        commands = Commands.NmapCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetNmap(), False, True)

    def __Naabu(self):
        commands = Commands.NaabuCommands()
        for c in commands:
            General.ExecuteCommand(c, GlobalEnv.GetNaabu(), False, True)

    def __dnsRecords(self):
        Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTargetDomains())
        with open(GlobalEnv.GetPortScanningTargetDomains())as f:
            for d in f:
                domain = d.strip()
                flagForArecord = True
                for record_type in self.__record_types:
                    try:
                        answers = dns.resolver.resolve(domain, record_type)
                        line = f"\n{record_type} Records for {domain}"
                        print(line)
                        Files.WriteToFile(GlobalEnv.GetDnsRecords(), 'a', line)
                        Files.WriteToFile(GlobalEnv.GetLogFile(), 'a', line)
                        for rdata in answers:
                            line = rdata.to_text()
                            print(line)
                            Files.WriteToFile(GlobalEnv.GetDnsRecords(), "a", line)
                            Files.WriteToFile(GlobalEnv.GetLogFile(), "a", line)
                            if flagForArecord:
                                Files.WriteToFile(GlobalEnv.GetPortScanningTarget(), 'a', line)
                        flagForArecord = False
                    except Exception as e:
                        line = f"Error fetching {record_type} records: {e}"
                        print(line)
                        Files.WriteToFile(GlobalEnv.GetLogFile(), "a", line)
        Files.RemoveDuplicateFromFile(GlobalEnv.GetPortScanningTarget())

    def Execute(self):
        self.__prepare()
        self.__dnsRecords()
        self.__Masscan()
        self.__Nmap()
        self.__Naabu()
