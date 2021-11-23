import pkg_resources

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
# from plone.i18n.normalizer.base import baseNormalize

import json

# Codici ISO e ISTAT dei paesi esteri
# https://www.salute.gov.it/portale/tracciabilita/dettaglioPubblicazioniTracciabilita.jsp?lingua=italiano&id=1055

nazioni = json.loads(pkg_resources.resource_string('unibo.vocabularies', "nazioni.json"))["Nazioni"]

nazioniVocabulary = SimpleVocabulary([
    SimpleTerm(value=item["Sigla Estesa"], token=item["Sigla Estesa"], title=item["Descrizione"])
    for item in sorted(nazioni, key=lambda d: d['Descrizione'])
])
