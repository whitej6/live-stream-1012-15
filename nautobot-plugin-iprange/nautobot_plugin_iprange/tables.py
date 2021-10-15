from django.db import models
import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ButtonsColumn, ToggleColumn

from nautobot_plugin_iprange.models import IPRange


class IPRangeTable(BaseTable):
    pk = ToggleColumn()
    start_address = tables.Column(linkify=True)
    vrf = tables.LinkColumn()
    actions = ButtonsColumn(IPRange, buttons=("edit", "delete"))

    class Meta(BaseTable.Meta):
        model = IPRange
        fields = ["pk", "start_address", "end_address", "vrf", "size", "description"]
