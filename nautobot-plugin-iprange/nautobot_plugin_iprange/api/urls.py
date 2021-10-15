from nautobot.core.api import OrderedDefaultRouter

from nautobot_plugin_iprange.api.views import IPRangeViewSet


router = OrderedDefaultRouter()
router.register("ip-range", IPRangeViewSet)

urlpatterns = router.urls
