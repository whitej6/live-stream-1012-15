from nautobot.extras.plugins import PluginConfig


__version__ = "0.1.0"


class StreamPlugin(PluginConfig):
    name = "nautobot_plugin_iprange"
    verbose_name = "Nautobot Plugin to model IP Ranges"
    author = "whitej6"
    description = "My super cool stream plugin where I modeled IP Ranges"
    base_url = "ip-range"
    required_settings = []
    default_settings = {}
    min_version = "1.1.0"
    max_version = "1.9999"
    caching_config = {}


config = StreamPlugin
