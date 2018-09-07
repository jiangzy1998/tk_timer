import json

class storage():
    def __init__(self):
        pass

    def write(self,first_min,first_sec,first_ms,
                   second_min,second_sec,second_ms,
                   third_min,third_sec,third_ms,
                   pun1,pun2,pun3):
        data = {'first_min' : first_min, 'first_sec' : first_sec,'first_ms' : first_ms,
        'second_min' : second_min, 'second_sec' : second_sec,'second_ms' : second_ms,
        'third_min' : third_min, 'third_sec' : third_sec,'third_ms' : third_ms
        ,'pun1' : pun1,'pun2' : pun2,'pun3' : pun3}

        with open("./storage.json","w") as w:
            json.dump(data,w)
    
    def read(self):
        with open("./storage.json","r") as r:
            r = json.load(open('./storage.json', 'r'))
            return r['first_min'],r['first_sec'],r['first_ms'],r['second_min'],r['second_sec'],r['second_ms'],r['third_min'],r['third_sec'],r['third_ms'],r['pun1'],r['pun2'],r['pun3']
