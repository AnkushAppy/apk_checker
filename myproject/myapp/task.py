from myproject.myapp.models import Document
from myproject.myapp.models import FileInfo
from myproject.myapp.forms import DocumentForm
from androguard.core.bytecodes import apk

#djang-rq
from django_rq import job



#put redis job descriptor here but later
@job
def apk_reader(file_url, file_orignal_name):

	a=apk.APK('/Users/dolcera23/Desktop/myproject/media/documents/' + file_orignal_name)
	d = a.get_permissions()
	newfile = FileInfo(file_name=file_url, permissions_info = d)
	newfile.save()