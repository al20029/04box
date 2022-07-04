import subprocess

with open('out_UserName.txt', 'w') as pfp:
    subprocess.run('echo %USERNAME%', encoding='utf-8', stdout=pfp, shell=True)
with open('out_UserName.txt', 'r') as lines:
    Result_echo = lines.read().splitlines()
    # print(lines)
subprocess.run('del out_UserName.txt', shell=True)
for s in Result_echo:
    if len(s) != 0:
        UserName = s.replace(' ', '').replace('  ', '')
        break
print(UserName)
ins = 'del C:\\Users\\' + UserName + '\\AppData\\Roaming\\Microsoft\\Windows\\\"Start Menu\"\\Programs\\Startup\\a.txt'
print(ins)
subprocess.run(ins, encoding='utf-8', shell=True)