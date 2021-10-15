from nautobot.core.api.serializers import ValidatedModelSerializer
from nautobot.ipam.api.nested_serializers import NestedVRFSerializer
from rest_framework.serializers import CharField

from nautobot_plugin_iprange.models import IPRange


class IPRangeSerializer(ValidatedModelSerializer):
    start_address = CharField()
    end_address = CharField()
    # vrf = NestedVRFSerializer()

    class Meta:
        model = IPRange
        fields = "__all__"
        # fields = ["display", "vrf", "id", "start_address", "end_address"]
