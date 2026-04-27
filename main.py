# 파일이름 : 은하탐사대 관리 시스템
# 작 성 자 : 남상민

explorers_list = []
total_skill_points = 0

print("="*45)
print("[오리온 프로젝트: 은하 탐사대 관리 시스템]")
print("="*45)

for i in range(1, 4):
    print(f"\n({i}/3) {i}번째 탐사 대원의 정보를 입력하세요.")
    name = input("대원 이름 (문자열): ")
    oxygen = int(input("산소 보유량 (정수, 0~100): "))
    fuel_eff = float(input("연료 효율 (실수, 0.5~5.0): "))
    tech_skill = int(input("기술 점수 (정수, 0~100): "))
    is_special = input("특수 자원 보유 여부 (y/n): ")

    total_skill_points += tech_skill

    survival_index = (oxygen * 0.6) + (fuel_eff * 1.5) + (tech_skill * 2.2)

    explorers_list.append([name, oxygen, fuel_eff, tech_skill, survival_index, is_special])

print("\n" + "*" * 45)
print("[탐사대 정밀 진단 결과]")
print("*" * 45)

count = len(explorers_list)
scores_only = []
for member in explorers_list:
    scores_only.append(member[4])

top_score = max(scores_only)

scores_only.sort(reverse=True)

for member in explorers_list:
    m_name = member[0]
    m_ox = member[1]
    m_score = member[4]
    m_res = member[5]

    if m_score >= 200:
        rank = "S (마스터)"
        if m_score >= 230 and m_res == 'y':
            rank += "★[전설의 개척자]★"
    
    elif m_score >= 150:
        rank = "A (베테랑)"
    elif m_score >= 100:
        rank = "B (일반)"
    else:
        rank = "F (훈련병)"

    print(f"대원: {m_name:5s} | 기여 지수: {m_score:6.2f} | 판정: {rank}")

print("\n" + "-" * 45)
print(f"총 관리 대원: {count}명")
print(f"대원 기술 점수 총합: {total_skill_points}")
print(f"금일 최고 생존 지수: {top_score:.2f}")
print(f"점수 랭킹: {scores_only}")

print("\n[긴급 시스템 점검]")
for member in explorers_list:
    if member[1] < 20:
        print(f"!! 경고: {member[0]} 대원 산소 부족! 시스템을 중단하고 복귀 명령을 내립니다.")
        break
    else:
        continue

print("\n관리 업무가 정상적으로 종료되었습니다. 지구로 귀환합니다.")
print("=" * 45)


