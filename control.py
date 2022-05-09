# coding:utf-8
# import os;
# cmd = 'ping baidu.com';
# r = os.popen(cmd);
# for line in r.readlines():
#     print(line)

import win32com.client
speaker = win32com.client.Dispatch('SAPI.SpVoice')

content = ''
speaker.Speak(content)