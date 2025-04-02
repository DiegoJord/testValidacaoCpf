import pytest
from app.validacao import validar_cpf

def test_validar_cpf():
    assert validar_cpf("529.982.247-25") == True
    assert validar_cpf("111.111.111-11") == False
    assert validar_cpf("123.456.789-09") == False
    assert validar_cpf("52998224725") == True
    assert validar_cpf("00000000000") == False
    assert validar_cpf("529.982.247-24") == False

def test_cpf_com_formatacao():
    assert validar_cpf("529.982.247-25") == True
    assert validar_cpf("52998224725") == True

def test_cpf_com_letras():
    assert validar_cpf("529.982.247-2a") == False
    assert validar_cpf("abcdefghi12") == False

def test_cpf_invalido():
    assert validar_cpf("123.456.789-00") == False
    assert validar_cpf("000.000.000-00") == False
    assert validar_cpf("99999999999") == False