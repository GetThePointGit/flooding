from django.conf import settings
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns, url
from django.contrib import admin

import flooding_base.urls
import flooding_lib.urls
import flooding_presentation.urls
import flooding_visualization.urls
import lizard_worker.urls

from flooding.views import ScenarioWorkflowView

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^flooding/', include(flooding_lib.urls)),
    (r'^visualization/', include(flooding_visualization.urls)),
    (r'^presentation/', include(flooding_presentation.urls)),
    (r'^worker/', include(lizard_worker.urls)),
    (r'', include(flooding_base.urls)),

    url(r'^scenarios_processing/$', ScenarioWorkflowView.as_view(),
        name="scenarios_processing"),

    url(r'^scenarios_processing/step/(?P<step>\d+)$', ScenarioWorkflowView.as_view(),
        name="scenarios_processing"),

    url(r'^execute$', ScenarioWorkflowView.as_view(),
        name="execute_scenario"),

    (r'^i18n/', include('django.conf.urls.i18n')),
    )


if settings.DEBUG:
    # Add this also to the projects that use this application
    urlpatterns += patterns(
        '', (r'', include('django.contrib.staticfiles.urls')))
