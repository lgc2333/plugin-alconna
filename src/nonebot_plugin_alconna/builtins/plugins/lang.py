from nonebot.plugin import PluginMetadata, inherit_supported_adapters
from arclet.alconna import Args, Field, Option, Alconna, CommandMeta, namespace

from nonebot_plugin_alconna.i18n import Lang, lang
from nonebot_plugin_alconna import UniMessage, on_alconna

__plugin_meta__ = PluginMetadata(
    name="lang",
    description="i18n 指令",
    usage="/lang list/switch [lang]",
    type="application",
    homepage="https://github.com/nonebot/plugin-alconna/blob/master/src/nonebot_plugin_alconna/builtins/plugins/lang.py",
    config=None,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
)

with namespace("builtin/lang") as ns:
    ns.disable_builtin_options = {"shortcut", "completion"}

    cmd = on_alconna(
        Alconna(
            "lang",
            Option("list", help_text="查看支持的语言列表"),
            Option("switch", Args["locale", str, Field("NONE", completion=lambda: "比如 zh-CN")], help_text="切换语言"),
            meta=CommandMeta("i18n配置相关功能", compact=True),
        ),
        auto_send_output=True,
        use_cmd_start=True,
    )


@cmd.assign("list")
async def _():
    await cmd.finish(Lang.nbp_alc_builtin.lang_list() + "\n" + "\n".join(f" * {locale}" for locale in lang.locales))


@cmd.assign("switch")
async def _(locale: str):
    if locale == "NONE":
        resp = await cmd.prompt(UniMessage.i18n(Lang.nbp_alc_builtin.lang_locale_missing), timeout=30)
        if resp is None:
            await UniMessage.i18n(Lang.nbp_alc_builtin.lang_locale_timeout).finish()
        locale = str(resp)
    try:
        lang.select(locale)
    except ValueError as e:
        await cmd.finish(str(e))
    else:
        await UniMessage.i18n(Lang.nbp_alc_builtin.lang_switch, locale=locale).finish()
