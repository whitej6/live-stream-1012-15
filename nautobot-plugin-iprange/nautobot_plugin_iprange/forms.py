from django import forms
from nautobot.ipam.formfields import IPAddressFormField
from nautobot.ipam.models import VRF
from nautobot.utilities.forms import (
    BootstrapMixin,
    DynamicModelChoiceField,
    BulkEditForm,
    widgets,
)

from nautobot_plugin_iprange.models import IPRange


class IPRangeForm(BootstrapMixin, forms.ModelForm):
    start_address = IPAddressFormField()
    end_address = IPAddressFormField()
    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(), label="VRF", required=False
    )

    class Meta:
        model = IPRange
        fields = [
            "vrf",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance")
        initial = kwargs.get("initial", {}).copy()

        if instance.start_address != b"":
            initial["start_address"] = instance.start_address
        if instance.end_address != b"":
            initial["end_address"] = instance.end_address

        kwargs["initial"] = initial

        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()

        self.instance.start_address = self.cleaned_data.get("start_address")
        self.instance.end_address = self.cleaned_data.get("end_address")


class IPRangeFilterForm(BootstrapMixin, forms.Form):
    model = IPRange
    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(), label="VRF", required=False
    )
    description = forms.CharField(required=False, label="Description")


class IPRangeBulkEditForm(BootstrapMixin, BulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=IPRange.objects.all(), widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(required=False)
    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(), label="VRF", required=False
    )

    class Meta:
        nullable_fields = ["vrf"]
