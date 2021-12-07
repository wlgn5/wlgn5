year,mon,day=input("1차 백신 접종 년 월 일을 공백문자로 구분하여 입력하세요:").split()
days=28

year=int(year)
mon=int(mon)
day=int(day)

leap_year=False
month=[31,28,31,30,31,30,31,31,30,31,30,31]
leap_month=[31,29,31,30,31,30,31,31,30,31,30,31]

if(year%4==0 and year%100!=0)or year%400==0:
    leap_year=True

for i in range(days):
    day+=1

if leap_year==True:
    if day>leap_month[mon-1]:
        day=day-leap_month[mon-1]
        mon+=1

else:
    if day>month[mon-1]:
        day=day-month[mon-1]
        mon+=1

if mon>12:
    mon=1
    year+=1

    if(year%4==0 and year%100!=0)or year%400==0:
        leap_year=True
    else:
        leap_year=False

print("2차 백신 접종일은", year,"년", mon,"월", day,"일입니다.\n예방접종 후 15~30분간 접종기관에 머물러 이상반응 발생여부를 관찰합니다.\n예방접종 후 3시간 이상 주의 깊게 관찰합니다.\n예방접종 후 4주간은 특별한 관심을 가지고 관찰하며 평소와 다른 신체 증상이 나타나면 바로 의사의 진료를 받도록 합니다.\n예반접종 후 2일 정도는 고강도 운동 및 활동, 음주를 삼가주세요.")
