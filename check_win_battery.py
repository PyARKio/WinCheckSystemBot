# -- coding: utf-8 --
from __future__ import unicode_literals
import wmi
from time import sleep

while True:
    c = wmi.WMI()
    t = wmi.WMI(moniker="//./root/wmi")

    batts1 = c.CIM_Battery(Caption = 'Portable Battery')
    for i, b in enumerate(batts1):
        print('Battery %d Design Capacity: %d mWh' % (i, b.DesignCapacity or 0))

    batts = t.ExecQuery('Select * from BatteryFullChargedCapacity')
    for i, b in enumerate(batts):
        print('Battery %d Fully Charged Capacity: %d mWh' %
              (i, b.FullChargedCapacity))

    batts = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
    for i, b in enumerate(batts):
        print('\nBattery %d ***************' % i)
        print('Tag:               ' + str(b.Tag))
        print('Name:              ' + b.InstanceName)

        print('PowerOnline:       ' + str(b.PowerOnline))
        print('Discharging:       ' + str(b.Discharging))
        print('Charging:          ' + str(b.Charging))
        print('Voltage:           ' + str(b.Voltage / 1000) + ' V')
        print('DischargeCurrent:  ' + str(b.DischargeRate / b.Voltage) + ' A')
        print('ChargeCurrent:     ' + str(b.ChargeRate / b.Voltage) + ' A')
        print('DischargeRate:     ' + str(b.DischargeRate / 1000) + ' W')
        print('ChargeRate:        ' + str(b.ChargeRate / 1000) + ' W')
        print('RemainingCapacity: ' + str(b.RemainingCapacity / 1000) + ' W')
        print('Active:            ' + str(b.Active))
        print('Critical:          ' + str(b.Critical))
        if b.Discharging:
            rate = (b.RemainingCapacity / b.DischargeRate) * 60
            hours = int(rate // 60)
            minutes = int(rate - (hours * 60))
            print('Time               {}:{}'.format(hours, minutes))
        else:
            rate = (b.RemainingCapacity / b.ChargeRate) * 60
            hours = int(rate // 60)
            minutes = int(rate - (hours * 60))
            print('Time               {}:{}'.format(hours, minutes))

        sleep(5)



