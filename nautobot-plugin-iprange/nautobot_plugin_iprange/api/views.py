from nautobot.core.api.views import ModelViewSet

from nautobot_plugin_iprange.api.serializers import IPRangeSerializer
from nautobot_plugin_iprange.models import IPRange
from nautobot_plugin_iprange.filters import IPRangeFilterSet


class IPRangeViewSet(ModelViewSet):
    queryset = IPRange.objects.all()
    serializer_class = IPRangeSerializer
    filterset_class = IPRangeFilterSet
