from metro import map_metro, v92, v103, v102, v20, v35


def main():
    # start = input('Откуда: ')
    # end = input('Куда: ')

    # v1, v2, i = 0, 0, 0

    # while v1 == 0 or v2 == 0:
        
    #     if start == map_metro.nodes[i].name:
    #         v1 = map_metro.nodes[i]
    #     if end == map_metro.nodes[i].name:
    #         v2 = map_metro.nodes[i]

    #     i += 1

    result = map_metro.find_path(v20, v35)

    print(result)


if __name__ == '__main__':
    main()
