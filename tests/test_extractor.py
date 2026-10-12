from agente.extractor import validacion_respuesta
import pytest

def test_validar_respuesta():
    datos = {"descripcion": "Oficina a Centro Comercial",
        "proyecto": "Obra Minitas",}
    assert validacion_respuesta(datos) == datos 
    
def test_validar_respuesta_sin_proyecto():
    datos = {"descripcion": "Oficina a Centro Comercial",}
    with pytest.raises(ValueError):
        validacion_respuesta(datos)