# -*- coding: utf-8 -*-

from linepy import *
from thrift.protocol import TCompactProtocol
from thrift.transport import THttpClient
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
#from gtts import gTTS
from bs4 import BeautifulSoup
from bs4.element import Tag
import requests as uReq
from datetime import datetime
from googletrans import Translator
from zalgo_text import zalgo
import ast, codecs, json, os, pytz, re, LineService, random, sys, time, urllib.parse, subprocess, threading, pyqrcode, pafy, humanize, os.path, traceback
from threading import Thread,Event
import requests,uvloop
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
loop = uvloop.new_event_loop()

listApp = [
    "IOSIPAD\t8.12.2\tHelloWorld\t8.22.17", 
    "CHROMEOS\t2.1.5\tHelloWorld\t11.2.5", 
    "DESKTOPWIN\t5.9.2\tHelloWorld\t11.2.5", 
    "DESKTOPMAC\t5.9.2\tHelloWorld\t11.2.5", 
    "WIN10\t5.5.5\tHelloWorld\t11.2.5"
]
try:
	for app in listApp:
		try:
			try:
				with open("authToken.txt", "r") as token:
					authToken = token.read()
					if not authToken:
						client = LINE()
						with open("authToken.txt","w") as token:
							token.write(client.authToken)
						continue
					client = LINE(authToken, speedThrift=False, appName="{}\t2.1.5\tAditmadzs\t11.2.5".format(app))
				break
			except Exception as error:
				print(error)
				if error == "REVOKE":
					exit()
				elif "auth" in error:
					continue
				else:
					exit()
		except Exception as error:
			print(error)
except Exception as error:
	print(error)
clientMid = client.profile.mid
clientStart = time.time()
clientPoll = OEPoll(client)

languageOpen = codecs.open("language.json","r","utf-8")
mentioOpen = codecs.open("tagme.json","r","utf-8")
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("setting.json","r","utf-8")
ownerOpen = codecs.open("owner.json","r","utf-8")
adminOpen = codecs.open("admin.json","r","utf-8")
stickerOpen = codecs.open("sticker.json","r","utf-8")
stickertOpen = codecs.open("stickertemplate.json","r","utf-8")
textaddOpen = codecs.open("text.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
waitOpen = codecs.open("wait.json","r","utf-8")
answeOpen = codecs.open("autoanswer.json","r","utf-8")

language = json.load(languageOpen)
tagme = json.load(mentioOpen)
read = json.load(readOpen)
settings = json.load(settingsOpen)
owner = json.load(ownerOpen)
admin = json.load(adminOpen)
stickers = json.load(stickerOpen)
stickerstemplate = json.load(stickertOpen)
textsadd = json.load(textaddOpen)
images = json.load(imagesOpen)
wait = json.load(waitOpen)
autoanswer = json.load(answeOpen)

welcome = []
offbot = []
temp_flood = {}
ssnd = []
rynk = {
    "myProfile": {
        "displayName": "",
    }
}
RfuCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}
kasar = "kontol","memek","kntl","ajg","anjing","asw","anju","gblk","goblok","bgsd","bangsad","bangsat"

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd.startswith('ex\n'):
      if sender in clientMid:
        try:
            sep = text.split('\n')
            ryn = text.replace(sep[0] + '\n','')
            f = open('exec.txt', 'w')
            sys.stdout = f
            print(' ')
            exec(ryn)
            print('\n%s' % str(datetime.now()))
            f.close()
            sys.stdout = sys.__stdout__
            with open('exec.txt','r') as r:
                txt = r.read()
            client.sendMessage(to, txt)
        except Exception as e:
            pass
      else:
        client.sendMessage(to, 'Apalo !')
    elif cmd.startswith('exc\n'):
      if sender in clientMid:
        sep = text.split('\n')
        ryn = text.replace(sep[0] + '\n','')
        if 'print' in ryn:
        	ryn = ryn.replace('print(','client.sendExecMessage(to,')
        	exec(ryn)
        else:
        	exec(ryn)
      else:
        client.sendMessage(to, 'Apalo !')

def logError(text):
    client.log("[ PEOPLE ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))

def waktu(self,secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Bulan" % (months)
    if weeks != 0: text += " %02d Minggu" % (weeks)
    if days != 0: text += " %02d Hari" % (days)
    if hours !=  0: text +=  " %02d Jam" % (hours)
    if mins != 0: text += " %02d Menit" % (mins)
    if secs != 0: text += " %02d Detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

def DESKTOPMAC():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "DESKTOPMAC\t5.9.2\tAditmadzsToken\tTools\t10.13.2",
    "x-lal": "ja-US_US",
    }
    return Headers
def DESKTOPWIN():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "DESKTOPWIN\t5.10.0\tAditmadzsToken\tTools\t10.13.2",
    "x-lal": "ja-US_US",
    }
    return Headers
def IOSIPAD():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "IOSIPAD\t8.12.2\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def CHROMEOS():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "CHROMEOS\t2.1.5\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def WIN10():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "WIN10\t5.5.5\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers
def ANDROID():
    Headers = {
    'User-Agent': "Line/8.3.2",
    'X-Line-Application': "ANDROID\t8.12.5\tAditmadzsToken\tTools\t11.2.5",
    "x-lal": "ja-US_US",
    }
    return Headers

def token(to,nametoken,msg_id,sender):
    try:
        a = nametoken
        a.update({'x-lpqs' : '/api/v4/TalkService.do'})
        transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4/TalkService.do')
        transport.setCustomHeaders(a)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        clienttoken = LineService.Client(protocol)
        qr = clienttoken.getAuthQrcode(keepLoggedIn=1, systemName='AditmadzsToken')
        link = "line://au/q/" + qr.verifier
        client.sendReplyMessage(msg_id, to, "Click This Link Only For 2 Minute :)\n\n{}".format(link))
        a.update({"x-lpqs" : '/api/v4/TalkService.do', 'X-Line-Access': qr.verifier})
        json.loads(requests.session().get('https://gd2.line.naver.jp/Q', headers=a).text)
        a.update({'x-lpqs' : '/api/v4p/rs'})
        transport = THttpClient.THttpClient('https://gd2.line.naver.jp/api/v4p/rs')
        transport.setCustomHeaders(a)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        clienttoken = LineService.Client(protocol)
        req = LoginRequest()
        req.type = 1
        req.verifier = qr.verifier
        req.e2eeVersion = 1
        res = clienttoken.loginZ(req)
        try:
            token = res.authToken
            contact = client.getContact(sender)
            client.sendMessage(sender, "Nama : {}\nMid : {}\nTOKEN : {}\n\nCreator".format(contact.displayName,contact.mid,token))
            client.sendContact(sender, clientMid)
        except Exception as e:
            client.sendMessage(to, str(e))
    except Exception as error:
        client.sendMessage(to, "Login Success")

def searchRecentMessages(to,id):
    for a in client.talk.getRecentMessagesV2(to,101):
        if a.id == id:
            return a
    return None

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost
def sendTextTemplate(to, text):
    data = {
            "type": "flex",
            "altText": "Xeberlhyn",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#F0F8FF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate5(to, text):
    data = {
            "type": "flex",
            "altText": "THE PEOPLE TEAM",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#F0F8FF"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "sɪʟᴀʜᴋᴀɴ ᴘɪʟɪʜ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "🎶SOUNDCLOUD🎶",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate1(to, text):
    data = {
                "type": "template",
                "altText": "xeberlhyn",
                "contents": {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                               "text": text,
                               "size": "sm",
                               "margin": "none",
                               "color": "#8B008B",
                               "wrap": True,
                               "weight": "regular",
                               "type": "text"
                            }
                        ]
                    }
                }
            }
    client.postTemplate(to, data)

def sendTextTemplate2(to, text):
    data = {
            "type": "flex",
            "altText": "Xeberlhyn",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000CD"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    client.postTemplate(to, data)

def sendTextTemplate3(to, text):
    data = {
            "type": "flex",
            "altText": "THE PEOPLE TEAM",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#F0F8FF"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴄʀᴇᴀᴛᴏʀ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "https://line.me/ti/p/~nandasri33"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "🎸 THE PE❍PLE TEAM 🎸",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  }
}
}
    client.postTemplate(to, data)

def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(client.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~nandasri33"
           }                                                
 }
]
                          }
                      }
    client.postTemplate(to, data)

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = client.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "welcome"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
      #  client.sendMessage(to, textx)
    except Exception as error:
        client.sendMessage(to)
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = client.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "babay"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        #client.sendMessage(to, textx)
    except Exception as error:
        client.sendMessage(to)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(client.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
#        client.sendMessage(to, textx)

    except Exception as error:
        client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def rynSplitText(text,lp=''):
    separate = text.split(" ")
    if lp == '':
        adalah = text.replace(separate[0]+" ","")
    elif lp == 's':
        adalah = text.replace(separate[0]+" "+separate[1]+" ","")
    else:
        adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
    return adalah


def Pertambahan(a,b):
    jum = a+b
    print(a, "+",b," = ",jum)
def Pengurangan(a,b):
    jum = a-b
    print(a, "-",b," = ",jum)
def Perkalian(a,b):
    jum = a*b
    print(a, "x",b," = ",jum)
def Pembagian(a,b):
    jum = a/b
    print(a, ":",b," = ",jum)
def Perpangkatan(a,b):
    jum = a**b
    print(a,"Pangkat ",b," = ",jum )

def urlEncode(url):
  import base64
  return base64.b64encode(url.encode()).decode('utf-8')

def urlDecode(url):
  import base64
  return base64.b64decode(url.encode()).decode('utf-8')

def removeCmdv(text, key=""):
    setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(" ")
    return text_.replace(sep[0] + " ", "")

def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''
    rmv = len(key + cmd) + 1
    return text[rmv:]

def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def commander(text):
    pesan = text.lower()
    if settings["setKey"] == False:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

def backupData():
    try:
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = settings
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = unsend
        f = codecs.open('unsend.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        bekep = tagme
        f = codecs.open('tagme.json','w','utf-8')
        json.dump(bekep, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def GenPictureQRCode(to,url):
    fn=url+".png"
    wildan=pyqrcode.create(url)
    wildan.png(fn, scale=6, module_color=[0, 0, 0, 128], background="#00FFFF")
    wildan.show()
    client.sendImage(to,fn)
    os.remove(fn)

def google_url_shorten(url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    #return resp['id'].replace("https://","")

def generateLink(to, ryn, rynurl=None):
    path = client.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.jpg')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    url = 'https://fahminogameno.life/uploadimage/action.php'
    r = requests.post(url, data=data, files=files)
    client.sendMessage(to, '%s\n%s' % (r.status_code,r.text))
    client.sendMessage(to, '{}{}'.format(rynurl,urlEncode('https://fahminogameno.life/uploadimage/images/ryngenerate.png')))

def uploadFile(ryn):
    url = 'https://fahminogameno.life/uploadimage/action.php'
    path = client.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.png')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    r = requests.post(url, data=data, files=files)
    if r.status_code == 200:
        return path

def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output TeamAnuBot.mp3 {}'.format(link))
    try:
        client.sendAudio(to, 'TeamAnuBot.mp3')
        time.sleep(2)
        os.remove('TeamAnuBot.mp3')
    except Exception as e:
        client.sendMessage(to, 'ãERRORã\nMungkin Link salah cek lagi coba')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
    try:
        client.sendVideo(to, "TeamAnuBot.mp4")
        time.sleep(2)
        os.remove('TeamAnuBot.mp4')
    except Exception as e:
        client.sendMessage(to, ' 「 ERROR 」\nMungkin Link Nya Salah GaN~', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+client.getContact(clientMid).pictureStatus, 'AGENT_NAME': '「 ERROR 」', 'AGENT_LINK': 'https://line.me/ti/p/~mobaloghanabi.'})

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "「BOT ACTIVE AGAIN」"
                        client.sendMessage(tmp, veza, {'AGENT_LINK': "https://line.me/ti/p/~mobaloghanabi", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)

def delExpirev2():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        veza = "「BOT ACTIVE AGAIN」"
                        client.sendMessage(tmp, veza, {'AGENT_LINK': "https://line.me/ti/p/~mobaloghanabi", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as error:
                        logError(error)

def sendHelp():
    sendhelp = settings["autoResponMessage"]
    client.sendMessage(to, sendhelp)
def menuHelp():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuHelp =  "╭━━━━━━╦══════╦━━━━━━╮" + "\n" + \
                "│╭━━━━━━━━━━━━━━━━━━━╮" + "\n" + \
                "╠❂࿇➢           Ħ€ŁP Μ€ŇỮ" + "\n" + \
                "│╰━━━━━━━━━━━━━━━━━━━╯" + "\n" + \
                "│╭═😉😉PE❍PLE B❍T😉😉═💝" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ʜᴇʟᴘ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴀʙᴏᴜᴛ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ʟɪsᴛ ᴛᴏᴋᴇɴ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴛʀᴀɴsʟᴀᴛᴇ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "sᴛᴀᴛᴜs" + "\n" + \
                "╠❂🇮🇩➢ " + key + "sᴇᴛᴛɪɴɢs" + "\n" + \
                "╠❂🇮🇩➢ " + key + "sᴇʟғ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ɢʀᴏᴜᴘ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "sᴇᴄɪᴀʟ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴍᴇᴅɪᴀ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴛᴀɢ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "sᴛᴀᴛᴜs sᴇᴛᴛɪɴɢs" + "\n" + \
                "│╰════[ 🎇🎆 🎊 🎆🎇]═══💝" + "\n" + \
                "╰━━━━━━╩══════╩━━━━━━╯" 
    return menuHelp

def menuStat():
    if settings['setKey'] == True:
       settings['keyCommand']
    else:
        key = ''
    menuStat =  "╭━━━━━━╦═════╦━━━━━━╮" + "\n" + \
                "│╭━━━━━━━━━━━━━━━━━━╮" + "\n" + \
                "╠❂࿇➢     ŞŦΔŦỮŞ Μ€ŇỮ" + "\n" + \
                "│╰━━━━━━━━━━━━━━━━━━╯" + "\n" + \
                "│╭═😉🎉PE❍PLE B❍T😉═💝" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴍʏᴋᴇʏ" + "\n" + \
                "╠🇮🇩➢ " + key + "ʟᴏɢᴏᴜᴛ" + "\n" + \
                "╠🇮🇩➢ " + key + "ʀᴇɴᴇᴡ" + "\n" + \
                "╠🇮🇩➢ " + key + "ʀᴜɴᴛɪᴍᴇ" + "\n" + \
                "╠🇮🇩➢ " + key + "sᴘᴇᴇᴅ" + "\n" + \
                "│╰═══[ 🎇🎆 🎊 🎆🎇]═══💝" + "\n" + \
                "╰━━━━━━╩═════╩━━━━━━╯" 
    return menuStat

def menuSett():
    if settings['setKey'] == True:
       settings['keyCommand']
    else:
        key = ''
    menuSett =  "╭━━━━━━╦═════╦━━━━━━╮" + "\n" + \
                "│╭━━━━━━━━━━━━━━━━━━╮" + "\n" + \
                "╠❂࿇➢         Ş€Ŧ Μ€ŇỮ" + "\n" + \
                "│╰━━━━━━━━━━━━━━━━━━╯" + "\n" + \
                "│╭═😉🎉PE❍PLE B❍T😉═💝" + "\n" + \
                "╠🇮🇩➢ " + key + "sᴇᴛᴋᴇʏ「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴀᴜᴛᴏᴀᴅᴅ「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴀᴜᴛᴏᴊᴏɪɴ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴀᴜᴛᴏᴊᴏɪɴᴛɪᴄᴋᴇᴛ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴀᴜᴛᴏʀᴇᴀᴅ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴀᴜᴛᴏʀᴇsᴘᴏɴ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴄʜᴇᴄᴋᴄᴏɴᴛᴀᴄᴛ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴄʜᴇᴄᴋᴘᴏsᴛ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴄʜᴇᴄᴋsᴛɪᴄᴋᴇʀ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴘᴜʙʟɪᴄ  「ᴏɴ/ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "sᴇᴛᴋᴇʏ  「ᴛᴇxᴛ」" + "\n" + \
                "╠🇮🇩➢ " + key + "sᴇᴛᴀᴜᴛᴏᴀᴅᴅᴍᴇssᴀɢᴇ" + "\n" + \
                "│╰═══[ 🎇🎆 🎊 🎆🎇]═══💝" + "\n" + \
                "╰━━━━━━╩═════╩━━━━━━╯"
    return menuSett


def statusSett():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    statusSett =  "╭━━━━━━╦═════╦━━━━━━╮" + "\n" + \
                "│╭━━━━━━━━━━━━━━━━━━╮" + "\n" + \
                "╠❂࿇➢       ŞŦΔŦỮŞ Ş€Ŧ" + "\n" + \
                "│╰━━━━━━━━━━━━━━━━━━╯" + "\n" + \
                "│╭═😉🎉PE❍PLE B❍T😉═💝" + "\n" + \
                "╠🇮🇩➢ " + key + "sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ" + "\n" + \
                "╠🇮🇩➢ " + key + "sᴛᴀᴛᴜs sᴇʟғ" + "\n" + \
                "╠🇮🇩➢ " + key + "sᴛᴀᴛᴜs ɢʀᴏᴜᴘ" + "\n" + \
                "╠🇮🇩➢ " + key + "sᴛᴀᴛᴜs ʀᴇsᴘᴏɴ ᴄʜᴀᴛ" + "\n" + \
                "╠🇮🇩➢ " + key + "sᴛᴀᴛᴜs ᴊᴏɪɴ ɢʀᴏᴜᴘ" + "\n" + \
                "│╰═══[ 🎇🎆 🎊 🎆🎇]═══💝" + "\n" + \
                "╰━━━━━━╩═════╩━━━━━━╯"
    return statusSett
  
def menuSelf():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuSelf =  "╭━━━━━━╦═════╦━━━━━━╮" + "\n" + \
                "│╭━━━━━━━━━━━━━━━━━━╮" + "\n" + \
                "╠❂࿇➢      ŞŦΔŦỮŞ Ş€Ŧ" + "\n" + \
                "│╰━━━━━━━━━━━━━━━━━━╯" + "\n" + \
                "│╭═😉🎉PE❍PLE B❍T😉═💝" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴄʜᴀɴɢᴇɴᴀᴍᴇ: 「ᴛᴇxᴛ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴄʜᴀɴɢᴇʙɪᴏ: 「ᴛᴇxᴛ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴍᴇ" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴍʏᴍɪᴅ" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴍʏʙɪᴏ" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴍʏɴᴀᴍᴇ" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴍʏʙɪᴏ" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴍʏᴘɪᴄᴛᴜʀᴇ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴍʏᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴍʏᴄᴏᴠᴇʀ" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴍʏᴘʀᴏғɪʟᴇ" + "\n" + \
                "╠🇮🇩➢ " + key + "ɢᴇᴛᴍɪᴅ @ᴍᴇɴᴛɪᴏɴ" + "\n" + \
                "╠🇮🇩➢ " + key + "ɢᴇᴛɴᴀᴍᴇ @ᴍᴇɴᴛɪᴏɴ" + "\n" + \
                "╠🇮🇩➢ " + key + "ɢᴇᴛʙɪᴏ @ᴍᴇɴᴛɪᴏɴ" + "\n" + \
                "╠🇮🇩➢ " + key + "ɢᴇᴛᴘɪᴄᴛᴜʀᴇ @ᴍᴇɴᴛɪᴏɴ" + "\n" + \
                "╠🇮🇩➢ " + key + "ɢᴇᴛᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ @ᴍᴇɴᴛɪᴏɴ" + "\n" + \
                "╠🇮🇩➢ " + key + "ɢᴇᴛᴄᴏᴠᴇʀ @ᴍᴇɴᴛɪᴏɴ" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴄʟᴏɴᴇᴘʀᴏғɪʟᴇ @ᴍᴇɴᴛɪᴏɴ " + "\n" + \
                "╠🇮🇩➢ " + key + "ʀᴇsᴛᴏʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
                "╠🇮🇩➢ " + key + "ʙᴀᴄᴋᴜᴘᴘʀᴏғɪʟᴇ" + "\n" + \
                "╠🇮🇩➢ " + key + "ғʀɪᴇɴᴅʟɪsᴛ" + "\n" + \
                "╠🇮🇩➢ " + key + "ғʀɪᴇɴᴅɪɴғᴏ 「ɴᴜᴍʙᴇʀ」" + "\n" + \
                "╠🇮🇩➢ " + key + "ʙʟᴏᴄᴋʟɪsᴛ" + "\n" + \
                "╠🇮🇩➢ " + key + "ғʀɪᴇɴᴅʙʀᴏᴀᴅᴄᴀsᴛ" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴄʜᴀɴɢᴇᴘɪᴄᴛᴜʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
                "╠🇮🇩➢ " + key + "ᴄʜᴀᴛᴛᴏғʀ-「ɴᴜᴍ」-「ᴛᴇxᴛ」" + "\n" + \
                "╠🇮🇩➢ " + key + "sᴘᴀᴍᴄʜᴀᴛ 「ɴᴜᴍ」 「ᴛᴇxᴛ」" + "\n" + \
                "│╰═══[ 🎇🎆 🎊 🎆🎇]═══💝" + "\n" + \
                "╰━━━━━━╩═════╩━━━━━━╯"
    return menuSelf
  
def menuGrup():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuGrup =  "╭━━━━━━╦══════╦━━━━━━╮" + "\n" + \
                "│╭━━━━━━━━━━━━━━━━━━━╮" + "\n" + \
                "╠❂࿇➢      Μ€ŇỮ GŘØỮP" + "\n" + \
                "│╰━━━━━━━━━━━━━━━━━━━╯" + "\n" + \
                "│╭═😉😉PE❍PLE B❍T😉😉═💝" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴄʜᴀɴɢᴇɢʀᴏᴜᴘɴᴀᴍᴇ: 「ᴛᴇxᴛ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ɢʀᴏᴜᴘᴄʀᴇᴀᴛᴏʀ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ɢʀᴏᴜᴘɪᴅ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ɢʀᴏᴜᴘɴᴀᴍᴇ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴏᴘᴇɴǫʀ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴄʟᴏsᴇǫʀ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ɢʀᴏᴜᴘʟɪsᴛ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴍᴇᴍʙᴇʀʟɪsᴛ  「ᴏɴ\ᴏғғ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴘᴇɴᴅɪɴɢʟɪsᴛ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴡᴇʟᴄᴏᴍᴇ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ɢʀᴏᴜᴘɪɴғᴏ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ɢʀᴏᴜᴘʙʀᴏᴀᴅᴄᴀsᴛ: 「ᴛᴇxᴛ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴄʜᴀɴɢᴇɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴍᴜᴛᴇ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴜɴᴍᴜᴛᴇ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ʟᴇᴀᴠᴇɢᴄ 「ɴᴜᴍ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "sᴇɴᴅᴄʀᴀsʜᴛᴏɢᴄ 「ɴᴜᴍ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ɪɴᴠɪᴛᴇᴛᴏɢᴄ 「ɴᴜᴍ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴍᴜᴛᴇʙᴏᴛɪɴɢᴄ 「ɴᴜᴍ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴜɴᴍᴜᴛᴇʙᴏᴛɪɴɢᴄ 「ɴᴜᴍ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴄʜᴀᴛᴏᴡɴᴇʀ 「ᴛᴇxᴛ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ᴄʜᴀᴛᴛᴏɢᴄ-「ɴᴜᴍ」-「ᴛᴇxᴛ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "ɢɪғᴛ" + "\n" + \
                "╠❂🇮🇩➢ " + key + "sᴇɴᴅɢɪғᴛᴛᴏɢᴄ 「ɴᴜᴍ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "sᴘᴀᴍᴛᴀɢ 「ɴᴜᴍ」 「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "sᴘᴀᴍᴄᴀʟʟ 「ɴᴜᴍ」 「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
                "╠❂🇮🇩➢ " + key + "sᴘᴀᴍɢʀᴏᴜᴘᴄᴀʟʟ 「ɴᴜᴍ」" + "\n" + \
                "│╰════[ 🎇🎆 🎊 🎆🎇]═══💝" + "\n" + \
                "╰━━━━━━╩══════╩━━━━━━╯"
    return menuGrup

def menuMention():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuMention =  "╭───「 Mention Menu𝔰 」" + "\n" + \
                "├ " + key + "Mimic 「On/Off」" + "\n" + \
                "├ " + key + "MimicList " + "\n" + \
                "├ " + key + "MimicAdd @Mention " + "\n" + \
                "├ " + key + "MimicDel @Mention " + "\n" + \
                "├ " + key + "UserAdd @Mention " + "\n" + \
                "├ " + key + "UserDel @Mention " + "\n" + \
                "├ " + key + "User List " + "\n" + \
                "├ " + key + "AdminAdd @Mention " + "\n" + \
                "├ " + key + "AdminDel @Mention " + "\n" + \
                "├ " + key + "Admin List " + "\n" + \
                "├ " + key + "MentionAll " + "\n" + \
                "├ " + key + "Mentionme " + "\n" + \
                "├ " + key + "DelMentionMe " + "\n" + \
                "├ " + key + "DelAllMentionMe " + "\n" + \
                "├────────────" + "\n" + \
                "├Creator : • Xeberlhyn" + "\n" + \
                "╰───「 {} 」".format(client.getProfile().displayName)
    return menuMention
  
def menuSpcl():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuSpcl =  "╭───「 Special Menu𝔰 」" + "\n" + \
                "├ " + key + "AddSticker「Text」" + "\n" + \
                "├ " + key + "DelSticker「Text」 " + "\n" + \
                "├ " + key + "ListSticker " + "\n" + \
                "├ " + key + "AddStickerTemplate「Text」" + "\n" + \
                "├ " + key + "DelStickerTemplate「Text」 " + "\n" + \
                "├ " + key + "ListStickerTemplate " + "\n" + \
                "├ " + key + "AddImage「Text」" + "\n" + \
                "├ " + key + "DelImage「Text」 " + "\n" + \
                "├ " + key + "ListImage " + "\n" + \
                "├ " + key + "AddText「Text」" + "\n" + \
                "├ " + key + "DelText「Text」 " + "\n" + \
                "├ " + key + "ListText " + "\n" + \
                "├ " + key + "Lurking 「On/Off」" + "\n" + \
                "├ " + key + "Lurking " + "\n" + \
                "├────────────" + "\n" + \
                "├Creator : • Xeberlhyn" + "\n" + \
                "╰───「 {} 」".format(client.getProfile().displayName)
    return menuSpcl
  
def menuMdia():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuMdia =  "╭─────「 Media Menu𝔰 」" + "\n" + \
                "╠🔘➣ " + key + "Al-Quran 「Number」" + "\n" + \
                "╠🔘➣ " + key + "AnimeStream「Search」 " + "\n" + \
                "╠🔘➣ " + key + "Aniongoing *" + "\n" + \
                "╠🔘➣ " + key + "ArtiMimpi 「Mimpi」" + "\n" + \
                "╠🔘➣ " + key + "ArtiNama 「Name」" + "\n" + \
                "╠🔘➣ " + key + "AsmaulHusna 「Number」" + "\n" + \
                "╠🔘➣ " + key + "Ayat Sajadah" + "\n" + \
                "╠🔘➣ " + key + "Brainly 「Text」" + "\n" + \
                "╠🔘➣ " + key + "CoolText 「Text」" + "\n" + \
                "╠🔘➣ " + key + "Danbooru「Page」" + "\n" + \
                "╠🔘➣ " + key + "Drakor「Search」 " + "\n" + \
                "╠🔘➣ " + key + "DrakorOnGoing " + "\n" + \
                "╠🔘➣ " + key + "FoggingWindows 「Text」 「Num 1 - 3」" + "\n" + \
                "╠🔘➣ " + key + "FsCosplay 「Text」" + "\n" + \
                "╠🔘➣ " + key + "Fsv 「Text」" + "\n" + \
                "╠🔘➣ " + key + "Graffity 「Text」" + "\n" + \
                "╠🔘➣ " + key + "Instagram 「Username」" + "\n" + \
                "╠🔘➣ " + key + "InstaPost 「Url」" + "\n" + \
                "╠🔘➣ " + key + "InstaStory 「Username」" + "\n" + \
                "╠🔘➣ " + key + "LedText 「Text」" + "\n" + \
                "╠🔘➣ " + key + "LineDownload 「URL」" + "\n" + \
                "╠🔘➣ " + key + "LinePost 「URL」" + "\n" + \
                "╠🔘➣ " + key + "Motivation" + "\n" + \
                "╠🔘➣ " + key + "MtoH(Masehi to Hijriaj) 「Date」" + "\n" + \
                "╠🔘➣ " + key + "Murrotal 「Num」" + "\n" + \
                "╠🔘➣ " + key + "NeonText 「Text」" + "\n" + \
                "╠🔘➣ " + key + "NewDrakor " + "\n" + \
                "╠🔘➣ " + key + "Praytime「Kota」" + "\n" + \
                "╠🔘➣ " + key + "PrettyJSON 「URL」" + "\n" + \
                "╠🔘➣ " + key + "Pulsk *" + "\n" + \
                "╠🔘➣ " + key + "Quotes " + "\n" + \
                "╠🔘➣ " + key + "Retrowave 「Text」 「Text2」 「Text3」 「Num 1 - 5」 「Num 1 - 4」" + "\n" + \
                "╠🔘➣ " + key + "Samehadaku 「Anime Name」" + "\n" + \
                "╠🔘➣ " + key + "SearchImage 「Search」" + "\n" + \
                "╠🔘➣ " + key + "SearchLyric 「Search」" + "\n" + \
                "╠🔘➣ " + key + "SearchMusic 「Search」" + "\n" + \
                "╠🔘➣ " + key + "SearchYoutube 「Search」" + "\n" + \
                "╠🔘➣ " + key + "SoupsLetters「Text」" + "\n" + \
                "╠🔘➣ " + key + "SSWEB 「Url」" + "\n" + \
                "╠🔘➣ " + key + "Stickerline「Text」" + "\n" + \
                "╠🔘➣ " + key + "StreetSigns 「Text」" + "\n" + \
                "╠🔘➣ " + key + "Themeline「Text」" + "\n" + \
                "╠🔘➣ " + key + "Token ChromeOS " + "\n" + \
                "╠🔘➣ " + key + "Waifu「Name」" + "\n" + \
                "╠🔘➣ " + key + "WhoIs 「Name」" + "\n" + \
                "╠🔘➣ " + key + "WriteCookies 「Text」" + "\n" + \
                "╠🔘➣ " + key + "Youtube 「Search」" + "\n" + \
                "╠🔘➣ " + key + "YtDownload「Url」*" + "\n" + \
                "╠🔘➣ " + key + "YtMp3 「Url」" + "\n" + \
                "╠🔘➣ " + key + "YtMp4 「Url」" + "\n" + \
                "├────────────" + "\n" + \
                "╠🔘➣ * = Under Maintenance" + "\n" + \
                "╠🔘➣ ^ = Coming Soon" + "\n" + \
                "╰─────「 {} 」".format(client.getProfile().displayName)
    return menuMdia

def menuBot():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuBot =  "╭───「 Bot Menu𝔰 」" + "\n" + \
                "├ " + key + "Changename: 「Text」" + "\n" + \
                "├ " + key + "Changebio: 「Text」" + "\n" + \
                "├ " + key + "Changecover" + "\n" + \
                "├ " + key + "Changepict" + "\n" + \
                "├ " + key + "Changedual" + "\n" + \
                "├ " + key + "Clear Chat" + "\n" + \
                "├ " + key + "Spaminvite|「Group Name」|「Num」|@Mention" + "\n" + \
                "├ " + key + "Spaminvmid|「Group Name」|「Num」|「MID」" + "\n" + \
                "├ " + key + "Grouplist" + "\n" + \
                "├ " + key + "Responsename" + "\n" + \
                "├ " + key + "MyBot" + "\n" + \
                "├Creator : • Xeberlhyn" + "\n" + \
                "╰───「 {} 」".format(client.getProfile().displayName)
    return menuBot
  
def menuTextToSpeech():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuTextToSpeech =  "╭───「 Text To Speech 」" + "\n" + \
                        "├≽ " + key + "af : Afrikaans" + "\n" + \
                        "├≽ " + key + "sq : Albanian" + "\n" + \
                        "├≽ " + key + "ar : Arabic" + "\n" + \
                        "├≽ " + key + "hy : Armenian" + "\n" + \
                        "├≽ " + key + "bn : Bengali" + "\n" + \
                        "├≽ " + key + "ca : Catalan" + "\n" + \
                        "├≽ " + key + "zh : Chinese" + "\n" + \
                        "├≽ " + key + "zh-cn : Chinese (Mandarin/China)" + "\n" + \
                        "├≽ " + key + "zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                        "├≽ " + key + "zh-yue : Chinese (Cantonese)" + "\n" + \
                        "├≽ " + key + "hr : Croatian" + "\n" + \
                        "├≽ " + key + "cs : Czech" + "\n" + \
                        "├≽ " + key + "da : Danish" + "\n" + \
                        "├≽ " + key + "nl : Dutch" + "\n" + \
                        "├≽ " + key + "en : English" + "\n" + \
                        "├≽ " + key + "en-au : English (Australia)" + "\n" + \
                        "├≽ " + key + "en-uk : English (United Kingdom)" + "\n" + \
                        "├≽ " + key + "en-us : English (United States)" + "\n" + \
                        "├≽ " + key + "eo : Esperanto" + "\n" + \
                        "├≽ " + key + "fi : Finnish" + "\n" + \
                        "├≽ " + key + "fr : French" + "\n" + \
                        "├≽ " + key + "de : German" + "\n" + \
                        "├≽ " + key + "el : Greek" + "\n" + \
                        "├≽ " + key + "hi : Hindi" + "\n" + \
                        "├≽ " + key + "hu : Hungarian" + "\n" + \
                        "├≽ " + key + "is : Icelandic" + "\n" + \
                        "├≽ " + key + "id : Indonesian" + "\n" + \
                        "├≽ " + key + "it : Italian" + "\n" + \
                        "├≽ " + key + "ja : Japanese" + "\n" + \
                        "├≽ " + key + "km : Khmer (Cambodian)" + "\n" + \
                        "├≽ " + key + "ko : Korean" + "\n" + \
                        "├≽ " + key + "la : Latin" + "\n" + \
                        "├≽ " + key + "lv : Latvian" + "\n" + \
                        "├≽ " + key + "mk : Macedonian" + "\n" + \
                        "├≽ " + key + "no : Norwegian" + "\n" + \
                        "├≽ " + key + "pl : Polish" + "\n" + \
                        "├≽ " + key + "pt : Portuguese" + "\n" + \
                        "├≽ " + key + "ro : Romanian" + "\n" + \
                        "├≽ " + key + "ru : Russian" + "\n" + \
                        "├≽ " + key + "sr : Serbian" + "\n" + \
                        "├≽ " + key + "si : Sinhala" + "\n" + \
                        "├≽ " + key + "sk : Slovak" + "\n" + \
                        "├≽ " + key + "es : Spanish" + "\n" + \
                        "├≽ " + key + "es-es : Spanish (Spain)" + "\n" + \
                        "├≽ " + key + "es-us : Spanish (United States)" + "\n" + \
                        "├≽ " + key + "sw : Swahili" + "\n" + \
                        "├≽ " + key + "sv : Swedish" + "\n" + \
                        "├≽ " + key + "ta : Tamil" + "\n" + \
                        "├≽ " + key + "th : Thai" + "\n" + \
                        "├≽ " + key + "tr : Turkish" + "\n" + \
                        "├≽ " + key + "uk : Ukrainian" + "\n" + \
                        "├≽ " + key + "vi : Vietnamese" + "\n" + \
                        "├≽ " + key + "cy : Welsh" + "\n" + \
                        "╰───「 Jangan Typo 」" + "\n" + \
                        "Contoh : " + key + "say-id chiken"
    return menuTextToSpeech

def menuTranslate():
    if settings['setKey'] == True:
        key = settings['keyCommand']
    else:
        key = ''
    menuTranslate = "╭───「 Translate 」" + "\n" + \
                    "├≽ " + key + "af : afrikaans" + "\n" + \
                    "├≽ " + key + "sq : albanian" + "\n" + \
                    "├≽ " + key + "am : amharic" + "\n" + \
                    "├≽ " + key + "ar : arabic" + "\n" + \
                    "├≽ " + key + "hy : armenian" + "\n" + \
                    "├≽ " + key + "az : azerbaijani" + "\n" + \
                    "├≽ " + key + "eu : basque" + "\n" + \
                    "├≽ " + key + "be : belarusian" + "\n" + \
                    "├≽ " + key + "bn : bengali" + "\n" + \
                    "├≽ " + key + "bs : bosnian" + "\n" + \
                    "├≽ " + key + "bg : bulgarian" + "\n" + \
                    "├≽ " + key + "ca : catalan" + "\n" + \
                    "├≽ " + key + "ceb : cebuano" + "\n" + \
                    "├≽ " + key + "ny : chichewa" + "\n" + \
                    "├≽ " + key + "zh-cn : chinese (simplified)" + "\n" + \
                    "├≽ " + key + "zh-tw : chinese (traditional)" + "\n" + \
                    "├≽ " + key + "co : corsican" + "\n" + \
                    "├≽ " + key + "hr : croatian" + "\n" + \
                    "├≽ " + key + "cs : czech" + "\n" + \
                    "├≽ " + key + "da : danish" + "\n" + \
                    "├≽ " + key + "nl : dutch" + "\n" + \
                    "├≽ " + key + "en : english" + "\n" + \
                    "├≽ " + key + "eo : esperanto" + "\n" + \
                    "├≽ " + key + "et : estonian" + "\n" + \
                    "├≽ " + key + "tl : filipino" + "\n" + \
                    "├≽ " + key + "fi : finnish" + "\n" + \
                    "├≽ " + key + "fr : french" + "\n" + \
                    "├≽ " + key + "fy : frisian" + "\n" + \
                    "├≽ " + key + "gl : galician" + "\n" + \
                    "├≽ " + key + "ka : georgian" + "\n" + \
                    "├≽ " + key + "de : german" + "\n" + \
                    "├≽ " + key + "el : greek" + "\n" + \
                    "├≽ " + key + "gu : gujarati" + "\n" + \
                    "├≽ " + key + "ht : haitian creole" + "\n" + \
                    "├≽ " + key + "ha : hausa" + "\n" + \
                    "├≽ " + key + "haw : hawaiian" + "\n" + \
                    "├≽ " + key + "iw : hebrew" + "\n" + \
                    "├≽ " + key + "hi : hindi" + "\n" + \
                    "├≽ " + key + "hmn : hmong" + "\n" + \
                    "├≽ " + key + "hu : hungarian" + "\n" + \
                    "├≽ " + key + "is : icelandic" + "\n" + \
                    "├≽ " + key + "ig : igbo" + "\n" + \
                    "├≽ " + key + "id : indonesian" + "\n" + \
                    "├≽ " + key + "ga : irish" + "\n" + \
                    "├≽ " + key + "it : italian" + "\n" + \
                    "├≽ " + key + "ja : japanese" + "\n" + \
                    "├≽ " + key + "jw : javanese" + "\n" + \
                    "├≽ " + key + "kn : kannada" + "\n" + \
                    "├≽ " + key + "kk : kazakh" + "\n" + \
                    "├≽ " + key + "km : khmer" + "\n" + \
                    "├≽ " + key + "ko : korean" + "\n" + \
                    "├≽ " + key + "ku : kurdish (kurmanji)" + "\n" + \
                    "├≽ " + key + "ky : kyrgyz" + "\n" + \
                    "├≽ " + key + "lo : lao" + "\n" + \
                    "├≽ " + key + "la : latin" + "\n" + \
                    "├≽ " + key + "lv : latvian" + "\n" + \
                    "├≽ " + key + "lt : lithuanian" + "\n" + \
                    "├≽ " + key + "lb : luxembourgish" + "\n" + \
                    "├≽ " + key + "mk : macedonian" + "\n" + \
                    "├≽ " + key + "mg : malagasy" + "\n" + \
                    "├≽ " + key + "ms : malay" + "\n" + \
                    "├≽ " + key + "ml : malayalam" + "\n" + \
                    "├≽ " + key + "mt : maltese" + "\n" + \
                    "├≽ " + key + "mi : maori" + "\n" + \
                    "├≽ " + key + "mr : marathi" + "\n" + \
                    "├≽ " + key + "mn : mongolian" + "\n" + \
                    "├≽ " + key + "my : myanmar (burmese)" + "\n" + \
                    "├≽ " + key + "ne : nepali" + "\n" + \
                    "├≽ " + key + "no : norwegian" + "\n" + \
                    "├≽ " + key + "ps : pashto" + "\n" + \
                    "├≽ " + key + "fa : persian" + "\n" + \
                    "├≽ " + key + "pl : polish" + "\n" + \
                    "├≽ " + key + "pt : portuguese" + "\n" + \
                    "├≽ " + key + "pa : punjabi" + "\n" + \
                    "├≽ " + key + "ro : romanian" + "\n" + \
                    "├≽ " + key + "ru : russian" + "\n" + \
                    "├≽ " + key + "sm : samoan" + "\n" + \
                    "├≽ " + key + "gd : scots gaelic" + "\n" + \
                    "├≽ " + key + "sr : serbian" + "\n" + \
                    "├≽ " + key + "st : sesotho" + "\n" + \
                    "├≽ " + key + "sn : shona" + "\n" + \
                    "├≽ " + key + "sd : sindhi" + "\n" + \
                    "├≽ " + key + "si : sinhala" + "\n" + \
                    "├≽ " + key + "sk : slovak" + "\n" + \
                    "├≽ " + key + "sl : slovenian" + "\n" + \
                    "├≽ " + key + "so : somali" + "\n" + \
                    "├≽ " + key + "es : spanish" + "\n" + \
                    "├≽ " + key + "su : sundanese" + "\n" + \
                    "├≽ " + key + "sw : swahili" + "\n" + \
                    "├≽ " + key + "sv : swedish" + "\n" + \
                    "├≽ " + key + "tg : tajik" + "\n" + \
                    "├≽ " + key + "ta : tamil" + "\n" + \
                    "├≽ " + key + "te : telugu" + "\n" + \
                    "├≽ " + key + "th : thai" + "\n" + \
                    "├≽ " + key + "tr : turkish" + "\n" + \
                    "├≽ " + key + "uk : ukrainian" + "\n" + \
                    "├≽ " + key + "ur : urdu" + "\n" + \
                    "├≽ " + key + "uz : uzbek" + "\n" + \
                    "├≽ " + key + "vi : vietnamese" + "\n" + \
                    "├≽ " + key + "cy : welsh" + "\n" + \
                    "├≽ " + key + "xh : xhosa" + "\n" + \
                    "├≽ " + key + "yi : yiddish" + "\n" + \
                    "├≽ " + key + "yo : yoruba" + "\n" + \
                    "├≽ " + key + "zu : zulu" + "\n" + \
                    "├≽ " + key + "fil : Filipino" + "\n" + \
                    "├≽ " + key + "he : Hebrew" + "\n" + \
                    "╰───「 Jangan Typo 」" + "\n" + \
                    "Contoh : " + key + "tr-id chiken"
    return menuTranslate

async def clientBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                client.findAndAddContactsByMid(op.param1)
            client.sendMention(op.param1, settings["autoAddMessage"], [op.param1])

        if op.type == 13:
            if settings["autoJoin"] and clientMid in op.param3:
                group = client.getGroup(op.param1)
                group.notificationDisabled = False
                client.acceptGroupInvitation(op.param1)
                client.updateGroup(group)
                client.sendMention(op.param1, settings["autoJoinMessage"], [op.param2])
        if op.type == 13:
            if settings["autoJoin"] and clientMid in op.param3:
              group = client.getGroup(op.param1)
              if settings["memberCancel"]["on"] == True:
                if len(group.members) <= settings["memberCancel"]["members"]:
                  client.acceptGroupInvitation(op.param1)
                  client.sendMention(op.param1, "sᴏʀʀʏ ᴍᴇᴍʙᴇʀs ɪs ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴡɪᴛʜ ᴍʏ sᴇᴛᴛɪɴɢ :(" ,[op.param2])
                  client.leaveGroup(op.param1)
                else:
                  client.acceptGroupInvitation(op.param1)
                  client.sendMention(op.param1, settings["autoJoinMessage"], [op.param2])

        if op.type == 15:
            if op.param1 in welcome:
                ginfo = client.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])
                contact = client.getContact(op.param2).picturePath
                data = {
                        "type": "flex",
                        "altText": "xeberlhyn",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(client.getContact(op.param2).displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#FF0000"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "text",
            "text": "💠 GOOD BYE 💠",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FFD700"
          },
          {
            "type": "text",
            "text": "➣ Selamat Jalan Saudara\n➣ Smoga Smakin Sukses\n➣ Dan Kami Dari Pengurus,\n➣ Minta Maaf Jikalau\n➣ Selama Kita Bersama\n➣ Kami Salah Dalam Berkata\n➣ Terimakasih",
            "size": "md",
            "weight": "bold",
            "color": "#ADFF2F",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#0000FF"
    },
    "footer": {
      "backgroundColor": "#DC143C"
    }
  },
  
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "BOSS",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~nandasri33"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  }
}
}
                client.postTemplate(op.param1, data)
                sendStickerTemplate(op.param1, "https://i.ibb.co/WGt0yGK/animasi-bergerak-selamat-tinggal-0020.gif")

        if op.type == 17:
            if op.param1 in welcome:
                ginfo = client.getGroup(op.param1)
                welcomeMembers(op.param1, [op.param2])
                contact = client.getContact(op.param2)
                data = {
                        "type": "flex",
                        "altText": "xeberlhyn",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(client.getContact(op.param2).displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#FF0000"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "text",
            "text": "💠 WELCOME TO THE ROOM 💠",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FFD700"
          },
          {
            "type": "text",
            "text": "➣ Jangan Lupa Cek Note\n➣ Ciptakan Keamanan Room,\n➣ Dan Harmoni Persahabatan\n➣ Karena Kita Semua\n➣ Sahabat Disini\n➣ Terimakasih",
            "size": "md",
            "weight": "bold",
            "color": "#ADFF2F",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#0000FF"
    },
    "footer": {
      "backgroundColor": "#DC143C"
    }
  },
  
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "BOSS",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~nandasri33"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  }
}
}
                client.postTemplate(op.param1, data)
                sendStickerTemplate(op.param1, "https://i.ibb.co/rGSVfNg/89933.gif")

        if op.type == 55:
            if op.param1 in read["readPoint"]:
                if op.param2 not in read["readMember"][op.param1]:
                    read["readMember"][op.param1].append(op.param2)

        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = client.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = client.getContact(op.param2)
                        data = {
                                "type": "flex",
                                "altText": "sider xeberlhyn",
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "            📽 ɕɕt℘ 📽",
            "size": "xl",
            "weight": "bold",
            "wrap": True,
            "color": "#FFFF00"
          },
          {
            "type": "text",
            "text": "📣sɪɴɪ ᴄʜᴀᴛ ᴅᴏɴᴋ ᴋᴀᴋ😄\n📣ᴋᴇɴᴀʟᴀɴ ᴀᴍᴀ ʏᴀɴɢ ʟᴀɪɴ😃\n📣ʙɪᴀʀ ᴍᴀᴋɪɴ ᴀᴋʀᴀʙ😅😅",
            "size": "md",
            "weight": "bold",
            "color": "#40E0D0",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(client.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴄʀᴇᴀᴛᴏʀ",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~nandasri33"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴏʀᴅᴇʀ",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "action": {
          "type": "uri",
          "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(client.getContact(op.param2).displayName),
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
      }
    ]
  }
}
}
                        client.postTemplate(op.param1, data);
#=======================================================================================================
        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                cmd = command(text)
                ryyn = "u3a1a2458a60d209a3d4802e789b7d540"
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
#===============================================================================================================================================
                        if cmd == "off":
                              if msg._from in ["u3a1a2458a60d209a3d4802e789b7d540"]:
                                if to not in offbot:
                                  client.sendMessageWithFooter(to, "❂➣ Mode Mute Active Di Group ini")
                                  offbot.append(to)
                                  print(to)
                                  
                                else:
                                  client.sendMessageWithFooter(to, "❂➣ Sukses Menonaktifkan Mute di Room ini")

                        if cmd == "on":
                              if msg._from in ["u3a1a2458a60d209a3d4802e789b7d540"]:
                                if to in offbot:
                                  offbot.remove(to)
                                  client.sendMessageWithFooter(to, "❂➣ Mode Mute Aktif")
                                  print(to)
                                  
                                else:
                                  client.sendMessageWithFooter(to, "❂➣ Sukses Mengaktifkan Mute Di Room ini")

#===================BAGIAN TOKEN =====================================================
                        if cmd == "token desktopmac":
                                ryn = DESKTOPMAC()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()
                        if cmd == "token desktopwin":
                                ryn = DESKTOPWIN()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()
                        if cmd == "token iosipad":
                                ryn = IOSIPAD()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()
                        if cmd == "token chromeos":
                                ryn = CHROMEOS()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()
                        if cmd == "token win10":
                                ryn = WIN10()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()
                        if cmd == "token android":
                                ryn = ANDROID()
                                Thread(target=token,args=(to,ryn,msg_id,sender,)).start()

                        if cmd == "list":
                                client.sendReplyMessage(msg_id, to, "1. Token Desktopmac\n2. Token Desktopwin\n3. Token Iosipad\n4. Token Chromeos\n5. Token Win10")
                                lists = {"result": [{"name": "Token Desktopwin",},{"name": "Token Chromeos",},{"name": "Token Iosipad",},{"name": "Token Desktopmac",},{"name": "Token Win10",}]}
                                if lists["result"] != []:
                                        ret_ = []
                                        for fn in lists["result"]:
                                                if len(ret_) >= 20:
                                                    pass
                                                else:
                                                    ret_.append({
                                                            "title": "{}".format(fn["name"]),
                                                            "text": "Click This Button For Get Your Token",
                                                            "styles": {
                                                             "footer": {
                                                              "backgroundColor": "#000000"
                                                             }
                                                           },
                                                           "type": "bubble",
                                                           "footer": {
                                                             "type": "box",   
                                                             "layout": "horizontal",
                                                             "contents": [
                                                               {
                                                                 "type": "text",
                                                                 "text": " ØP€Ň ØŘĐ€Ř",
                                                                 "size": "xl",
                                                                 "wrap": True,
                                                                 "weight": "bold",
                                                                 "color": "#FFFFFF",
                                                                 "actions": {
                                                                   "type": "uri",
                                                                   "uri": "line://app/1603968955-ORWb9RdY/?type=text&text={}".format(urllib.parse.quote("{}".format(fn["name"])))
                                                                 },
                                                                 "align": "center"            
                                                               }
                                                             ]
                                                           }
                                                        }
                                                    )
                                        k = len(ret_)//10
                                        for aa in range(k+1):
                                            data = {
                                                    "type": "template",
                                                    "altText": "Token",
                                                    "template": {
                                                        "type": "carousel",
                                                        "columns": ret_[aa*10 : (aa+1)*10]
                                                    }
                                                }
                                            client.postTemplate(to, data)


                        if cmd == "list token":
                                lists = {"result": [{"name": "Token Desktopwin",},{"name": "Token Chromeos",},{"name": "Token Iosipad",},{"name": "Token Desktopmac",},{"name": "Token Win10",}]}
                                if lists["result"] != []:
                                        ret_ = []
                                        for fn in lists["result"]:
                                                if len(ret_) >= 20:
                                                    pass
                                                else:
                                                    ret_.append({
                                                            "title": "{}".format(fn["name"]),	
                                                            "text": "Click This Button For Get Your Token",
                                                         #   "size": "xl",
                                                        #    "weight": "bold",
                                                            "actions": [
                                                                {
                                                                    "type": "uri",
                                                                    "label": "Click Me",
                                                                    "uri": "line://app/1603968955-ORWb9RdY/?type=text&text={}".format(urllib.parse.quote("{}".format(fn["name"])))
                                                                }
                                                            ]
                                                        }
                                                    )
                                        k = len(ret_)//10
                                        for aa in range(k+1):
                                            data = {
                                                    "type": "template",
                                                    "altText": "Token",
                                                    "template": {
                                                        "type": "carousel",
                                                        "columns": ret_[aa*10 : (aa+1)*10]
                                                    }
                                                }
                                            client.postTemplate(to, data)


                        elif cmd.startswith("uji3 "):
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "❂➣ Penyanyi: "+str(d)
                                hasil += "\n❂➣ Judul : "+str(c)
                                data = {
  "contents": [
    {
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/27ZtgNz/20190105-183730.jpg"
                  },
                  {
                    "text": "❂➣ 15 вσтs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "320k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ŦΔP Ħ€Ř€ ŦØ ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ØP€Ň ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "line://app/1603968955-ORWb9RdY/?type=song={}".format(str(urllib.parse.quote(urutan)))
            },
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                client.postFlex(to, data)
                                client.sendAudioWithURL(to, e)
                            except Exception as error:
                                client.sendMessage(to, "?? error\n?? " + str(error))
                                logError(error)

                        elif cmd.startswith("mp3 "):
                          if wait["selfbot"] == True:    
                           if msg._from in admin: 
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "?? Penyanyi: "+str(d)
                                hasil += "\n?? Judul : "+str(c)
                                aditmadzs.sendImageWithURL(to,g)
                                aditmadzs.sendAudioWithURL(to,e)
                                aditmadzs.sendMessage(msg.to,hasil)
                            except Exception as error:
                                aditmadzs.sendMessage(to, "?? error\n?? " + str(error))
                                logError(error)


#=========================ORDERAN==================================================================
                        if cmd == "order":
                                    data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
        "action": {
          "uri": "http://line.me/ti/p/nandasri33",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "ʙᴏᴛ ᴄʟ ᴘʀᴏᴛᴇᴄᴛ",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/27ZtgNz/20190105-183730.jpg"
                  },
                  {
                    "text": "❂➣ 5 вσтs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          
          {
            "text": "150K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/27ZtgNz/20190105-183730.jpg"
                  },
                  {
                    "text": "❂➣ 7 вσтs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/27ZtgNz/20190105-183730.jpg"
                  },
                  {
                    "text": "❂➣ 10 вσтs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/27ZtgNz/20190105-183730.jpg"
                  },
                  {
                    "text": "❂➣ 15 вσтs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "320k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ŦΔP Ħ€Ř€ ŦØ ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ØP€Ň ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/Jq2MKBW/20190105-101329.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~nandasri33",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "sᴇʟғ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/Jq2MKBW/20190105-101329.jpg"
                  },
                  {
                    "text": "❂➣ 5 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/Jq2MKBW/20190105-101329.jpg"
                  },
                  {
                    "text": "❂➣ 10 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/Jq2MKBW/20190105-101329.jpg"
                  },
                  {
                    "text": "❂➣ 15 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "300k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/Jq2MKBW/20190105-101329.jpg"
                  },
                  {
                    "text": "❂➣ 20 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "370k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ŦΔP Ħ€Ř€ ŦØ ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ØP€Ň ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "body": {
        "type": "cover",
        "backgroundColor": "#00FFFF"
      },
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/RvR6bm6/1546633145808.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~nandasri33",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "sᴇʟғ ʙᴏᴛ ᴛʜᴇ ᴘᴇᴏᴘʟᴇ",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/RvR6bm6/1546633145808.jpg"
                  },
                  {
                    "text": "❂➣ sᴇʟғʙᴏᴛ ɴᴏ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "70k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/RvR6bm6/1546633145808.jpg"
                  },
                  {
                    "text": "❂➣ sᴇʟғʙᴏᴛ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "100k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/RvR6bm6/1546633145808.jpg"
                  },
                  {
                    "text": "❂➣ sᴇʟғʙᴏᴛ 5 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/RvR6bm6/1546633145808.jpg"
                  },
                  {
                    "text": "❂➣ sᴇʟғʙᴏᴛ 7 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "❂➣ 200k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ŦΔP Ħ€Ř€ ŦØ ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ØP€Ň ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/TW3t9qC/20190107-085111.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~nandasri33",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "ᴘᴇᴍᴀsᴀɴɢᴀɴ ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/TW3t9qC/20190107-085111.jpg"
                  },
                  {
                    "text": "❂➣ ʀᴏᴏᴍ / ɢᴄ sᴍᴜʟᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/TW3t9qC/20190107-085111.jpg"
                  },
                  {
                    "text": "❂➣ ʀᴏᴏᴍ ᴇᴠᴇɴᴛ sᴍᴜʟᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200k Sampai Selesai",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/TW3t9qC/20190107-085111.jpg"
                  },
                  {
                    "text": "❂➣ ʀᴏᴏᴍ ᴄʜᴀᴛᴛɪɴɢ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "180k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/TW3t9qC/20190107-085111.jpg"
                  },
                  {
                    "text": "❂➣ DLL",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "--",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ŦΔP Ħ€Ř€ ŦØ ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ØP€Ň ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}

                                    client.postFlex(to, data)


                        elif cmd == "promo":
                            if msg._from in admin:
                                saya = client.getGroupIdsJoined()
                                for groups in saya:
                                    data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
        "action": {
          "uri": "http://line.me/ti/p/nandasri33",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "ʙᴏᴛ ᴄʟ ᴘʀᴏᴛᴇᴄᴛ",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/27ZtgNz/20190105-183730.jpg"
                  },
                  {
                    "text": "❂➣ 5 вσтs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          
          {
            "text": "150K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/27ZtgNz/20190105-183730.jpg"
                  },
                  {
                    "text": "❂➣ 7 вσтs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200K/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/27ZtgNz/20190105-183730.jpg"
                  },
                  {
                    "text": "❂➣ 10 вσтs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/27ZtgNz/20190105-183730.jpg"
                  },
                  {
                    "text": "❂➣ 15 вσтs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "320k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ŦΔP Ħ€Ř€ ŦØ ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ØP€Ň ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/Jq2MKBW/20190105-101329.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~nandasri33",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "sᴇʟғ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/Jq2MKBW/20190105-101329.jpg"
                  },
                  {
                    "text": "❂➣ 5 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/Jq2MKBW/20190105-101329.jpg"
                  },
                  {
                    "text": "❂➣ 10 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/Jq2MKBW/20190105-101329.jpg"
                  },
                  {
                    "text": "❂➣ 15 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "300k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/Jq2MKBW/20190105-101329.jpg"
                  },
                  {
                    "text": "❂➣ 20 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "370k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ŦΔP Ħ€Ř€ ŦØ ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ØP€Ň ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "body": {
        "type": "cover",
        "backgroundColor": "#00FFFF"
      },
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/RvR6bm6/1546633145808.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~nandasri33",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "sᴇʟғ ʙᴏᴛ ᴛʜᴇ ᴘᴇᴏᴘʟᴇ",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/RvR6bm6/1546633145808.jpg"
                  },
                  {
                    "text": "❂➣ sᴇʟғʙᴏᴛ ɴᴏ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "70k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/RvR6bm6/1546633145808.jpg"
                  },
                  {
                    "text": "❂➣ sᴇʟғʙᴏᴛ ᴛᴇᴍᴘʟᴀᴛᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "100k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/RvR6bm6/1546633145808.jpg"
                  },
                  {
                    "text": "❂➣ sᴇʟғʙᴏᴛ 5 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/RvR6bm6/1546633145808.jpg"
                  },
                  {
                    "text": "❂➣ sᴇʟғʙᴏᴛ 7 ᴀsɪsᴛ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "❂➣ 200k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ŦΔP Ħ€Ř€ ŦØ ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ØP€Ň ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/TW3t9qC/20190107-085111.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~nandasri33",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "ᴘᴇᴍᴀsᴀɴɢᴀɴ ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/TW3t9qC/20190107-085111.jpg"
                  },
                  {
                    "text": "❂➣ ʀᴏᴏᴍ / ɢᴄ sᴍᴜʟᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "150k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/TW3t9qC/20190107-085111.jpg"
                  },
                  {
                    "text": "❂➣ ʀᴏᴏᴍ ᴇᴠᴇɴᴛ sᴍᴜʟᴇ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200k Sampai Selesai",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/TW3t9qC/20190107-085111.jpg"
                  },
                  {
                    "text": "❂➣ ʀᴏᴏᴍ ᴄʜᴀᴛᴛɪɴɢ",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "180k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url": "https://i.ibb.co/TW3t9qC/20190107-085111.jpg"
                  },
                  {
                    "text": "❂➣ DLL",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "--",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "ŦΔP Ħ€Ř€ ŦØ ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": " ØP€Ň ØŘĐ€Ř",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "https://line.me/ti/p/~nandasri33"
            },
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                    client.postFlex(groups, data)

                        elif cmd.startswith("mp3"):
                            try:
                                proses = text.split("|")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "❂➣ Penyanyi: "+str(d)
                                hasil += "\n❂➣ Judul : "+str(c)
                                data = {
                                        "type": "flex",
                                        "altText": "Musik Xeberlhyn",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#00FFFF"
    },
    "footer": {
      "backgroundColor": "#9932CC"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": g,
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "「THE PEOPLE」\n      「TEAM」\n\n       「MP3」",
            "size": "sm",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": hasil,
                "size": "xs",
                "margin": "none",
                "color": "#FF6347",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "              PLAY",
                "size": "xxl",
                "weight": "bold",
                "action": {
                  "uri": e,
                  "type": "uri",
                  "label": "Audio"
                },
                "margin": "xl",
                "align": "start",
                "color": "#FFD700",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                client.postTemplate(to, data)
                            except Exception as error:
                                client.sendMessage(to, "?? error\n?? " + str(error))
                                logError(error)

                        elif cmd.startswith("sing "):
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] +" ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                time.sleep(2)
                                data = {
                                        "type": "flex",
                                        "altText": "smule Xeberlhyn",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#00FFFF"
    },
    "footer": {
      "backgroundColor": "#9932CC"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://i.ibb.co/gyzYpJ5/images-3.jpg",
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "「THE PEOPLE」\n      「TEAM」\n\n     「SMULE」",
            "size": "sm",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "❂➣ ID Smule : "+smule+"\n❂➣ Link:\n"+links,
                "size": "xs",
                "margin": "none",
                "color": "#FF6347",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "             LIHAT",
                "size": "xxl",
                "weight": "bold",
                "action": {
                  "uri": links,
                  "type": "uri",
                  "label": "Audio"
                },
                "margin": "xl",
                "align": "start",
                "color": "#FFD700",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                client.postTemplate(to, data)
                            except Exception as e:
                                pass

                        if cmd == "berita":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)                               	
                                data = {
                                        "type": "flex",
                                        "altText": "PENGUMUMAN THE PEOPLE TEAM",
                                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "       ✨🎊sᴀʟᴀᴍ ʜᴀʀᴍᴏɴɪ🎊✨\n\n🍭ᴅɪʙᴇʀɪᴛᴀʜᴜᴋᴀɴ ᴋᴇᴘᴀᴅᴀ\n🍭sᴇᴍᴜᴀ ᴘᴇsᴇʀᴛᴀ ᴇᴠᴇɴ\n🍭ᴘᴇʀᴇsᴍɪᴀɴ ʜᴠɢ\n🍭ʙᴀʜᴡᴀ ᴏᴄ ᴊᴏɪɴᴀɴ\n🍭ᴀᴋᴀɴ ᴅɪᴛᴜᴛᴜᴘ ᴘᴀᴅᴀ\n🍭ᴛᴀɴɢɢᴀʟ 18 ᴊᴀɴ 2019 \n🍭ᴘᴜᴋᴜʟ 23.59 ᴡɪʙ.\n🍭ɪᴋᴜᴛɪ ʀᴜʟᴇs ʏᴀɴɢ ᴀᴅᴀ ᴅɪ ɴᴏᴛᴇ",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#F0F8FF"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "       🙏ᴛᴇʀɪᴍᴀᴋᴀsɪʜ🙏",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "   🎉℘εŋɢนɱนɱศŋ🎉",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
      }
    ]
  }
}
}
                                client.postTemplate(to, data)



#============================ABOUT====================================
                        if cmd == "about":
                                groups = client.getGroupIdsJoined()
                                contacts = client.getAllContactIds()
                                blockeds = client.getBlockedContactIds()
                                crt = "u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540"
                                supp = "u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540","u3a1a2458a60d209a3d4802e789b7d540"
                                suplist = []
                                lists = []
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                runtime = timeNoww - clientStart
                                runtime = timeChange(runtime)
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n│ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "About Xeberlhyn",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(client.getContact(clientMid).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "   THE PE❍PLE\n     🎭TEAM🎭\n\n    🍦SELFBOT🍦",
            "size": "sm",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "text": "👔җэвэяℓђýи в๏†ร👔",
            "size": "xl",
            "align": "center",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "🎸ɴᴀᴍᴀ: {}".format(client.getProfile().displayName),
                "size": "md",
                "margin": "none",
                "color": "#ADFF2F",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#800080"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "🌠 ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ : {}".format(str(runtime)),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "🌠 ᴊᴜᴍʟᴀʜ ɢʀᴏᴜᴘ : {}".format(str(len(groups))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "🌠 ᴊᴜᴍʟᴀʜ ᴛᴇᴍᴀɴ : {}".format(str(len(contacts))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "🌠 ᴊᴜᴍʟᴀʜ ʙʟᴏᴋ : {}".format(str(len(blockeds))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "🌠 ᴠᴇʀsɪᴏɴ : v5.0",
                "size": "xs",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "url": "https://i.ibb.co/27ZtgNz/20190105-183730.jpg",
                "type": "icon",
                "size": "md"
              },
              {
                "text": "🌟 Mყ Sน℘℘σгt 🌟\n❂🇮🇩➣ ᴛʜᴇ ᴘᴇ❍ᴘʟᴇ ʙ❍ᴛs\n❂🇮🇩➣ ᴀɴᴜ ʙ❍ᴛs\n❂🇮🇩➣ ᴀsᴇᴘ ʙ❍ᴛs\n❂🇮🇩➣ ʙʀ❍ɴᴅ❍ɴɢ ʙ❍ᴛs\n❂🇮🇩➣ ᴋɪʙᴀᴢ ʙ❍ᴛs\n❂🇮🇩➣ ʀ❍ɴᴅ❍ ʙ❍ᴛs\n❂🇮🇩➣ ᴀʀᴛʜᴀ ʙ❍ᴛs",
                "size": "xs",
                "margin": "none",
                "color": "#FF6347",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "          ᴄʀᴇᴀᴛᴏʀ",
                "size": "xxl",
                "weight": "bold",
                "action": {
                  "uri": "https://line.me/ti/p/~nandasri33",
                  "type": "uri",
                  "label": "Add Creator"
                },
                "margin": "xl",
                "align": "start",
                "color": "#F0F8FF",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "            ᴏʀᴅᴇʀ",
                "size": "xxl",
                "weight": "bold",
                "action": {
                  "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=order",
                  "type": "uri",
                  "label": " 「Open Order」"
                },
                "margin": "xl",
                "align": "start",
                "color": "#F0F8FF",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                client.postTemplate(to, data)



                        if cmd == "me":
                                contact = client.getProfile()
                                mids = [contact.mid]
                                status = client.getContact(sender)                               	
                                data = {
                                        "type": "flex",
                                        "altText": "Me Message THE PEOPLE TEAM",
                                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "รtศtนร ℘гσʄıɭε :",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#7FFF00"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "align": "center",
            "size": "sm",
            "weight": "bold",
            "color": "#FF00FF",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ᴄʀᴇᴀᴛᴏʀ",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "action": {
          "type": "uri",
          "uri": "https://line.me/ti/p/~nandasri33"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ᴏʀᴅᴇʀ",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "action": {
          "type": "uri",
          "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "hero": {
    "aspectMode": "cover",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(client.getContact(sender).pictureStatus),
    "size": "full",
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(status.displayName),
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7FFF00",
        "align": "center"
      }
    ]
  }
}
}
                                client.postTemplate(to, data)






#============================ME=======================================

#=====================================================================================================================
                        if msg.toType != 0 and msg.toType == 2:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    if ryyn in mention["M"]:
                                        if ryyn in mention["M"]:
                                            if to not in tagme['ROM']:
                                                tagme['ROM'][to] = {}
                                            if sender not in tagme['ROM'][to]:
                                                tagme['ROM'][to][sender] = {}
                                            if 'msg.id' not in tagme['ROM'][to][sender]:
                                                tagme['ROM'][to][sender]['msg.id'] = []
                                            if 'waktu' not in tagme['ROM'][to][sender]:
                                                tagme['ROM'][to][sender]['waktu'] = []
                                            tagme['ROM'][to][sender]['msg.id'].append(msg.id)
                                            tagme['ROM'][to][sender]['waktu'].append(msg.createdTime)

                            elif receiver in temp_flood:
                                if temp_flood[receiver]["expire"] == True:
                                    if cmd == "buka":
                                        temp_flood[receiver]["expire"] = False
                                        temp_flood[receiver]["time"] = time.time()
                                        client.sendMessageWithFooter(to, "BOT ACTIVE AGAIN")
                                    return
                                elif time.time() - temp_flood[receiver]["time"] <= 5:
                                    temp_flood[receiver]["flood"] += 1
                                    if temp_flood[receiver]["flood"] >= 500:
                                        temp_flood[receiver]["flood"] = 0
                                        temp_flood[receiver]["expire"] = True
                                        ret_ = "Bots will be SILENT for a while in this group because of SPAM\n or Type Open"
                                        userid = "https://line.me/ti/p/~" + client.profile.userid
                                        client.sendMessage(to,'「Detect Flood」\n'+str(ret_), {'AGENT_NAME': ' Notif Spam','AGENT_LINK': 'http://line.me/ti/p/mobaloghanabi','AGENT_ICON': 'http://klikuntung.com/images/messengers/line-logo.png' })
                                else:
                                    temp_flood[receiver]["flood"] = 0
                                temp_flood[receiver]["time"] = time.time()
                            else:
                                temp_flood[receiver] = {
                                 "time": time.time(),
                                 "flood": 0,
                                 "expire": False
                                }
            except Exception as error:
                logError(error)
#========================================BAGIAN STICKER===================================================================
        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                cmd = commander(text)
                for cmd in cmd.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == True:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != client.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:                            	
#=============================STICKER==========================================================================
                            if "haha" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/9Yp3hNN/AW1238395-00.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~nandasri33"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)

                            elif "kok tau" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/JtqYf3t/AW1238502-06.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~nandasri33"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)

                            elif "hadeh" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/dJ1H13M/Benjol.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~nandasri33"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)

                            elif "assalamualaikum" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/WfBYGNc/6898988-20140614015502.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~nandasri33"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)

                            elif "asalam" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/WfBYGNc/6898988-20140614015502.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~nandasri33"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)

                            elif "sue" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~nandasri33"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)

                            elif "kamvre" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/CVMQ40k/7c8ab257ee3b7e1ef283b7c0a35d9d2c.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~nandasri33"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)

                            elif "sepi" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/hHG5Mwb/AW316819-05.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~nandasri33"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)


                            elif "love" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/hXGJ5Y3/Gif-BBM-Bergerak.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~nandasri33"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)
            except Exception as error:
                logError(error)

        if op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != client.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "╔══[ Details Post ]"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = client.getContact(sender)
                                        auth = "\n╠❂🇮🇩➢ Penulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\n╠❂🇮🇩➢ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\n╠❂🇮🇩➢ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\n╠❂🇮🇩➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\n╠❂🇮🇩➢ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\n╠❂🇮🇩➢ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\n╠❂🇮🇩➢ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\n╠❂🇮🇩➢ Tulisan :\n╠❂🇮🇩➢ {}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\n╚══[ Finish ]"
                                    client.sendMessage(to, str(ret_))
                                except:
                                    sendTextTemplate(to, "❂🇮🇩➢ Post tidak valid")
                            if msg.toType in (2,1,0):
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                adw = client.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                adws = client.createComment(purl[0], purl[1], settings["commentPost"])
                                sendTextTemplate(to, "❂🇮🇩➢ Done Like Boss !")
            except Exception as error:
                logError(error)
#==========================================================================================================
        if op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != client.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return

                            if terminal == "logout":
                              if msg._from in admin:
                                logout = "ʙᴇʀʜᴀsɪʟ ᴍᴇᴍᴀᴛɪᴋᴀ ʙᴏᴛ"
                                contact = client.getContact(sender)
                                icon = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                name = contact.displayName
                                link = "line://ti/p/~nandasri33"
                                client.sendFooter(to, logout, icon, name, link )
                                sys.exit("[ INFO ] BOT SHUTDOWN")

                            elif terminal == "reset":
                              if msg._from in owner:
                                restart = "ʙᴏᴛ sᴜᴋsᴇs ᴅɪ ʀᴇsᴇᴛ ᴜʟᴀɴɢ ʙᴏs"
                                contact = client.getContact(sender)
                                sendTextTemplate(to, restart)
                                restartBot()

                            elif terminal == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - clientStart
                                runtime = timeChange(runtime)
                                run = "❂🇮🇩➣ ʙᴏᴛ ᴛᴇʟᴀʜ ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ\n⏰{}".format(str(runtime))
                                sendTextTemplate(to, run)

                            elif terminal == "speed":
                            	get_profile_time_start = time.time()
                            	get_profile = client.getProfile()
                            	get_profile_time = time.time() - get_profile_time_start
                            	speed = " {} ᴅᴇᴛɪᴋ".format(str(get_profile_time))
                            	sendTextTemplate(to, speed)

                            elif terminal == "gid":
                              if msg._from in admin:
                                gid = client.getGroupIdsJoined()
                                h = ""
                                for i in gid:
                                    h += "❂➣ %s:\n%s\n\n" % (client.getGroup(i).name,i)
                                sendTextTemplate(to,"                 ĐΔ₣ŦΔŘ IĐ GŘØỮPŞ\n\n"+h)

                            elif terminal == "namagroup":
                              if msg._from in admin:
                                gid = client.getGroup(to)
                                sendTextTemplate(to, "🔹 ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ 🔹\n❂➣ {}".format(gid.displayName))

                            elif terminal == "fotogroup":
                              if msg._from in admin:
                                gid = client.getGroup(to)
                                sendTextTemplate(to,"http://dl.profile.line-cdn.net/{}".format(gid.pictureStatus))

                            elif terminal == "reject":
                              if settings["selfbot"] == True:
                                if msg._from in admin:
                                  ginvited = client.getGroupIdsInvited()
                                  if ginvited != [] and ginvited != None:
                                      for gid in ginvited:
                                          client.rejectGroupInvitation(gid)
                                      sendTextTemplate(to, "❂➣ ʙᴇʀʜᴀsɪʟ ᴛᴏʟᴀᴋ sᴇʙᴀɴʏᴀᴋ {} ᴜɴᴅᴀɴɢᴀɴ ɢʀᴏᴜᴘ".format(str(len(ginvited))))
                                  else:
                                      sendTextTemplate(to, "❂➣ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜɴᴅᴀɴɢᴀɴ ʏᴀɴɢ ᴛᴇʀᴛᴜɴᴅᴀ")

                            elif terminal == "cek error":
                                if sender in admin:
                                    with open('errorLog.txt', 'r') as er:
                                        error = er.read()
                                    client.sendMessageWithFooter(to, str(error))

                            elif terminal == "reset error":
                                if sender in admin:
                                    with open('errorLog.txt', 'w') as er:
                                        error = er.write("")
                                    client.sendMessageWithFooter(to, str(error))

                            elif terminal.startswith("setkey: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                settings["keyCommand"] = str(key).lower()
                                sendTextTemplate(to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴜʙᴀʜ sᴇᴛ ᴋᴇʏ ᴄᴏᴍᴍᴀɴᴅ ᴍᴇɴᴊᴀᴅɪ : 「{}」".format(str(key).lower()))

                            elif terminal == "help":
                                with open("help.json","r") as f:
                                    data = json.load(f)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                            if len(ret_) >= 20:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["link"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "{}".format(str(fn["name"])),
                                                        "uri": "{}".format(str(fn["linkliff"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                                "type": "template",
                                                "altText": "Help Message",
                                                "template": {
                                                    "type": "image_carousel",
                                                    "columns": ret_[aa*10 : (aa+1)*10]
                                                }
                                            }
                                        client.postTemplate(to, data)

                            elif terminal == "status":
                                helpStatus = menuStat()
                                sendTextTemplate3(to, helpStatus)
                            elif terminal == "settings":
                                helpSettings = menuSett()
                                sendTextTemplate3(to, helpSettings)
                            elif terminal == "self":
                                helpSelf = menuSelf()
                                sendTextTemplate3(to, helpSelf)
                            elif terminal == "group":
                                helpGroup = menuGrup()
                                sendTextTemplate(to, helpGroup)
                            elif terminal == "special":
                                helpSpecial = menuSpcl()
                                sendTextTemplate3(to, helpSpecial)
                            elif terminal == "media":
                                helpMedia = menuMdia()
                                sendTextTemplate3(to, helpMedia)
                            elif terminal == "tag":
                                helpMention = menuMention()
                                sendTextTemplate3(to, helpMention)
                            elif terminal == "status setting":
                                sendTextTemplate3(to, statusSett())

                            elif terminal == "remove":
                                client.removeAllMessages(op.param2)
                                sendTextTemplate(to, "sᴜᴄᴄᴇsғᴜʟʟʏ ᴄʟᴇᴀʀ ᴍᴇssᴀɢᴇs")

                            elif terminal == "status message":
                                try:
                                    ret_ = "╭───「 Status Message 」"
                                    if settings["checkContact"] == True: ret_ += "\n├≽ Check Contact : ON"
                                    else: ret_ += "\n├≽ Check Contact : OFF"
                                    if settings["checkPost"] == True: ret_ += "\n├≽ Check Post : ON"
                                    else: ret_ += "\n├≽ Check Post : OFF"
                                    if settings["checkSticker"] == True: ret_ += "\n├≽ Check Sticker : ON"
                                    else: ret_ += "\n├≽ Check Sticker : OFF"
                                    if settings["setKey"] == True: ret_ += "\n├≽ Set Key : ON"
                                    else: ret_ += "\n├≽ Set Key : OFF"
                                    if settings["autoAdd"] == True: ret_ += "\n├≽ Auto Add : ON"
                                    else: ret_ += "\n├≽ Auto Add : OFF"
                                    if settings["autoRespon"] == True: ret_ += "\n├≽ Auto Respon : ON"
                                    else: ret_ += "\n├≽ Auto Respon : OFF"
                                    if settings["autoReply"] == True: ret_ += "\n├≽ Auto Reply : ON"
                                    else: ret_ += "\n├≽ Auto Reply : OFF"
                                    if to in settings["sticker"] == True: ret_ += "\n├≽ Sticker : ON"
                                    else: ret_ += "\n├≽ Sticker : OFF"
                                    if to in settings["simiSimi"] == True: ret_ += "\n├≽ Simi Simi : ON"
                                    else: ret_ += "\n├≽ Simi Simi : OFF"
                                    if to in settings["sniff"] == True: ret_ += "\n├≽ Sniff Mode : ON"
                                    else: ret_ += "\n├≽ Sniff Mode : OFF"
                                    if settings["autoJoin"] == True: ret_ += "\n├≽ Auto Join : ON"
                                    else: ret_ += "\n├≽ Auto Join : OFF"
                                    if settings["autoJoinTicket"] == True: ret_ += "\n├≽ Auto Join Ticket : ON"
                                    else: ret_ += "\n├≽ Auto Join Ticket : OFF"
                                    if settings["autoJoinTicketBot"] == True: ret_ += "\n├≽ Auto Join Ticket Bot : ON"
                                    else: ret_ += "\n├≽ Auto Join Ticket Bot : OFF"
                                    if settings["autoRead"] == True: ret_ += "\n├≽ Auto Read : ON"
                                    else: ret_ += "\n├≽ Auto Read : OFF"
                                    sendTextTemplate3(to, ret_)
                                except Exception as error:
                                    sendTextTemplate3(to, str(error))

                            elif terminal == "open":
                              if msg._from in admin:
                                if msg.toType == 2:
                                   X = client.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   client.updateGroup(X)
                                   sendTextTemplate(msg.to, "❂➣ Url Opened")

                            elif terminal == "close":
                              if msg._from in admin:
                                  if msg.toType == 2:
                                     X = client.getGroup(msg.to)
                                     X.preventedJoinByTicket = True
                                     client.updateGroup(X)
                                     sendTextTemplate(msg.to, "❂➣ Url Closed")

                            elif terminal == "url":
                              if msg._from in admin:
                                  if msg.toType == 2:
                                     x = client.getGroup(msg.to)
                                     if x.preventedJoinByTicket == True:
                                        x.preventedJoinByTicket = False
                                        client.updateGroup(x)
                                     gurl = client.reissueGroupTicket(msg.to)
                                     sendTextTemplate(msg.to, "❂➣ Nama : "+str(x.name)+ "\n❂➣ Url grup : http://line.me/R/ti/g/"+gurl)                                                                                                                                              

                            elif terminal == "grouplist":
                                groups = client.getGroupIdsJoined()
                                ret_ = "╭━━━━━━╦═════╦━━━━━━╮\n│╭━━━━━━━━━━━━━━━━━━╮\n╠❂࿇➢     ĐΔ₣ŦΔŘ GŘØỮP\n│╰━━━━━━━━━━━━━━━━━━╯\n│╭═😉🎉 PE❍PLE B❍T😉═💝"
                                no = 0
                                for gid in groups:
                                    group = client.getGroup(gid)
                                    no += 1
                                    ret_ += "\n╠🌟➢ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                ret_ += "\n│╰═══[ 🎇🎆 {} 🎆🎇]═══💝\n╰━━━━━━╩═════╩━━━━━━╯".format(str(len(groups)))
                                client.sendReplyMessage(msg_id, to, str(ret_))

                            elif terminal == "memberlist":
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    num = 0
                                    ret_ = "╭━━━━━━╦═════╦━━━━━━╮\n│╭━━━━━━━━━━━━━━━━━━╮\n╠❂࿇➢     ĐΔ₣ŦΔŘ GŘØỮP\n│╰━━━━━━━━━━━━━━━━━━╯\n│╭═😉🎉 PE❍PLE B❍T😉═💝"
                                    for contact in group.members:
                                        num += 1
                                        ret_ += "\n╠🌟➢ {}. {}".format(num, contact.displayName)
                                    ret_ += "\n│╰═══[ 🎇🎆 {} 🎆🎇]═══💝\n╰━━━━━━╩═════╩━━━━━━╯".format(len(group.members))
                                    client.sendReplyMessage(msg_id, to, ret_)

#===============================MEDIA=============================================================
                            elif text.lower() == 'kalender':
                              if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = "❂➣ "+ hasil + " : " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n\n❂➣ Jam : 🔹 " + timeNow.strftime('%H:%M:%S') + " 🔹"
                                sendTextTemplate(msg.to, readTime)

                            elif terminal.startswith("soundcloud "):
                                def sdc():
                                    kitsunesplit = rynSplitText(msg.text.lower()).split(" ")
                                    r = requests.get('https://soundcloud.com/search?q={}'.format(rynSplitText(msg.text.lower())))
                                    soup = BeautifulSoup(r.text,'html5lib')
                                    data = soup.find_all(class_='soundTitle__titleContainer')
                                    data = soup.select('li > h2 > a')
                                    if len(kitsunesplit) == 1:
                                        a = '          🎺 NOTE PILIHAN LAGU 🎺\n____________________________________';no=0
                                        for b in data:
                                            no+=1
                                            a+= '\n{}. {}'.format(no,b.text)
                                        sendTextTemplate5(to,a)
                                    if len(kitsunesplit) == 2:
                                        a = data[int(kitsunesplit[1])-1];b = list(a)[0]
                                        kk = random.randint(0,999)
                                        sendTextTemplate5(to,'Judul: {}\nStatus: Waiting... For Upload'.format(a.text))
                                        hh=subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output {}.mp3 {}'.format(kk,'https://soundcloud.com{}'.format(a.get('href'))))
                                        try:client.sendAudio(to,'{}.mp3'.format(kk))
                                        except Exception as e:sendTextTemplate(to,' 「 ERROR 」\nJudul: {}\nStatus: {}\nImportant: Try again'.format(a.text,e))
                                        os.remove('{}.mp3'.format(kk))
                                ryn = Thread(target=sdc)
                                ryn.daemon = True
                                ryn.start()
                                ryn.join()


                            elif terminal == "autojoin on":
                              if msg._from in admin:
                                if settings["autoJoin"] == True:
                                    sendTextTemplate(to, "Auto join telah aktif")
                                else:
                                    settings["autoJoin"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto join")
                            elif terminal == "autojoin off":
                              if msg._from in admin:
                                if settings["autoJoin"] == False:
                                    sendTextTemplate(to, "Auto join telah nonaktif")
                                else:
                                    settings["autoJoin"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto join")

                            elif terminal == "autojointicket on":
                              if msg._from in admin:
                                if settings["autoJoinTicket"] == True:
                                    sendTextTemplate(to, "Auto join ticket telah aktif")
                                else:
                                    settings["autoJoinTicket"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto join ticket")
                            elif terminal == "autojointicket off":
                              if msg._from in admin:
                                if settings["autoJoinTicket"] == False:
                                    sendTextTemplate(to, "Auto join ticket telah nonaktif")
                                else:
                                    settings["autoJoinTicket"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto join ticket")

                            elif terminal == "autoread on":
                              if msg._from in admin:
                                if settings["autoRead"] == True:
                                    client.sendMessage(to, "Auto read telah aktif")
                                else:
                                    settings["autoRead"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto read")
                            elif terminal == "autoread off":
                              if msg._from in admin:
                                if settings["autoRead"] == False:
                                    client.sendMessage(to, "Auto read telah nonaktif")
                                else:
                                    settings["autoRead"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto read")

                            elif terminal == "autorespon on":
                              if msg._from in admin:
                                if settings["autoRespon"] == True:
                                    sendTextTemplate(to, "Auto respon telah aktif")
                                else:
                                    settings["autoRespon"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto respon")
                            elif terminal == "autorespon off":
                              if msg._from in admin:
                                if settings["autoRespon"] == False:
                                    sendTextTemplate(to, "Auto respon telah nonaktif")
                                else:
                                    settings["autoRespon"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto respon")

                            elif terminal == "autoreply on":
                              if msg._from in admin:
                                if settings["autoReply"] == True:
                                    sendTextTemplate(to, "Auto Reply telah aktif")
                                else:
                                    settings["autoReply"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan auto reply")
                            elif terminal == "autoreply off":
                              if msg._from in admin:
                                if settings["autoReply"] == False:
                                    sendTextTemplate(to, "Auto Reply telah nonaktif")
                                else:
                                    settings["autoReply"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan auto Reply")

                            elif terminal == "checkcontact on":
                              if msg._from in admin:
                                if settings["checkContact"] == True:
                                    sendTextTemplate(to, "Check details contact telah aktif")
                                else:
                                    settings["checkContact"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan check details contact")
                            elif terminal == "checkcontact off":
                              if msg._from in admin:                          
                                if settings["checkContact"] == False:
                                    sendTextTemplate(to, "Check details contact telah nonaktif")
                                else:
                                    settings["checkContact"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan Check details contact")

                            elif terminal == "checkpost on":
                              if msg._from in admin:                          
                                if settings["checkPost"] == True:
                                    sendTextTemplate(to, "Check details post telah aktif")
                                else:
                                    settings["checkPost"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan check details post")
                            elif terminal == "checkpost off":
                              if msg._from in admin:                          
                                if settings["checkPost"] == False:
                                    sendTextTemplate(to, "Check details post telah nonaktif")
                                else:
                                    settings["checkPost"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan check details post")

                            elif terminal == "checksticker on":
                              if msg._from in admin:
                                if settings["checkSticker"] == True:
                                    sendTextTemplate(to, "Check details sticker telah aktif")
                                else:
                                    settings["checkSticker"] = True
                                    sendTextTemplate(to, "Berhasil mengaktifkan check details sticker")
                            elif terminal == "checksticker off":
                              if msg._from in admin:                          
                                if settings["checkSticker"] == False:
                                    sendTextTemplate(to, "Check details sticker telah nonaktif")
                                else:
                                    settings["checkSticker"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan check details sticker")

                            elif terminal == "sticker on":
                              if msg._from in admin:                          
                                if to in settings["sticker"]:
                                    sendTextTemplate(to, "Sticker telah aktif")
                                else:
                                    if to not in settings["sticker"]:
                                        settings["sticker"].append(to)
                                    sendTextTemplate(to, "Berhasil mengaktifkan sticker")
                            elif terminal == "sticker off":
                              if msg._from in admin:                          
                                if to not in settings["sticker"]:
                                    sendTextTemplate(to, "Sticker telah nonaktif")
                                else:
                                    if to in settings["sticker"]:
                                        settings["sticker"].remove(to)
                                    sendTextTemplate(to, "Berhasil menonaktifkan sticker")

                            elif terminal == "deletefriend on":
                              if msg._from in admin:                          
                                if settings["delFriend"] == True:
                                    sendTextTemplate(to, "Send Contact !!!!")
                                else:
                                    settings["delFriend"] = True
                                    sendTextTemplate(to, "Send Contact :)")
                            elif terminal == "deletefriend off":
                              if msg._from in admin:                          
                                if settings["delFriend"] == False:
                                    sendTextTemplate(to, "Udah Ga aktif !!!")
                                else:
                                    settings["delFriend"] = False
                                    sendTextTemplate(to, "Berhasil menonaktifkan delete friend")

                            elif terminal == "autokick on":
                              if msg._from in owner or admin:                          
                                if protectGroup[to]["autoKick"] == True:
                                    sendTextTemplate(to, "Auto Kick telah aktif")
                                else:
                                    protectGroup[to]["autoKick"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan Auto Kick")
                            elif terminal == "autokick off":
                              if msg._from in owner or admin:                          
                                if protectGroup[to]["autoKick"] == False:
                                    sendTextTemplate(to, "Auto Kick telah nonaktif")
                                else:
                                    protectGroup[to]["autoKick"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan auto Kick")

                            elif 'Welcome ' in msg.text:
                              if msg._from in admin:
                                 spl = msg.text.replace('Welcome ','')
                                 if spl == 'on':
                                     if msg.to in welcome:
                                          msgs = "❂➣ Welcome Msg sudah aktif"
                                     else:
                                          welcome.append(msg.to)
                                          ginfo = client.getGroup(msg.to)
                                          msgs = "❂➣ Welcome Msg diaktifkan\n❂➣ Di Group :\n" +str(ginfo.name)
                                     sendTextTemplate(to, "❂➣ Diaktifkan\n" + msgs)
                                 elif spl == 'off':
                                       if msg.to in welcome:
                                            welcome.remove(msg.to)
                                            ginfo = client.getGroup(msg.to)
                                            msgs = "❂➣ Welcome Msg dinonaktifkan\n❂➣ Di Group :\n" +str(ginfo.name)
                                       else:
                                            msgs = "❂➣ Welcome Msg sudah tidak aktif"
                                       sendTextTemplate(to, "Dinonaktifkan\n" + msgs)

#==================================================================================================================================
                            elif terminal.startswith("setautoaddchat: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoAddMessage"] = txt
                                    client.sendMessage(to, "Berhasil mengubah pesan auto add menjadi : 「{}」".format(txt))
                                except:
                                    client.sendMessage(to, "Gagal mengubah pesan auto add")

                            elif terminal.startswith("setautoresponchat: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoResponMessage"] = txt
                                    client.sendMessage(to, "Berhasil mengubah pesan auto respon menjadi : 「{}」".format(txt))
                                except:
                                    client.sendMessage(to, "Gagal mengubah pesan auto respon")

                            elif terminal.startswith("setautojoinchat: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoJoinMessage"] = txt
                                    client.sendMessage(to, "Berhasil mengubah pesan auto join menjadi : 「{}」".format(txt))
                                except:
                                    client.sendMessage(to, "Gagal mengubah pesan auto join")

                            elif terminal.startswith("setautojoingroup: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = int(sep[1])
                                try:
                                    settings["memberCancel"]["members"] = txt
                                    client.sendMessage(to, "Succesfully set auto join group if mem {}".format(txt))
                                except:
                                    client.sendMessage(to, "Gagal mengubah auto join group")

                            elif terminal.startswith("setautoanswerchat: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["autoAnswerMessage"] = txt
                                    client.sendMessage(to, "Berhasil mengubah pesan auto answer menjadi : 「{}」".format(txt))
                                except:
                                    client.sendMessage(to, "Gagal mengubah pesan auto answer")

                            elif terminal.startswith("setcomment: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                try:
                                    settings["commentPost"] = txt
                                    client.sendMessage(to, "Succes\nComment : 「{}」".format(txt))
                                except:
                                    client.sendMessage(to, "Failed")
                            elif terminal.startswith("addsettings to "):
                              if sender in owner:
                                txt = removeCmd("addsettings to", text)
                                settings["{}".format(txt)] = []
                                f=codecs.open('setting.json','w','utf-8')
                                json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                client.sendReplyMessage(msg_id, to, "Succesfully add {} to settings".format(txt))

                            elif terminal.startswith("addsettings "):
                              if sender in owner:
                              	txt = removeCmd("addsettings", text)
                              	settings["{}".format(txt)] = False
                              	f=codecs.open('setting.json','w','utf-8')
                              	json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                              	client.sendReplyMessage(msg_id, to, "Succesfully add {} to settings".format(txt))

                            elif terminal.startswith("delsettings "):
                              if sender in owner:
                              	txt = removeCmd("delsettings", text)
                              	del settings["{}".format(txt)]
                              	client.sendReplyMessage(msg_id, to, "Succesfully del {} in settings".format(txt))

                            elif terminal == "myurl":
                              if msg._from in admin:
                                client.reissueUserTicket()
                                arr = client.profile.displayName + " Ticket URL : http://line.me/ti/p/" + client.getUserTicket().id
                                client.sendReplyMessage(msg_id, to, arr)

#===============================BAGIAN SPAM================================================================
                            elif terminal.startswith("spaminvmid"):
                                dan = text.split("|")
                                nam = dan[1]
                                jlh = int(dan[2])
                                tar = dan[3]
                                grr = client.groups
                                client.findAndAddContactsByMid(tar)
                                if jlh <= 101:
                                    for var in range(0,jlh):
                                        gcr = client.createGroup(nam, [tar])
                                        Thread(target=client.inviteIntoGroup,args=(gcr.id, [tar]),).start()
                                        time.sleep(2)
                                        client.leaveGroup(gcr.id)
                                    client.sendMention(to, "Succesfully Spam Invite @! to Group {}".format(gcr.name), [tar])

                            elif terminal.startswith("spaminvite"):
                                key = eval(msg.contentMetadata["MENTION"])
                                tar = key["MENTIONEES"][0]["M"]
                                dan = text.split("|")
                                nam = dan[1]
                                jlh = int(dan[2])
                                grr = client.groups
                                client.findAndAddContactsByMid(tar)
                                if jlh <= 101:
                                    for var in range(0,jlh):
                                        gcr = client.createGroup(nam, [tar])
                                        client.inviteIntoGroup(gcr.id, [tar])
                                        time.sleep(2)
                                        client.leaveGroup(gcr.id)
                                    client.sendMention(to, "Succesfully Spam Invite @! to Group {}".format(gcr.name), [tar])
                                
                            elif terminal.startswith("chatowner: "):
                                contact = client.getContact(sender)
                                sep = text.split(" ")
                                ryan = text.replace(sep[0] + " ","")
                                for own in owner:
                                    result = "@!"
                                    result += "\nSender : {}".format(contact.displayName)
                                    result += "\nPesan : {}".format(ryan)
                                    result += "\nMid : {}".format(contact.mid)
                                    client.sendReplyMessage(msg_id, to, "Succesfully send chat to Owner")
                                    client.sendMention(own, result, [sender])
                                    client.sendContact(own, sender)

                            elif terminal.startswith("invtogc"):
                                key = eval(msg.contentMetadata["MENTION"])
                                tar = key["MENTIONEES"][0]["M"]
                                dan = text.split("|")
                                grr = client.getGroupIdsJoined()
                                client.findAndAddContactsByMid(tar)
                                try:
                                    listGroup = grr[int(dan)-1]
                                    gri = client.getGroup(listGroup)
                                    client.inviteIntoGroup(gri.id, [tar])
                                    client.sendMessage(to, "Succesfully invite {} to group {}".format(tar.displayName, gri.name))
                                except Exception as e:
                                    client.sendMessage(to, str(e))

                            elif terminal.startswith('spamtag '):
                                sep = text.split(" ")
                                num = int(sep[1])                           
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        for var in range(0,num):
                                            client.sendMention(to, "@!", [ls])

                            elif terminal.startswith('spamcall '):
                                sep = text.split(" ")
                                num = int(sep[1])
                                try:                           
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            for var in range(0,num):
                                                group = client.getGroup(to)
                                                members = [ls]
                                                kunkun = client.getContact("u874a7502c02896b2edbb3445c2615d35").displayName
                                                client.acquireGroupCallRoute(to)
                                                client.inviteIntoGroupCall(to, contactIds=members)
                                            client.sendMention(to, "Succesfully Spamcall to @!", [ls])
                                except Exception as error:
                                    client.sendMessage(to, str(error))

          
                            elif terminal.startswith("spamchat"):
                              if sender in owner:
                                text = text.split("-")
                                jmlh = int(text[2])
                                balon = jmlh * (text[3]+"\n")
                                if text[1] == "on":
                                    if jmlh <= 999:
                                        for x in range(jmlh):
                                            client.sendMessage(to, text[3])
                                    else:
                                        client.sendMention(to, "Sorry the amount is too much :) @!", [sender])
                                elif text[1] == "off":
                                  if jmlh <= 999:
                                    client.sendMessage(to, balon)
                                  else:
                                    client.sendMention(to, "Sorry the amount is too much :) @!", [sender])

                            elif terminal.startswith('spamgift '):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    gf = "b07c07bc-fcc1-42e1-bd56-9b821a826f4f","7f2a5559-46ef-4f27-9940-66b1365950c4","53b25d10-51a6-4c4b-8539-38c242604143","a9ed993f-a4d8-429d-abc0-2692a319afde"
                                    txt = "~Gift~"
                                    client.sendMentionWithFooter(to, txt, "Succesfully Spam gift to your pc", [sender])
                                    for var in range(0,num):
                                       contact = client.getContact(sender)
                                       client.sendGift(contact.mid, random.choice(gf), "theme")                

                            elif terminal.startswith('spamgroupcall '):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    client.sendMessage(to, "Succesfully Spam Call to Group")
                                    for var in range(0,num):
                                       group = client.getGroup(to)
                                       members = [mem.mid for mem in group.members]
                                       client.acquireGroupCallRoute(to)
                                       client.inviteIntoGroupCall(to, contactIds=members)

#================================================================================================================
                            elif terminal == "user list":
                                if owner == []:
                                   client.sendMessage(to, "User Is Empty")
                                else:
                                    client.sendMessage(to, "Wait........")
                                    user = ""
                                    user = "├≽ User List «¥"
                                    for mid in owner:
                                        user += "\n├≽ "+client.getContact(mid).displayName
                                    user += "\n├≽ Finish «¥"
                                    client.sendMessage(to, user)

                            elif terminal == "admin list":
                                if admin == []:
                                   client.sendMessage(to, "Admin Is Empty")
                                else:
                                    client.sendMessage(to, "Wait........")
                                    user = ""
                                    user = "├≽ Admin List «¥"
                                    for mid in admin:
                                        user += "\n├≽ "+client.getContact(mid).displayName
                                    user += "\n├≽» Finish ««¥"
                                    client.sendMessage(to, user)

#=======================ADD- STICKER ==================================================================================
                            elif terminal.startswith("addsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["addSticker"]["status"] = True
                                    settings["addSticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = {}
                                    f = codecs.open('sticker.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Send your stickers!")
                                else:
                                    sendTextTemplate(to, "Stickers name already in List!")                     

                            elif terminal.startswith("delsticker "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(to, "Sticker itu tidak ada dalam list")

                            elif terminal == "list sticker":
                               if msg._from in owner:
                                 no = 0
                                 ret_ = "Daftar Sticker \n\n"
                                 for sticker in stickers:
                                     no += 1
                                     ret_ += str(no) + ". " + sticker.title() + "\n"
                                 ret_ += "\nTotal {} Stickers".format(str(len(stickers)))
                                 client.sendMessageWithFooter(to, ret_)

#============================ADD STICKER TEMPLATE====================================≠
                            elif terminal.startswith("addstickertemplate "):
                              ssn = client.getContact(sender).mid
                              ssnd.append(ssn)
                              if sender in ssnd:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["addStickertemplate"]["statuss"] = True
                                    settings["addStickertemplate"]["namee"] = str(name.lower())
                                    stickerstemplate[str(name.lower())] = {}
                                    f = codecs.open('stickertemplate.json','w','utf-8')
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Send your stickers!")
                                else:
                                    sendTextTemplate(to, "Stickers name already in List!")

                            elif terminal.startswith("deletstickertemplate "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickerstemplate:
                                    del stickerstemplate[str(name.lower())]
                                    f = codecs.open("stickertemplate.json","w","utf-8")
                                    json.dump(stickerstemplate, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Berhasil menghapus sticker\n {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(to, "Sticker itu tidak ada dalam list")

                            elif terminal == "list sticker template":
                               if msg._from in owner:
                                 no = 0
                                 ret_ = "Daftar Sticker Template\n\n"
                                 for sticker in stickerstemplate:
                                     no += 1
                                     ret_ += str(no) + ". " + sticker.title() + "\n"
                                 ret_ += "\nTotal {} Stickers Template".format(str(len(stickers)))
                                 client.sendMessageWithFooter(to, ret_)

                                    

#============================================================================================
                            elif terminal.startswith("changekey"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                settings["tatan"] = "{}".format(txt)
                                client.sendReplyMessage(msg_id, to, "Succesfully Changekey with key >> {}".format(settings["tatan"]))


                            elif terminal.startswith("kick "):
                              if sender in owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.kickoutFromGroup(to, [ls])

                            elif terminal.startswith("rename: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if len(name) <= 999:
                                    profile = client.getProfile()
                                    profile.displayName = name
                                    client.updateProfile(profile)
                                    client.sendMessageWithFooter(to, "Berhasil mengubah nama menjadi : {}".format(name))
                              else:
                                  txt = ("Hmmmm gk bsa ya :(","Sorryy :(","Jgn Ubah Namaku :(")
                                  pop = random.choice(txt)
                                  client.sendMessageWithFooter(to, pop)

                            elif terminal.startswith("changebio: "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                bio = text.replace(sep[0] + " ","")
                                if len(bio) <= 500:
                                    profile = client.getProfile()
                                    profile.statusMessage = bio
                                    client.updateProfile(profile)
                                    client.sendMessageWithFooter(to, "Berhasil mengubah bio menjadi : {}".format(bio))

                            elif terminal == "people me":
                                client.sendMention(to, "@!", [sender])
                                client.sendFakeReplyContact(msg_id, to, sender)

                            elif terminal == "myprofile":
                                text = "~ Profile ~"
                                contact = client.getContact(sender)
                                cover = client.getProfileCoverURL(sender)
                                result = "╔══[ Details Profile ]"
                                result += "\n├≽ Display Name : @!"
                                result += "\n├≽ Mid : {}".format(contact.mid)
                                result += "\n├≽ Status Message : {}".format(contact.statusMessage)
                                result += "\n├≽ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                result += "\n├≽ Cover : {}".format(str(cover))
                                result += "\n╚══[ Finish ]"
                                client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                client.sendMentionWithFooter(to, text, result, [sender])

                            elif terminal == "mymid":
                                contact = client.getContact(sender)
                                client.sendMention(to, "@!: {}".format(contact.mid), [sender])

                            elif terminal == "myname":
                                contact = client.getContact(sender)
                                client.sendMention(to, "@!: {}".format(contact.displayName), [sender])

                            elif terminal == "mybio":
                                contact = client.getContact(sender)
                                client.sendMention(to, "@!: {}".format(contact.statusMessage), [sender])

                            elif terminal == "mypicture":
                                contact = client.getContact(sender)
                                client.sendReplyImageWithURL(msg_id, to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                            elif terminal == "myvideoprofile":
                                contact = client.getContact(sender)
                                if contact.videoProfile == None:
                                    return client.sendMessage(to, "Anda tidak memiliki video profile")
                                client.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                            elif terminal == "mycover":
                                cover = client.getProfileCoverURL(sender)
                                client.sendImageWithURL(to, str(cover))

                            elif terminal == "mycover url":
                                cover = client.getProfileCoverURL(sender)
                                client.sendMessage(to, str(cover))

                            elif terminal == "responsename":
                              if sender in admin:
                                group = client.getGroup(to)
                                midMembers = [contact.mid for contact in group.members]
                                for data in midMembers:
                                    client.sendMessage(to, "{}".format(client.getContact(data).displayName), contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(data).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(data).pictureStatus)})
                            elif terminal == "mybot":
                              if sender in admin:
                                group = client.getGroup(to)
                                midMembers = [contact.mid for contact in group.members]
                                no = 0
                                for data in midMembers:
                                    no += 1
                                    client.sendMessage(to, "THE PE?PLE TEAM {}".format(str(no)), contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(data).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(data).pictureStatus)})

                            elif terminal.startswith("getmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.sendMention(to, "@!: \n{}".format(ls), [ls])

                            elif terminal.startswith("getcontact "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                client.sendContact(to, txt)

                            elif terminal.startswith("getidline "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        checkticket = client.getContact(ls).userid
                                        client.sendMention(to, "@!: {}".format(checkticket), [ls])

                            elif terminal.startswith("getname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMention(to, "@!: {}".format(contact.displayName), [ls])

                            elif terminal.startswith("getbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendMention(to, "@!: {}".format(contact.statusMessage), [ls])

                            elif terminal.startswith("getpicture "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))

                            elif terminal.startswith("getvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = client.getContact(ls)
                                        if contact.videoProfile == None:
                                            return client.sendMention(to, "@!tidak memiliki video profile", [ls])
                                        client.sendVideoWithURL(to, "http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))

                            elif terminal.startswith("getcover "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        cover = client.getProfileCoverURL(ls)
                                        client.sendImageWithURL(to, str(cover))

                            elif terminal.startswith("cloneprofile "):
                              if msg._from in owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.cloneContactProfile(ls)
                                        client.sendContact(to, sender)
                                        client.sendMessage(to, "Berhasil clone profile")

                            elif terminal == "invite to group":
                              if msg._from in owner:
                                if settings["groupInvite"] == True:
                                    client.sendMessage(to, "Kirim Kontaknya :)")
                                else:
                                    settings["groupInvite"] = True
                                    client.sendMessage(to, "Send Contact :)")

                            elif terminal == "friendlist":
                              if msg._from in owner:
                                contacts = client.getAllContactIds()
                                num = 0
                                result = "╔══[ Friend List ]"
                                for listContact in contacts:
                                    contact = client.getContact(listContact)
                                    num += 1
                                    result += "\n├≽ {}. {}".format(num, contact.displayName)
                                result += "\n╚══[ Total {} Friend ]".format(len(contacts))
                                client.sendReplyMessage(msg_id, to, result)

                            elif terminal.startswith("friendinfo "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                contacts = client.getAllContactIds()
                                try:
                                    listContact = contacts[int(query)-1]
                                    contact = client.getContact(listContact)
                                    cover = client.getProfileCoverURL(listContact)
                                    result = "├≽» Details Profile ««¥"
                                    result += "\n├≽ Display Name : @!"
                                    result += "\n├≽ Mid : {}".format(contact.mid)
                                    result += "\n├≽ Status Message : {}".format(contact.statusMessage)
                                    result += "\n├≽ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                    result += "\n├≽ Cover : {}".format(str(cover))
                                    result += "\n├≽» Finish ««¥"
                                    client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                    client.sendMention(to, result, [contact.mid])
                                except Exception as error:
                                    logError(error)

                            elif terminal.startswith("delfriendmid "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                client.deleteContact(txt)
                                client.sendFakeMessage(to, "Done Boskuh",txt)

                            elif terminal.startswith("delfriend "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.deleteContact(ls)
                                        client.sendReplyMessage(msg_id, to, "Udah euy")

                            elif terminal.startswith("addfavorite "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.addFavorite(ls)
                                        client.sendReplyMention(msg_id, to, "Succesfully add @! to Favorite Friend", [ls])

                            elif terminal.startswith("rename "):
                                sep = text.split(" ")
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        client.renameContact(ls,sep[1])
                                        client.sendReplyMention(msg_id, to, "Succesfully change @! display name to {}".format(sep[1]), [ls])

                            elif terminal == "blocklist":
                              if msg._from in owner:
                                blockeds = client.getBlockedContactIds()
                                num = 0
                                result = "├≽» List Blocked ««¥"
                                for listBlocked in blockeds:
                                    contact = client.getContact(listBlocked)
                                    num += 1
                                    result += "\n├≽ {}. {}".format(num, contact.displayName)
                                result += "\n├≽ Total {} Blocked ]".format(len(blockeds))
                                client.sendMessage(to, result)

                            elif terminal.startswith("changegroupname: "):
                                if msg.toType == 2:
                                    sep = text.split(" ")
                                    groupname = text.replace(sep[0] + " ","")
                                    if len(groupname) <= 100:
                                        group = client.getGroup(to)
                                        group.name = groupname
                                        client.updateGroup(group)
                                        client.sendMessage(to, "Berhasil mengubah nama group menjadi : {}".format(groupname))

                            elif terminal.startswith("no"):
                                sep = text.split("|")
                                nom = sep[1]
                                nam = sep[2]
                                client.sendContactHP(to, "Kntlll", nom, nam)
                            elif terminal == "foot":
                                con = {'AGENT_ICON': 'http://profile.line-cdn.net/0hcr26oFItPF0PTxGrOrtDCjMKMjB4YToVdyx1MypOZmR1LXMPMiF2b31GMD5xfSgPZCogOC1GZmwq', 'AGENT_NAME': 'Runtime', 'AGENT_LINK': 'line://app/1600328768-y3yq64nw/?type=text&text=runtime'}
                                client.sendMessage(to, "LKJ", con, 0)

                            elif terminal == "grouppicture":
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    groupPicture = "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus)
                                    client.sendImageWithURL(to, groupPicture)

                            elif terminal == "all mid":
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    num = 0
                                    ret_ = "╭───「 Mid List On Group {} 」".format(group.name)
                                    for contact in group.members:
                                        num += 1
                                        ret_ += "\n├≽ {}.{}\n├{}".format(num, contact.displayName, contact.mid)
                                    ret_ += "\n╰───「 Total {} Members 」".format(len(group.members))
                                    client.sendReplyMessage(msg_id, to, ret_)

                            elif terminal == "pendinglist":
                                if msg.toType == 2:
                                    group = client.getGroup(to)
                                    ret_ = "╭───「 Pending List 」"
                                    no = 0
                                    if group.invitee is None or group.invitee == []:
                                        return client.sendReplyMessage(msg_id, to, "Tidak ada pendingan")
                                    else:
                                        for pending in group.invitee:
                                            no += 1
                                            ret_ += "\n├≽ {}. {}".format(str(no), str(pending.displayName))
                                        ret_ += "\n╰───「 Total {} Pending 」".format(str(len(group.invitee)))
                                        client.sendReplyMessage(msg_id, to, str(ret_))

                        ## Remote
                            elif terminal.startswith("leavegc "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    client.leaveGroup(group.id)
                                    client.sendMessage(to, "Succesfully leave to Group {}".format(group.name))
                                except Exception as error:
                                    logError(error)

                            elif terminal.startswith("sendcrashtogc "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    client.sendContact(group.id, "u73629292,'")
                                    client.sendMessage(to, "Succesfully send Crash to Group {}".format(group.name))
                                except Exception as error:
                                    logError(error)

                            elif terminal.startswith("invitetogc "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    client.inviteIntoGroup(group.id, [sender])
                                    client.sendMention(to, "Succesfully invite @! to Group {}".format(group.name), [sender])
                                except Exception as error:
                                    logError(error)

                            elif terminal.startswith("mutebotingc "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    if group not in offbot:
                                      client.sendMessageWithFooter(to, "Berhasil Mure Bot Di Group {}".format(group.name))
                                      offbot.append(group.id)
                                      print(group.id)
                                    else:
                                      client.sendMessageWithFooter(to, "Failed Mute Bot In Group {}".format(group.name))
                                except Exception as error:
                                    logError(error)

                            elif terminal.startswith("unmutebotingc "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                listGroup = groups[int(query)-1]
                                group = client.getGroup(listGroup)
                                if group.id in offbot:
                                    offbot.remove(group.id)
                                    client.sendMessageWithFooter(to, "Berhasil Unmute Bot Di Group {}".format(group.name))
                                    print(group.id)
                                else:
                                    client.sendMessageWithFooter(to, "Failed Unmute Bot In Group {}".format(group.name))

                            elif terminal.startswith("chattogc"):
                              if sender in owner:
                                dan = text.split("-")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(dan[1])-1]
                                    group = client.getGroup(listGroup)
                                    client.sendMessage(group.id, dan[2])
                                except:
                                    pass

                            elif terminal.startswith("chattofr"):
                              if sender in owner:
                                dan = text.split("-")
                                frs = client.getAllContactIds()
                                try:
                                    listFriend = frs[int(dan[1])-1]
                                    friend = client.getContact(listFriend)
                                    client.sendMessage(friend.mid, dan[2])
                                except:
                                    pass

                            elif terminal.startswith("sendgifttogc "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                groups = client.getGroupIdsJoined()
                                try:
                                    listGroup = groups[int(query)-1]
                                    group = client.getGroup(listGroup)
                                    gf = "b07c07bc-fcc1-42e1-bd56-9b821a826f4f","7f2a5559-46ef-4f27-9940-66b1365950c4","53b25d10-51a6-4c4b-8539-38c242604143","a9ed993f-a4d8-429d-abc0-2692a319afde"
                                    client.sendGift(group.id, random.choice(gf), "theme")
                                    txt = "~Gift~"
                                    client.sendMentionWithFooter(to, txt, "Succesfully send gift to Group {} :)".format(group.name), [sender])
                                except:
                                    pass
                            elif terminal == "checkme":
                              client.sendMessage(to, "waiting...")
                              if sender in owner:
                                contact = client.getContact(sender)
                                cover = client.getProfileCoverURL(sender)
                                result = "╔══[ Check Profile ]"
                                result += "\n├≽ Display Name : @!"
                                result += "\n├≽ Mid : {}".format(contact.mid)
                                result += "\n├≽ Status Profile"
                                result += "\n├≽ Whitelist : True"
                                result += "\n├≽ Blacklist : False"
                                result += "\n╚══[ Finish ]"
                                client.sendMention(to, result, [sender])
                              elif sender in settings["blackList"]:
                                contact = client.getContact(sender)
                                cover = client.getProfileCoverURL(sender)
                                result = "╔══[ Check Profile ]"
                                result += "\n├≽ Display Name : @!"
                                result += "\n├≽ Mid : {}".format(contact.mid)
                                result += "\n├≽ Status Profile"
                                result += "\n├≽ Whitelist : False"
                                result += "\n├≽ Blacklist : True"
                                result += "\n╚══[ Finish ]"
                                client.sendMention(to, result, [sender])
                              else:
                                contact = client.getContact(sender)
                                cover = client.getProfileCoverURL(sender)
                                result = "╔══[ Check Profile ]"
                                result += "\n├≽ Display Name : @!"
                                result += "\n├≽ Mid : {}".format(contact.mid)
                                result += "\n├≽ Status Profile"
                                result += "\n├≽ Whitelist : False"
                                result += "\n├≽ Blacklist : False"
                                result += "\n╚══[ Finish ]"
                                client.sendMention(to, result, [sender])

                            elif terminal.startswith("get note"):
                                data = client.getGroupPost(to)
                                try:
                                    music = data['result']['feeds'][int(text.split(' ')[2]) - 1]
                                    b = [music['post']['userInfo']['writerMid']]
                                    try:
                                        for a in music['post']['contents']['textMeta']:b.append(a['mid'])
                                    except:pass
                                    try:
                                        g= "\n\nDescription:\n"+str(music['post']['contents']['text'].replace('@','@!'))
                                    except:
                                        g=""
                                    a="\n   Total Like: "+str(music['post']['postInfo']['likeCount'])
                                    a +="\n   Total Comment: "+str(music['post']['postInfo']['commentCount'])
                                    gtime = music['post']['postInfo']['createdTime']
                                    a +="\n   Created at: "+str(humanize.naturaltime(datetime.fromtimestamp(gtime/1000)))
                                    a += g
                                    zx = ""
                                    zxc = " 「 Groups 」\nType: Get Note\n   Penulis : "+a
                                    try:
                                        client.sendReplyMessage(msg_id, to, zxc)
                                    except Exception as e:
                                        client.sendMessage(to, str(e))
                                    try:
                                        for c in music['post']['contents']['media']:
                                            params = {'userMid': client.getProfile().mid, 'oid': c['objectId']}
                                            path = client.server.urlEncode(client.server.LINE_OBS_DOMAIN, '/myhome/h/download.nhn', params)
                                            if 'PHOTO' in c['type']:
                                                try:
                                                    client.sendImageWithURL(to,path,'POST')
                                                except:pass
                                            else:
                                                pass
                                            if 'VIDEO' in c['type']:
                                                try:
                                                    client.sendVideoWithURL(to,path)
                                                except:pass
                                            else:
                                                pass
                                    except:
                                        pass
                                except Exception as e:
                                    return sendTextTemplate(to,"「 Auto Respond 」\n"+str(e))

                            elif terminal == "groupinfo":
                                group = client.getGroup(to)
                                try:
                                    try:
                                        groupCreator = group.creator.mid
                                    except:
                                        groupCreator = "Tidak ditemukan"
                                    if group.invitee is None:
                                        groupPending = "0"
                                    else:
                                        groupPending = str(len(group.invitee))
                                    if group.preventedJoinByTicket == True:
                                        groupQr = "Tertutup"
                                        groupTicket = "Tidak ada"
                                    else:
                                        groupQr = "Terbuka"
                                        groupTicket = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(group.id)))
                                    ret_ = "╔══[ Group Information ]"
                                    ret_ += "\n├≽ Nama Group : {}".format(group.name)
                                    ret_ += "\n├≽ ID Group : {}".format(group.id)
                                    ret_ += "\n├≽ Pembuat : @!"
                                    ret_ += "\n├≽ Jumlah Member : {}".format(str(len(group.members)))
                                    ret_ += "\n├≽ Jumlah Pending : {}".format(groupPending)
                                    ret_ += "\n├≽ Group Qr : {}".format(groupQr)
                                    ret_ += "\n├≽ Group Ticket : {}".format(groupTicket)
                                    ret_ += "\n╚══[ Success ]"
                                    client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus))
                                    client.sendMention(to, str(ret_), [groupCreator])
                                except:
                                    ret_ = "╔══[ Group Information ]"
                                    ret_ += "\n├≽ Nama Group : {}".format(group.name)
                                    ret_ += "\n├≽ ID Group : {}".format(group.id)
                                    ret_ += "\n├≽ Pembuat : {}".format(groupCreator)
                                    ret_ += "\n├≽ Jumlah Member : {}".format(str(len(group.members)))
                                    ret_ += "\n├≽ Jumlah Pending : {}".format(groupPending)
                                    ret_ += "\n├≽ Group Qr : {}".format(groupQr)
                                    ret_ += "\n├≽ Group Ticket : {}".format(groupTicket)
                                    ret_ += "\n╚══[ Success ]"
                                    client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus))
                                
                            elif terminal.startswith("groupvideocall "):
                              if msg._from in owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                num = int(txt)
                                client.sendMessage(to, "Berhasil Invite Ke Dalam VideoCall Group :)")
                                for anu in range(0,num):
                                    group = client.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    client.inviteIntoGroupVideoCall(to, contactIds=members)

                            elif terminal in ('mentionall','tag all','oi kalian'):
                                try:group = client.getGroup(to);midMembers = [contact.mid for contact in group.members]
                                except:group = client.getRoom(to);midMembers = [contact.mid for contact in group.contacts]
                                midSelect = len(midMembers)//20
                                for mentionMembers in range(midSelect+1):
                                    no = 0
                                    ret_ = "╭───「 Mention Members 」"
                                    dataMid = []
                                    if msg.toType == 2:
                                        for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"├≽ {}. @!".format(str(no))
                                        ret_ += "\n╰───「 Total {} Members 」".format(str(len(dataMid)))
                                        client.sendReplyMention(msg_id, to, ret_, dataMid)
                                    else:
                                        for dataMention in group.contacts[mentionMembers*20 : (mentionMembers+1)*20]:
                                            dataMid.append(dataMention.mid)
                                            no += 1
                                            ret_ += "\n"+"├≽ {}. @!".format(str(no))
                                        ret_ += "\n╰───「 Total {} Members 」".format(str(len(dataMid)))
                                        client.sendReplyMention(msg_id, to, ret_, dataMid)

                            elif terminal == "sider on":
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate2(to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                            elif terminal == "sider off":
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate2(to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sendTextTemplate2(to, "Sudak tidak aktif")

                            elif terminal == "lurking on":
                              if msg._from in owner or admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if to in read['readPoint']:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    read['readPoint'][to] = msg_id
                                    read['readMember'][to] = []
                                    sendTextTemplate(to, "Lurking telah diaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    read['readPoint'][to] = msg_id
                                    read['readMember'][to] = []
                                    sendTextTemplate(to, "Set reading point : \n{}".format(readTime))
                            elif terminal == "lurking off":
                              if msg._from in owner or admin:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if to not in read['readPoint']:
                                    sendTextTemplate(to,"Lurking telah dinonaktifkan")
                                else:
                                    try:
                                        del read['readPoint'][to]
                                        del read['readMember'][to]
                                    except:
                                        pass
                                    sendTextTemplate(to, "Delete reading point : \n{}".format(readTime))
                            elif "lurking" in msg.text.lower():
                              if msg._from in owner or admin:
                                if to in read['readPoint']:
                                    if read["readMember"][to] == []:
                                        return client.sendMessage(to, "Tidak Ada Sider")
                                    else:
                                        no = 0
                                        result = "╔══[ Reader ]"
                                        for dataRead in read["readMember"][to]:
                                            no += 1
                                            result += "\n├≽ {}. @!".format(str(no))
                                        result += "\n╚══[ Total {} Sider ]".format(str(len(read["readMember"][to])))
                                        sendTextTemplate(to, result, read["readMember"][to])
                                        read['readMember'][to] = []

                            elif terminal == "clonecontact":
                              if msg._from in owner:
                                settings["cloneContact"] = True
                                client.sendMessageWithFooter(to, "Silahkan Kirim Contactnya :)")
                            elif terminal == "clone contact off":
                                if settings["cloneContact"] == False:
                                    client.sendMessage(to, "Clone Contact Has been Aborted")
                                else:
                                    settings["cloneContact"] = False
                                    client.sendMessage(to, "Succesfully Aborted \n\nClone Contact Profile")

                            elif terminal == "changedual":
                                settings["changeDual"] = True
                                client.sendMessage(to, "Send Vidd :)")

                            elif terminal == "allcvp off":
                              if sender in owner:
                                if settings["allchangedual"] == False:
                                    client.sendMessage(to, "CVP Has Been Aborted")
                                else:
                                    settings["allchangedual"] = False
                                    client.sendMessage(to, "Succesfully Aborted \n\nChange Video & Picture")

                            elif terminal == "cvp off":
                                if settings["changeDual"] == False:
                                    client.sendMessage(to, "CVP Has Been Aborted")
                                else:
                                    settings["changeDual"] = False
                                    client.sendMessage(to, "Succesfully Aborted \n\nChange Video & Picture")

                            elif terminal == "changepict":
                              if msg._from in owner:
                                settings["changePictureProfile"] = True
                                client.sendMessage(to, "Silahkan kirim gambarnya")

                            elif terminal == "changecover":
                              if sender in owner:
                                settings["changeCover"] = True
                                client.sendMessage(to, "Send Pict :)")

                            elif terminal == "changevp":
                              if msg._from in owner:
                                settings["changeVpProfile"] = True
                                client.sendMessage(to, "Silahkan kirim Videonya")

                            elif terminal == "changegrouppicture":
                                if msg.toType == 2:
                                    if to not in settings["changeGroupPicture"]:
                                        settings["changeGroupPicture"].append(to)
                                    client.sendMessage(to, "Silahkan kirim gambarnya")
                            elif terminal == "mimic on":
                                if settings["mimic"]["status"] == True:
                                    client.sendMessage(to, "Reply message telah aktif")
                                else:
                                    settings["mimic"]["status"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan reply message")
                            elif terminal == "mimic off":
                              if msg._from in owner:
                                if settings["mimic"]["status"] == False:
                                    client.sendMessage(to, "Reply message telah nonaktif")
                                else:
                                    settings["mimic"]["status"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan reply message")
                            elif terminal == "mimiclist":
                              if msg._from in owner:
                                if settings["mimic"]["target"] == {}:
                                    client.sendMessage(to, "Tidak Ada Target")
                                else:
                                    no = 0
                                    result = "╔══[ Mimic List ]"
                                    target = []
                                    for mid in settings["mimic"]["target"]:
                                        target.append(mid)
                                        no += 1
                                        result += "\n├≽ {}. @!".format(no)
                                    result += "\n╚══[ Total {} Mimic ]".format(str(len(target)))
                                    client.sendMention(to, result, target)
                            elif terminal.startswith("mimicadd "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            if ls in settings["mimic"]["target"]:
                                                client.sendMessage(to, "Target sudah ada dalam list")
                                            else:
                                                settings["mimic"]["target"][ls] = True
                                                client.sendMessage(to, "Berhasil menambahkan target")
                                        except:
                                            client.sendMessage(to, "Gagal menambahkan target")
                            elif terminal.startswith("mimicdel "):
                              if msg._from in owner:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        try:
                                            if ls not in settings["mimic"]["target"]:
                                                client.sendMessage(to, "Target sudah tida didalam list")
                                            else:
                                                del settings["mimic"]["target"][ls]
                                                client.sendMessage(to, "Berhasil menghapus target")
                                        except:
                                            client.sendMessage(to, "Gagal menghapus target")

                            elif terminal.startswith("praytime "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0]+ " ","")
                                url = requests.get("https://time.siswadi.com/pray/{}".format(txt))
                                data = url.json()
                                ret_ = "╭───「 Praytime at {} 」".format(txt)
                                ret_ += "\n├≽ Date : {}".format(data["time"]["date"])
                                ret_ += "\n├≽ Subuh : {}".format(data["data"]["Fajr"])
                                ret_ += "\n├≽ Dzuhur : {}".format(data["data"]["Dhuhr"])
                                ret_ += "\n├≽ Ashar : {}".format(data["data"]["Asr"])
                                ret_ += "\n├≽ Magrib : {}".format(data["data"]["Maghrib"])
                                ret_ += "\n├≽ Isha : {}".format(data["data"]["Isha"])
                                ret_ += "\n├≽ 1/3 Malam : {}".format(data["data"]["SepertigaMalam"])
                                ret_ += "\n├≽ Tengah Malam : {}".format(data["data"]["TengahMalam"])
                                ret_ += "\n├≽ 2/3 Malam : {}".format(data["data"]["DuapertigaMalam"])
                                ret_ += "\n├≽ 「 Always Remember to Your God :) 」"
                                ret_ += "\n╰───「 {} 」".format(txt)
                                client.sendMessageWithFooter(to, str(ret_))
                                address = ''.format(data["location"]["address"])
                                latitude = float(data["location"]["latitude"])
                                longitude = float(data["location"]["longitude"])
                                client.sendLocation(to, address,latitude,longitude)


                            elif terminal.startswith("acaratv "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/acaratv.php?id={}&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba&type=separate".format(txt))
                                data = url.json()
                                no = 0
                                result = "╔══[ ~ Acara TV ~ ]"
                                for anu in data:
                                    no += 1
                                    result += "\n├≽ {}. {} >>> {} ".format(str(no),str(anu["acara"]),str(anu["jam"]))
                                result += "\n╚══[ ~ Acara TV ~ ]"
                                client.sendMessageWithFooter(to, result)

                            elif terminal.startswith("zodiak "):
                              if msg._from in owner:
                                sep = msg.text.split(" ")
                                query = text.replace(sep[0] + " ","")
                                r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                                data = r.text
                                data = json.loads(data)
                                data1 = data["description"]
                                data2 = data["color"]
                                translator = Translator()
                                hasil = translator.translate(data1, dest='id')
                                hasil1 = translator.translate(data2, dest='id')
                                A = hasil.text
                                B = hasil1.text
                                ret_ = "🍀 Ramalan zodiak {} hari ini 🍀\n".format(str(query))
                                ret_ += str(A)
                                ret_ += "\n======================\n🍀 Tanggal : " +str(data["current_date"])
                                ret_ += "\n🍀 Rasi bintang : "+query
                                ret_ += " ("+str(data["date_range"]+")")
                                ret_ += "\n🍀 Pasangan Zodiak : " +str(data["compatibility"])
                                ret_ += "\n🍀 Angka keberuntungan : " +str(data["lucky_number"])
                                ret_ += "\n🍀 Waktu keberuntungan : " +str(data["lucky_time"])
                                ret_ += "\n🍀 Warna kesukaan : " +str(B)
                                client.sendMessage(to, str(ret_))


                            elif terminal.startswith("samehadaku "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/samehadaku.php?id={}&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba".format(txt))
                                data = url.json()
                                no = 0
                                result = "╔══[ ~ Samehadaku ~ ]"
                                for anu in data:
                                    no += 1
                                    result += "\n├≽ {}. {}".format(str(no),str(anu["title"]))
                                    result += "\n├≽ {}".format(str(anu["url"]))
                                    result += "\n├≽ {}".format(str(anu["date"]))
                                result += "\n╚══[ {} Anime ]".format(str(len(data)))
                                client.sendMessageWithFooter(to, result)
                             
                            elif terminal.startswith("mtoh "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.aladhan.com/v1/gToH?date={}".format(txt))
                                data = url.json()
                                result = "~ Hijriah ~ = {}".format(str(data["data"]["hijri"]["date"]))
                                result += "\n~ Masehi ~ = {}".format(str(data["data"]["gregorian"]["date"]))
                                client.sendMessageWithFooter(to, result)

                            elif terminal.startswith("asmaulhusna"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.aladhan.com/asmaAlHusna/{}".format(txt))
                                data = url.json()
                                result = "~ Asma Allah ke {} = ~ {} ~".format(txt,data["data"][0]["name"])
                                result += "\n~Artinya =~ {} ~".format(data["data"][0]["en"]["meaning"])
                                client.sendMessageWithFooter(to, result)

                            elif terminal.startswith("al-qur'an"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                web = requests.get("http://api.alquran.cloud/surah/{}".format(txt))
                                data = web.json()
                                result = "~[~{}~]~".format(data["data"]["englishName"])
                                quran = data["data"]
                                result += "\n~ Surah ke {} ~".format(quran["number"])
                                result += "\n~ Nama Surah ~ {} ~".format(quran["name"])
                                result += "\n~ {} Ayat ~".format(quran["numberOfAyahs"])
                                result += "\n~ {} ~".format(quran["name"])
                                result += "\n~ Ayat Sajadah = {} ~".format(quran["ayahs"][0]["sajda"])
                                result += "\n==================\n"
                                no = 0
                                for ayat in data["data"]["ayahs"]:
                                    no += 1
                                    result += "\n{}. {}".format(no,ayat['text'])
                                k = len(result)//10000
                                for aa in range(k+1):
                                    sendTextTemplate(to,'{}'.format(result[aa*10000 : (aa+1)*10000]))

                            elif terminal.startswith("murrotal"):
                                try:
                                    sep = text.split(" ")
                                    txt = int(text.replace(sep[0] + " ",""))
                                    if 0 < txt < 115:
                                        if txt not in [2,3,4,5,6,7,9,10,11,12,16,17,18,20,21,23,26,37]:
                                            if len(str(txt)) == 1:
                                                audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(txt) + "-muslimcentral.com.mp3"
                                                client.sendAudioWithURL(to, audionya)
                                            elif len(str(txt)) == 2:
                                                audionya =  "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(txt) + "-muslimcentral.com.mp3"
                                                client.sendAudioWithURL(to, audionya)
                                            else:
                                                audionya =  "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(txt) + "-muslimcentral.com.mp3"
                                                client.sendAudioWithURL(to, audionya)
                                        else:
                                            client.sendMessage(to, "The Surah is too long")
                                    else:
                                        client.sendMessage(to, "Holy Qur'an Only have 114 surah :)")
                                except Exception as error:
                                    client.sendMessage(to, "error\n"+str(error))
                                    logError(error)

                            elif terminal == "ayat sajadah":
                                url = requests.get("http://api.alquran.cloud/sajda/quran-uthmani")
                                data = url.json()
                                result = "~[Ayat Sajadah]~"
                                for ayat in data["data"]["ayahs"]:
                                    ayatnya = ayat["text"]
                                    result += "\n{}".format(ayatnya)
                                    result += "\n Surah {}".format(ayat["surah"]["englishName"])
                                result += "\n ~~~~~~ Juz {} ~~~~~~".format(ayat["juz"])
                                sendTextTemplate(to, result)

                            elif terminal == "pulsk":                                
                                r = requests.get("https://farzain.com/api/pulsk.php?apikey=oQ61nCJ2YBIP1qH25ry6cw2ba")
                                data=r.text
                                data=json.loads(data)
                                if data != []:    
                                    no = 0
                                    hasil = "[ Pulsk Result ]"
                                    for sam in data:                                     
                                        no += 1                  
                                        hasil += "\n" + str(no) + ". " + str(sam["title"])+"\n"+ str(sam["link"])+"\n"+ str(sam["views"])+"\n"+ str(sam["share"])
                                    client.sendMessageWithFooter(to, str(hasil))

                            elif terminal.startswith("listmeme"):
                              if msg._from in owner:
                                proses = text.split(" ")
                                keyword = text.replace(proses[0] + " ","")
                                count = keyword.split("|")
                                search = str(count[0])
                                r = requests.get("http://api.imgflip.com/get_memes")
                                data = json.loads(r.text)
                                if len(count) == 1:
                                    no = 0
                                    hasil = "🍀 Daftar Meme Image 🍀\n"
                                    for aa in data["data"]["memes"]:
                                        no += 1
                                        hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                    hasil += " "
                                    client.sendMessage(to,hasil)
                                    client.sendMention(to, "\nJika ingin menggunakan, \nSilahkan ketik:\n\n🍀 Listmeme | urutan\n🍀 Meme text1 | text2 | urutan", [sender])
                                if len(count) == 2:
                                    try:
                                        num = int(count[1])
                                        gambar = data["data"]["memes"][num - 1]
                                        hasil = "{}".format(str(gambar["name"]))
                                        client.sendMention(to, "🍀 Meme Image 🍀\nTunggu \nFoto sedang diproses...", [sender])
                                        client.sendMessage(to, hasil)
                                        client.sendImageWithURL(to, gambar["url"])
                                    except Exception as e:
                                        client.sendMessage(to," "+str(e))
                            elif terminal.startswith("meme "):  
                                if msg._from in owner:
                                    code = msg.text.split(" ")
                                    txt = msg.text.replace(code[0] + "/" + " ","")
                                    txt2 = msg.text.replace(txt[0] + "/" + " ","")
                                    naena = "https://api.imgflip.com/"+txt2+".jpg"
                                    try:
                                         start = time.time()
                                         client.sendMessage(to,"🍀Meme Image🍀\nType : Meme Image\nTime taken : %s seconds" % (start))
                                         client.sendImageWithURL(to, naena)
                                    except Exception as error:
                                         sendTextTemplate(to, str(error))

                            elif terminal.startswith("ssweb "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = "https://api.site-shot.com//?url={}&width=1280&height=2080&5ba006ea23010.jpg".format(txt)
                                Thread(target=client.sendImageWithURL,args=(to, url,)).start()

                            elif terminal.startswith("linedownload "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                client.sendImageWithURL(to, txt)
                                client.sendVideoWithURL(to, txt)

                            elif terminal.startswith("linepost "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://farzain.com/api/special/line.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                client.sendImageWithURL(to, data["result"])
                                client.sendVideoWithURL(to, data["result"])
                            elif terminal.startswith("newalbum "):
                            	txt = removeCmd("newalbum", text)
                            	url = requests.get("http://api-jooxtt.sanook.com/web-fcgi-bin/web_search?country=id&lang=en&search_input={}&sin=0&ein=30".format(txt))
                            	data = url.json()
                            	urlv = requests.get("http://api-jooxtt.sanook.com/web-fcgi-bin/web_album_singer?country=id&lang=en&cmd=1&sin=0&ein=2&singerid={}".format(data["itemlist"][0]["singerid"]))
                            	datav = url.json()
                            	tex = "╭───「 New Album 」"
                            	tex += "\n├≽ Name : {}".format(urlDecode(datav["name"]))
                            	tex += "\n├≽ Song : {}".format(datav["songnum"])
                            	tex += "\n├≽ Album: {}".format(datav["albumnum"])
                            	tex += "\n╰───「 {} 」".format(urlDecode(datav["name"]))
                            	client.sendReplyImageWithURL(msg_id, to, datav["pic"])
                            	client.sendReplyMessage(msg_id, to, tex)

                            elif terminal.startswith("tiktok"):
                            	def tiktoks():
                            		try:
		                                url = requests.get("https://rest.farzain.com/api/tiktok.php?country=jp&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba&type=json")
		                                data = url.json()
		                                client.sendVideoWithURL(to, data["first_video"])
                            		except:
		                            	client.sendMessage(to, data["result"])
                            	ryn = Thread(target=tiktoks)
                            	ryn.daemon = True
                            	ryn.start()

                            elif terminal.startswith("artinama "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://api.eater.site/api/name/?apikey=beta&name={}".format(txt))
                                data = url.json()
                                client.sendMessageWithFooter(to, str(data["result"][0]["name"]))

                            elif terminal.startswith("artimimpi "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://farzain.com/api/mimpi.php?q={}&apikey=oQ61nCJ2YBIP1qH25ry6cw2ba".format(txt))
                                data = url.json()
                                client.sendMessageWithFooter(to, str(data["result"]))

                            elif terminal.startswith("ytmp3"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                def yt():
                                    youtubeMp3(to, txt)
                                treding = Thread(target=yt)
                                treding.daemon = True
                                treding.start()

                            elif terminal.startswith("ytmp4"):
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                treding = Thread(target=youtubeMp4,args=(to,txt,))
                                treding.daemon = True
                                treding.start()

                            elif cmd.startswith("youtubesearch "):
	                            sep = text.split(" ")
	                            search = text.replace(sep[0] + " ","")
	                            params = {"search_query": search}
	                            with _session as web:
	                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
	                                r = web.get("https://www.youtube.com/results", params = params)
	                                soup = BeautifulSoup(r.content, "html5lib")
	                                ret_ =  "╭───「 Youtube Result 」"
	                                datas = []
	                                for data in soup.select(".yt-lockup-title > a[title]"):
	                                    if "&lists" not in data["href"]:
	                                        datas.append(data)
	                                for data in datas:
	                                    ret_ += "\n-≽[ {} ]".format(str(data["title"]))
	                                    ret_ += "\n-≽https://www.youtube.com{}".format(str(data["href"]))
	                                ret_ += "\n╰───「 {} 」".format(len(datas))
	                                client.sendMessage(to, str(ret_))

                            elif terminal.startswith("youtubemp4 "):
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ","")
                                    query = urllib.parse.quote(textToSearch)
                                    search_url="https://www.youtube.com/results?search_query="
                                    mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                    sb_url = search_url + query
                                    sb_get = requests.get(sb_url, headers = mozhdr)
                                    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                    x = (yt_links[1])
                                    yt_href =  x.get("href")
                                    yt_href = yt_href.replace("watch?v=", "")
                                    qx = "https://youtu.be" + str(yt_href)
                                    vid = pafy.new(qx)
                                    stream = vid.streams
                                    best = vid.getbest()
                                    best.resolution, best.extension
                                    for s in stream:
                                        me = best.url
                                        hasil = ""
                                        title = "Judul [ " + vid.title + " ]"
                                        author = '\n\n•-≽ Author : ' + str(vid.author)
                                        durasi = '\n•-≽ Duration : ' + str(vid.duration)
                                        suka = '\n•-≽ Likes : ' + str(vid.likes)
                                        rating = '\n•-≽ Rating : ' + str(vid.rating)
                                        deskripsi = '\n•-≽ Deskripsi : ' + str(vid.description)
                                    client.sendVideoWithURL(msg.to, me)
                                    client.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                                except Exception as e:
                                    client.sendMessage(msg.to,str(e))

                            elif terminal.startswith("youtubemp3 "):
                                try:
                                    sep = msg.text.split(" ")
                                    textToSearch = msg.text.replace(sep[0] + " ","")
                                    query = urllib.parse.quote(textToSearch)
                                    search_url="https://www.youtube.com/results?search_query="
                                    mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                    sb_url = search_url + query
                                    sb_get = requests.get(sb_url, headers = mozhdr)
                                    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                    x = (yt_links[1])
                                    yt_href =  x.get("href")
                                    yt_href = yt_href.replace("watch?v=", "")
                                    qx = "https://youtu.be" + str(yt_href)
                                    vid = pafy.new(qx)
                                    stream = vid.streams
                                    bestaudio = vid.getbestaudio()
                                    bestaudio.bitrate
                                    best = vid.getbest()
                                    best.resolution, best.extension
                                    for s in stream:
                                        shi = bestaudio.url
                                        me = best.url
                                        vin = s.url
                                        hasil = ""
                                        title = "Judul [ " + vid.title + " ]"
                                        author = '\n\n❂⊱• Author : ' + str(vid.author)
                                        durasi = '\n❂⊱• Duration : ' + str(vid.duration)
                                        suka = '\n❂⊱• Likes : ' + str(vid.likes)
                                        rating = '\n❂⊱• Rating : ' + str(vid.rating)
                                        deskripsi = '\n❂⊱• Deskripsi : ' + str(vid.description)
                                    client.sendImageWithURL(to, me)
                                    client.sendAudioWithURL(to, shi)
                                    client.sendMessage(to,title+ author+ durasi+ suka+ rating+ deskripsi)
                                except Exception as e:
                                    client.sendMessage(to,str(e))

                            elif terminal.startswith('ssweb'):
                                sep = msg.text.split(" ")
                                nazri = msg.text.replace(sep[0] + " ","")
                                Thread(target=client.sendImageWithURL(to, 'http://api.screenshotmachine.com/?key=3ae749&dimension=1920x1080&format=jpg&url='+nazri)).start()

                            elif terminal.startswith("drakor"):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://api.eater.pw/drakor/{}".format(txt))
                                dat = url.json()
                                drk = "「{}」".format(txt)
                                num = 0
                                for dr in dat["result"]:
                                    num += 1
                                    drk += "\n{}.「Judul」 : {}".format(str(num),str(dr["judul"]))
                                    drk += "\n   「Link」  : {}".format(str(dr["link"]))
                                drk += "\nTotal 「{}」 Drakor".format(str(len(dat["result"])))
                                client.sendReplyMessage(msg_id, to, drk)

                            elif terminal.startswith("ytdl "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/yt_download.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                def sendVid():
                                    client.sendVideoWithURL(to, data["urls"][1]["id"])
                                td = Thread(target=sendVid)
                                td.daemon = True
                                td.start()

                            elif terminal.startswith("ytdownload "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/yt_download.php?id={}&apikey=ppqeuy".format(txt))
                                data = url.json()
                                data = data["urls"][1]["id"]
                                if "\/" in data:
                                	data = data.replace("\/","/")
                                else:
                                	pass
                                zzz = google_url_shorten(data)
                                client.sendMessageMusic(to, title='Youtube', url='line://app/1603138059-k9Egggar?type=video&ocu=https://{}&piu=https://ngebotantipusing.com/hmmk.jpg'.format(zzz))


                            elif terminal.startswith("youtube "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("http://api.w3hills.com/youtube/search?keyword={}&api_key=86A7FCF3-6CAF-DEB9-E214-B74BDB835B5B".format(txt))
                                data = url.json()
                                if data["videos"] != []:
                                        ret_ = []
                                        for fn in data["videos"]:
                                                if len(ret_) >= 30:
                                                    pass
                                                else:
                                                    ret_.append({
                                                              "thumbnailImageUrl": "{}".format(fn["thumbnail"]),
                                                              "imageSize": "cover",
                                                              "imageBackgroundColor": "#FF0000",
                                                              "title": "{}....".format(fn['title'][:36]),
                                                              "text": "search: Youtube",
                                                              "actions": [
                                                                  {
                                                                      "type": "uri",
                                                                      "label": "Click Me to download",
                                                                      "uri": "line://app/1603968955-ORWb9RdY/?type=text&text={}".format(urllib.parse.quote("ytdl {}".format(fn["id"])))
                                                                  }
                                                              ]
                                                        }
                                                    )
                                        k = len(ret_)//20
                                        for aa in range(k+1):
                                            data = {
                                                    "type": "template",
                                                    "altText": "Youtube",
                                                    "template": {
                                                        "type": "carousel",
                                                        "columns": ret_[aa*15 : (aa+1)*15]
                                                    }
                                                }
                                            client.postTemplate(to, data)

                            elif terminal == "testlist":
                                data = {
                                    "type": "flex",
                                    "altText": "Simisimi",
                                    "contents": {
                                        "type": "bubble",
                                        "body": {
                                            "contents": [{
                                                "contents": [{
                                                    "text": "1. sedih",
                                                    "size": "sm",
                                                    "type": "text"
                                                }, {
                                                    "url": "https://stickershop.line-scdn.net/stickershop/v1/sticker/42423/IOS/sticker.png;compress=true",
                                                    "size": "sm",
                                                    "type": "image",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://app/1600328768-y3yq64nw/?type=sticker&tstk=gg&stkid=42423&stkpkgid=2027&send=true"
                                                    }
                                                }],
                                                "layout": "horizontal",
                                                "type": "box",
                                                "flex": 1
                                            }],
                                            "layout": "vertical",
                                            "type": "box",
                                            "spacing": "md"
                                        },
                                        "header": {
                                            "contents": [{
                                                "weight": "bold",
                                                "color": "#aaaaaa",
                                                "text": "「 LIST KEYWORDZ 」",
                                                "size": "sm",
                                                "type": "text",
                                                "align": "center"
                                            }],
                                            "layout": "horizontal",
                                            "type": "box"
                                        }
                                    }
                                }
                                client.postTemplate(to, data)

                            elif terminal.startswith("searchyoutube "):
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                cond = txt.split("|")
                                search = cond[0]
                                url = requests.get("http://api.w3hills.com/youtube/search?keyword={}&api_key=86A7FCF3-6CAF-DEB9-E214-B74BDB835B5B".format(search))
                                data = url.json()
                                if len(cond) == 1:
                                    no = 0
                                    result = "╔══[ Youtube Search ]"
                                    for anu in data["videos"]:
                                        no += 1
                                        result += "\n├≽ {}. {}".format(str(no),str(anu["title"]))
                                        result += "\n├≽ {}".format(str(anu["webpage"]))
                                    result += "\n╚══[ Total {} Result ]".format(str(len(data["videos"])))
                                    client.sendMessage(to, result)
                                elif len(cond) == 2:
                                    num = int(str(cond[1]))
                                    if num <= len(data):
                                        search = data["videos"][num - 1]
                                        ret_ = "╔══[ Youtube Info ]"
                                        ret_ += "\n├≽ Channel : {}".format(str(search["publish"]["owner"]))
                                        ret_ += "\n├≽ Title : {}".format(str(search["title"]))
                                        ret_ += "\n├≽ Release : {}".format(str(search["publish"]["date"]))
                                        ret_ += "\n├≽ Viewers : {}".format(str(search["stats"]["views"]))
                                        ret_ += "\n├≽ Likes : {}".format(str(search["stats"]["likes"]))
                                        ret_ += "\n├≽ Dislikes : {}".format(str(search["stats"]["dislikes"]))
                                        ret_ += "\n├≽ Rating : {}".format(str(search["stats"]["rating"]))
                                        ret_ += "\n├≽ Description : {}".format(str(search["description"]))
                                        ret_ += "\n╚══[ {} ]".format(str(search["webpage"]))
                                        client.sendImageWithURL(to, str(search["thumbnail"]))
                                        client.sendMessage(to, str(ret_))
                            elif terminal.startswith("searchimage "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                url = requests.get("https://rest.farzain.com/api/gambarg.php?id={}&apikey=VBbUElsjMS84rXUO7wRlIwjFm".format(txt))
                                data = url.json()
                                client.sendImageWithURL(to, data["url"])

                            elif terminal.startswith("searchlyric "):
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                cond = txt.split("|")
                                query = cond[0]
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0"
                                    url = web.get("https://www.musixmatch.com/search/{}".format(urllib.parse.quote(query)))
                                    data = BeautifulSoup(url.content, "html.parser")
                                    result = []
                                    for trackList in data.findAll("ul", {"class":"tracks list"}):
                                        for urlList in trackList.findAll("a"):
                                            title = urlList.text
                                            url = urlList["href"]
                                            result.append({"title": title, "url": url})
                                    if len(cond) == 1:
                                        ret_ = "╔══[ Musixmatch Result ]"
                                        num = 0
                                        for title in result:
                                            num += 1
                                            ret_ += "\n├≽ {}. {}".format(str(num), str(title["title"]))
                                        ret_ += "\n╚══[ Total {} Lyric ]".format(str(len(result)))
                                        ret_ += "\n\nUntuk melihat lyric, silahkan gunakan command {}SearchLyric {}|「number」".format(str(setKey), str(query))
                                        client.sendMessage(to, ret_)
                                    elif len(cond) == 2:
                                        num = int(cond[1])
                                        if num <= len(result):
                                            data = result[num - 1]
                                            with requests.session() as web:
                                                web.headers["user-agent"] = "Mozilla/5.0"
                                                url = web.get("https://www.musixmatch.com{}".format(urllib.parse.quote(data["url"])))
                                                data = BeautifulSoup(url.content, "html5lib")
                                                for lyricContent in data.findAll("p", {"class":"mxm-lyrics__content "}):
                                                    lyric = lyricContent.text
                                                    client.sendMessage(to, lyric)

                            if text.lower() == "mykey":
                                client.sendMessage(to, "Keycommand yang diset saat ini : 「{}」".format(str(settings["keyCommand"])))
                            elif text.lower() == "setkey on":
                              if msg._from in owner:
                                if settings["setKey"] == True:
                                    client.sendMessage(to, "Setkey telah aktif")
                                else:
                                    settings["setKey"] = True
                                    client.sendMessage(to, "Berhasil mengaktifkan setkey")
                            elif text.lower() == "setkey off":
                              if msg._from in owner:
                                if settings["setKey"] == False:
                                    client.sendMessage(to, "Setkey telah nonaktif")
                                else:
                                    settings["setKey"] = False
                                    client.sendMessage(to, "Berhasil menonaktifkan setkey")
                            if text is None: return

                            if "/ti/g/" in msg.text.lower():
                                if settings["autoJoinTicket"] == True:
                                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                    links = link_re.findall(text)
                                    n_links = []
                                    for l in links:
                                        if l not in n_links:
                                            n_links.append(l)
                                    for ticket_id in n_links:
                                        group = client.findGroupByTicket(ticket_id)
                                        client.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        client.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))

                        elif msg.contentType == 2:
                            if settings["changeDual"] == True:
                                def cvp():
                                    client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/cvp.mp4")
                                    client.sendMessage(to, "Send Pict :)")
                                td = Thread(target=cvp)
                                td.daemon = True
                                td.start()

                        elif msg.contentType == 1:
                            if settings["changeDual"] == True:
                                def change():
                                    pict = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changeDual"] = False
                                    client.updateVideoAndPictureProfile(pict, "LineAPI/tmp/cvp.mp4")
                                    client.sendMessage(to, "Succesfully change video & picture profile")
                                    client.deleteFile(pict)
                                    client.deleteFile("LineAPI/tmp/cvp.mp4")
                                td = Thread(target=change)
                                td.daemon = True
                                td.start()
                            if to in settings["decode"]:
                                generateLink(to, msg_id)
                            if to in settings["watercolor"] == True:
                                uploadFile(msg_id)
                                client.sendImageWithURL(to, 'http://ari-api.herokuapp.com/watercolor?type=2&rancol=on&url={}'.format(urlEncode("https://fahminogameno.life/uploadimage/images/ryngenerate.jpg")))
                            if to in settings["drawink"]:
                            	uploadFile(msg_id)
                            	client.sendImageWithURL(to, 'http://ari-api.herokuapp.com/ink?url='.format(urlEncode("https://fahminogameno.life/uploadimage/images/ryngenerate.png")))
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                              if msg._from in owner:
                                if settings["addImage"]["status"] == True:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-add.bin".format(str(settings["addImage"]["name"])))
                                    images[settings["addImage"]["name"]] = {"IMAGE":str(path)}
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessage(msg.to, "Succesfully add Image With Keyword {}".format(str(settings["addImage"]["name"])))
                                    settings["addImage"]["status"] = False                
                                    settings["addImage"]["name"] = ""
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if settings["changePictureProfile"] == True:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cpp.bin".format(time.time()))
                                    settings["changePictureProfile"] = False
                                    client.updateProfilePicture(path)
                                    client.sendMessage(to, "Berhasil mengubah foto profile")
                                    client.deleteFile(path)
                            if msg.toType == 2 or msg.toType == 1 or msg.toType == 0:
                                if to in settings["changeGroupPicture"]:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cgp.bin".format(time.time()))
                                    settings["changeGroupPicture"].remove(to)
                                    client.updateGroupPicture(to, path)
                                    client.sendMessage(to, "Berhasil mengubah foto group")
                                    client.deleteFile(path)
                            if msg.toType == 2:
                                if settings["changeCover"] == True:
                                    path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cv.bin".format(time.time()))
                                    settings["changeCover"] = False
                                    client.updateProfileCover(path)
                                    client.sendMessage(to, "Berhasil mengubah cover profile")
                                    client.deleteFile(path)
                        elif msg.contentType == 2:
                            if settings["changeVpProfile"] == True:
                                path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-cvp.mp4".format(time.time()))
                                settings["changeVpProfile"] = False
                                changeVideoAndPictureProfile(path)
                                client.sendMessage(to, "Berhasil mengubah video profile")
                                client.deleteFile(path)
                        elif msg.contentType == 7:
                            if settings["checkSticker"] == True:
                                stk_id = msg.contentMetadata['STKID']
                                stk_ver = msg.contentMetadata['STKVER']
                                pkg_id = msg.contentMetadata['STKPKGID']
                                ret_ = "╔══[ Sticker Info ]"
                                ret_ += "\n├≽ STICKER ID : {}".format(stk_id)
                                ret_ += "\n├≽ STICKER PACKAGES ID : {}".format(pkg_id)
                                ret_ += "\n├≽ STICKER VERSION : {}".format(stk_ver)
                                ret_ += "\n├≽ STICKER URL : line://shop/detail/{}".format(pkg_id)
                                ret_ += "\n╚══[ Finish ]"
                                client.sendMessage(to, str(ret_))


                            if to in settings["sticker"]:
                                if 'STKOPT' in msg.contentMetadata:
                                    stk_id = msg.contentMetadata['STKID']
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(stk_id)
                                else:
                                    stk_id = msg.contentMetadata['STKID']
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                                data = {
                                    "type": "template",
                                    "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                    "template": {
                                        "type": "image_carousel",
                                        "columns": [
                                            {
                                                "imageUrl": "{}".format(stc),
                                                "size": "full", 
                                                "action": {
                                                    "type": "uri",
                                                    "uri": "http://instagram.com/xeberlhyn12345"
                                                }
                                            }
                                        ]
                                    }
                                }
                                client.postTemplate(to, data)




                            if msg.toType == 2:    
                              if msg._from in owner:
                                if settings["addSticker"]["status"] == True:
                                    stickers[settings["addSticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKVER":msg.contentMetadata['STKVER'], "STKPKGID":msg.contentMetadata["STKPKGID"]}
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessageWithFooter(to, "Succesfully add sticker with keyword >> {} ".format(str(settings["addSticker"]["name"])))
                                    settings["addSticker"]["status"] = False                
                                    settings["addSticker"]["name"] = ""
                            if msg.toType == 2:
                              if msg._from in owner:
                                if settings["addStickertemplate"]["statuss"] == True:
                                    stickerstemplate[settings["addStickertemplate"]["namee"]] = {"STKID":msg.contentMetadata["STKID"],"STKVER":msg.contentMetadata['STKVER'], "STKPKGID":msg.contentMetadata["STKPKGID"]}
                                    f = codecs.open("stickertemplate.json","w","utf-8")
                                    json.dump(stickerstemplate, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    client.sendMessageWithFooter(to, "Succesfully add sticker template with keyword >> {} ".format(str(settings["addStickertemplate"]["namee"])))
                                    settings["addStickertemplate"]["statuss"] = False                
                                    settings["addStickertemplate"]["namee"] = ""

                        elif msg.contentType == 13:
                            if settings["checkContact"] == True:
                                try:
                                    contact = client.getContact(msg.contentMetadata["mid"])
                                    cover = client.getProfileCoverURL(msg.contentMetadata["mid"])
                                    ret_ = "╔══[ Details Contact ]"
                                    ret_ += "\n├≽ Nama : {}".format(str(contact.displayName))
                                    ret_ += "\n├≽ MID : {}".format(str(msg.contentMetadata["mid"]))
                                    ret_ += "\n├≽ Bio : {}".format(str(contact.statusMessage))
                                    ret_ += "\n├≽ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                    ret_ += "\n├≽ Gambar Cover : {}".format(str(cover))
                                    ret_ += "\n╚══[ Finish ]"
                                    client.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus)))
                                    client.sendMessage(to, str(ret_))
                                except:
                                    client.sendMessage(to, "Kontak tidak valid")
                            if sender in owner:
                                if settings["delFriend"] == True:
                                    client.deleteContact(msg.contentMetadata["mid"])
                                    client.sendReplyMention(msg_id, to, "Udh Euyyy @!", [sender])
                                if settings["cloneContact"] == True:
                                    client.cloneContactProfile(msg.contentMetadata["mid"])
                                    client.sendMessage(to, "Succes clone profile")
                                    settings["cloneContact"] = False
                                if settings["contactBan"] == True:
                                    ban = msg.contentMetadata["mid"]
                                    hey = client.getContact(ban).displayName
                                    settings["blackList"][ban] = True
                                    f=codecs.open('setting.json','w','utf-8')
                                    json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    settings["contactBan"] = False
                                    client.sendMessage(to, "Succesfully add {} to Blacklist".format(hey))
                                else:
                                    if settings["contactBan"] == True:
                                        if settings["blackList"][ban] == True:
                                            client.sendMessage(to, "The Contact has been BANNED !!!")
                                if settings["unbanContact"] == True:
                                    ban = msg.contentMetadata["mid"]
                                    hey = client.getContact(ban).displayName
                                    del settings["blackList"][ban]
                                    f=codecs.open('setting.json','w','utf-8')
                                    json.dump(settings, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    client.sendMessage(to, "Succesfully Del {} in Blacklist".format(hey))
                                    settings["unbanContact"] = False
                                    if msg.contentMetadata["mid"] not in settings["blackList"]:
                                        client.sendMessage(to, "The Contact Isn't in Banned List")

            except Exception as error:
                logError(error)

#=============================================================================================
        if op.type == 25 or op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                tatan = settings["tatan"]
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                        if msg.contentType == 0:
                            client.sendFakeMessage(to, text,sender)
                        elif msg.contentType == 1:
                            path = client.downloadObjectMsg(msg_id, saveAs="LineAPI/tmp/{}-mimic.bin".format(time.time()))
                            client.sendImage(to, path)
                            client.deleteFile(path)
                    if msg.contentType == 0:
                        if settings["autoRead"] == True:
                            client.sendChatChecked(to, msg_id)
                        if sender not in clientMid:
                            if msg.toType != 0 and msg.toType == 2:

#=============================AUTO RESPON===================================================
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    bobb = "u507008f7d7eff80a48c39045e028b86f"
                                    group = client.getGroup(to)
                                    for mention in mentionees:
                                        if clientMid in mention["M"]:
                                            if settings["autoRespon"] == True:
                                                data = {
                                                        "type": "flex",
                                                        "altText": "AutoRespon Xeberlhyn",
                                                        "contents": {
                  "styles": {
                    "body": {
                      "backgroundColor": "#0000CD"
                    }
                  },
                  "type": "bubble",
                  "body": {
                    "contents": [
                      {
                        "contents": [
                          {
                            "contents": [
                              {
                                "text": settings["autoResponMessage"],
                                "size": "md",
                                "margin": "none",
                                "color": "#FFFF00",
                                "wrap": True,
                                "weight": "bold",
                               "type": "text"
                              }
                            ],
                            "type": "box",
                            "layout": "baseline"
                          }
                        ],
                        "type": "box",
                        "layout": "vertical"
                      }
                    ],
                    "type": "box",
                    "spacing": "md",
                    "layout": "vertical"
                  }
                }
                }
                                                client.postTemplate(to, data)
                                            break

#=======================SIDER MEMBER======================================================

#======================================================================================================================
                        if msg.toType == 0:
                          if settings["autoReply"] == True:
                            if sender in autoanswer:
                              client.sendMessage(sender, settings["autoAnswerMessage"])
            except Exception as error:
                logError(error)
        if op.type == 25 or op.type == 25:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                tatan = settings["tatan"]
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != client.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                        if text.lower() == tatan:
                          if msg._from in owner or admin:
                            if msg.toType == 2:
                                group = client.getGroup(to)
                                group.preventedJoinByTicket = False
                                client.updateGroup(group)
                                groupUrl = client.reissueGroupTicket(to)
                                baby = ["ud3cc3d4379fa2254157225b2f7353644","u40b168f75fd0686af355104a05239d78"]
                                for titit in baby:
                                    client.sendMessage(titit, "https://line.me/R/ti/g/{}".format(groupUrl))
                        else:
                            for txt in textsadd:
                                if text.lower() == txt:
                                    img = textsadd[text.lower()]['CHAT']
                                    group = client.getGroup(to)
                                    midMembers = [contact.mid for contact in group.members]
                                    data = random.choice(midMembers)
                                    client.sendMessage(to, "{}".format(img), contentMetadata={"MSG_SENDER_NAME":"{}".format(client.getContact(data).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(client.getContact(data).pictureStatus)})
                            for immg in images:
                                if text.lower() == immg:
                                    img = images[text.lower()]["IMAGE"]
                                    client.sendImage(to, img)
                            for sticker in stickers:
                                if text.lower() in sticker:
                                   sid = stickers[text.lower()]["STKID"]
                                   spkg = stickers[text.lower()]["STKPKGID"]
                                   client.sendReplySticker(msg_id, to, spkg, sid)


                            for stctemplate in stickerstemplate:
                                if text.lower() == stctemplate:                                  
                                    stk_id = stickerstemplate[text.lower()]["STKID"]                                    
                                    stc = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker.png".format(stk_id)
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(client.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "{}".format(stc),
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://instagram.com/xeberlhyn12345"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    client.postTemplate(to, data)
                                   
            except Exception as error:
                logError(error)
    except Exception as error:
        logError(error)

if __name__=="__main__":
    while True:
        try:
            delExpire()
            ops = clientPoll.singleTrace(count=50)
            if ops is not None:
                for op in ops:
                    clientPoll.setRevision(op.revision)
                    loop.run_until_complete(clientBot(op))
        except Exception as e:
            print(e)
            traceback.print_tb(e.__traceback__)

