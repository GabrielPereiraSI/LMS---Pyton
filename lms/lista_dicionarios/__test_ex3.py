from ex3 import media,insere_dic, dic

def test_ex3():
    dic['Fernando'] = [10, 8]
    assert media('Fernando') == 9
    dic['Amanda'] = [5, 7]
    assert media('Amanda') == 6
    