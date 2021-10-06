a = [0 ,1 ,0]

for i in range(5):
    # 배열 b 확장
    b = [0] * (i+4)

    #배열 b에 원소 추가
    for j in range(i+2):
        b[j+1] = a[j] + a[j+1]

    print(' ' *  (10-i), end = " ")

    # 배열에 원소를 추가한 부분까지만 출력
    for k in range(i + 2) :
        print(b[k+1], end = " ")

    print()
    # 반복은 수행하기 위해 배열 대체
    a = b