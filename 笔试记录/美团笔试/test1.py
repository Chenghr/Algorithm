
if __name__ == "__main__":
    s = input("")

    count = 0

    for ch in s:
        if ch == ' ':
            count += 1
    
    print(count)