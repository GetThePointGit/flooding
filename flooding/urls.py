from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

import flooding_base.urls
import flooding_lib.urls
import flooding_presentation.urls
import flooding_visualization.urls
import flooding_worker.urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^flooding/', include(flooding_lib.urls)),
    (r'^visualization/', include(flooding_visualization.urls)),
    (r'^presentation/', include(flooding_presentation.urls)),
    (r'^worker/', include(flooding_worker.urls)),
    (r'', include(flooding_base.urls)),
    )


if settings.DEBUG:
    # Add this also to the projects that use this application
    urlpatterns += patterns('',
        (r'', include('staticfiles.urls')),
    )
