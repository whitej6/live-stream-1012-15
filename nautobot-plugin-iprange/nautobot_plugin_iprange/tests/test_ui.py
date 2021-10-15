from nautobot.utilities.testing import ViewTestCases

from nautobot_plugin_iprange.models import IPRange


class IPRangeViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    model = IPRange
    form_data = {"start_address": "10.0.0.1", "end_address": "10.0.0.3"}
    bulk_edit_data = {"description": "test update description"}

    @classmethod
    def setUpTestData(cls) -> None:
        IPRange.objects.create(start_address="192.168.0.0", end_address="192.168.0.1")
        IPRange.objects.create(start_address="192.168.1.0", end_address="192.168.1.1")
        IPRange.objects.create(start_address="192.168.2.0", end_address="192.168.2.1")

    def test_bulk_import_objects_with_constrained_permission(self):
        pass

    def test_bulk_import_objects_with_permission(self):
        pass

    def test_bulk_import_objects_without_permission(self):
        pass
