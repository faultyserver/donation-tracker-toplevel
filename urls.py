from django.conf.urls import patterns, include, url

from django.contrib import admin

import tracker.urls
from tracker.views import logout
import ajax_select.urls

urlpatterns = [
    url(r'^tracker/', include(tracker.urls)),
    url(r'^admin/lookups/', include(ajax_select.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/', logout),
]

try:
    import tracker_ui.urls
    urlpatterns += [url(r'^ui/', include(tracker_ui.urls))]
except ImportError as e:
    import traceback
    import warnings
    print traceback.print_exc()
    warnings.warn("Could not locate tracker_ui module, starting without it")
