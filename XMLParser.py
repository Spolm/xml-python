import xml.etree.ElementTree as etree
nsmap = {}
results = []

def add(elem, nsmap):
    return ('npi')

def fixtag(ns, tag, nsmap):
  return '{' + nsmap[ns] + '}' + tag
for event, elem in etree.iterparse('Test.xml', events=('start-ns','start','end')):
    #Obtenemos el namespace
    if event == 'start-ns':
        ns, url = elem
        nsmap[ns] = url
        #entra en este if cada vez que inicia un tag
    if event == 'start':
        url = elem
        # print('tag:', elem.tag, '\n attrib:',elem.attrib)
        #imprime clave y valor
        #clave: namespace:nombre 
        for key in elem.attrib.keys():
            print('clave:', key, 'valor:',elem.attrib[key])

        # if elem.tag == fixtag('ns1', 'Products', nsmap):
        #     for child in elem:
    # print(results)
    if event == 'end':        
            # print('attrib:', elem.attrib,' Value ', elem.text)
            result = add(elem, nsmap)
            results.append(result)
    #print('atributo:', elem.attrib)
    # print (event, elem)

    

