#!/bin/bash

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

set -e

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 [cancel|INT]"
  exit 1
fi

if [[ $1 == "cancel" ]]; then
  /sbin/shutdown -c
  echo "Shutdown cancelled"
elif [[ $1 == "now" ]]; then
  /sbin/shutdown now
  echo "Shutting down the system"
else
  /sbin/shutdown -P $1
  echo "System will shut down in $1 minutes"
fi

