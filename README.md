Installation
============

[![Python package](https://github.com/chdemko/pandoc-latex-margin/workflows/Python%20package/badge.svg?branch=develop)](https://github.com/chdemko/pandoc-latex-margin/actions/workflows/python-package.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-margin/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-latex-margin?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-margin.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-margin/)
[![Code Climate](https://codeclimate.com/github/chdemko/pandoc-latex-margin/badges/gpa.svg)](https://codeclimate.com/github/chdemko/pandoc-latex-margin/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-latex-margin/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-latex-margin)
[![Codacy](https://img.shields.io/codacy/grade/7df59d426cab4adca51d86403f0cc4b6.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-latex-margin/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-margin.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-margin/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-margin.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgMzIgMzIiCiAgIGhlaWdodD0iMzJweCIKICAgaWQ9InN2ZzIiCiAgIHZlcnNpb249IjEuMSIKICAgdmlld0JveD0iMCAwIDMyIDMyIgogICB3aWR0aD0iMzJweCIKICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgc29kaXBvZGk6ZG9jbmFtZT0iMTAzNTA5X3RleHRfZG9jdW1lbnRfaWNvbi5zdmciCiAgIGlua3NjYXBlOnZlcnNpb249IjEuMS4yICgwYTAwY2Y1MzM5LCAyMDIyLTAyLTA0KSIKICAgeG1sbnM6aW5rc2NhcGU9Imh0dHA6Ly93d3cuaW5rc2NhcGUub3JnL25hbWVzcGFjZXMvaW5rc2NhcGUiCiAgIHhtbG5zOnNvZGlwb2RpPSJodHRwOi8vc29kaXBvZGkuc291cmNlZm9yZ2UubmV0L0RURC9zb2RpcG9kaS0wLmR0ZCIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZGVmcwogICAgIGlkPSJkZWZzMTIxNSIgLz48c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9Im5hbWVkdmlldzEyMTMiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgICBpbmtzY2FwZTpwYWdlc2hhZG93PSIyIgogICAgIGlua3NjYXBlOnBhZ2VvcGFjaXR5PSIwLjAiCiAgICAgaW5rc2NhcGU6cGFnZWNoZWNrZXJib2FyZD0iMCIKICAgICBzaG93Z3JpZD0iZmFsc2UiCiAgICAgaW5rc2NhcGU6em9vbT0iMjIuNDY4NzUiCiAgICAgaW5rc2NhcGU6Y3g9IjE2IgogICAgIGlua3NjYXBlOmN5PSIxNS45Nzc3NDciCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxOTIwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjExNjMiCiAgICAgaW5rc2NhcGU6d2luZG93LXg9IjE5MjAiCiAgICAgaW5rc2NhcGU6d2luZG93LXk9IjAiCiAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJzdmcyIiAvPjxnCiAgICAgaWQ9ImJhY2tncm91bmQiPjxyZWN0CiAgICAgICBmaWxsPSJub25lIgogICAgICAgaGVpZ2h0PSIzMiIKICAgICAgIHdpZHRoPSIzMiIKICAgICAgIGlkPSJyZWN0MTIwMCIgLz48L2c+PGcKICAgICBpZD0iZG9jdW1lbnRfeDVGX3RleHQiCiAgICAgc3R5bGU9ImZpbGw6I2ZmZmZmZiI+PHBvbHlnb24KICAgICAgIHBvaW50cz0iNCwyMiA0LDIwIDE2LDIwIDE2LDIyIDQsMjIgICIKICAgICAgIGlkPSJwb2x5Z29uMTIwMyIKICAgICAgIHN0eWxlPSJmaWxsOiNmZmZmZmYiIC8+PHBvbHlnb24KICAgICAgIHBvaW50cz0iNCwxNCA0LDEyIDIwLDEyIDIwLDE0IDQsMTQgICIKICAgICAgIGlkPSJwb2x5Z29uMTIwNSIKICAgICAgIHN0eWxlPSJmaWxsOiNmZmZmZmYiIC8+PHBvbHlnb24KICAgICAgIHBvaW50cz0iNCwxOCA0LDE2IDIwLDE2IDIwLDE4IDQsMTggICIKICAgICAgIGlkPSJwb2x5Z29uMTIwNyIKICAgICAgIHN0eWxlPSJmaWxsOiNmZmZmZmYiIC8+PHBhdGgKICAgICAgIGQ9Ik0xOC40MTQsMEgwdjMyaDI0VjUuNTg0TDE4LjQxNCwweiBNMTcuOTk4LDIuNDEzTDIxLjU4Niw2aC0zLjU4OFYyLjQxM3ogTTIsMzBWMS45OThoMTR2Ni4wMDFoNlYzMEgyeiIKICAgICAgIGlkPSJwYXRoMTIwOSIKICAgICAgIHN0eWxlPSJmaWxsOiNmZmZmZmYiIC8+PC9nPjwvc3ZnPgo=)](https://pypi.org/project/pandoc-latex-margin/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-latex-margin.svg?logo=github)](https://github.com/chdemko/pandoc-latex-margin/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-latex-margin/develop?logo=github)](https://github.com/chdemko/pandoc-latex-margin/commit/develop/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-margin.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gVXBsb2FkZWQgdG86IFNWRyBSZXBvLCB3d3cuc3ZncmVwby5jb20sIEdlbmVyYXRvcjogU1ZHIFJlcG8gTWl4ZXIgVG9vbHMgLS0+Cgo8c3ZnCiAgIGhlaWdodD0iODAwcHgiCiAgIHdpZHRoPSI4MDBweCIKICAgdmVyc2lvbj0iMS4xIgogICBpZD0iX3gzMl8iCiAgIHZpZXdCb3g9IjAgMCA1MTIgNTEyIgogICB4bWw6c3BhY2U9InByZXNlcnZlIgogICBzb2RpcG9kaTpkb2NuYW1lPSJiYWxhbmNlLTEtc3ZncmVwby1jb20uc3ZnIgogICBpbmtzY2FwZTp2ZXJzaW9uPSIxLjEuMiAoMGEwMGNmNTMzOSwgMjAyMi0wMi0wNCkiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnMKICAgaWQ9ImRlZnMzMzg2IiAvPjxzb2RpcG9kaTpuYW1lZHZpZXcKICAgaWQ9Im5hbWVkdmlldzMzODQiCiAgIHBhZ2Vjb2xvcj0iI2ZmZmZmZiIKICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgaW5rc2NhcGU6cGFnZXNoYWRvdz0iMiIKICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgaW5rc2NhcGU6cGFnZWNoZWNrZXJib2FyZD0iMCIKICAgc2hvd2dyaWQ9ImZhbHNlIgogICBpbmtzY2FwZTp6b29tPSIwLjg5ODc1IgogICBpbmtzY2FwZTpjeD0iNDAwIgogICBpbmtzY2FwZTpjeT0iMzk5LjQ0MzY3IgogICBpbmtzY2FwZTp3aW5kb3ctd2lkdGg9IjE5MjAiCiAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjExNjMiCiAgIGlua3NjYXBlOndpbmRvdy14PSIxOTIwIgogICBpbmtzY2FwZTp3aW5kb3cteT0iMCIKICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0iX3gzMl8iIC8+CjxzdHlsZQogICB0eXBlPSJ0ZXh0L2NzcyIKICAgaWQ9InN0eWxlMzM3NyI+Cgkuc3Qwe2ZpbGw6IzAwMDAwMDt9Cjwvc3R5bGU+CjxnCiAgIGlkPSJnMzM4MSIKICAgc3R5bGU9ImZpbGw6I2ZmZmZmZiI+Cgk8cGF0aAogICBjbGFzcz0ic3QwIgogICBkPSJNNTAwLjYwOSwzMjIuMjc1bC01Ny40MjgtMTYyLjgzNGMwLjEzNSwwLjAwOCwwLjI3OSwwLjAyNSwwLjQwNiwwLjAyNSAgIGMzOS41MzgsMC42NzcsNDkuNDIyLTIwLjU4LDU0LjU2Ni0yNy45NGM3LjExOC0xMC4xNzEtNy45MS0yMC4zNDMtMTUuODE2LTEzLjU1OGMtNy45MDYsNi43NzUtMjkuMjY0LDIxLjAxMS03MC4zODYsMi4wMjQgICBDMzc0Ljg3NCwxMDIuODc1LDMwOS44Nyw3My4wOTgsMjcxLjkyLDY3LjM5OXYtMzljMC04Ljc5OS03LjEyNy0xNS45MjEtMTUuOTE4LTE1LjkyMWMtOC43OTUsMC0xNS45MjIsNy4xMjItMTUuOTIyLDE1LjkyMXYzOSAgIGMtMzcuOTUsNS42OTktMTAyLjk1MywzNS40NzYtMTQwLjAzMSw1Mi41OTNjLTQxLjEyMSwxOC45ODctNjIuNDgsNC43NTEtNzAuMzg2LTIuMDI0Yy03LjkwNi02Ljc4NC0yMi45MzUsMy4zODgtMTUuODE2LDEzLjU1OCAgIGM1LjE0NSw3LjM2LDE1LjAyOCwyOC42MTcsNTQuNTY2LDI3Ljk0YzAuMTMyLDAsMC4yNzYtMC4wMTcsMC40MDItMC4wMjVMMTEuMzkxLDMyMi4yNzVIMCAgIGMxMS40OTcsMzguMDI1LDQ2LjgwNCw2NS43MzYsODguNTk1LDY1LjczNmM0MS43ODYsMCw3Ny4wOTMtMjcuNzExLDg4LjU5LTY1LjczNmgtMTEuMzg2bC02MC4zNTUtMTcxLjEzNCAgIGMzNy4xODMtMTEuNDY3LDg5LjU2OS0zMS4wNTYsMTM0LjYzNi0zNC4wNzJ2MjQuMjNoLTguNTA3djI2Ny43NDhIMjE4LjM3djIzLjg1OGMtOC43MTUsMC0xNy41NjksMC0yNC44NzQsMCAgIGMtMjMuMzU0LDAtMjIuNjYzLDMyLjk2OS0yMi42NjMsMzIuOTY5Yy0xOS4yMzMsMC0yOC44NSwxNS4xMDEtMjguODUsMzMuNjQ4aDIyOC4wMzNjMC0xOC41NDYtOS42MTYtMzMuNjQ4LTI4Ljg0NS0zMy42NDggICBjMCwwLDAuNjg2LTMyLjk2OS0yMi42NjgtMzIuOTY5Yy03LjMwNSwwLTE2LjE1OSwwLTI0Ljg3NCwwdi0yMy44NThoLTEzLjIwM1YxNDEuM2gtOC41MDd2LTI0LjIzICAgYzQ1LjA3MiwzLjAxNSw5Ny40NTcsMjIuNjA0LDEzNC42NCwzNC4wNzJsLTYwLjM1OCwxNzEuMTM0aC0xMS4zODdjMTEuNDk2LDM4LjAyNSw0Ni44MDQsNjUuNzM2LDg4LjU5LDY1LjczNiAgIGM0MS43OSwwLDc3LjA5OC0yNy43MTEsODguNTk0LTY1LjczNkg1MDAuNjA5eiBNMTQxLjI0MywzMjIuMjc1SDM1Ljk0OEw4OC41OTUsMTczTDE0MS4yNDMsMzIyLjI3NXogTTM3MC43NTgsMzIyLjI3NUw0MjMuNDEsMTczICAgbDUyLjY0MywxNDkuMjc1SDM3MC43NTh6IgogICBpZD0icGF0aDMzNzkiCiAgIHN0eWxlPSJmaWxsOiNmZmZmZmYiIC8+CjwvZz4KPC9zdmc+Cg==)](https://raw.githubusercontent.com/chdemko/pandoc-latex-margin/develop/LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-margin.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-margin/)
[![Poetry version](https://img.shields.io/badge/poetry-1.2%20|%201.3%20|%201.4%20|%201.5%20|%201.6%20|%201.7-blue.svg?logo=poetry)](https://python-poetry.org/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20|%202.12%20|%202.13%20|%202.14%20|%202.15%20|%202.16%20|%202.17%20|%202.18%20|%202.19%20|%203.0%20|%203.1-blue.svg?logo=markdown)](https://pandoc.org/)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-margin?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gVXBsb2FkZWQgdG86IFNWRyBSZXBvLCB3d3cuc3ZncmVwby5jb20sIEdlbmVyYXRvcjogU1ZHIFJlcG8gTWl4ZXIgVG9vbHMgLS0+Cgo8c3ZnCiAgIHdpZHRoPSI4MDBweCIKICAgaGVpZ2h0PSI4MDBweCIKICAgdmlld0JveD0iMCAwIDI0IDI0IgogICBmaWxsPSJub25lIgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmc0IgogICBzb2RpcG9kaTpkb2NuYW1lPSJkb3dubG9hZC1zdmdyZXBvLWNvbS5zdmciCiAgIGlua3NjYXBlOnZlcnNpb249IjEuMS4yICgwYTAwY2Y1MzM5LCAyMDIyLTAyLTA0KSIKICAgeG1sbnM6aW5rc2NhcGU9Imh0dHA6Ly93d3cuaW5rc2NhcGUub3JnL25hbWVzcGFjZXMvaW5rc2NhcGUiCiAgIHhtbG5zOnNvZGlwb2RpPSJodHRwOi8vc29kaXBvZGkuc291cmNlZm9yZ2UubmV0L0RURC9zb2RpcG9kaS0wLmR0ZCIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZGVmcwogICAgIGlkPSJkZWZzOCIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9Im5hbWVkdmlldzYiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgICBpbmtzY2FwZTpwYWdlc2hhZG93PSIyIgogICAgIGlua3NjYXBlOnBhZ2VvcGFjaXR5PSIwLjAiCiAgICAgaW5rc2NhcGU6cGFnZWNoZWNrZXJib2FyZD0iMCIKICAgICBzaG93Z3JpZD0iZmFsc2UiCiAgICAgaW5rc2NhcGU6em9vbT0iMC44OTg3NSIKICAgICBpbmtzY2FwZTpjeD0iNDAwIgogICAgIGlua3NjYXBlOmN5PSIzOTkuNDQzNjciCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxOTIwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjExNjMiCiAgICAgaW5rc2NhcGU6d2luZG93LXg9IjE5MjAiCiAgICAgaW5rc2NhcGU6d2luZG93LXk9IjAiCiAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJzdmc0IiAvPgogIDxwYXRoCiAgICAgZmlsbC1ydWxlPSJldmVub2RkIgogICAgIGNsaXAtcnVsZT0iZXZlbm9kZCIKICAgICBkPSJNOCAxMEM4IDcuNzkwODYgOS43OTA4NiA2IDEyIDZDMTQuMjA5MSA2IDE2IDcuNzkwODYgMTYgMTBWMTFIMTdDMTguOTMzIDExIDIwLjUgMTIuNTY3IDIwLjUgMTQuNUMyMC41IDE2LjQzMyAxOC45MzMgMTggMTcgMThIMTYuOUMxNi4zNDc3IDE4IDE1LjkgMTguNDQ3NyAxNS45IDE5QzE1LjkgMTkuNTUyMyAxNi4zNDc3IDIwIDE2LjkgMjBIMTdDMjAuMDM3NiAyMCAyMi41IDE3LjUzNzYgMjIuNSAxNC41QzIyLjUgMTEuNzc5MyAyMC41MjQ1IDkuNTE5OTcgMTcuOTI5NiA5LjA3ODI0QzE3LjQ4NjIgNi4yMDIxMyAxNS4wMDAzIDQgMTIgNEM4Ljk5OTc0IDQgNi41MTM4MSA2LjIwMjEzIDYuMDcwMzYgOS4wNzgyNEMzLjQ3NTUxIDkuNTE5OTcgMS41IDExLjc3OTMgMS41IDE0LjVDMS41IDE3LjUzNzYgMy45NjI0MyAyMCA3IDIwSDcuMUM3LjY1MjI4IDIwIDguMSAxOS41NTIzIDguMSAxOUM4LjEgMTguNDQ3NyA3LjY1MjI4IDE4IDcuMSAxOEg3QzUuMDY3IDE4IDMuNSAxNi40MzMgMy41IDE0LjVDMy41IDEyLjU2NyA1LjA2NyAxMSA3IDExSDhWMTBaTTEzIDExQzEzIDEwLjQ0NzcgMTIuNTUyMyAxMCAxMiAxMEMxMS40NDc3IDEwIDExIDEwLjQ0NzcgMTEgMTFWMTYuNTg1OEw5LjcwNzExIDE1LjI5MjlDOS4zMTY1OCAxNC45MDI0IDguNjgzNDIgMTQuOTAyNCA4LjI5Mjg5IDE1LjI5MjlDNy45MDIzNyAxNS42ODM0IDcuOTAyMzcgMTYuMzE2NiA4LjI5Mjg5IDE2LjcwNzFMMTEuMjkyOSAxOS43MDcxQzExLjY4MzQgMjAuMDk3NiAxMi4zMTY2IDIwLjA5NzYgMTIuNzA3MSAxOS43MDcxTDE1LjcwNzEgMTYuNzA3MUMxNi4wOTc2IDE2LjMxNjYgMTYuMDk3NiAxNS42ODM0IDE1LjcwNzEgMTUuMjkyOUMxNS4zMTY2IDE0LjkwMjQgMTQuNjgzNCAxNC45MDI0IDE0LjI5MjkgMTUuMjkyOUwxMyAxNi41ODU4VjExWiIKICAgICBmaWxsPSIjMDAwMDAwIgogICAgIGlkPSJwYXRoMiIKICAgICBzdHlsZT0iZmlsbDojZmZmZmZmIiAvPgo8L3N2Zz4K)](https://pepy.tech/project/pandoc-latex-margin)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-margin.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgdmlld0JveD0iMCAwIDMyIDMyIgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcxMDY0IgogICBzb2RpcG9kaTpkb2NuYW1lPSIyNjcyNzY4X2FwcF9iYXR0ZXJ5X3N0YXR1c19vYmplY3RfZXNzZW50aWFsX2ljb24uc3ZnIgogICBpbmtzY2FwZTp2ZXJzaW9uPSIxLjEuMiAoMGEwMGNmNTMzOSwgMjAyMi0wMi0wNCkiCiAgIHhtbG5zOmlua3NjYXBlPSJodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy9uYW1lc3BhY2VzL2lua3NjYXBlIgogICB4bWxuczpzb2RpcG9kaT0iaHR0cDovL3NvZGlwb2RpLnNvdXJjZWZvcmdlLm5ldC9EVEQvc29kaXBvZGktMC5kdGQiCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgeG1sbnM6c3ZnPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgPGRlZnMKICAgICBpZD0iZGVmczEwNjgiIC8+CiAgPHNvZGlwb2RpOm5hbWVkdmlldwogICAgIGlkPSJuYW1lZHZpZXcxMDY2IgogICAgIHBhZ2Vjb2xvcj0iI2ZmZmZmZiIKICAgICBib3JkZXJjb2xvcj0iIzY2NjY2NiIKICAgICBib3JkZXJvcGFjaXR5PSIxLjAiCiAgICAgaW5rc2NhcGU6cGFnZXNoYWRvdz0iMiIKICAgICBpbmtzY2FwZTpwYWdlb3BhY2l0eT0iMC4wIgogICAgIGlua3NjYXBlOnBhZ2VjaGVja2VyYm9hcmQ9IjAiCiAgICAgc2hvd2dyaWQ9ImZhbHNlIgogICAgIGlua3NjYXBlOnpvb209IjIyLjQ2ODc1IgogICAgIGlua3NjYXBlOmN4PSIxNiIKICAgICBpbmtzY2FwZTpjeT0iMTUuOTc3NzQ3IgogICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iMTkyMCIKICAgICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIxMTYzIgogICAgIGlua3NjYXBlOndpbmRvdy14PSIxOTIwIgogICAgIGlua3NjYXBlOndpbmRvdy15PSIwIgogICAgIGlua3NjYXBlOndpbmRvdy1tYXhpbWl6ZWQ9IjEiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ic3ZnMTA2NCIgLz4KICA8dGl0bGUKICAgICBpZD0idGl0bGUxMDU5IiAvPgogIDxnCiAgICAgZGF0YS1uYW1lPSIyNi1CYXR0ZXJ5IHN0YXR1cyIKICAgICBpZD0iXzI2LUJhdHRlcnlfc3RhdHVzIgogICAgIHN0eWxlPSJmaWxsOiNmZmZmZmYiPgogICAgPHBhdGgKICAgICAgIGQ9Ik0zMSwxM0gzMFYxMmExLDEsMCwwLDAtMS0xSDI4VjEwYTIsMiwwLDAsMC0yLTJIMmEyLDIsMCwwLDAtMiwyVjIyYTIsMiwwLDAsMCwyLDJIMjZhMiwyLDAsMCwwLDItMlYyMWgxYTEsMSwwLDAsMCwxLTFWMTloMWExLDEsMCwwLDAsMS0xVjE0QTEsMSwwLDAsMCwzMSwxM1ptLTUtMVYyMkgxOFYxMGg4WiIKICAgICAgIGlkPSJwYXRoMTA2MSIKICAgICAgIHN0eWxlPSJmaWxsOiNmZmZmZmYiIC8+CiAgPC9nPgo8L3N2Zz4K)](https://pypi.org/project/pandoc-latex-margin/)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-margin.svg?logo=read-the-docs&logoColor=white)](http://pandoc-latex-margin.readthedocs.io/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgaGVpZ2h0PSI0OCIKICAgdmlld0JveD0iMCAwIDQ4IDQ4IgogICB3aWR0aD0iNDgiCiAgIHZlcnNpb249IjEuMSIKICAgaWQ9InN2ZzEzNDgiCiAgIHNvZGlwb2RpOmRvY25hbWU9IjM1MjE0OF9zdHlsZV9pY29uLnN2ZyIKICAgaW5rc2NhcGU6dmVyc2lvbj0iMS4xLjIgKDBhMDBjZjUzMzksIDIwMjItMDItMDQpIgogICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgeG1sbnM6c29kaXBvZGk9Imh0dHA6Ly9zb2RpcG9kaS5zb3VyY2Vmb3JnZS5uZXQvRFREL3NvZGlwb2RpLTAuZHRkIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxMzUyIiAvPgogIDxzb2RpcG9kaTpuYW1lZHZpZXcKICAgICBpZD0ibmFtZWR2aWV3MTM1MCIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSIwIgogICAgIHNob3dncmlkPSJmYWxzZSIKICAgICBpbmtzY2FwZTp6b29tPSIxNC45NzkxNjciCiAgICAgaW5rc2NhcGU6Y3g9IjE3LjA1NzAyNCIKICAgICBpbmtzY2FwZTpjeT0iMjQiCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxNTU5IgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9Ijk3MCIKICAgICBpbmtzY2FwZTp3aW5kb3cteD0iMTk2OSIKICAgICBpbmtzY2FwZTp3aW5kb3cteT0iMCIKICAgICBpbmtzY2FwZTp3aW5kb3ctbWF4aW1pemVkPSIwIgogICAgIGlua3NjYXBlOmN1cnJlbnQtbGF5ZXI9InN2ZzEzNDgiIC8+CiAgPHBhdGgKICAgICBkPSJNNS4wNiAzOS4zMWwyLjY5IDEuMTF2LTE4LjA1bC00Ljg1IDExLjcxYy0uODQgMi4wMy4xMyA0LjM4IDIuMTYgNS4yM3ptMzktNy40MmwtOS45Mi0yMy45M2MtLjYyLTEuNS0yLjA4LTIuNDMtMy42MS0yLjQ2LS41My0uMDEtMS4wNy4wOS0xLjYuM2wtMTQuNzMgNi4xYy0xLjUuNjItMi40MiAyLjA3LTIuNDYgMy42LS4wMS41NC4wOCAxLjA4LjMgMS42MWw5LjkxIDIzLjkzYy42MyAxLjUyIDIuMSAyLjQ0IDMuNjYgMi40Ni41MiAwIDEuMDQtLjA5IDEuNTUtLjNsMTQuNzMtNi4xYzIuMDMtLjg0IDMuMDEtMy4xOCAyLjE3LTUuMjF6bS0yOC4zMS0xNC4zOWMtMS4xIDAtMi0uOS0yLTJzLjktMiAyLTIgMiAuOSAyIDItLjkgMi0yIDJ6bS00IDIyYzAgMi4yIDEuOCA0IDQgNGgyLjkxbC02LjkxLTE2LjY4djEyLjY4eiIKICAgICBpZD0icGF0aDEzNDQiCiAgICAgc3R5bGU9ImZpbGw6I2ZmZmZmZiIgLz4KICA8cGF0aAogICAgIGQ9Ik0wIDBoNDh2NDhoLTQ4eiIKICAgICBmaWxsPSJub25lIgogICAgIGlkPSJwYXRoMTM0NiIgLz4KPC9zdmc+Cg==)](https://pypi.org/project/black/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-latex-margin.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gVXBsb2FkZWQgdG86IFNWRyBSZXBvLCB3d3cuc3ZncmVwby5jb20sIEdlbmVyYXRvcjogU1ZHIFJlcG8gTWl4ZXIgVG9vbHMgLS0+Cgo8c3ZnCiAgIGZpbGw9IiMwMDAwMDAiCiAgIHdpZHRoPSI4MDBweCIKICAgaGVpZ2h0PSI4MDBweCIKICAgdmlld0JveD0iMCAwIDI0IDI0IgogICBkYXRhLW5hbWU9IkxheWVyIDEiCiAgIHZlcnNpb249IjEuMSIKICAgaWQ9InN2ZzE0NzYiCiAgIHNvZGlwb2RpOmRvY25hbWU9IndlaWdodC1zdmdyZXBvLWNvbS5zdmciCiAgIGlua3NjYXBlOnZlcnNpb249IjEuMS4yICgwYTAwY2Y1MzM5LCAyMDIyLTAyLTA0KSIKICAgeG1sbnM6aW5rc2NhcGU9Imh0dHA6Ly93d3cuaW5rc2NhcGUub3JnL25hbWVzcGFjZXMvaW5rc2NhcGUiCiAgIHhtbG5zOnNvZGlwb2RpPSJodHRwOi8vc29kaXBvZGkuc291cmNlZm9yZ2UubmV0L0RURC9zb2RpcG9kaS0wLmR0ZCIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZGVmcwogICAgIGlkPSJkZWZzMTQ4MCIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9Im5hbWVkdmlldzE0NzgiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgICBpbmtzY2FwZTpwYWdlc2hhZG93PSIyIgogICAgIGlua3NjYXBlOnBhZ2VvcGFjaXR5PSIwLjAiCiAgICAgaW5rc2NhcGU6cGFnZWNoZWNrZXJib2FyZD0iMCIKICAgICBzaG93Z3JpZD0iZmFsc2UiCiAgICAgaW5rc2NhcGU6em9vbT0iMC44OTg3NSIKICAgICBpbmtzY2FwZTpjeD0iNDAwIgogICAgIGlua3NjYXBlOmN5PSIzOTkuNDQzNjciCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxOTIwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjExNjMiCiAgICAgaW5rc2NhcGU6d2luZG93LXg9IjE5MjAiCiAgICAgaW5rc2NhcGU6d2luZG93LXk9IjAiCiAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJzdmcxNDc2IiAvPgogIDxwYXRoCiAgICAgZD0iTTE5LDRIMTcuNTVBMy4wOCwzLjA4LDAsMCwwLDE3LDNhMywzLDAsMCwwLTIuMjUtMUg5LjI3QTMsMywwLDAsMCw3LDNhMy4wOCwzLjA4LDAsMCwwLS41NywxSDVBMywzLDAsMCwwLDIsN1YxOWEzLDMsMCwwLDAsMywzSDE5YTMsMywwLDAsMCwzLTNWN0EzLDMsMCwwLDAsMTksNFpNOC41Miw0LjM0QTEsMSwwLDAsMSw5LjI3LDRoNS40NmExLDEsMCwwLDEsLjc1LjM0LDEsMSwwLDAsMSwuMjUuNzhsLS41LDRhMSwxLDAsMCwxLTEsLjg4SDEyLjU5bDEuMTQtMi40YTEsMSwwLDAsMC0xLjgtLjg2TDEwLjM3LDEwaC0uNmExLDEsMCwwLDEtMS0uODhsLS41LTRBMSwxLDAsMCwxLDguNTIsNC4zNFpNMjAsMTlhMSwxLDAsMCwxLTEsMUg1YTEsMSwwLDAsMS0xLTFWN0ExLDEsMCwwLDEsNSw2SDYuMzdsLjQyLDMuMzdhMywzLDAsMCwwLDMsMi42M2g0LjQ2YTMsMywwLDAsMCwzLTIuNjNMMTcuNjMsNkgxOWExLDEsMCwwLDEsMSwxWm0tNi0zSDEwYTEsMSwwLDAsMCwwLDJoNGExLDEsMCwwLDAsMC0yWiIKICAgICBpZD0icGF0aDE0NzQiCiAgICAgc3R5bGU9ImZpbGw6I2ZmZmZmZiIgLz4KPC9zdmc+Cg==)](http://pandoc-latex-margin.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-latex-margin.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gVXBsb2FkZWQgdG86IFNWRyBSZXBvLCB3d3cuc3ZncmVwby5jb20sIEdlbmVyYXRvcjogU1ZHIFJlcG8gTWl4ZXIgVG9vbHMgLS0+Cgo8c3ZnCiAgIGZpbGw9IiMwMDAwMDAiCiAgIHdpZHRoPSI4MDBweCIKICAgaGVpZ2h0PSI4MDBweCIKICAgdmlld0JveD0iMCAwIDI0IDI0IgogICBkYXRhLW5hbWU9IkxheWVyIDEiCiAgIHZlcnNpb249IjEuMSIKICAgaWQ9InN2ZzE0NzYiCiAgIHNvZGlwb2RpOmRvY25hbWU9IndlaWdodC1zdmdyZXBvLWNvbS5zdmciCiAgIGlua3NjYXBlOnZlcnNpb249IjEuMS4yICgwYTAwY2Y1MzM5LCAyMDIyLTAyLTA0KSIKICAgeG1sbnM6aW5rc2NhcGU9Imh0dHA6Ly93d3cuaW5rc2NhcGUub3JnL25hbWVzcGFjZXMvaW5rc2NhcGUiCiAgIHhtbG5zOnNvZGlwb2RpPSJodHRwOi8vc29kaXBvZGkuc291cmNlZm9yZ2UubmV0L0RURC9zb2RpcG9kaS0wLmR0ZCIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZGVmcwogICAgIGlkPSJkZWZzMTQ4MCIgLz4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9Im5hbWVkdmlldzE0NzgiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjNjY2NjY2IgogICAgIGJvcmRlcm9wYWNpdHk9IjEuMCIKICAgICBpbmtzY2FwZTpwYWdlc2hhZG93PSIyIgogICAgIGlua3NjYXBlOnBhZ2VvcGFjaXR5PSIwLjAiCiAgICAgaW5rc2NhcGU6cGFnZWNoZWNrZXJib2FyZD0iMCIKICAgICBzaG93Z3JpZD0iZmFsc2UiCiAgICAgaW5rc2NhcGU6em9vbT0iMC44OTg3NSIKICAgICBpbmtzY2FwZTpjeD0iNDAwIgogICAgIGlua3NjYXBlOmN5PSIzOTkuNDQzNjciCiAgICAgaW5rc2NhcGU6d2luZG93LXdpZHRoPSIxOTIwIgogICAgIGlua3NjYXBlOndpbmRvdy1oZWlnaHQ9IjExNjMiCiAgICAgaW5rc2NhcGU6d2luZG93LXg9IjE5MjAiCiAgICAgaW5rc2NhcGU6d2luZG93LXk9IjAiCiAgICAgaW5rc2NhcGU6d2luZG93LW1heGltaXplZD0iMSIKICAgICBpbmtzY2FwZTpjdXJyZW50LWxheWVyPSJzdmcxNDc2IiAvPgogIDxwYXRoCiAgICAgZD0iTTE5LDRIMTcuNTVBMy4wOCwzLjA4LDAsMCwwLDE3LDNhMywzLDAsMCwwLTIuMjUtMUg5LjI3QTMsMywwLDAsMCw3LDNhMy4wOCwzLjA4LDAsMCwwLS41NywxSDVBMywzLDAsMCwwLDIsN1YxOWEzLDMsMCwwLDAsMywzSDE5YTMsMywwLDAsMCwzLTNWN0EzLDMsMCwwLDAsMTksNFpNOC41Miw0LjM0QTEsMSwwLDAsMSw5LjI3LDRoNS40NmExLDEsMCwwLDEsLjc1LjM0LDEsMSwwLDAsMSwuMjUuNzhsLS41LDRhMSwxLDAsMCwxLTEsLjg4SDEyLjU5bDEuMTQtMi40YTEsMSwwLDAsMC0xLjgtLjg2TDEwLjM3LDEwaC0uNmExLDEsMCwwLDEtMS0uODhsLS41LTRBMSwxLDAsMCwxLDguNTIsNC4zNFpNMjAsMTlhMSwxLDAsMCwxLTEsMUg1YTEsMSwwLDAsMS0xLTFWN0ExLDEsMCwwLDEsNSw2SDYuMzdsLjQyLDMuMzdhMywzLDAsMCwwLDMsMi42M2g0LjQ2YTMsMywwLDAsMCwzLTIuNjNMMTcuNjMsNkgxOWExLDEsMCwwLDEsMSwxWm0tNi0zSDEwYTEsMSwwLDAsMCwwLDJoNGExLDEsMCwwLDAsMC0yWiIKICAgICBpZD0icGF0aDE0NzQiCiAgICAgc3R5bGU9ImZpbGw6I2ZmZmZmZiIgLz4KPC9zdmc+Cg==)](http://pandoc-latex-margin.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-latex-margin.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-latex-margin)

*pandoc-latex-margin* is a [pandoc] filter for changing margin size to `CodeBlock` and `Div` that have speficied classes or `latex-left-margin` and `latex-right-margin` attributes.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-margin* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows].

Install *pandoc-latex-margin* using the bash command

~~~shell
$ pipx install pandoc-latex-margin
~~~

To upgrade to the most recent release, use

~~~shell
$ pipx install --upgrade pandoc-latex-margin
~~~

`pipx` is a script to install and run python applications in isolated environments from the Python Package Index, [PyPI]. It can be installed using instructions given [here](https://pipx.pypa.io/stable/).

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-margin*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-margin/issues

Notes
-----

* format icon by [Picol](https://www.iconfinder.com/icons/103509/document_text_icon)
* license icon by [Icooon Mono](https://www.svgrepo.com/svg/479891/balance-1)
* download icon by [zest](https://www.svgrepo.com/svg/509901/download)
* status icon by [Just Icon](https://www.iconfinder.com/icons/2672768/app_battery_essential_object_status_ui_ux_icon)
* code style icon by [Google Material Design icons](https://www.iconfinder.com/icons/352148/style_icon)
* size icon by [Iconscout](https://www.svgrepo.com/svg/358408/weight)

