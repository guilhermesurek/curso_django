from aula8.forms import PetForm
from datetime import date
import pytest

def test_pet_form_valid():
    data = {
        "nome": "rex",
        "data_nascimento": date(2019, 1, 1)
    }
    form = PetForm(data=data)

    assert form.is_valid()

@pytest.mark.parametrize("name", ['Putinho', "putinho", "PUTINHO", "PuTiNhO"])
def test_pet_form_invalid(name):
    data = {
        "nome": "putinho",
        "data_nascimento": date(2019, 1, 1)
    }
    form = PetForm(data=data)

    assert form.is_valid() is False