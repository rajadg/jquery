

from django.http import HttpResponse, JsonResponse


def lang_info(request):
    '''
        Simply render a response with some formatting
    '''
    accept_lang = request.META["HTTP_ACCEPT_LANGUAGE"]
    if ";" in accept_lang:
        accept_lang = accept_lang.split(";")[0]
    if "," in accept_lang:
        accept_lang = accept_lang.split(",")
    else:
        accept_lang = [accept_lang, ]
    out_js = "var lang_list=%s;" % accept_lang
    return HttpResponse(out_js)


def login_info(request):
    out_data = dict()
    out_data.update({"user": request.POST.get("user", "?"),
                     "password": request.POST.get("password", "*")})
    return JsonResponse(out_data)
