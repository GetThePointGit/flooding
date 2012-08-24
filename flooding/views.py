# Create your views here.

import logging

from django.http import HttpResponse
from django.utils import simplejson as json
from django.shortcuts import render_to_response
from django.views.generic import View

from flooding_worker import executor
from flooding_worker import models as workermodels

from flooding_lib import models as libmodels


logger = logging.getLogger(__name__)


class ScenarioWorkflowView(View):
    """
    Scenario processing view:
    shows latest execution status, logging.
    Contains functionality to execute a Scenario
    """
    template = 'scenarios_processing.html'

    def get(self, request, stap=1, amount_per_stap=20):
        scenarios = libmodels.Scenario.objects.all()
        processing = {}

        for scenario in scenarios:
            workflows = workermodels.Workflow.objects.filter(
                scenario=scenario.id)

            scenario_workflow = {
                'scenario_id': scenario.id,
                'scenario_name': scenario.name,
                'template_id': scenario.workflow_template.id,
                'template_code': scenario.workflow_template.code}

            if workflows.exists():
                workflow = workflows.latest('tcreated')
                scenario_workflow.update({
                        'workflows_count': workflows.count(),
                        'workflow': workflow})
            processing.update({scenario.id: scenario_workflow})

        context = {'processing': processing,
                   'stap': stap,
                   'amount_per_stap': amount_per_stap}

        return render_to_response(self.template, context)

    def post(self, request):
        scenario_id = request.POST.get('scenario_id')
        template_id = request.POST.get('template_id')
        success = executor.start_workflow(scenario_id, template_id)
        message = "Scenario {0} is {1} in de wachtrij geplaatst."
        if success == False:
            message = message.format(scenario_id, "NIET")
        else:
            message = message.format(scenario_id, "")
        context = {'success': success, 'message': message}
        return HttpResponse(content=json.dumps(context))
