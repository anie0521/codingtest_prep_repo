N = int(input())

for i in range(1, N+1):
		# 각 자리수 i를 문자형으로 바꾸고 리스트에 저장해 자릿수 합을 구함
    cnt = sum(map(int, str(i)))
    
    # 자릿수의 합과 생성자를 합해 분해합을 구함
    res = cnt + i
    
    # 분해합과 입력값을 비교
    if res == N:
        print(i)
        break
    
    # 생성자 i와 입력값이 같으면 생성자가 없다는 것
    if i == N:
        print(0)
