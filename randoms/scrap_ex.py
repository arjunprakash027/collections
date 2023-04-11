from lxml import html
import requests

page = requests.get('https://www.mercadolibre.com.do/#from=homecom')

tree = html.fromstring(page.content)

certifications = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "cookie-consent-banner-opt-out__action--key-accept", " " ))] | //*[(@id = "root-app")]//h2')

if certifications:
    print("Certifications found")
else:
    print("Certifications not found")

for certificates in certifications:
    print(certificates.text)