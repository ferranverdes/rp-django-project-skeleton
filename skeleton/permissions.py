from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		return True if request.method in permissions.SAFE_METHODS else False

class IsAccountAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		return True if any ([
			bool(request.user and request.user.is_staff),
			request.method in permissions.SAFE_METHODS
		]) else False
