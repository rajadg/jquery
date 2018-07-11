

import json
import os
from django.http import HttpResponse, JsonResponse


music_info = None


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


def get_usage_log(request):
    global music_info
    if music_info is None:
        data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "data")
        data_file = os.path.join(data_folder, "trial.json")
        with open(data_file, 'rb') as fp:
            all_data = json.load(fp)
            music_info = list(all_data.values())

    first_item = int(request.GET["first_item"])
    page_size = int(request.GET["page_size"])
    total_items = len(music_info)

    out_data = dict()
    if page_size < 0:
        page_size = total_items
    if first_item < total_items:
        last_item = first_item + page_size - 1
        if last_item >= total_items:
            last_item = total_items - 1
        out_data["last_item"] = last_item
        out_data["items"] = music_info[first_item:last_item + 1]
        out_data["count"] = last_item - first_item
    else:
        out_data["items"] = list()
        out_data["last_item"] = -1
        out_data["count"] = 0
    return JsonResponse(out_data)

