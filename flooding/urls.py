from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

import lizard_base.urls
import lizard_flooding.urls
import lizard_presentation.urls
import lizard_visualization.urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^flooding/', include(lizard_flooding.urls)),
    (r'^visualization/', include(lizard_visualization.urls)),
    (r'^presentation/', include(lizard_presentation.urls)),
    (r'', include(lizard_base.urls)),
    )


if settings.DEBUG:
    # Add this also to the projects that use this application
    urlpatterns += patterns('',
        (r'', include('staticfiles.urls')),
    )
