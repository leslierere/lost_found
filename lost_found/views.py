from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('info_site_list_url_pattern')