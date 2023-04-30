import win32evtlog

server = 'localhost'
logtype = 'Application'

hand = win32evtlog.OpenEventLog(server,logtype)

total = win32evtlog.GetNumberOfEventLogRecords(hand)

print(total)

events = win32evtlog.ReadEventLog(hand, win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0,1)

for event in events:
    print(event.SourceName)