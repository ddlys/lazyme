#!/usr/bin/python

# Copyright (C) 2017 ddly
#
# This file is part of LazyMe.
#
# LazyMe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from re import search as RSearch
from optparse import OptionParser
from subprocess import check_output as SysCall
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class Validator(object):
    @staticmethod
    def Volume(s):
        try:
            v = int(s)
            return v <= 100 and v >= 0
        except:
            return False


class Controller:
    shutdown = False

    @staticmethod
    def Exec(cmd):
        try:
            return SysCall(cmd, shell=True)
        except:
            return 

    @staticmethod
    def SetVolume(v):
        if Validator.Volume(v):
            return Controller.Exec("./setVolume.sh " + str(v))

    @staticmethod
    def GetVolume():
        return Controller.Exec("./getVolume.sh")

    @staticmethod
    def Shutdown(v):
        res = Controller.Exec("./shutdown.sh " + str(v))
        Controller.shutdown = True
        return res

    @staticmethod
    def ShutdownNow(v):
        res = Controller.Exec("./shutdown.sh now")
        Controller.shutdown = True
        return res

    @staticmethod
    def CancelShutdown(v):
        res = Controller.Exec("./shutdown.sh " + str(v))
        Controller.shutdown = False
        return res


class Loader:
    @staticmethod
    def LoadIndexPage(path, serveraddr):
        try:
            with open(path) as f:
                data = f.read()
                vol = Controller.GetVolume()
                chk = "checked=true" if Controller.shutdown else ""
                host, port = serveraddr
                return ( data
                    .replace("__VOLUME__", str(vol))
                    .replace("__CHK__", str(chk))
                    .replace("__HOST__", str(host))
                    .replace("__PORT__", str(port)) )
        except:
            return ""


class Router:
    routes = {}

    @staticmethod
    def Add(path, foo):
        Router.routes.update({path: foo})

    @staticmethod
    def Call(path):
        for p, f in Router.routes.iteritems():
            m = RSearch(p, path)
            if m and len(m.groups()) == 1:
                return f(m.group(1))


Router.Add(".*/volume/([0-9]+)", Controller.SetVolume)
Router.Add(".*/shutdown/([0-9]+)", Controller.Shutdown)
Router.Add(".*/shutdown/(now)", Controller.ShutdownNow)
Router.Add(".*/shutdown/(cancel)", Controller.CancelShutdown)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        indexPage = Loader.LoadIndexPage("index.tmpl", self.server.server_address)
        self.wfile.write(indexPage)

    def do_POST(self):
        if Router.Call(self.path):
            self.send_response(200)
        else:
            self.send_response(400)


class Server(object):
    def __init__(self, host, port):
        self.httpd = HTTPServer((host, port), Handler)

    def Start(self):
        self.httpd.serve_forever()


class Cmd:
    @staticmethod
    def ReadOptions():
        parser = OptionParser()
        parser.add_option("-i", dest="interface", type="str", default="0.0.0.0")
        parser.add_option("-p", dest="port", type="int", default=12345)
        options, args = parser.parse_args()
        return options


class Main:
    @staticmethod
    def Run():
        opt = Cmd.ReadOptions()
        server = Server(opt.interface, opt.port)
        server.Start()


Main.Run()

