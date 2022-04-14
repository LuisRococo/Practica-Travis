import pytest
from library.books.models import *

@pytest.mark.django_db
def test_new_language ():
    langauge = BookLanguage.objects.create(name='nombre1', short_name = 'nombre2')
    count = BookLanguage.objects.all().count()
    print (count)
    assert (count > 0)


@pytest.mark.parametrize('name, short_name, name_validate',
(
	('lenguage1','leng1', 'lenguage1'), 
	('lenguage2','leng2', 'lenguage2'), 
	('lenguage3','leng3', 'lenguage3')
))
@pytest.mark.django_db
def test_language_check_for_data_corrupttion (name, short_name, name_validate):
    language = BookLanguage.objects.create(name=name, short_name=short_name)
    print(f'Object Value: {language.name} - Validation Value: {name_validate}')
    assert (language.name == name_validate)


@pytest.mark.parametrize('name, short_name, total_size',
(
	('lenguage1','leng1', 3), 
	('lenguage2','leng2', 5), 
	('lenguage3','leng3', 7)
))
@pytest.mark.django_db
def test_language_row_creation (name, short_name, total_size):
    for i in range(total_size):
        BookLanguage.objects.create(name=name, short_name=short_name)
    count = BookLanguage.objects.all().count()
    print(f'Expected Quantity: {total_size} - Result: {count}')
    assert(total_size == count)

@pytest.mark.parametrize('name, short_name, new_name',
(
	('lenguage1','leng1', 'new value 1'), 
	('lenguage2','leng2', 'new value 2'), 
	('lenguage3','leng3', 'new value 3')
))
@pytest.mark.django_db
def test_language_update (name, short_name, new_name):
    instance = BookLanguage.objects.create(name=name, short_name=short_name)
    #print(dir(instance))
    instance.name = new_name
    instance.save()
    print(f'Update To: {new_name} - Updated Value: {instance.name}')
    assert(new_name == instance.name)

#ideas
# 1. check creation of isntances (name, short_name, size)
# 2. check check_for_data_corruption
# 3. check delete

#other ideas
# 4. check update