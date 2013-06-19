# Create your views here.
import sys
sys.path.append('/Users/python-sdk-3.0.0/qbox') # Change the path to where the sdk stored 
import uptoken

from django.http import HttpResponse
from django.http import HttpResponseRedirect

def uploadWithKeyAndCustomField(request):
    # Pass parameter scope(bucket name).
    tokenObj=uptoken.UploadToken(scope="wyangspace")
    token=tokenObj.generate_token()
    a='''<html>
 <body>
  <form method="post" action="http://up.qiniu.com/" enctype="multipart/form-data">
   <input name="token" type="hidden" value="'''
    
    b='''">
   <input name="x:custom_field_name" value="x:me">
   Image key in qiniu cloud storage: <input name="key" value="foo bar.jpg"><br>
   Image to upload: <input name="file" type="file"/>
   <input type="submit" value="Upload">
  </form>
 </body>
</html>'''
    htmlStr=a+token+b
    
    return HttpResponse(htmlStr)
