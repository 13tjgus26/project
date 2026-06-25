import os  # 파일 존재 여부를 확인하고 삭제하기 위해 os 라이브러리를 가져옵니다.

# 1. 빈 지도 생성 함수
def create_map(size):
    grid_map = []                                     # 빈 리스트를 만듭니다.
    for i in range(size):                             # 지도 세로 크기만큼 반복합니다.
        row = ["."] * size                            # "."으로 채워진 한 줄(리스트)을 만듭니다.
        grid_map.append(row)                          # 만든 줄을 전체 지도 리스트에 추가합니다.
    return grid_map                                   # 완성된 2차원 리스트 지도를 반환합니다.


# 2. 좌표 유효성 검사 함수 (★함수 늘리기용: 코드를 더 쪼갰습니다)
def is_valid_coordinate(x, y, size):
    if x < 0 or x >= size or y < 0 or y >= size:      # 입력된 숫자가 지도 범위를 벗어났는지 확인합니다.
        return False                                  # 범위를 벗어났다면 가짜(False)를 반환합니다.
    return True                                       # 안전한 범위라면 진짜(True)를 반환합니다.


# 3. 핫플 정보 입력 및 저장 함수
def add_place(hotplace_list, size):
    name = input("핫플 이름을 입력하세요: ")          # 사용자에게 장소 이름을 입력받습니다.
    category = input("카테고리를 입력하세요 (카페/식당): ") # 카테고리를 입력받습니다.
    
    try:
        x = int(input(f"X 좌표를 입력하세요 (0 ~ {size-1}): ")) # X 좌표를 숫자로 입력받습니다.
        y = int(input(f"Y 좌표를 입력하세요 (0 ~ {size-1}): ")) # Y 좌표를 숫자로 입력받습니다.
    except ValueError:                                # 숫자가 아닌 글자가 입력되어 오류가 발생하면 실행합니다.
        print("❌ 에러: 좌표는 반드시 '숫자'로만 입력해주세요! 저장 실패.") # 에러 메시지를 출력합니다.
        return                                        # 함수를 즉시 종료합니다.
    
    if not is_valid_coordinate(x, y, size):           # 쪼갠 함수를 사용해 좌표 유효성을 검사합니다.
        print("❌ 에러: 지도를 벗어난 좌표입니다! 저장 실패.") # 에러 메시지를 출력합니다.
        return                                        # 함수를 즉시 종료합니다.
        
    spot = {"name": name, "category": category, "x": x, "y": y} # 입력받을 데이터를 딕셔너리로 묶습니다.
    hotplace_list.append(spot)                        # 전체 핫플 리스트에 저장합니다.
    print(f"✅ {name} 등록 완료!")                    # 등록 성공 메시지를 출력합니다.


# 4. 텍스트 지도 출력 함수
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


# 5. 구역별 밀집도 계산 함수
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
            
    print(f"📊 설정하신 구역 내에 총 {count}개의 핫플이 있습니다.") # 최종 계산된 개수를 출력합니다.


# 6. [신규 추가] 핫플 개별 검색 함수 (★함수 늘리기 및 기능 추가)
def search_place(hotplace_list):
    print("\n--- 핫플 개별 검색 ---")
    search_name = input("검색할 핫플 이름을 입력하세요: ") # 찾고 싶은 장소 이름을 입력받습니다.
    
    for spot in hotplace_list:                        # 데이터베이스를 순회하며 검색합니다.
        if spot["name"] == search_name:               # 같은 이름의 장소를 찾았다면 실행합니다.
            print(f"🔍 검색 결과 -> 이름: {spot['name']}, 종류: {spot['category']}, 위치: ({spot['x']}, {spot['y']})")
            return                                    # 찾았으므로 함수를 즉시 종료합니다.
            
    print("❌ 해당 이름의 핫플 정보가 존재하지 않습니다.") # 반복문이 끝날 때까지 못 찾았다면 출력합니다.


# 7. 파일 저장 함수
def save_data(hotplace_list):
    f = open("hotplaces.txt", "w", encoding="utf-8")  # hotplaces.txt 파일을 쓰기 모드로 엽니다.
    for spot in hotplace_list:                        # 저장된 핫플을 하나씩 꺼냅니다.
        line = f"{spot['name']},{spot['category']},{spot['x']},{spot['y']}\n" # 쉼표로 구분된 텍스트 문자열을 만듭니다.
        f.write(line)                                 # 파일에 한 줄을 씁니다.
    f.close()                                         # 파일을 닫습니다.
    print("💾 데이터가 'hotplaces.txt' 파일에 안전하게 저장되었습니다.") # 안내 메시지를 출력합니다.


# 8. 파일 불러오기 함수
def load_data():
    hotplace_list = []                                # 데이터를 담을 빈 리스트를 만듭니다.
    try:
        f = open("hotplaces.txt", "r", encoding="utf-8") # hotplaces.txt 파일을 읽기 모드로 엽니다.
        lines = f.readlines()                         # 파일의 모든 줄을 읽어와 리스트로 만듭니다.
        for line in lines:                            # 한 줄씩 꺼내어 반복합니다.
            line = line.strip()                       # 줄바꿈 문자(\n)를 제거합니다.
            if line:                                  # 빈 줄이 아니라면 실행합니다.
                parts = line.split(",")               # 쉼표를 기준으로 글자들을 자릅니다.
                spot = {"name": parts[0], "category": parts[1], "x": int(parts[2]), "y": int(parts[3])} # 다시 딕셔너리로 복원합니다.
                hotplace_list.append(spot)            # 리스트에 추가합니다.
        f.close()                                     # 파일을 닫습니다.
        print("📂 기존에 저장된 핫플 데이터를 성공적으로 불러왔습니다!") # 성공 메시지를 출력합니다.
    except FileNotFoundError:                         # 만약 저장된 파일이 없다면(처음 실행 시) 실행합니다.
        print("ℹ️ 기존 저장 파일이 없습니다. 새로운 데이터 투어를 시작합니다.") # 안내 메시지를 출력합니다.
    return hotplace_list                              # 불러온 리스트를 반환합니다.


# 9. [신규 추가] 전체 데이터 초기화 함수 (★함수 늘리기 및 기능 추가)
def clear_map_data():
    confirm = input("⚠️ 정말 모든 데이터를 삭제하시겠습니까? (y/n): ")
    if confirm.lower() == 'y':                        # 대소문자 상관없이 y를 눌렀다면 실행합니다.
        if os.path.exists("hotplaces.txt"):           # 저장 파일이 실제로 존재하는지 확인합니다.
            os.remove("hotplaces.txt")                # 텍스트 파일을 컴퓨터에서 물리적으로 삭제합니다.
        print("🧹 저장된 파일과 모든 데이터가 완전히 초기화되었습니다.")
        return True                                   # 초기화 성공을 알립니다.
    print("❌ 초기화가 취소되었습니다.")
    return False                                  # 초기화 취소를 알립니다.


# ========================================================
# 메인 프로그램 제어 (실행부)
# ========================================================
map_size = int(input("지도의 크기를 입력하세요 (추천: 5 ~ 10): ")) # 처음 시작할 때 지도의 크기를 설정합니다.
my_hotplaces = load_data()                            # 시작하자마자 파일에서 기존 데이터를 불러옵니다.

while True:                                           # 사용자가 종료할 때까지 무한 반복합니다.
    print("\n[ 메뉴를 선택하세요 ]")                  # 메뉴 목록을 보여줍니다.
    print("1. 핫플 등록하기")                         # 1번 메뉴 안내
    print("2. 현재 지도 보기")                         # 2번 메뉴 안내
    print("3. 구역 밀집도 분석")                       # 3번 메뉴 안내
    print("4. 특정 핫플 이름 검색")                    # 4번 메뉴 안내 (★새로 추가)
    print("5. 모든 데이터 초기화")                    # 5번 메뉴 안내 (★새로 추가)
    print("6. 프로그램 종료 및 자동 저장")              # 6번 메뉴 안내 (번호 변경)
    
    choice = input("선택 (1~6): ")                    # 사용자에게 메뉴 번호를 입력받습니다.
    
    if choice == "1":                                 # 1을 입력했다면 실행합니다.
        add_place(my_hotplaces, map_size)             # 핫플 등록 함수를 호출합니다.
    elif choice == "2":                               # 2를 입력했다면 실행합니다.
        display_map(my_hotplaces, map_size)           # 지도 출력 함수를 호출합니다.
    elif choice == "3":                               # 3을 입력했다면 실행합니다.
        analyze_density(my_hotplaces)                 # 밀집도 분석 함수를 호출합니다.
    elif choice == "4":                               # 4를 입력했다면 실행합니다.
        search_place(my_hotplaces)                    # 핫플 검색 함수를 호출합니다.
    elif choice == "5":                               # 5를 입력했다면 실행합니다.
        if clear_map_data():                          # 데이터 초기화 함수를 실행하고 성공했다면
            my_hotplaces = []                         # 프로그램 안의 리스트도 빈 상자로 만듭니다.
    elif choice == "6":                               # 6을 입력했다면 실행합니다.
        save_data(my_hotplaces)                       # 종료하기 전에 데이터를 파일에 저장합니다.
        print("👋 프로그램을 종료합니다. 즐거운 핫플 탐방 되세요!") # 종료 메시지를 출력합니다.
        break                                         # while 반복문을 탈출하여 프로그램을 끝냅니다.
    else:                                             # 1~6 외에 다른 것을 입력했다면 실행합니다.
        print("⚠️ 잘못된 입력입니다. 1에서 6 사이의 숫자를 입력해주세요.") # 경고 메시지를 출력합니다.
    