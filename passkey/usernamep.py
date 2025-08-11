import os
import random
import time
import secrets
import binascii
import uuid
import requests
import SignerPy
import telebot
from telebot.types import InlineKeyboardMarkup as mk
from telebot.types import InlineKeyboardButton as bt
def get_ksj(username):
    secret=secrets.token_hex(16)

    url = "https://api16-normal-c-alisg.tiktokv.com/passport/find_account/tiktok_username/"
    params={
        'request_tag_from':"h5",
        'iid':str(random.randint(1, 10**19)),
        'device_id':str(random.randint(1, 10**19)),
        'ac':"WIFI",
        'channel':"googleplay",
        'aid':"567753",
        'app_name':"tiktok_studio",
        'version_code':"370301",
        'version_name':"37.3.1",
        'device_platform':"android",
        'os':"android",
        'ab_version':"37.3.1",
        'ssmix':"a",
        'device_type':"RMX3269",
        'device_brand':"realme",
        'language':"en",
        'os_api':"28",
        'os_version':"10",
        'openudid':str(binascii.hexlify(os.urandom(8)).decode()),
        'manifest_version_code':"370301",
        'resolution':"720*1448",
        'dpi':"420",
        'update_version_code':"370301",
        '_rticket':str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
        'is_pad':"0",
        'current_region':"en",
        'app_type':"normal",
        'sys_region':"en",
        'last_install_time':"1650243523",
        'mcc_mnc':"41840",
        'timezone_name':"Asia/Baghdad",
        'carrier_region_v2':"418",
        'residence':"ُen",
        'app_language':"en",
        'carrier_region':"IQ",
        'ac2':"wifi",
        'uoo':"0",
        'op_region':"IQ",
        'timezone_offset':"10800",
        'build_number':"37.3.1",
        'host_abi':"arm64-v8a",
        'locale':"en",
        'region':"IQ",
        'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
        'cdid':str(uuid.uuid4()),
        'support_webview':"1",
        'cronet_version':"f6248591_2024-09-11",
        'ttnet_version':"4.2.195.9-tiktok",
        'use_store_region_cookie':"1",
        'app_version':"37.3.1"
    }
    
    cookies = {"passport_csrf_token": secret,"passport_csrf_token_default": secret}
    payload = {'mix_mode': "1",
    'username': username,
    }
    m=SignerPy.sign(params=params,cookie=cookies,payload=payload)
    headers={'User-Agent':'com.zhiliaoapp.musically/2023105030 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)','x-tt-passport-csrf-token':cookies['passport_csrf_token'],'x-argus':m["x-argus"],'x-gorgon':m["x-gorgon"],'x-khronos':m["x-khronos"],'x-ladon':m["x-ladon"],'x-ss-stub':m['x-ss-stub'],'x-ss-req-ticket':m['x-ss-req-ticket'],'content-type': "application/x-www-form-urlencoded"}
    response = requests.post(url, params=params, data=payload, headers=headers,cookies=cookies)
    # print(response.json())
    if "token" in response.text:
        token=response.json()["data"]["token"]
        params={
        'not_login_ticket': token,
        'request_tag_from':"h5",
        'iid':params["iid"],
        'device_id':params["device_id"],
        'ac':"WIFI",
        'channel':"googleplay",
        'aid':"567753",
        'app_name':"tiktok_studio",
        'version_code':"370301",
        'version_name':"37.3.1",
        'device_platform':"android",
        'os':"android",
        'ab_version':"37.3.1",
        'ssmix':"a",
        'device_type':"RMX3269",
        'device_brand':"realme",
        'language':"en",
        'os_api':"28",
        'os_version':"10",
        'openudid':params["openudid"],
        'manifest_version_code':"370301",
        'resolution':"720*1448",
        'dpi':"420",
        'update_version_code':"370301",
        '_rticket':str(round(random.uniform(1.2,1.6)*100000000)*-1)+"4632",
        'is_pad':"0",
        'current_region':"en",
        'app_type':"normal",
        'sys_region':"en",
        'last_install_time':"1650243523",
        'mcc_mnc':"41840",
        'timezone_name':"Asia/Baghdad",
        'carrier_region_v2':"418",
        'residence':"ُen",
        'app_language':"en",
        'carrier_region':"IQ",
        'ac2':"wifi",
        'uoo':"0",
        'op_region':"IQ",
        'timezone_offset':"10800",
        'build_number':"37.3.1",
        'host_abi':"arm64-v8a",
        'locale':"en",
        'region':"IQ",
        'ts':str(round(random.uniform(1.2,1.6)*100000000)*-1),
        'cdid':params["cdid"],
        'support_webview':"1",
        'cronet_version':"f6248591_2024-09-11",
        'ttnet_version':"4.2.195.9-tiktok",
        'use_store_region_cookie':"1",
        'app_version':"37.3.1"
    }
        m=SignerPy.sign(params=params,cookie=cookies)
        headers={'User-Agent':'com.zhiliaoapp.musically/2023105030 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)','x-tt-passport-csrf-token':cookies['passport_csrf_token'],'x-argus':m["x-argus"],'x-gorgon':m["x-gorgon"],'x-khronos':m["x-khronos"],'x-ladon':m["x-ladon"],'x-ss-stub':m['x-ss-stub'],'x-ss-req-ticket':m['x-ss-req-ticket'],'content-type': "application/x-www-form-urlencoded"}
        response = requests.post("https://api16-normal-c-alisg.tiktokv.com/passport/auth/available_ways/", params=params,  headers=headers,cookies=cookies)
        # print(response.json())
        if  'success' in response.text:
            passkey=response.json()["data"]["has_passkey"]
            out_passley=response.json()["data"]['has_oauth']
            ksj=response.json()["data"]['oauth_platforms']
            return{
                "passkey":passkey,
                "out_passkey":out_passley,
                "ksj":ksj,
                "message":"success" 
            }
        else:
            return {"message":"error"}
        
       
    elif "verify_center_decision_conf" in response.text:
        return{"message":"error","status":"captch",'use':"vpn"}
    else:
        return{"message":"error","status":"user not found"}
