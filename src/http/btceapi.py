


import hmac
import hashlib
import httplib
import urllib
import time
import json

class BTCApi():
    __api_key = '246AXTXJ-3IR9L3CG-867CXYLE-TA5GQCAE-W4JUEBLZ';
    __api_secret = '0e63bd72b5e8f3bb6612a176c86df1331e88f1a28e22e193fe36eba801402eb7';
    __nonce = 1
    __wait_for_nonce = False
    
        
    def __init__(self):
        pass
        #self.__api_key = api_key
        #self.__api_secret = api_secret
        #self.__wait_for_nonce = wait_for_nonce
    
    def __nonce(self):
        if self.__wait_for_nonce:
            time.sleep(1)
        self.__nonce_v = str(time.time()).split('.')[0]


    def __signature(self, params):
        return hmac.new(self.__api_secret, params, digestmod=hashlib.sha512).hexdigest()
    
    def __api_call(self, method, params):
        self.__nonce()
        params['method'] = method
        params['nonce'] = str(self.__nonce_v)
        params = urllib.urlencode(params)
        headers = {     "Content-type" : "application/x-www-form-urlencoded",
                        "Key" : self.__api_key,
                        "Sign" : self.__signature(params)}
        
        conn = httplib.HTTPSConnection("btc-e.com")
        conn.request("POST", "/tapi", params, headers)
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    
    def get_param(self, couple, param):
        conn = httplib.HTTPSConnection("btc-e.com")
        conn.request("GET", "/api/2/" + couple + "/" + param)
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    
    def getInfo(self):
        return self.__api_call('getInfo', {})

    def TransHistory(self, tfrom, tcount, tfrom_id, tend_id, torder, tsince, tend):
          params = {
               "from"        : tfrom,
               "count"        : tcount,
               "from_id"        : tfrom_id,
               "end_id"        : tend_id,
               "order"        : torder,
               "since"        : tsince,
               "end"        : tend}
          return self.__api_call('TransHistory', params)
     
    
    def TradeHistory(self, tfrom, tcount, tfrom_id, tend_id, torder, tsince, tend, tpair):
        params = {
               "from"        : tfrom,
               "count"        : tcount,
               "from_id"        : tfrom_id,
               "end_id"        : tend_id,
               "order"        : torder,
               "since"        : tsince,
               "end"        : tend,
               "pair"        : tpair}
        return self.__api_call('TradeHistory', params)
    
     
    def ActiveOrders(self, tpair):
        params = { "pair" : tpair }
        return self.__api_call('ActiveOrders', params)
    
    def Trade(self, tpair, ttype, trate, tamount):
          params = {
               "pair"        : tpair,
               "type"        : ttype,
               "rate"        : trate,
               "amount"        : tamount}
          return self.__api_call('Trade', params)
      
    def CancelOrder(self, torder_id):
        params = { "order_id" : torder_id }
        return self.__api_call('CancelOrder', params)
