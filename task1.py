import pickle

import k_means

model_map = ['color_moment', 'elbp', 'hog']
reduction_technique_map = [None, None, None, k_means.compute_k_means]

def start_task1():
    model = int(input('model number: '))
    x = input('value for x: ')
    k = int(input('value for k: '))
    reduction_technique = int(input('reduction technique: '))

    with open('metadata.pickle', 'rb') as handle:
        metadata = pickle.load(handle)

    data_matrix, semantics_matrix = [], []
    for key in metadata:
        key_tokens = key.split('.')[0].split('-')
        if key_tokens[0] == x:
            data_matrix.append(metadata[key][model_map[model]])

    try:
        semantics_matrix = reduction_technique_map[reduction_technique](data_matrix)
    except:
        print('Invalid reduction technique selection, please select from 0-3')
        return

    print('random')