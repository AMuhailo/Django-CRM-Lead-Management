from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class LoginMixinOrganisation(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organisation:
            return redirect('lead:lead_list_url')
        return super().dispatch(request, *args, **kwargs)