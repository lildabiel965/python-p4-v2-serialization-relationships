from models import *


class TestAnimal:
    '''Class Animal in models.py'''

    def test_converts_to_dict(self):
        '''can convert Animal objects to dictionaries.'''
        a = Animal(name="Lion", species="Panthera leo", zookeeper_id=1, enclosure_id=1)
        assert a.to_dict()
        assert isinstance(a.to_dict(), dict)


class TestEnclosure:
    '''Class Enclosure in models.py'''

    def test_converts_to_dict(self):
        '''can convert Enclosure objects to dictionaries.'''
        e = Enclosure(environment="Savannah", open_to_visitors=True)
        assert e.to_dict()
        assert isinstance(e.to_dict(), dict)


class TestZookeeper:
    '''Class Zookeeper in models.py'''

    def test_converts_to_dict(self):
        '''can convert Zookeeper objects to dictionaries.'''
        z = Zookeeper(name="John Doe", birthday="1980-01-01")
        assert z.to_dict()
        assert isinstance(z.to_dict(), dict)
