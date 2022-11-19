import pandas as pd

# insert_file = open('sql/ElevatorLocation.sql', 'w', encoding='utf-8')
file_path = "ApiFile/지하철노선위경도정보.csv"

excel_source = pd.read_csv(file_path)
stationXY = {}

def getStationXY():
    for i in range(len(excel_source)):
        row = excel_source.iloc[i]
        stationName, lat, lon = row[0], row[2], row[3]
        stationXY[stationName] = [lat, lon]
    return stationXY

getStationXY()
print(stationXY)