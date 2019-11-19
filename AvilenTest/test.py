def main():
    lines = open('input.txt').read().split('\n')
    m = int(lines[-2])
    for line in lines[:-2]:
        i, s = line.split(':')
        if m%int(i) == 0:
            print(s)


if __name__ == '__main__':
    main()
