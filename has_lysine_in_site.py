import pandas as pd

def has_lysine_in_site():
    df = pd.read_excel('ATP_binding_sites.xlsx')

    def how_many_k(start, end, sequence):
        window_list = []
        k_count = 0

        for i in range(start-1, end):
            window_list.append(sequence[i])  # create a list of the letters in the window
            if sequence[i] == 'K':
                k_count += 1        # keep track of how many lysine

        window_string = ''.join(window_list)  # list to string

        return k_count, window_string

    print('')

    lysine_list = []
    for index, row in df.iterrows():
        x = how_many_k(row['binding_location_start'], row['binding_location_end'], row['sequence'])
        print(x)
        lysine_list.append(x)

    print(lysine_list)

    count_list = [x[0] for x in lysine_list]
    region_list = [x[1] for x in lysine_list]

    df['lysines_in_binding_region'] = count_list
    df['binding region'] = region_list

    print(len(df))

    df.to_excel('ATP_binding_sites.xlsx', sheet_name='Sheet1', index=False)

has_lysine_in_site()
