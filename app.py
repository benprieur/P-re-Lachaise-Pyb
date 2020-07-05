import sys
import pywikibot
from pywikibot import pagegenerators
siteC = pywikibot.Site(u'commons', u'commons')
siteC.login()

category = pywikibot.Category(siteC, u'Graves in the Père-Lachaise Cemetery')
gen = category.subcategories(recurse=True)

INCLUDE = "{{Category definition: Object"
WIKIDATA = "|wikidata         = "
STRICT = "|strict           = no "
__LINE__ = "\n"

cmp = 0

for cat in gen:

    #print(cat.title())
    text = cat.text

    if text.find(WIKIDATA) < 0 and text.find(STRICT) <0:
        text = text.replace(INCLUDE, INCLUDE + __LINE__ + WIKIDATA + __LINE__ + STRICT)
    elif text.find(WIKIDATA) >= 0 and text.find(STRICT) <0:
        text = text.replace(INCLUDE, INCLUDE + __LINE__ + STRICT)

    if cat.text != text:
      cat.text = text
      cat.save(u"Add parameters wikidata and/or strict to 'Category definition' template")

      cmp = cmp + 1
      print("EDITED ===> " + cat.title() + " " + str(cmp))

