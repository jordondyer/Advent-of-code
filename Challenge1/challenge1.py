def main():
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path+'/data.txt') as f:
        contents = f.read()
    all_calories = contents.split('\n\n')

    elv_cals = []
    for cals in all_calories:
        all_cals = cals.split('\n')
        all_cals = sum([int(x) for x in all_cals])
        elv_cals.append(all_cals)

    print(max(elv_cals))
    print(sum(sorted(elv_cals,reverse=True)[:3]))

if __name__ == '__main__':
    main()