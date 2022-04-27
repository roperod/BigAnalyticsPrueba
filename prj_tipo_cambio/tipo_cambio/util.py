from re import fullmatch

from numpy import full

_url = "https://www.banguat.gob.gt/variables/ws/TipoCambio.asmx"

_header = {"Content-Type": "text/xml"}

def get_data(fecha):
    fecha = str(fecha).replace("-","/")
    if fullmatch("([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}",fecha):
        return f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <TipoCambioRango xmlns="http://www.banguat.gob.gt/variables/ws/">
                    <fechainit>{fecha}</fechainit>
                    <fechafin>{fecha}</fechafin>
                    </TipoCambioRango>
                </soap:Body>
                </soap:Envelope>"""
    else:
        return ""


def get_variable(xml:str, var:str):
    # <?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><TipoCambioDiaResponse xmlns="http://www.banguat.gob.gt/variables/ws/"><TipoCambioDiaResult><CambioDolar><VarDolar><fecha>26/04/2022</fecha><referencia>7.65144</referencia></VarDolar></CambioDolar><TotalItems>1</TotalItems></TipoCambioDiaResult></TipoCambioDiaResponse></soap:Body></soap:Envelope>
    start = xml.find("<"+var+">")
    end = xml.find("</"+var+">")
    if start!=-1 and end!=-1:
        return xml[start+len(var)+2:end]
    else:
        return ''