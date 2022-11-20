import xml.etree.ElementTree as ET
import StationXY

# 총 91개
insert_file = open('sql/WCStatus.sql', 'w', encoding='utf-8')

root = ET.parse('ApiFile/WheelChairChargerStatus.xml').getroot()
print(root)

apiDataList = root.find('apiDataList').findall('apiData')
insert_file.write("drop table WCStatus;\n")
insert_file.write("create table WCStatus(\n\
        DetailLoca      VARCHAR(70),\n\
        StationName     VARCHAR(70),\n\
        SubwayLine      NUMBER,\n\
        Floor           VARCHAR(30),\n\
        ChargerCnt      NUMBER,\n\
        SyncChargerCnt  NUMBER,\n\
        Tel             VARCHAR(20),\n\
        Lat             NUMBER,\n\
        Lon             NUMBER\n\
        );\n")
stationXY = StationXY.getStationXY()
for item in apiDataList:
    detailLoca = item.find('HP_STUP_DTL_LCTN').text
    stationName = item.find('HP_STN_NM').text
    subwayLine = int(item.find('HP_LINE_CD').text)
    floor = item.find('HP_STUP_STRY_CD').text
    chargerCnt = int(item.find('HP_ELC_CNV_QTT').text)
    syncChargerCnt = int(item.find('HP_SYNC_ELC_QTT').text)
    tel = item.find('HP_STN_TEL_NO').text
    # print(stationName, subwayLine, floor, detailLoca, chargerCnt, syncChargerCnt, tel)

    if "(" in stationName:
        print(stationName.find("("))
        str = stationName[0:stationName.find("(")]
    elif any(temp.isdigit() for temp in stationName):
        for i in range(len(stationName)):
            if stationName[i].isdigit():
                str = stationName[0:i]
    elif stationName == "성서산단역":
        str = "성서산업단지역"
    else:
        str = stationName


    for key in stationXY.keys():
        if str in key:
            lat = stationXY.get(key)[0]
            lon = stationXY.get(key)[1]
            break
    insert_file.write(
        f'insert into WCStatus values ( \'{detailLoca}\',\'{stationName}\', {subwayLine}, \'{floor}\', {chargerCnt}, {syncChargerCnt}, \'{tel}\', {lat}, {lon});\n')
# print(content)


