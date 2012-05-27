#!/usr/bin/python
from lxml import etree
import httplib,urllib,sys
import cgi
import cgitb
cgitb.enable()
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

form = cgi.FieldStorage()

#if "area" not in form or "region" not in form or "ciudad" not in form:
#    print "<H1>Error</H1>"
#    print "Por favor rellene los campos area, region o ciudad."
#else:
#print "<p>pais:", form["pais"].value
#print "<p>area:", form["area"].value
#print "<p>ciudad:", form["ciudad"].value
#	print "<p>regimen:", form["regimen"].value
#	print "<p>alojamiento:", form["alojamiento"].value
#	print "<p>habitaciones:", form["habitaciones"].value
#	print "<p>adultos:", form["adultos"].value
#	print "<p>nino1:", form["nino1"].value
#	print "<p>nino2:", form["nino2"].value
#	print "<p>nino3:", form["nino3"].value
#	print "<p>nino4:", form["nino4"].value
#	print "<p>nino5:", form["nino5"].value

#    # Formateamos la salida del método
#arbolpais = etree.fromstring(cliente.service.GET_COUNTRIES())
#   # Definimos el listado que utilizaremos en el primer bucle
#paises = arbolpais.xpath ("//country/@name")

URL = 'http://wstest.rhodasol.es/wsserhs/rhodasol'

try:
    urllib.urlopen(URL).read()
    print "Conectado al servidor",'\n'
except:
    print "No es posible conectar con el servidor"
    sys.exit(1)


# Indicamos el elemento raiz de petición con los atributos 'type',
    # 'version' y 'sessionId' 
raizpeticion = etree.Element("request", \
    attrib={"type":"ACCOMMODATIONS_AVAIL","version":"4.1","sessionId":"5551123"})
    # Creamos la estructura del arbol a partir del elemento raiz
arbolpeticion = etree.ElementTree (raizpeticion)
    # Definimos el primer hijo del elemento raiz, es cliente y tiene
    # atributos 'code','branch' y 'password'
cliente = etree.SubElement(raizpeticion,"client",\
    attrib={"code":"ESTTRV", "branch":"8249", "password":"ESTTRVtest"})
    # Definimos el segundo hijo del raiz, es lenguaje y tiene el atributo 'code'
lenguaje = etree.SubElement(raizpeticion,"languaje", attrib={"code":"SPA"})
    # Definimos el tercer hijo del raiz, es criterio_b y contiene más elementos
criterio_b = etree.SubElement(raizpeticion,"searchCriteria")
    # Definimos los hijos de criterio_b, son criterio y todos tienen los atributos
    # 'type', 'code' y 'value', cambia el valor de 'code'
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"0", "code":"country", "value":""})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"0", "code":"area", "value":""})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"0", "code":"region", "value":"41"})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"0", "code":"city", "value":""})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"1", "code":"accommodationCode", "value":""})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"1", "code":"accommodationType", "value":"0"})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"1", "code":"category", "value":""})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"2", "code":"priceType", "value":"3"})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"2", "code":"offer", "value":""})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"2", "code":"concept", "value":""})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"2", "code":"board", "value":""})
criterio = etree.SubElement(criterio_b,"criterion", \
    attrib={"type":"2", "code":"cancelPolicies", "value":"1"})
    # Definimos el cuarto hijo del elemento raiz, es periodo y tiene los 
    # atributos de inicio > start y fin > end
periodo = etree.SubElement(raizpeticion, "period", \
    attrib={"start":"20120727", "end":"20120729"})
    # Definimos el quinto hijo del raiz, es rooms contiene los elementos de la estancia
habitaciones = etree.SubElement(raizpeticion, "rooms")
    # Definimos el primer hijo de rooms
habitacion = etree.SubElement(habitaciones, "room", \
    attrib={"type":"1", "adults":"2", "children":"0"})

pet_xml = etree.tostring(arbolpeticion,pretty_print=True)

print pet_xml

parameter = urllib.urlencode({'XML': pet_xml})
response = urllib.urlopen(URL, parameter)
print response.read()


# print etree.tostring(respuesta,pretty_print=True)