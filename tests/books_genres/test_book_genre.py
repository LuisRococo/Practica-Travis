import pytest
from library.books.models import *

@pytest.mark.parametrize('name, cant_create, cant_delete, cant_result',
(
	('name1', 5, 3, 2), 
	('name1', 5, 5, 0),
    ('name1', 7, 6, 1)
))
@pytest.mark.django_db
def test_genre_delete (name, cant_create, cant_delete, cant_result):
    instances = []
    for i in range(cant_create):
        instances.append(BookGenre.objects.create(name=name))
    for i in range(cant_delete):
        instance = instances[i]
        instance.delete()
    count = BookGenre.objects.all().count()
    print(f'Cant Result: {cant_result} - Actual Result: {count}')
    assert(count==cant_result)

@pytest.mark.parametrize('name, is_scary, new_value',
(
	('genre1', True, False), 
	('lenguage2',False, True), 
	('lenguage3', True, False)
))
@pytest.mark.django_db
def test_genre_update (name, is_scary, new_value):
    instance = BookGenre.objects.create(name=name, is_scary=is_scary)
    instance.is_scary = new_value
    instance.save()
    print(f'Update To: {new_value} - Updated Value: {instance.is_scary}')
    assert(new_value == instance.is_scary)


@pytest.mark.parametrize('name, is_scary, total_size',
(
	('name1',True, 3), 
	('name2',False, 5), 
	('name3',True, 7)
))
@pytest.mark.django_db
def test_genre_row_creation (name, is_scary, total_size):
    for i in range(total_size):
        BookGenre.objects.create(name=name, is_scary=is_scary)
    count = BookGenre.objects.all().count()
    print(f'Expected Quantity: {total_size} - Result: {count}')
    assert(total_size == count)