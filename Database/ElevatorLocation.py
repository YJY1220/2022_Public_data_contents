import pandas as pd
import StationXY

insert_file = open('sql/ElevatorLocation.sql', 'w', encoding='utf-8')
file_path = "ApiFile/국가철도공단_대구도시철도공사_엘리베이터_20211124.csv"

excel_source = pd.read_csv(file_path)
insert_file.write("drop table ElevatorLocation;\n")
insert_file.write("create table ElevatorLocation(\n\
            FacilityName      VARCHAR(50),\n\
            SubwayLine        NUMBER,\n\
            StationName       VARCHAR(70),\n\
            EntranceNum       NUMBER,\n\
            MaxMember         NUMBER,\n\
            MaxWeight       VARCHAR(100),\n\
            Lat             NUMBER,\n\
            Lon             NUMBER\n\
            );\n")

stationXY = StationXY.getStationXY()
for i in range(len(excel_source)):
    lat = -1
    lon = -1
    row = excel_source.iloc[i]
    facilityName, subwayLine, stationName, entranceNum, maxMember, maxWeight\
        = row[0], row[1][0], row[2], row[3], row[5], row[6]
    # print(row[5])
    if pd.isna(maxMember):
        maxMember = -1
    if pd.isna(maxWeight):
        maxWeight = -1

    if "(" in stationName:
        str = stationName[0:stationName.find("(")]
        print("("+str)
    else:
        str = stationName
        print(str)

    for key in stationXY.keys():
        if str in key:
            lat = stationXY.get(key)[0]
            lon = stationXY.get(key)[1]
            break

    insert_file.write(
        f'insert into ElevatorLocation values ( \'{facilityName}\', {subwayLine}, \'{stationName}\', {entranceNum}, {maxMember}, {maxWeight}, {lat}, {lon});\n')
