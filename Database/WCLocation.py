import requests
import config
import StationXY

insert_file = open('sql/WCLocation.sql', 'w', encoding='utf-8')

apikey = 'doPQWaK3RF%2F2FlmWgDKlCKgwO2GOqQhA8wLBewPmouVYI5ezOEv0QZX3abbjFiHpWYaCZZ9mV9VJcgoPA5PJIQ%3D%3D'
url = 'https://api.odcloud.kr/api/15041281/v1/uddi:7887b8fa-79a3-4b95-9eb0-8d55381d2f7a?page=1&perPage=20&serviceKey='\
      + config.WCLocation_api_key

requestData = requests.get(url)

if requestData.status_code == 200:
    print('RequestOk')
    jsonData = requestData.json()
    insert_file.write("drop table WCLocation;\n")
    insert_file.write("create table WCLocation( \n\
        DetailLoca      VARCHAR(70),\n\
        StationName     VARCHAR(40),\n\
        SubwayLine      NUMBER,\n\
        Floor           NUMBER,\n\
        UpDown          VARCHAR(1),\n\
        Organization    VARCHAR(20),\n\
        ChargerCount    NUMBER,\n\
        Lat             NUMBER,\n\
        Lon             NUMBER\n\
        );\n")
    stationXY = StationXY.getStationXY()

    for i in range(jsonData.get('currentCount')):
        lists = jsonData.get('data')[i]
        detailLoca, subwayLine, stationName, Floor, organization, chargerCnt = lists.get('상세위치'), int(lists.get('선명')[0]), lists.get('역명'), lists.get('역층'), lists.get('철도운영기관명'), lists.get('충전설비수')

        if "(" in stationName:
            print(stationName.find("("))
            str = str[0:stationName.find("(")]
        else:
            str = stationName

        for key in stationXY.keys():
            if str in key:
                lat = stationXY.get(key)[0]
                lon = stationXY.get(key)[1]
                break

        if lists.get('지상지하구분') == '지상':
            upDown = 'U'
        else:
            upDown = 'D'

        print(jsonData.get('data')[i])
        insert_file.write(f'insert into WCLocation values ( \'{detailLoca}\', \'{stationName}\', {subwayLine}, {Floor}, \'{upDown}\', \'{organization}\', {chargerCnt}, {lat}, {lon});\n')
