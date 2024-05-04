for _ in range(int(input())):
    n = int(input())
    s = input()
    map_cnt = s.count('map')
    pie_cnt = s.count('pie')
    mapie_cnt = s.count('mapie')
    print((map_cnt+pie_cnt)-mapie_cnt)