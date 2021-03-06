#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Docker API
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Docker API.
#
# Hive Docker API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Docker API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Docker API. If not, see <http://www.apache.org/licenses/>.

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import base

class DockerApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "docker",
            *args, **kwargs
        )

    @appier.route("/", "GET")
    def index(self):
        return self.containers()

    @appier.route("/containers", "GET")
    def containers(self):
        api = self.get_api()
        containers = api.list_containers()
        return containers

    @appier.route("/containers/<str:id>/restart", ("GET", "POST"))
    def restart_container(self, id):
        api = self.get_api()
        container = api.restart_container(id)
        return container

    def get_api(self):
        api = base.get_api()
        return api

if __name__ == "__main__":
    app = DockerApp()
    app.serve()
else:
    __path__ = []
