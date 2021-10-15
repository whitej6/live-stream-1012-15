from django.db.models import base
from nautobot.extras.filters import CreatedUpdatedFilterSet
from nautobot.utilities.filters import BaseFilterSet, TagFilter

from nautobot_plugin_iprange.models import IPRange


class IPRangeFilterSet(BaseFilterSet, CreatedUpdatedFilterSet):
    tags = TagFilter()

    class Meta:
        model = IPRange
        fields = ["id", "vrf", "size", "description", "tags"]
