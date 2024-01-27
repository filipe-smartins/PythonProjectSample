from src.module1_dir.module1 import print_lower_name, print_upper_name, print_capitalized_name
from settings.settings import name


def test_print_lower_name():
    assert print_lower_name(name) == 'Your lower name is: filipe martins'


def test_print_upper_name():
    assert print_upper_name(name) == 'Your upper name is: FILIPE MARTINS'


def test_print_capitalized_name():
    assert print_capitalized_name(name) == 'Your capitalized name is: Filipe martins'
