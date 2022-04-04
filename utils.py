import pickle

def dump_pickle(file,dir):
    """
    cannot serialize a bytes object larger than 4 GiB
    """
    with open(dir,'wb') as f:
        pickle.dump(file,f,protocol=4)

def load_pickle(dir):
    with open(dir,'rb') as f:
        out_file = pickle.load(f)
    return out_file


def distinct(ls):
    return len(set(ls))


def chunk_list(datas, chunksize):
    
    """Split list into the chucks

    Params:
        datas     (list): data that want to split into the chunk
        chunksize (int) : how much maximum data in each chunks

    Returns:
        chunks (obj): the chunk of list
        
    # https://stackoverflow.com/questions/41868890/how-to-loop-through-a-python-list-in-batch
    """

    for i in range(0, len(datas), chunksize):
        yield datas[i:i + chunksize]