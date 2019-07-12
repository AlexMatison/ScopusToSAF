from pybliometrics.scopus import ScopusSearch
from pybliometrics.scopus import AbstractRetrieval
from pybliometrics.scopus import AuthorRetrieval
from lxml import etree as et
import os
import requests
from config import dcmappings

saf_root_directory = 'saf'
science_direct_base_url = 'https://api.elsevier.com/content/article/doi/'

apiKey = os.environ['SCOPUS_API_KEY']
scopus_search_string = os.environ['SCOPUS_SEARCH_STRING']

s = ScopusSearch(scopus_search_string, refresh=True, view='COMPLETE')

print(s.get_results_size())
eids = s.get_eids()
counter = 0


orcid_mapping = {
    'schema': 'local',
    'attributes': {
        'element': 'contributor',
        'qualifier': 'author_orcid_id'
    }
}

def GetOrcidFromScopusID(scopus_id):
    try:
        author = AuthorRetrieval(scopus_id)
    except:
        print('exception trying to get author')
        return None
    print(author)
    
    #orcid = getattr(author, 'orcid')
    try:
        orcid = getattr(author, 'orcid')
    except:
        print('exception trying to get authors orcid')
        return None
    print('ORCID: ', orcid)
    return None # Remove this temporarily
    return orcid
    

for index, eid in enumerate(eids):
    item_from_scopus = AbstractRetrieval(eid, id_type='eid', view='FULL')
    #print(abstract)
    #print(abstract.abstract)
    #print(eid)
    
    print(item_from_scopus.__dict__.keys())
    
    doi = item_from_scopus.doi
    root = et.Element('dublin_core', schema='dc')
    
    # TODO generate this automatically
    xmls = {
        'dc': et.Element('dublin_core', schema='dc'),
        'local': et.Element('dublin_core', schema='local')
    }
    
    is_science_direct = False
    
    for dcmapping in dcmappings:
        try:
            attribute_value = getattr(item_from_scopus, dcmapping['scopus_name'])
        except:
            continue
        if attribute_value is None:
            continue
        #print(dcmapping['scopus_name'], attribute_value)
        if dcmapping['type'] == 'value' and dcmapping['include_in_xml_output']:
            dcvalue = et.SubElement(xmls[dcmapping['schema']], 'dcvalue') #, element=dcmapping['attributes']['element'], qualifier=dcmapping['attributes']['qualifier'])
            for key, value in dcmapping['attributes'].items():
                dcvalue.set(key, value)
            dcvalue.text = str(attribute_value)
        elif dcmapping['type'] == 'list_of_tuples':
            if dcmapping['tuple_key'] is not None and dcmapping['include_in_xml_output']:
                for item in attribute_value:
                    dcvalue = et.SubElement(xmls[dcmapping['schema']], 'dcvalue')
                    for key, value in dcmapping['attributes'].items():
                        dcvalue.set(key, value)
                    dcvalue.text = str(getattr(item, dcmapping['tuple_key']))
                    if dcmapping['tuple_key'] == 'auid':
                        # This is the authors scopus id, try and find their orcid
                        orcid_id = GetOrcidFromScopusID(getattr(item, dcmapping['tuple_key']))
                        if orcid_id is not None:
                            dcvalue = et.SubElement(xmls[orcid_mapping['schema']], 'dcvalue')
                            for key, value in orcid_mapping['attributes'].items():
                                dcvalue.set(key, value)
                            dcvalue.text = orcid_id
        
        is_science_direct = False
        #if dcmapping['scopus_name'] == 'publisher':
        #    if dcvalue.text.startswith('Elsevier'):
        #        is_science_direct = True
        #    else:
        #        is_science_direct = False
        #    print('publisher = ' + dcvalue.text)
    if getattr(item_from_scopus, 'doi') is not None:
        dcvalue = et.SubElement(xmls['dc'], 'dcvalue')
        dcvalue.set('element', 'identifier')
        dcvalue.set('qualifier', 'uri')
        dcvalue.text = 'https://dx.doi.org/' + getattr(item_from_scopus, 'doi')
        
    # Create SAF directory
    item_directory = os.path.join(saf_root_directory, 'item_' + str(index+1))
    #print(item_directory)
    if os.path.exists(item_directory):
        print("ERROR directory already exists")
    else:
        os.mkdir(item_directory)
    
    for schema, xml in xmls.items():
        if schema == 'dc':
            xml_filename = os.path.join(item_directory, 'dublin_core.xml')
        else:
            xml_filename = os.path.join(item_directory, 'metadata_' + schema + '.xml')

        with open(xml_filename, 'wb') as f:
            f.write(et.tostring(xml, pretty_print=True))
    
    # attempt to download science direct articles
    if is_science_direct:
        full_text_url = science_direct_base_url + doi
        parameters = {
            'apiKey': apiKey,
            'doi': doi
        }
            #'httpAccept': 'application/xml'
        response = requests.get(full_text_url, params=parameters, stream=True)
        print(response.status_code)
        if response.status_code == 200:
            with open(os.path.join(item_directory, 'document.xml'), 'wb') as f:
                #f.write(response.content)
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        
    print('********')
    if index > 2:
        break