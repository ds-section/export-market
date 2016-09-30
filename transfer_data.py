import pandas as pd

# read every row and transfer to string that split by comma and double quote
def formalize_row(row):
    
    rs = ''

    for col in row.split('|'):
        # erase double quote and space
        col = col.replace('\"', '').strip()
        rs += ('\"' + col + '\",')

    # Change the last comma to \n
    rs = rs[:-1].upper() + '\n'

    return(rs)

# input txt from export goods than output accepted csv to sql 
def formalize_to_well_form_csv(txt_path):
    
    f_list = []
    csv_path = txt_path.split('.')[0] + '.csv'

    with open(txt_path, 'r') as f:

        for line in f:
            f_list.append(formalize_row(line))

    with open(csv_path, 'w') as f:
        
        for row in f_list:
            f.write(row)
    
    print('formalize_to_well_form_csv(' + txt_path + ') finished!')

# use pandas to clean the comma out in weight col, add _id
# input: csv, output: the same csv 
def parse_col(csv_path):
    
    csv = pd.read_csv(csv_path)

    # set the col to str type (replacable)
    csv['數量'] = csv['數量'].astype(str)
    csv['重量'] = csv['重量'].astype(str)
    csv['價值'] = csv['價值'].astype(str)

    csv['數量'] = csv['數量'].str.replace(pat=',', repl='')
    csv['重量'] = csv['重量'].str.replace(pat=',', repl='')
    csv['價值'] = csv['價值'].str.replace(pat=',', repl='')

    # add an id to index
    csv.index.name = '_id'

    ## save the csv file back
    csv.to_csv(csv_path, sep=',', encoding='utf-8')
    print('parse_weight_col_to_int(' + csv_path + ') finished!')

# count bad double quotes in col 英文貨品
def count_double_quotes():
    double_quotes_times = 0
    loop_time = 0

    for row in csv['英文貨品']:
        
        for element in row:
            
            loop_time += 1

            if '\"' in element:
                double_quotes_times += 1
                print_flag = True
            else:
                pass

    print('done, double_quotes_times:', double_quotes_times)
    print('loop_time:', loop_time)
    print('len(csv[\'英文貨品\']):', len(csv['英文貨品']))


file = '2016-07'
txt_path = 'export-goods/' + file + '.txt'
csv_path = 'export-goods/' + file + '.csv'


formalize_to_well_form_csv(txt_path)
parse_col(csv_path)
print()

csv = pd.read_csv(csv_path)
print(csv.dtypes)
print()







