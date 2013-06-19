#Python Example
===============
本Python网页上传工具通过Django框架搭建并使用七牛云存储提供的Python-SDK演示了如何使用Python和Python-SDK开发一个简单的web版文件上传工具样例。
主要内容如下：

安装Django
下载并配置七牛Python-SDK
创建Django项目

#安装Django
下载[Django-1.5.1.tar.gz](www.djangoproject.com/download)到本地 运行以下命令执行安装：

     tar xzvf Django-1.5.1.tar.gz
     cd Django-1.5.1
     sudo python setup.py install
#下载并配置Python-SDK
下载[七牛Python－SDK](https://github.com/qiniu/python-sdk)保存在本地。
进入Python-SDK目录，找到并修改config.py
       
       ACCESS_KEY = 'YOUR_ACCESS_KEY'
       SECRET_KEY = 'YOUR_SECRET_KEY'
       
 
#通过Django创建项目
在下面的操作中将会创建一个名为 djproject的项目：
        
        django-admin.py startproject djproject
该语句将在django-admin.py所在的目录中创建一个名为jdproject的目录，进入该项目，可以看到如下几个文件： 

manage.py: 可以使网站管理员来管理Django项目

setting.py: 此Django项目配置文件

urls.py: 包含URL配置文件，用户访问Django应用的方式

###创建一个Django应用
使用manage.py 创建一个名为Users的应用:
        
        manage.py startapp Users

使用startapp命令后，将会在djproject目录下生成一个Users目录。可一个看到Users目录下包含：

models.py: 定义数据模型相关信息

tests.py: 该应用的测试文件

views.py: 包含视图相关的信息
这个应用将用于显示上传文件的页面。



###URL设计
在urls.py文件中定义URL。向urls.py中添加如下代码:
            
    urlpatterns = patterns('',

    url(r'^Users/', 'Users.views.uploadWithKeyAndCustomField', name='uploadWithKeyAndCustomField'),
    
    
当访问localhost:8000/Users时，将调用Users目录下views.py文件中的uploadWithKeyAndCustomField()函数。
###创建视图

配置Users目录下，views.py文件的代码如下：
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

    
    

这段代码样例，可以指定文件存储到space的文件名，以及用户自定义的custom_field_name. 

七牛API中关于custom_field_name的说明如下：
自定义变量，必须以 x: 开头命名，不限个数。可以在 uploadToken 的 callbackBody 选项中使用 $(x:custom_field_name) 求值。

views.py中的uploadWithKeyAndCustomField()函数，将会生成uploadtoken。文件上传成功后显示up.qiniu.com返回的信息。

    
这样上传文件页面都已经配置完毕。
###启动服务器
   在命令行中，切换到djproject目录，输入如下命令：
         
      manage.py runserver
      
然后访问 http://localhost:8000/Users/ 