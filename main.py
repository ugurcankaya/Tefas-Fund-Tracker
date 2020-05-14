import requests
import lxml.html
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
link = "https://tefas.gov.tr/FonAnaliz.aspx?FonKod=AFT"
f = requests.get(link,  verify=False)
principal = 118861
firstPaid = 6367.68

html = f.text
doc = lxml.html.fromstring(html)
for element in doc.xpath('//*[@id="MainContent_PanelInfo"]/div[1]/ul[1]/li[1]/span'):
  val = str( element.text_content().strip() )

value =  float(val.replace(",", "."))
presentVal = round(value * principal, 2)

if firstPaid == presentVal:
  print("Neither Profit nor Lose")
  print(principal*value)
elif firstPaid > presentVal:
  print("Lose!  = -" + str( round(firstPaid-presentVal, 2) ) + "TL")
  print(principal*value)
else:
  print("Gain!  = +" + str( round(presentVal-firstPaid, 2) ) + "TL")
  print(principal*value)
print(value)
