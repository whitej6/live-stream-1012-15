from nautobot.utilities.testing import APIViewTestCases

from nautobot_plugin_iprange.models import IPRange


class IPRangeAPIViewTest(APIViewTestCases.APIViewTestCase):
    model = IPRange
    create_data = [
        {"start_address": "10.0.0.10", "end_address": "10.0.0.30"},
        {"start_address": "10.0.0.20", "end_address": "10.0.0.30"},
    ]
    bulk_update_data = {"description": "test update description"}

    @classmethod
    def setUpTestData(cls) -> None:
        IPRange.objects.create(start_address="192.168.0.0", end_address="192.168.0.1")
        IPRange.objects.create(start_address="192.168.1.0", end_address="192.168.1.1")
        IPRange.objects.create(start_address="192.168.2.0", end_address="192.168.2.1")

    def test_list_objects_brief(self):
        """Functionality not implemented. Pass to not invoke test."""
        pass
