from nautobot.core.api.views import ModelViewSet

from nautobot_plugin_iprange.api.serializers import IPRangeSerializer
from nautobot_plugin_iprange.models import IPRange


class IPRangeViewSet(ModelViewSet):
    queryset = IPRange.objects.all()
    serializer_class = IPRangeSerializer
