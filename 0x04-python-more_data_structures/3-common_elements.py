#!/usr/bin/python3
def common_elements(set_1, set_2):
    cmn = {ele for ele in set_1 if ele in set_2}
    return cmn
