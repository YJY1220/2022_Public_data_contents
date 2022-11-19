import pandas as pd

insert_file = open('sql/WCLocation2.sql', 'w', encoding='utf-8')
file_path = "ApiFile/대구광역시_전동휠체어급속충전기_입지.xlsx"

excel_source = pd.read_excel(file_path, engine="openpyxl")
insert_file.write("drop table WCLocation2;\n")
insert_file.write("create table WCLocation2(\n\
            FacilityName      VARCHAR(70),\n\
            LocCode           VARCHAR(40),\n\
            Address           VARCHAR(80),\n\
            Latitude          NUMBER,\n\
            Longitude         NUMBER,\n\
            Description       VARCHAR(100),\n\
            OpenTime          VARCHAR(40),\n\
            CloseTime         VARCHAR(40),\n\
            SatOpenTime       VARCHAR(40),\n\
            SatCloseTime      VARCHAR(40),\n\
            HolOpenTime       VARCHAR(40),\n\
            HolCloseTime      VARCHAR(40),\n\
            SyncChargerCnt    NUMBER,\n\
            AirYn             VARCHAR(1),\n\
            PhoneChargerYn    VARCHAR(1),\n\
            Tel               VARCHAR(13)\n\
            );\n")

for i in range(len(excel_source)):
    row = excel_source.iloc[i]
    facilityName, locCode, address, lat, lon, description,\
    openTime, closeTime, satOpenTime, satCloseTime, \
    holOpenTime, holCloseTime, syncChargerCnt, \
    airYn, phoneChargerYn, tel \
        = row[0], row[3], row[4], row[6], row[7],row[8], \
          row[9], row[10], row[11], row[12],\
          row[13], row[14], row[15], \
          row[16], row[17], row[19]
    insert_file.write(
        f'insert into WCLocation2 values ( \'{facilityName}\', \'{locCode}\', \'{address}\', {lat}, {lon}, \'{description}\', '
        f'\'{openTime}\', \'{closeTime}\', \'{satOpenTime}\', \'{satCloseTime}\', \'{holOpenTime}\',\'{holCloseTime}\', '
        f'{syncChargerCnt}, \'{airYn}\', \'{phoneChargerYn}\', \'{tel}\');\n')
