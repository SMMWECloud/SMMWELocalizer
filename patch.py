#!/usr/bin/python
import sys,json

package_orig="SMM_WE.exe.bak"
package_out="SMM_WE.exe"
codec="utf-8"
locale_file="zh_CN.json"
build_platform="Linux" # Linux or Windows

if build_platform=="Linux":split="/"
if build_platform=="Windows":split="\\"
print("SMM:WE Localizer")
print("By YidaozhanYa")
whitelist=json.loads(open(sys.path[0]+split+"whitelist.json",'r').read())['whitelist']
f=open(sys.path[0]+"/"+package_orig,"rb")
s=f.read()
f.close()
j=json.loads(open(sys.path[0]+split+locale_file,'r').read())
for str in j:
    str1=str
    str2=j[str]
    if len(str1.encode(codec))<len(str2.encode(codec)):
        print(str1+' Out of range')
        exit()
    elif len(str1.encode(codec))==len(str2.encode(codec)):
        if str1 in whitelist:
            print("Whitelist "+ str1)
            s=s.replace(bytes(str1,codec),bytes(str2,codec))
        else:
            print("Replace "+ str1)
            s=s.replace(bytes(str1,codec),bytes(str2,codec),1)
    elif len(str1.encode(codec))>len(str2.encode(codec)):
        if str1 in whitelist:
            print("Whitelist "+ str1)
            s=s.replace(bytes(str1,codec),bytes(str2+" "*(len(str1.encode(codec))-len(str2.encode(codec))),codec))
        else:
            print("Replace "+ str1)
            s=s.replace(bytes(str1,codec),bytes(str2+" "*(len(str1.encode(codec))-len(str2.encode(codec))),codec),1)
f=open(sys.path[0]+split+package_out,"wb")
f.write(s)
f.close()
print("Build completed!")
