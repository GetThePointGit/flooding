from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

import flooding_base.urls
import flooding_lib.urls
import lizard_presentation.urls
import lizard_visualization.urls
import flooding_worker.urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^flooding/', include(flooding_lib.urls)),
    (r'^visualization/', include(lizard_visualization.urls)),
    (r'^presentation/', include(lizard_presentation.urls)),
    (r'^worker/', include(flooding_worker.urls)),
    (r'', include(flooding_base.urls)),
    )


if settings.DEBUG:
    # Add this also to the projects that use this application
    urlpatterns += patterns('',
        (r'', include('staticfiles.urls')),
    )
