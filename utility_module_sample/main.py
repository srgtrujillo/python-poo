# -*- encoding: utf-8 -*-
####################################################################################
#    Utility Module Sample
#    Copyright (C) 2016  Sergio Trujillo Martínez (sergiotrujillomartinez@gmail.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
####################################################################################

from utility_module import math_functions
from utility_module.math_functions import fibonacci

if __name__ == '__main__':
    print "7! = ", math_functions.factorial(7)
    print "fibonacci(8) = ", fibonacci(8)
