import sys
import subprocess

target = sys.argv[1]
problems = []
for i in range(len(sys.argv)):
    if i < 2:
        continue
    problems.append(sys.argv[i])

print(problems)

for problem in problems:
    dirname = target + '/' + target + '_' + problem
    subprocess.check_call('mkdir -p ' + dirname, shell=True)
    subprocess.check_call('cp -r template/* ' + dirname, shell=True)
    subprocess.check_call('sed -i s/\{DOWNLOAD_URL\}/https:\\\/\\\/atcoder.jp\\\/contests\\\/' + target + '\\\/tasks\\\/' + target + '_' + problem + '/g ' + dirname + '/Makefile', shell=True)

with open(target + '/Makefile', mode='w') as f:
    f.write('''dlall:
''')
    for problem in problems:
        f.write('	cd ' + target + '_' + problem +  '''; make dl
''')
