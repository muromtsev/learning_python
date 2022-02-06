"""
Реализация веб-сеовера на языке Python, способная запускать сервер
CGI-сценарий на языке Python. Обслуживает файлы и сценарии в текущем
рабочем каталоге, сценарии на языке Python  должны находится в каталоге
webdir/cgi-bin или webdir/htbin..
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 8080

os.chdir(webdir)                                       # run in HTML root dir
srvraddr = ("", port)                                  # my hostname, portnumber
srvrobj  = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever() 
