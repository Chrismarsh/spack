# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRioxarray(PythonPackage):
    """rasterio xarray extension."""

    homepage = "https://github.com/corteva/rioxarray"
    pypi = "rioxarray/rioxarray-0.4.1.post0.tar.gz"

    maintainers("adamjstewart")

    license("Apache-2.0")

    version("0.17.0", sha256="46c29938827fff268d497f7ae277077066fcfbac4e53132ed3d4e2b96455be62")  
    version(
        "0.4.1.post0", sha256="f043f846724a58518f87dd3fa84acbe39e15a1fac7e64244be3d5dacac7fe62b"
    )

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-rasterio", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-xarray@0.17:", type=("build", "run"))
    depends_on("py-pyproj@2.2:", type=("build", "run"))
