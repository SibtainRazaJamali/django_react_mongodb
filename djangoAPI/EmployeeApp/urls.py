from EmployeeApp import views
from django.conf.urls import url

urlpatterns=[
	url(r"^department$",views.departmentApi),
	url(r"^department/([0-9]+)$",views.departmentApi)
]

