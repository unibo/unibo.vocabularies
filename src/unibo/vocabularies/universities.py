import pkg_resources

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import json

# OpenData MIUR
# http://dati.ustat.miur.it/dataset/metadati/resource/a332a119-6c4b-44f5-80eb-3aca45a9e8e8
# update
# wget -O italian_universities.json \
#   "http://dati.ustat.miur.it/api/3/action/datastore_search?resource_id=a332a119-6c4b-44f5-80eb-3aca45a9e8e8&"

italianUniversities = json.loads(
        pkg_resources.resource_string(
            'unibo.vocabularies', "italian_universities.json")
    )["result"]["records"]

italianUniversitiesVocabulary = SimpleVocabulary([
    SimpleTerm(
        value=item["COD_Ateneo"],
        token=item["COD_Ateneo"],
        title=item["NomeEsteso"],
    )
    for item in sorted(italianUniversities, key=lambda d: d['NomeEsteso'])
])
