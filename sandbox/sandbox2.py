



def permission(permission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_superuser:
            return True
        return user.has_perm(self.__class__.__name__) or self.__class__.__name__ in user.groups.all().values_list('permissions__codename', flat = True)
    
    cls = type(f'{permission}', (), {'has_perm': has_permission})('')
    return cls


obj = permission("Permission")

print(obj.has_perm())


