from rest_framework.permissions import BasePermission

class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):

           if request.user == obj.created_by:

                return True

           else:

                return False
           

    
       
       