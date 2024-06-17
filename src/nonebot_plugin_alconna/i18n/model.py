# This file is @generated by tarina.lang CLI tool
# It is not intended for manual editing.

from tarina.lang.model import LangItem, LangModel


class CompletionNonebot:
    tab: LangItem = LangItem("completion", "nonebot.tab")
    enter: LangItem = LangItem("completion", "nonebot.enter")
    exit: LangItem = LangItem("completion", "nonebot.exit")
    other: LangItem = LangItem("completion", "nonebot.other")
    timeout: LangItem = LangItem("completion", "nonebot.timeout")
    exited: LangItem = LangItem("completion", "nonebot.exited")


class Completion:
    nonebot = CompletionNonebot


class NbpAlcLogGotPath:
    ms: LangItem = LangItem("nbp-alc", "log.got_path.ms")
    validate: LangItem = LangItem("nbp-alc", "log.got_path.validate")


class NbpAlcLogDiscord:
    ambiguous_command: LangItem = LangItem("nbp-alc", "log.discord.ambiguous_command")
    ambiguous_subcommand: LangItem = LangItem("nbp-alc", "log.discord.ambiguous_subcommand")


class NbpAlcLog:
    load_global_extensions: LangItem = LangItem("nbp-alc", "log.load_global_extensions")
    got_path = NbpAlcLogGotPath
    discord = NbpAlcLogDiscord
    parse: LangItem = LangItem("nbp-alc", "log.parse")


class NbpAlcErrorExtension:
    forbid_exclude: LangItem = LangItem("nbp-alc", "error.extension.forbid_exclude")
    path_load: LangItem = LangItem("nbp-alc", "error.extension.path_load")
    path_invalid: LangItem = LangItem("nbp-alc", "error.extension.path_invalid")


class NbpAlcError:
    discord_prefix: LangItem = LangItem("nbp-alc", "error.discord_prefix")
    extension = NbpAlcErrorExtension
    matcher_got_path: LangItem = LangItem("nbp-alc", "error.matcher_got_path")


class NbpAlc:
    log = NbpAlcLog
    error = NbpAlcError


class NbpAlcBuiltinLang:
    list: LangItem = LangItem("nbp-alc/builtin", "lang.list")
    switch: LangItem = LangItem("nbp-alc/builtin", "lang.switch")
    locale_missing: LangItem = LangItem("nbp-alc/builtin", "lang.locale_missing")
    locale_timeout: LangItem = LangItem("nbp-alc/builtin", "lang.locale_timeout")


class NbpAlcBuiltinHelp:
    plugin_name_unknown: LangItem = LangItem("nbp-alc/builtin", "help.plugin_name_unknown")
    plugin_name: LangItem = LangItem("nbp-alc/builtin", "help.plugin_name")
    plugin_id: LangItem = LangItem("nbp-alc/builtin", "help.plugin_id")
    plugin_path: LangItem = LangItem("nbp-alc/builtin", "help.plugin_path")
    plugin_module: LangItem = LangItem("nbp-alc/builtin", "help.plugin_module")
    plugin_version: LangItem = LangItem("nbp-alc/builtin", "help.plugin_version")


class NbpAlcBuiltin:
    lang = NbpAlcBuiltinLang
    help = NbpAlcBuiltinHelp


class Lang(LangModel):
    completion = Completion
    nbp_alc = NbpAlc
    nbp_alc_builtin = NbpAlcBuiltin
