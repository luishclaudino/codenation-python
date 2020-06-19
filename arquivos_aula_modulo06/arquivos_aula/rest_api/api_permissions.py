from rest_framework.permissions import BasePermission


#Tem que usar HTTPS quando for para produção pois alguém pode interceptar
#esse token e se passar pelo usuário
class OnlyAdminCanCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_staff
        return True
