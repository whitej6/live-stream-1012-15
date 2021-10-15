from django.test import TestCase

from nautobot.ipam.models import VRF

from nautobot_plugin_iprange.models import IPRange


class TestModels(TestCase):
    def setUp(self):
        self.vrf = VRF.objects.create(name="testvrf")

    def test_create_iprange_vrf(self):
        iprange = IPRange.objects.create(
            start_address="10.0.0.1", end_address="10.0.0.3", vrf=self.vrf
        )

        self.assertEqual(iprange.start_address, "10.0.0.1")
        self.assertEqual(iprange.end_address, "10.0.0.3")
        self.assertEqual(iprange.vrf.id, self.vrf.id)
        self.assertEqual(str(iprange), "10.0.0.1-10.0.0.3")
        self.assertEqual(iprange.size, 3)
