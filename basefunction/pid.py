# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import psutil


def get_all_pid():
    pid_list = psutil.pids()
    return pid_list


def get_pid_name(pid_list):
    for pid in pid_list:
        p_name = psutil.Process(pid).cmdline()
        print(pid, p_name)


if __name__ == "__main__":
    pid_list = get_all_pid()
    print(pid_list)
    get_pid_name(pid_list)
