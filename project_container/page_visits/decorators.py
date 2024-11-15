from django.http import HttpResponseForbidden
from functools import wraps

def permission_required_403(permission):
    """
    Decorator to check if the user has a specific permission.
    If not, it returns a 403 Forbidden response.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user has the required permission
            if not request.user.has_perm(permission):
                # If user doesn't have permission, return a 403 Forbidden response
                return HttpResponseForbidden("You do not have permission to view this resource.")
            
            # If the user has permission, call the original view function
            return view_func(request, *args, **kwargs)
        
        return _wrapped_view
    
    return decorator
