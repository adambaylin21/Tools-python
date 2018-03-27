import requests
from requests.auth import HTTPBasicAuth
import base64

url="http://sms.8x77.vn:8077/mt-services/MTService?wsdl"
headers = {'content-type': 'application/soap+xml'}
# headers = {'content-type': 'text/xml'}




smstext = b"Hello"
messenger = base64.b64encode(smstext)
body1 = """
<!--REQUEST.................-->
<env:Envelope  xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
 <env:Header>
 </env:Header>
 <env:Body   env:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <m:sendMT    xmlns:m="MTService">
   <string     xsi:type="xsd:string">0972937793</string>
   <string0     xsi:type="xsd:string">"""

body2 = """</string0>
   <string1     xsi:type="xsd:string">LUXURYFAN</string1>
   <string2     xsi:type="xsd:string">LUXURYFAN</string2>
   <string3     xsi:type="xsd:string">0</string3>
   <string4     xsi:type="xsd:string">0</string4>
   <string5     xsi:type="xsd:string">1</string5>
   <string6     xsi:type="xsd:string">1</string6>
   <string7     xsi:type="xsd:string">0</string7>
   <string8     xsi:type="xsd:string">0</string8>
  </m:sendMT>
 </env:Body>
</env:Envelope>"""
body = (body1 + messenger.decode("utf-8") + body2)
# response = requests.post(url,data=str(body),headers=headers,auth=('luxuryfan', 'bxluxur@678#'))
# print (response.content)
# with open('output.xml', 'w') as post:
#     post.write(str(response.content))
print (messenger)