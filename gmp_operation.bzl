def gmp_operation(
    name,
    src,
    deps,
    function_names):
  [native.cc_library(
      name = "%s_%s" % (name, function_name),
      srcs = [src],
      deps = deps,
      copts = ["-DOPERATION_" + function_name])
   for function_name in function_names]

  native.cc_library(
      name = name,
      deps = [":%s_%s" % (name, f) for f in function_names])
