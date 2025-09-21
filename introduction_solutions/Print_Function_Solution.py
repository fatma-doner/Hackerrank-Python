if __name__ == '__main__':
    n = int(input())
    
for i in range(n+1):
    if i ==0:
        continue
    print(i, end='')
    
    
#Normally, print() moves to a new line after each output.If we use end='', it prints on the same line without any space or character.