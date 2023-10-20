from .models import Avatar

def avatar_context(request):
    user_avatar = None
    if request.user.is_authenticated:
        try:
            user_avatar = Avatar.objects.get(user=request.user)# pylint: disable=no-member
        except Avatar.DoesNotExist:# pylint: disable=no-member
            pass
    return {'user_avatar': user_avatar}
