import urllib.request as ur
import os,json,threading
class Downloader:
    def __init__(self):
        pass
    def downloadHtml(self,url):
        flag=0
        while flag<=10:
            try:
                response=ur.urlopen(url)
                if response.getcode() != 200:
                    print("code isn't 200")
                    return None
                
                return response.read()
            except :
                print("download html fail ")
    def downloadImage(self,photos,name):
        if os.path.exists('./output/'):
            pass
        else:
            os.mkdir('./output/')
        if os.path.exists('./output/'+name):
            pass
        else:
            os.mkdir('./output/'+name)
        # with open('./output/'+name+'/list.json','w') as _file:
        #     _file.write(json.dumps(photos[1:len(photos)-1]))
        threads=[]
        last=0
        for i in range(1,len(photos),8):
            thread = _DownloadThread(str(i), photos[last:i*8],name,len(photos))
            last=i*8
            thread.start()
            threads.append(thread)
        thread = _DownloadThread(str(i), photos[last+1:len(photos)-1],name,len(photos))
        for i in threads:
            i.join()
            
class _DownloadThread(threading.Thread):
    def __init__(self, threadID, photos,name,allLen):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.photos = photos
        self.name = name
        self.allLen=allLen
    def run(self):
        print ("开始线程：" + self.threadID)
        self.downloadImage(self.name, self.photos,self.allLen)
        print ("完成线程：" + self.threadID)

    def downloadImage(self,name, photos,allLen):
        title=''
        
        for i in range(0,len(photos)):
            for key in photos[i]:
                title=key
                

                if os.path.exists('./output/'+name+"/"+title):
                    pass
                else:
                    os.mkdir('./output/'+name+"/"+title)
                
                j=0
                for photo in photos[i][key]:
                    j+=1
                    if photo==None:
                        continue
                    with open('./output/'+name+"/"+title+"/"+str(j)+".png", mode='wb') as _file:
                        #print(photo)
                        data=b''
                        failCount=0
                        while failCount<10:
                            try:
                                headers = {
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
                                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                                            "Accept-Encoding": "gzip, deflate",
                                            "Connection": "keep-alive",
                                            "Upgrade-Insecure-Requests": "1",
                                            "Pragma": "no-cache",
                                            "Cache-Control": "no-cache",
                                    }
                                req=ur.Request(url=photo,headers=headers)
                                response=ur.urlopen(req)
                                if response.getcode() != 200:
                                    print("fail_none")
                                data=response.read()
                                _file.write(data)
                                break
                            except:
                                #retry
                                failCount+=1    
                                if failCount>=10:
                                    print("img download Fail:"+photo)
                        
            print("进度："+str(i*100/allLen))                
            print('\n\n\n\n\n\n')
        # with open('./output/'+name+'/list.json','w') as _file:
        #      _file.write(json.dumps(photos))
