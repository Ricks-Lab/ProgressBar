#!/usr/bin/env python3
""" PBmodules  -  Pogress Bar Class

    Copyright (C) 2023  RicksLab

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your option)
    any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
    more details.

    You should have received a copy of the GNU General Public License along with
    this program.  If not, see <https://www.gnu.org/licenses/>.
"""
__author__ = 'RicksLab'
__copyright__ = 'Copyright (C) 2023 RicksLab'
__license__ = 'GNU General Public License'
__program_name__ = 'ProgressBar-Module'
__maintainer__ = 'RicksLab'
__docformat__ = 'reStructuredText'

# pylint: disable=multiple-statements
# pylint: disable=line-too-long
# pylint: disable=consider-using-f-string
# pylint: disable=bad-continuation

from typing import Union
from datetime import datetime


class ProgressBar:
    """ Module which defines Text Progress Bar and associated methods.
    """

    def __init__(self, bar_length: int = 80, bar_character: str = '#'):
        """ Initialize Progress Bar object with the 100% bar length set to the
            number of characters defined by bar_length.

        :param bar_length: length of the bar at 100% in number of characters
        :param bar_character: the character used in the creation of the progress bar.
        """
        self.bar_length: int = bar_length
        self.bar_character: str = bar_character[0]
        if not self.bar_character: self.bar_character = '#'
        self.prev_completion_length: int = 0
        self.start_time: datetime = datetime.now()
        self.end_time: datetime = self.start_time

    def update(self, completed_items: int, total_items: int) -> str:
        """ Update the progress bar based on updated number of completed and total items.

        :param completed_items: Total number of completed items
        :param total_items: An updated number of total_items
        :return: a string of the additional progress.
        """
        end_str = ''
        if completed_items >= total_items - 1:
            completed_items = total_items
            self.end_time = datetime.now()
            end_str = '\n'
        completion_length = int(self.bar_length * completed_items/total_items)
        increment_length = completion_length - self.prev_completion_length
        self.prev_completion_length = completion_length
        if increment_length < 1:
            return ''
        return '{}{}'.format(''.ljust(increment_length, self.bar_character), end_str)

    def elapsed_time(self, seconds: bool = False) -> Union[str, int]:
        """ Return the elapsed time for progress bar to complete.  By default, a formatted string
            of hours, minutes, and seconds is returned.  If seconds flag is True, then the number
            of elapsed seconds is returned.

        :param seconds:  If True, return the number of seconds, else a formatted string.
        :return:
        """
        t_delta_s = int((self.end_time - self.start_time).total_seconds())
        if seconds: return t_delta_s
        return self.elapsed_time_formatter(t_delta_s)

    @staticmethod
    def elapsed_time_formatter(time_delta_seconds: int) -> str:
        """ For the give number of seconds, return a formatted string of hours, minutes
            and seconds.

        :param time_delta_seconds: Time delta in seconds.
        :return: Formatted string of hours:minutes:seconds
        """
        hours = int(time_delta_seconds // 3600)
        minutes = int((time_delta_seconds - hours * 3600) // 60)
        seconds = int((time_delta_seconds - (hours * 3600 + minutes * 60)))
        return '{}h:{}m:{}s'.format(hours, minutes, seconds)
