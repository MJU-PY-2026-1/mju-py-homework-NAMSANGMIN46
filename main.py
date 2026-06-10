# 파일이름 : 은하탐사대 관리 시스템
# 작 성 자 : 남상민

import os

explorers_data = []
FILE_NAME = "crew_manifest.txt"

print("="* 55)
print("[오리온 프로젝트: 은하 지휘 통제 시스템 V3.0]")
print("="* 55)

print("▶ [시스템 부팅] 외부 데이터베이스 파일 확인 중...")
try :
    with open(FILE_NAME, "r", encoding="utf-8") as file :
        for line in file:
            if line.strip():
                parts = line.strip().split(",")
                name = parts[0]
                oxygen = int(parts[1])
                fuel = float(parts[2])
                tech = int(parts[3])
                score = float =(parts[4])
                rank = parts[5]

                explorers_data.append([name, oxygen, fuel, tech, score, rank])
    print(f"▶ 로드 성공: 기존에 저장된 대원 {len(explorers_data)}명의 명부를 불러왔습니다.")
except FileNotFoundError :
    print("▶ 시스템 안내: 기존 데이터 파일이 없습니다. 새로운 가상 명부를 개설합니다.")

while True: 
    print("\n" + "=" * 55)
    print("[메인 지휘 통제 메뉴]")
    print("=" * 55)
    print(" 1. 신규 탐사 대원 등록(데이터 추가 및 데이터 검증)")
    print(" 2. 탐사대 명부 조회 (이중 순회 및 리스트 인덱싱)")
    print(" 3. 현재 대원 명부 파일 수동 저장(File Write)")
    print(" 4. 지구 귀환( 데이터 자동 백업 후 시스템 종료)")
    print("=" * 55)

    choice = input("실행할 명령 번호를 선택하세요:")

    if choice =="1":
        print("\n--- [1. 신규 탐사 대원 등록] ---")
        name = input("대원 이름(문자열): ")
        try :
            oxygen = int(input("산소 보유량 (정수, 0~100): "))
            fuel = float(input("연료 효율 (실수, 0.5~5.0): "))
            tech = int(input("기술 점수 (정수, 0~100): "))
        except ValueError:
            print("\n▶ 오류 발생: 수치 입력 칸에는 반드시 숫자만 입력해야 합니다.")
            print("▶ 시스템 안내: 대원 등록을 취소하고 메인 메뉴로 돌아갑니다.")
            continue

        score = (oxygen * 0.7) + (fuel * 1.5) + (tech * 1.8)

        if score >= 200:
            rank = "S(마스터)"
        elif score >= 150:
            rank = "A(베테랑)"
        elif score >= 100:
            rank = "B(일반)"
        else :
            rank = "F(훈련병)"
            explorers_data.append([name, oxygen, fuel, tech, score, rank])
            print(f"\n▶ 시스템 안내: {name} 대원의 데이터가 이중 리스트에 안전하게 입력되었습니다.")
    elif choice =="2":
        print("\n--- [2. 탐사대 명부 및 정밀 진단 조회] ---")
        if not explorers_data:
            print("▶ 시스템 안내: 현재 통제 기지에 상주 중인 대원이 없습니다.")
            continue
        print("-" * 65)
        print(f"{'이름':<8} | {'산소':<5} | {'연료':<5} | {'기술':<5} | {'종합 지수':<8} | {'최종 등급':<6}")
        print("-" * 65)

        for i in range(len(explorers_data)):
            e_name = explorers_data[i][0]
            e_ox = explorers_data[i][1]
            e_fuel = explorers_data[i][2]
            e_tech = explorers_data[i][3]
            e_score = explorers_data[i][4]
            e_rank = explorers_data[i][5]
            print(f"{e_name:<8} | {e_ox:<6d} | {e_fuel:<6.1f} | {e_tech:<6d} | {e_score:<9.2f} | {e_rank:<6}")
        print("-" * 65)

        print("\n[대원별 세부 능력치 매트릭스 순회]")
        for row in explorers_data:
            print(f"[{row[0]} 대원 기록] -> ", end="")
            for item in row[1:]:
                print(f"({item})", end=" ")
            print()
    elif choice == "3" :
        print("\n--- [3. 현재 대원 명부 파일 수동 저장] ---")
        if not explorers_data:
            print("▶ 시스템 안내: 저장할 데이터가 없습니다.")
            continue
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for row in explorers_data:
                data_line = f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}\n"
                file.write(data_line)
        print(f"▶ 시스템 안내: 총 {len(explorers_data)}명의 데이터가 '{FILE_NAME}' 파일에 안전하게 저장되었습니다.")
    elif choice == "4":
        print("\n--- [4. 지구 귀환 및 시스템 종료] ---")
        print("▶ 안전한 기지 폐쇄를 위해 데이터를 자동으로 백업 파일에 기록합니다...")
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for row in explorers_data:
                data_line = f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}\n"
                file.write(data_line)
        print("▶ 시스템 안내: 모든 데이터 백업 완료. 프로그램을 안전하게 종료하고 지구로 귀환합니다.")
        break
    else:
        print("\n▶ 경고: 잘못된 메뉴 번호입니다. 1번부터 4번 사이의 명령을 입력하세요.")