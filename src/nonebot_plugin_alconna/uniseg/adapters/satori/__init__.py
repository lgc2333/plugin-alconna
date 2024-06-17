from importlib_metadata import PackageNotFoundError, distribution
from nonebot.adapters import MessageSegment as BaseMessageSegment

from nonebot_plugin_alconna.uniseg.loader import BaseLoader
from nonebot_plugin_alconna.uniseg.builder import MessageBuilder
from nonebot_plugin_alconna.uniseg.exporter import MessageExporter
from nonebot_plugin_alconna.uniseg.constraint import SupportAdapter
from nonebot_plugin_alconna.uniseg.segment import Emoji, custom_handler, custom_register


def get_satori_version():
    try:
        satori = distribution("nonebot-adapter-satori")
        return satori.version
    except PackageNotFoundError:
        return None


class Loader(BaseLoader):
    def __init__(self):
        if version := get_satori_version():
            if tuple(map(int, version.split(".")[:2])) < (0, 12):
                raise ImportError("nonebot-adapter-satori>=0.12 is required.")

        from nonebot.adapters.satori.message import Custom
        from nonebot.adapters.satori import Message, MessageSegment

        @custom_register(Emoji, "chronocat:face")
        def fbuild(builder: MessageBuilder, seg: BaseMessageSegment):
            if not isinstance(seg, Custom):
                raise ValueError("Emoji can only be built from Satori Message")
            return Emoji(seg.data["id"], seg.data.get("name"))(*builder.generate(seg.children))

        @custom_handler(Emoji)
        async def fexport(exporter: MessageExporter, seg: Emoji, bot, fallback):
            if exporter.get_message_type() is Message:
                return MessageSegment("chronocat:face", seg.data)(
                    await exporter.export(seg.children, bot, fallback)  # type: ignore
                )

    def get_adapter(self) -> SupportAdapter:
        return SupportAdapter.satori

    def get_builder(self):
        from .builder import SatoriMessageBuilder

        return SatoriMessageBuilder()

    def get_exporter(self):
        from .exporter import SatoriMessageExporter

        return SatoriMessageExporter()

    def get_fetcher(self):
        from .target import SatoriTargetFetcher

        return SatoriTargetFetcher()
