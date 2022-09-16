from collections import defaultdict

def check(year, month, day):
    if year < 2022 or year > 9999:
        return False
    
    if month < 1 or month > 12:
        return False
    
    if day < 1 or day > 31:
        return False
    
    # M1 = [1, 3, 5, 7, 8, 10, 12]
    M2 = [2, 4, 6, 9, 11]
    if month in M2 and day == 31:
        return False
    elif month == 2:
        if day > 29:
            return False
        elif day == 29:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  # 闰年判断
                return True
            else:
                return False
    
    return True

if __name__ == "__main__":
    q = int(input(''))
    dic = defaultdict(list)
    dic_message = defaultdict(list)

    for _ in range(q):
        a = input('').split()

        if a[0] == '1':
            year, month, day = int(a[1]), int(a[2]), int(a[3])

            if check(year, month, day):
                message = dic[(year, month, day)]
                if a[4] in dic_message:
                    print('existed')
                else:
                    message.append(a[4])
                    dic_message[a[4]] = [year, month, day]
                    print('done')
            else:
                print('error')
        
        elif a[0] == '2':
            year, month, day = int(a[1]), int(a[2]), int(a[3])

            if check(year, month, day):
                message = dic[(year, month, day)]
                print(len(message))
            else:
                print('error')
        
        else:
            if a[1] in dic_message:
                ans_list = dic_message[a[1]]

                ans = str(ans_list[0]) 

                for i in range(1, 3):
                    if ans_list[i] < 10:
                        ans += '/0'+str(ans_list[i])
                    else:
                        ans += '/'+str(ans_list[i])
                
                print(ans)
            else:
                print('not existed')
