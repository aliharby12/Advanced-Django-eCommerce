from rest_framework.permissions import BasePermission

# we will create a custom permission class
#  to prevent any user to edit any post does't belong to him
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self,request, view, obj):
        return obj.user == request.user
