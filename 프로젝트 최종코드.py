# 1. 빈 지도 생성 함수
def create_map(size):
    grid_map = []                                     # 빈 리스트를 만듭니다.
    for i in range(size):                           # 지도 세로 크기만큼 반복합니다.
        row = ["."] * size                            # "."으로 채워진 한 줄(리스트)을 만듭니다.
        grid_map.append(row)                          # 만든 줄을 전체 지도 리스트에 추가합니다.
    return grid_map                                   # 완성된 2차원 리스트 지도를 반환합니다.

# 2. 핫플 정보 입력 및 저장 함수
def add_place(hotplace_list, size):
    name = input("핫플 이름을 입력하세요: ")          # 사용자에게 장소 이름을 입력받습니다.
    category = input("카테고리를 입력하세요 (카페/식당): ") # 카테고리를 입력받습니다.
    
    try:
        x = int(input(f"X 좌표를 입력하세요 (0 ~ {size-1}): ")) # X 좌표를 숫자로 입력받습니다.
        y = int(input(f"Y 좌표를 입력하세요 (0 ~ {size-1}): ")) # Y 좌표를 숫자로 입력받습니다.
    except ValueError:                                # 숫자가 아닌 글자가 입력되어 오류가 발생하면 실행합니다.
        print("에러: 좌표는 반드시 '숫자'로만 입력해주세요! 저장 실패.") # 에러 메시지를 출력합니다.
        return                                        # 함수를 즉시 종료합니다.
    
    if x < 0 or x >= size or y < 0 or y >= size:      # 입력된 숫자가 지도 범위를 벗어났는지 확인합니다.
        print("에러: 지도를 벗어난 좌표입니다! 저장 실패.") # 에러 메시지를 출력합니다.
        return                                        # 함수를 즉시 종료합니다.
        
    spot = {"name": name, "category": category, "x": x, "y": y} # 입력받을 데이터를 딕셔너리로 묶습니다.
    hotplace_list.append(spot)                        # 전체 핫플 리스트에 저장합니다.
    print(f"{name} 등록 완료!")                    # 등록 성공 메시지를 출력합니다.

# 3. 텍스트 지도 출력 함수
def display_map(hotplace_list, size):
    grid_map = create_map(size)                       # 깨끗한 빈 지도를 새로 만듭니다.
    
    for spot in hotplace_list:                        # 저장된 핫플을 하나씩 꺼내어 반복합니다.
        x = spot["x"]                                 # 핫플의 X 좌표를 가져옵니다.
        y = spot["y"]                                 # 핫플의 Y 좌표를 가져옵니다.
        
        if spot["category"] == "카페":                # 카테고리가 카페라면 실행합니다.
            grid_map[y][x] = "C"                      # 지도 해당 칸을 'C'로 바꿉니다.
        elif spot["category"] == "식당":              # 카테고리가 식당이라면 실행합니다.
            grid_map[y][x] = "R"                      # 지도 해당 칸을 'R'로 바꿉니다.
            
    print(f"\n--- 핫플 분포 지도 ({size}x{size}) ---") # 지도 상단 타이틀을 출력합니다.
    for row in grid_map:                              # 지도의 행을 한 줄씩 꺼내어 반복합니다.
        print(" ".join(row))                          # 리스트 안의 글자들을 공백으로 연결해 한 줄로 출력합니다.
    print("---------------------------------")         # 지도 하단 구분선을 출력합니다.

# 4. 구역별 밀집도 계산 함수
def analyze_density(hotplace_list):
    print("\n--- 구역 밀집도 분석 ---")               # 분석 메뉴 타이틀을 출력합니다.
    start_x = int(input("시작 X 좌표 입력: "))        # 검사할 구역의 시작 X 좌표를 받습니다.
    end_x = int(input("끝 X 좌표 입력: "))            # 검사할 구역의 끝 X 좌표를 받습니다.
    start_y = int(input("시작 Y 좌표 입력: "))        # 검사할 구역의 시작 Y 좌표를 받습니다.
    end_y = int(input("끝 Y 좌표 입력: "))            # 검사할 구역의 끝 Y 좌표를 받습니다.
    
    count = 0                                         # 구역 내 핫플 개수를 세기 위한 변수입니다.
    for spot in hotplace_list:                        # 전체 핫플을 하나씩 검사합니다.
        if start_x <= spot["x"] <= end_x and start_y <= spot["y"] <= end_y: # 핫플이 지정된 사각형 범위 안에 있는지 확인합니다.
            count = count + 1                         # 범위 안에 있다면 개수를 1 증가시킵니다.
            
    print(f"설정하신 구역 내에 총 {count}개의 핫플이 있습니다.") # 최종 계산된 개수를 출력합니다.

# ========================================================
# 메인 프로그램 제어 (실행부)
# ========================================================
map_size = int(input("지도의 크기를 입력하세요 (추천: 5 ~ 10): ")) # 처음 시작할 때 지도의 크기를 설정합니다.
my_hotplaces = []

while True:                                           # 사용자가 종료할 때까지 무한 반복합니다.
    print("\n[ 메뉴를 선택하세요 ]")                  # 메뉴 목록을 보여줍니다.
    print("1. 핫플 등록하기")                         # 1번 메뉴 안내
    print("2. 현재 지도 보기")                         # 2번 메뉴 안내
    print("3. 구역 밀집도 분석")                       # 3번 메뉴 안내
    print("4. 프로그램 종료")                         # 4번 메뉴 안내
    
    choice = input("선택 (1~4): ")                    # 사용자에게 메뉴 번호를 입력받습니다.
    
    if choice == "1":                                 # 1을 입력했다면 실행합니다.
        add_place(my_hotplaces, map_size)             # 핫플 등록 함수를 호출합니다.
    elif choice == "2":                               # 2를 입력했다면 실행합니다.
        display_map(my_hotplaces, map_size)           # 지도 출력 함수를 호출합니다.
    elif choice == "3":                               # 3을 입력했다면 실행합니다.
        analyze_density(my_hotplaces)                 # 밀집도 분석 함수를 호출합니다.
    elif choice == "4":                               # 4를 입력했다면 실행합니다.
        print("프로그램을 종료합니다.") # 종료 메시지를 출력합니다.
        break                                         # while 반복문을 탈출하여 프로그램을 끝냅니다.
    else:                                             # 1~4 외에 다른 것을 입력했다면 실행합니다.
        print("잘못된 입력입니다. 1에서 4 사이의 숫자를 입력해주세요.") # 경고 메시지를 출력합니다.