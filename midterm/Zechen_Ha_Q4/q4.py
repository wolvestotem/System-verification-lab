import os
    

dir_path = ['pt_mode','PT_MODE']

def find_cur(string, path):
    # print('cur_dir is %s' % os.path.abspath(path))
    l = []

    for x in os.listdir(path):
        if os.path.exists(dir_path):
            if string in x:
                l.append(os.path.abspath(x))


def deeper_dir(string='', p='..'): 
    find_cur(string, p)
    for x in os.listdir(p):

        pp = p 
        if os.path.isdir(pp):
            pp = os.path.join(pp, x)
            if os.path.exists(pp):
                deeper_dir(string, pp)

if __name__=='__main__':
    deeper_dir()
