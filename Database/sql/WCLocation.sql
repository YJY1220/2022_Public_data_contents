/*
휠체어 전동 충전기 위치
DetailLoca      :상세위치
StationName     :역명
SubwayLine      :지하철 노선
Floor           :설치 층
UpDown          :지상지하구분 (U, D)
Organization    :철도운영기관명
ChargerCount    :충전설비수
Lat             :위도
Lon             :경도
 */

drop table WCLocation;
create table WCLocation( 
        DetailLoca      VARCHAR(70),
        StationName     VARCHAR(40),
        SubwayLine      NUMBER,
        Floor           NUMBER,
        UpDown          VARCHAR(1),
        Organization    VARCHAR(20),
        ChargerCount    NUMBER,
        Lat             NUMBER,
        Lon             NUMBER
        );
insert into WCLocation values ( 'B1 화장실 앞', '상인', 1, 1, 'D', '대구도시철도', 2, 35.81891945, 128.5377634);
insert into WCLocation values ( 'B1층 정면50m 고객안내센터 앞', '명덕(2.28민주운동기념회관)', 1, 1, 'D', '대구도시철도', 1, 35.81891945, 128.5377634);
insert into WCLocation values ( '2번출구에서 우측 B2층(50m)까지 내려와 화장실 옆', '중앙로', 1, 2, 'D', '대구도시철도', 1, 35.87085011, 128.5939694);
insert into WCLocation values ( 'B2 고객안내센터 앞', '대구역', 1, 2, 'D', '대구도시철도', 1, 35.87593813, 128.5962637);
insert into WCLocation values ( '1번 출구 입장 후 우측 21M', '동대구역', 1, 1, 'D', '대구도시철도', 2, 35.87755008, 128.6278968);
insert into WCLocation values ( '3번 출구', '다사', 2, 1, 'D', '대구도시철도', 1, 35.86482299, 128.458386);
insert into WCLocation values ( '6번 출구', '계명대', 2, 2, 'D', '대구도시철도', 2, 35.85150761, 128.4918363);
insert into WCLocation values ( 'B2 공중전화기옆', '성서산업단지', 2, 2, 'D', '대구도시철도', 1, 35.85171507, 128.5069827);
insert into WCLocation values ( '1번 엘레베이터 앞', '용산(서부법원·검찰청입구)', 2, 2, 'D', '대구도시철도', 2, 35.85171507, 128.5069827);
insert into WCLocation values ( 'B2 화장실 옆', '감삼', 2, 2, 'D', '대구도시철도', 1, 35.85430996, 128.5481213);
insert into WCLocation values ( 'B1 고객안내센터 앞', '청라언덕', 2, 1, 'D', '대구도시철도', 1, 35.85430996, 128.5481213);
insert into WCLocation values ( 'B3층 대서로 화장실 옆 4M', '반월당', 2, 3, 'D', '대구도시철도', 1, 35.86449649, 128.5933329);
insert into WCLocation values ( 'B3층 고객안내센터 앞 4M', '반월당', 2, 3, 'D', '대구도시철도', 1, 35.86449649, 128.5933329);
insert into WCLocation values ( 'B1 고객안내센터 옆', '고산', 2, 1, 'D', '대구도시철도', 1, 35.84292626, 128.6932401);
insert into WCLocation values ( 'B1 대합실(게이트 안쪽)', '정평', 2, 1, 'D', '대구도시철도', 1, 35.8340413, 128.7286623);
insert into WCLocation values ( 'B1 고객힐링쉼터 옆', '임당', 2, 1, 'D', '대구도시철도', 1, 35.83411783, 128.7408368);
insert into WCLocation values ( 'B1 고객안내센터 앞', '영남대', 2, 1, 'D', '대구도시철도', 1, 35.83619751, 128.7527455);
insert into WCLocation values ( '2층 대합실', '청라언덕', 3, 2, 'U', '대구도시철도', 2, 35.83619751, 128.7527455);
insert into WCLocation values ( '2층 대합실', '명덕(2.28민주운동기념회관)', 3, 2, 'U', '대구도시철도', 2, 35.83619751, 128.7527455);
