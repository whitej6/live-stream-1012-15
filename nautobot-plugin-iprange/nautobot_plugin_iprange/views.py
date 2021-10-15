from nautobot.core.views import generic

from nautobot_plugin_iprange import models, forms, filters, tables


class IPRangeEditView(generic.ObjectEditView):
    queryset = models.IPRange.objects.all()
    model_form = forms.IPRangeForm


class IPRangeDetailView(generic.ObjectView):
    queryset = models.IPRange.objects.all()


class IPRangeDeleteView(generic.ObjectDeleteView):
    queryset = models.IPRange.objects.all()


class IPRangeListView(generic.ObjectListView):
    queryset = models.IPRange.objects.all()
    filterset = filters.IPRangeFilterSet
    filterset_form = forms.IPRangeFilterForm
    action_buttons = ("add",)
    table = tables.IPRangeTable


class IPRangeBulkDeleteVIew(generic.BulkDeleteView):
    queryset = models.IPRange.objects.all()
    table = tables.IPRangeTable


class IPRangeBulkEditView(generic.BulkEditView):
    queryset = models.IPRange.objects.all()
    filterset = filters.IPRangeFilterSet
    table = tables.IPRangeTable
    form = forms.IPRangeBulkEditForm
