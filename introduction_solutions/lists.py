if __name__ == '__main__':
    liste =[]
    N = int(input()) # number of operations that we will perform
    for i in range(N):
        command_list = list(map(str, input().split()))
        if command_list[0] == 'insert':
            liste.insert(int(command_list[1]), int(command_list[2]))
        elif command_list[0] == 'print':
            print(liste)
        elif command_list[0] == 'remove':
            liste.remove(int(command_list[1]))
        elif command_list[0] == 'append':
            liste.append(int(command_list[1]))
        elif command_list[0] == 'sort':
            liste.sort()
        elif command_list[0] == 'pop':
            liste.pop()
        elif command_list[0] == 'reverse':
            liste.reverse()