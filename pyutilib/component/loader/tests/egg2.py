import pyutilib.component.core
import os
import sys

currdir = sys.argv[-2] + os.sep

pyutilib.component.core.PluginGlobals.add_env(
    pyutilib.component.core.PluginEnvironment("testing"))
service = pyutilib.component.core.PluginFactory(
    "EggLoader", namespace="project1", env='pca')
if service is None:
    print(
        "Cannot test the PyUtilib EggLoader Plugin on this system because the pkg_resources package is not available.")
    sys.exit(1)
#
#logging.basicConfig(level=logging.DEBUG)
#
pyutilib.component.core.PluginGlobals.get_env().load_services(
    path=[currdir + "eggs1", currdir + "eggs2"])
#
pyutilib.misc.setup_redirect(currdir + "egg2.out")
if sys.argv[-1] == 'json':
    pyutilib.component.core.PluginGlobals.pprint(json=True)
else:
    pyutilib.component.core.PluginGlobals.pprint()
pyutilib.misc.reset_redirect()
