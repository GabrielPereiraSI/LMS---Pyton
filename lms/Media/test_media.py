from media import calcula_media

def test_media():
    assert calcula_media([1,2,3]) == 2
    assert calcula_media([2,3,4,10]) == 4.75
    assert calcula_media([4]) == 4