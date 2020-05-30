import win32com.client


def WMIDateStringToDate(dtmDate):
    strDateTime = ""
    if (dtmDate[4] == 0):
        strDateTime = dtmDate[5] + '/'
    else:
        strDateTime = dtmDate[4] + dtmDate[5] + '/'
    if (dtmDate[6] == 0):
        strDateTime = strDateTime + dtmDate[7] + '/'
    else:
        strDateTime = strDateTime + dtmDate[6] + dtmDate[7] + '/'
        strDateTime = strDateTime + dtmDate[0] + dtmDate[1] + dtmDate[2] + dtmDate[3] + " " + dtmDate[8] + dtmDate[9] + ":" + dtmDate[10] + dtmDate[11] +':' + dtmDate[12] + dtmDate[13]
    return strDateTime

strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_Battery")
for objItem in colItems:
    if objItem.Availability != None:
        print("Availability: {}".format(objItem.Availability))
    if objItem.BatteryRechargeTime != None:
        print("BatteryRechargeTime: {}".format(objItem.BatteryRechargeTime))
    if objItem.BatteryStatus != None:
        print("BatteryStatus: {}".format(objItem.BatteryStatus))
    if objItem.Caption != None:
        print("Caption: {}".format(objItem.Caption))
    if objItem.Chemistry != None:
        print("Chemistry: {}".format(objItem.Chemistry))
    if objItem.ConfigManagerErrorCode != None:
        print("ConfigManagerErrorCode: {}".format(objItem.ConfigManagerErrorCode))
    if objItem.ConfigManagerUserConfig != None:
        print("ConfigManagerUserConfig: {}".format(objItem.ConfigManagerUserConfig))
    # if objItem.CreationClassName != None:
    #     print("CreationClassName:" + ` objItem.CreationClassName`)
    # if objItem.Description != None:
    #     print("Description:" + ` objItem.Description`)
    # if objItem.DesignCapacity != None:
    #     print("DesignCapacity:" + ` objItem.DesignCapacity`)
    # if objItem.DesignVoltage != None:
    #     print("DesignVoltage:" + ` objItem.DesignVoltage`)
    # if objItem.DeviceID != None:
    #     print("DeviceID:" + ` objItem.DeviceID`)
    # if objItem.ErrorCleared != None:
    #     print("ErrorCleared:" + ` objItem.ErrorCleared`)
    # if objItem.ErrorDescription != None:
    #     print("ErrorDescription:" + ` objItem.ErrorDescription`)
    # if objItem.EstimatedChargeRemaining != None:
    #     print("EstimatedChargeRemaining:" + ` objItem.EstimatedChargeRemaining`)
    # if objItem.EstimatedRunTime != None:
    #     print("EstimatedRunTime:" + ` objItem.EstimatedRunTime`)
    # if objItem.ExpectedBatteryLife != None:
    #     print("ExpectedBatteryLife:" + ` objItem.ExpectedBatteryLife`)
    # if objItem.ExpectedLife != None:
    #     print("ExpectedLife:" + ` objItem.ExpectedLife`)
    # if objItem.FullChargeCapacity != None:
    #     print("FullChargeCapacity:" + ` objItem.FullChargeCapacity`)
    # if objItem.InstallDate != None:
    #     print("InstallDate:" + WMIDateStringToDate(objItem.InstallDate))
    # if objItem.LastErrorCode != None:
    #     print("LastErrorCode:" + ` objItem.LastErrorCode`)
    # if objItem.MaxRechargeTime != None:
    #     print("MaxRechargeTime:" + ` objItem.MaxRechargeTime`)
    # if objItem.Name != None:
    #     print("Name:" + ` objItem.Name`)
    # if objItem.PNPDeviceID != None:
    #     print("PNPDeviceID:" + ` objItem.PNPDeviceID`)
    # print("PowerManagementCapabilities:")
    # strList = " "
    # try :
    #     for objElem in objItem.PowerManagementCapabilities :
    #         strList = strList + objElem + ","
    # except:
    #     strList = strList + 'null'
    # print(strList)
    # if objItem.PowerManagementSupported != None:
    #     print("PowerManagementSupported:" + objItem.PowerManagementSupported)
    # if objItem.SmartBatteryVersion != None:
    #     print("SmartBatteryVersion:" + objItem.SmartBatteryVersion)
    # if objItem.Status != None:
    #     print("Status:" + objItem.Status)
    # if objItem.StatusInfo != None:
    #     print("StatusInfo:" + ` objItem.StatusInfo`)
    # if objItem.SystemCreationClassName != None:
    #     print("SystemCreationClassName:" + ` objItem.SystemCreationClassName`)
    # if objItem.SystemName != None:
    #     print("SystemName:" + ` objItem.SystemName`)
    # if objItem.TimeOnBattery != None:
    #     print("TimeOnBattery:" + ` objItem.TimeOnBattery`)
    # if objItem.TimeToFullCharge != None:
    #     print("TimeToFullCharge:" + ` objItem.TimeToFullCharge`)

