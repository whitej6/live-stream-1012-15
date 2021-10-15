from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.urls import reverse
from nautobot.core.models.generics import PrimaryModel
from nautobot.ipam.fields import VarbinaryIPField
from netaddr import IPAddress


class IPRange(PrimaryModel):
    start_address = VarbinaryIPField(
        null=False, help_text="IPv4 or IPv6 starting host address"
    )
    end_address = VarbinaryIPField(
        null=False, help_text="IPv4 or IPv6 starting host address"
    )
    vrf = models.ForeignKey(
        to="ipam.VRF", on_delete=models.CASCADE, blank=True, null=True
    )
    description = models.CharField(max_length=200, blank=True)
    size = models.PositiveIntegerField(editable=False)

    class Meta:
        ordering = ["start_address"]
        verbose_name_plural = "IP Ranges"
        constraints = [
            UniqueConstraint(
                fields=["start_address", "end_address", "vrf"], name="unique_with_vrf"
            ),
            UniqueConstraint(
                fields=["start_address", "end_address"],
                name="unique_without_vrf",
                condition=models.Q(vrf=None),
            ),
        ]

    # def get_absolute_url(self):
    #     return reverse('plugins:nautobot_plugin_iprange:iprange')

    def __str__(self):
        return f"{self.start_address}-{self.end_address}"

    def save(self, *args, **kwargs):
        self.clean()
        self.size = int(IPAddress(self.end_address) - IPAddress(self.start_address)) + 1
        super().save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        if not getattr(self, "start_address") or not getattr(self, "end_address"):
            ValidationError("Must have a start_address and end_address.")
        if IPAddress(self.start_address) > IPAddress(self.end_address):
            ValidationError("start_address must be <= end_address.")

        super().clean(*args, **kwargs)
