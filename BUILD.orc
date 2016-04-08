cc_library(
    name = "orc-lib",
    srcs = glob(
        ["orc/*.h", "orc/*.c"],
        exclude = [
          "orc/orcarm.c",
          "orc/orccpu-arm.c",
          "orc/orccodemem.c",
        ])
        + ["config.h"],
    includes = ["."],
    defines = [
        "HAVE_CONFIG_H",
        "ORC_ENABLE_UNSTABLE_API",
    ],
)

genrule(
    name = "configure_gen",
    srcs = glob(["**/*"]),
    outs = ["config.h"],
    cmd = """
        $(location :configure_sh) --srcdir $$(dirname $(location config.h.in))
        cp config.h $@
    """,
    tools = [":configure_sh"])

sh_binary(
    name = "configure_sh",
    srcs = ["configure.sh"],
)

genrule(
    name = "configure_cp",
    srcs = ["configure"],
    outs = ["configure.sh"],
    cmd = "cp $< $@",
)
