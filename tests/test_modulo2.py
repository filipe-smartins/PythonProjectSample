from src.module2_dir.module2 import soma


def test_soma():
    assert soma('R$2.500', 'R$2.500') == 5000.0
    assert soma('R$ 2.500', 'R$ 2.500') == 5000.0
    assert soma('USD2.500', 'USD 2.500') == 5000.0
    assert soma('2.500', 'R$2.500') == 5000.0
    assert soma('2500', '2500') == 5000.0
