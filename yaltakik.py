import os


TEL_PATH = os.path.dirname(os.path.abspath(__file__)) + "/yaltakik.tel"
TEL_SET_PATH = os.path.dirname(os.path.abspath(__file__)) + "/yaltakik.tel.set"
SIMFER_TEXT_PATH = os.path.dirname()

def tel_filter(TEL_PATH):
    tels_list = []
    with open(TEL_PATH, 'r') as tels:
        for line in tels:
            tels_list.append(line.replace('\n', ''))
        return tels_list


TELS_SET = set(tel_filter(TEL_PATH))
print(TELS_SET)


def tel_set_writer(TELS_SET, TEL_SET_PATH):
    with open(TEL_SET_PATH, 'w') as tel_set:
        for tel in TELS_SET:
            tel_set.writelines(tel.replace(" ", "") + '\n')

# tel_set_writer(TELS_SET, TEL_SET_PATH)

