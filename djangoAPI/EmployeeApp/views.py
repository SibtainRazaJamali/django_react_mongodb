from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from EmployeeApp.models import Department,Employee



# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
	from EmployeeApp.serializers import EmployeeSerializer
	from EmployeeApp.serializers import DepartmentSerializer
	if request.method=='GET':
		departmentData=Department.objects.all()
		departmentSerialized= DepartmentSerializer(departmentData,many=True)
		return JsonResponse(departmentSerialized.data,safe=False)
	elif request.method=='POST':
		departmentParsed=JSONParser().parse(request)
		
		departmentSerialized = DepartmentSerializer(data=departmentParsed)
		if departmentSerialized.is_valid():
			departmentSerialized.save()
			return JsonResponse("Department added successfully.",safe=False)
		else:
			return JsonResponse("Failed to add a department.",safe=False)
	elif request.method=='PUT':
		departmentParsed=JSONParser().parse(request)
		department=Department.objects.get(DepartmentId=departmentParsed['DepartmentId'])
		DepartmentSerializer = DepartmentSerializer(department,data=departmentParsed)
		if DepartmentSerializer.is_valid():
			DepartmentSerializer.save()
			return JsonResponse("successfully updated department.",safe=False)
		else:
			return JsonResponse("failed to update the department.",safe=False)

	elif request.method=='DELETE':
		departmentToDelete=Department.objects.get(DepartmentId=id)
		departmentToDelete.delete()
		return JsonResponse("Department Deleted",safe=False)
