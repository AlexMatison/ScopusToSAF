dcmappings = [
    {
        'scopus_name': 'abstract',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'description', 'qualifier': 'abstract'},
        },
    {
        'scopus_name': 'affiliation',
        'type': 'list_of_tuples',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'aggregationType',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'authkeywords',
        'type': 'list',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'subject', 'qualifier': 'other'},
        },
    {
        'scopus_name': 'authorgroup',
        'type': 'list_of_tuples',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'authors',
        'type': 'list_of_tuples',
        'tuple_key': 'indexed_name',
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'contributor', 'qualifier': 'author'},
        },
    {
        'scopus_name': 'authors',
        'type': 'list_of_tuples',
        'tuple_key': 'auid',
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'contributor', 'qualifier': 'author'},
        },
    {
        'scopus_name': 'chemicals',
        'type': 'list_of_tuples',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'subject', 'qualifier': 'other'},
        },
    {
        'scopus_name': 'citedby_count',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'citedby_link',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'confcode',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'confdate',
        'type': 'list_of_tuples',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'conflocation',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'confname',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'publisher'},
        },
    {
        'scopus_name': 'confsponsor',
        'type': '?',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'contributor_group',
        'type': 'list_of_tuples',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'correspondence',
        'type': 'tuple',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'coverDate',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'description',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'description', 'qualifier': 'abstract'},
        },
    {
        'scopus_name': 'doi',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'identifier'},
        },
    {
        'scopus_name': 'eid',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'endingPage',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'funding',
        'type': 'list_of_tuples',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'funding_text',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'identifier',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'identifier'},
        },
    {
        'scopus_name': 'idxterms',
        'type': 'list',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'isbn',
        'type': 'tuple',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'identifier'},
        },
    {
        'scopus_name': 'issn',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'identifier'},
        },
    {
        'scopus_name': 'issueIdentifier',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'issuetitle',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'language',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'language'},
        },
    {
        'scopus_name': 'pageRange',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'publicationName',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'publisher'},
        },
    {
        'scopus_name': 'publisher',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'publisher'},
        },
    {
        'scopus_name': 'publisheraddress',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'refcount',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'references',
        'type': 'list_of_tuples',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'scopus_link',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'self_link',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'sequencebank',
        'type': 'list_of_tuples',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'source_id',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'sourcetitle_abbreviation',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'srctype',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'startingPage',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'subject_areas',
        'type': 'list_of_tuples',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'subject'},
        },
    {
        'scopus_name': 'title',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'title'},
        },
    {
        'scopus_name': 'url',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': True,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'uri'},
        },
    {
        'scopus_name': 'volume',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    {
        'scopus_name': 'website',
        'type': 'value',
        'tuple_key': None,
        'include_in_xml_output': False,
        'schema': 'dc',
        'attributes': {'element': 'identifier', 'qualifier': 'title'},
        },
    ]


			