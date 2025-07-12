from .models import Notification

def unread_notification_count(request):
    if request.user.is_authenticated:
        return {
            'unread_count': Notification.objects.filter(user=request.user, read=False).count(),
            'latest_notifications': Notification.objects.filter(user=request.user).order_by('-created_at')[:10],
        }
    return {'unread_count': 0, 'latest_notifications': []} 