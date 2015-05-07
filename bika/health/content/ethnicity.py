from zope.interface import implements
from Products.Archetypes import atapi
from Products.Archetypes.public import BaseContent
from bika.health.interfaces import IEthnicity
from bika.lims.content.bikaschema import BikaSchema
from bika.health import config


schema = BikaSchema.copy() + atapi.Schema((

))


class Ethnicity(BaseContent):
    # It implements the IEthnicity interface
    implements(IEthnicity)
    schema = schema

# Activating the content type in Archetypes' internal types registry
atapi.registerType(Ethnicity, config.PROJECTNAME)
