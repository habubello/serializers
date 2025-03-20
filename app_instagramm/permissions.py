from datetime import timedelta, datetime
from rest_framework.permissions import BasePermission, SAFE_METHODS

class CannotDeleteAfterTwoMinutes(BasePermission):
    """
    Komment 2 minutdan keyin o'chirilmasin
    """
    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            time_difference = datetime.now() - obj.created_at
            return time_difference <= timedelta(minutes=2)
        return True


class IsWeekday(BasePermission):
    """
    Kommentlar faqat ish kunlarida (Dushanbadan Jumagacha) ko'rinishi mumkin
    """
    def has_permission(self, request, view):
        today = datetime.today().weekday()  # 0 - Dushanba, 6 - Yakshanba
        return today in range(0, 5)  # Dushanba (0) dan Jumaga (4) gacha
