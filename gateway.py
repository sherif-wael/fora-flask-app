# Gateway Module Capture Requests and call apis
from requests import request
import skedda_api as skedda
from flask import Flask , request, jsonify
import json

app = Flask(__name__)

#Global Vars
subDomainsSessions = {
    'propadeleg':{
        'subUrl':'https://propadeleg.skedda.com:443/bookings',
        'subJson': {"booking": {"addConference": False, "allowInviteOthers": False, "arbitraryerrors": None, "attendees": [], "chargeTransactionId": None, "checkInAudits": None, "createdDate": None, "customFields": [], "decoupleBooking": None, "decoupleDate": None, "end": "2022-07-30T02:00:00", "endOfLastOccurrence": None, "hideAttendees": False, "lockInMargin": 4, "paymentStatus": 1, "piId": None, "price": 250, "recurrenceRule": None, "spaces": ["682213"], "start": "2022-07-30T01:00:00", "syncToExternalCalendar": False, "title": None, "type": 1, "venue": "148937", "venueuser": "2384161"}},
        'subCookies': {"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068C-RrCSE_zkRjMQF6UvcHLxDH3_0ZT1BDV0RO-szaKxXNB6ah-BxS85A5PcsvY8I_iyktCnZlHlKw2ZQIwZUjkEvIlwVnj3H4su3stZYtIDlry8o_H46zXYFHF47unHj0", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069hlzlvKlyOAiidBJ0gN2GVVOTqcit71UNYUMZgDUcmGmqpD4Jgs6cDqmjZnEzaKGq4nifPljWdCCzEZDvSvd_mg-O7-ROBehJ_WB9pzdfON6TZoy8xwlKbwTJFpPCNzfWVEQGhH-_3_lMMwrG4aZWe0dkTLhzRIM2M9V1eoxXB13IKo-chbmv1cDP1tadG2ChM2kw6QbyDvNHAiyV0GoRBQeAgjuduk2a48-vvteYc3mdoNzb9Bi5WsJo95Wi8MrEGHkVLz1eQKgExiDWS-XwEmHHNLMN4c1GEaaZuiyfX3IPWveMPRSCgz_gcYxFl7t61p0bwtAwYJnldTCOp6QQCf8Huw2KcChWhouavImZTeHgeZ1ywsX4Wr68Mx0sOCdID5a45sYVSsE8WsAKmWbiMdtRi0JdtXsIvEhJ8tsHa5KK5YO0YZxzII9oJ79aQ34RbbPvPK4pW_Zz3NLRJZje0CbI7Gg2WJ2aMNY9wKcGchRmVjjUQzVBGDkD9B4ixPtmr_qIczPIGKdNdDP9Wp-aLq5sjG8Wg23VGBmh3tpKpVGGMrR_tQZln431iOOVvkk-v2F9SfwEaEWRK2NRN6b7Ar6jtzWlu5v3DSvOMvtQsoLcP53mazA3Tb6KeOjTJ-z-V_JyiF4KE1pqxX7Y6zSXnNFgvZ3dQfRcVBUMFBFeGouLs3SyNWepbX9MgD0RMkPk"},
        'subHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv068cCyk_aNeNPxddL6XE3EFuXyOcyB3K4cAyUjdk_waukg-uT1OxpKmKMUbrxHnnibkmZPguM97E6QbwcPS2ekN9IULQ3P-NbI0KhvWjfPw9sfddfHz18sK2iwUa0SMfJ3rO21Y-4naxbH_Hjd8gcXyQQrSpfJUziKYjwTJMxKHPXw", "Sec-Ch-Ua-Mobile": "?0", "Content-Type": "application/json; charset=UTF-8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://propadeleg.skedda.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://propadeleg.skedda.com/booking?nbend=2022-07-30T02%3A00%3A00&nbspaces=682213&nbstart=2022-07-30T01%3A00%3A00&viewdate=2022-07-30", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'cancelUrl':'https://propadeleg.skedda.com:443/bookings/',
        'cancelCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068C-RrCSE_zkRjMQF6UvcHLxDH3_0ZT1BDV0RO-szaKxXNB6ah-BxS85A5PcsvY8I_iyktCnZlHlKw2ZQIwZUjkEvIlwVnj3H4su3stZYtIDlry8o_H46zXYFHF47unHj0", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069hlzlvKlyOAiidBJ0gN2GVVOTqcit71UNYUMZgDUcmGmqpD4Jgs6cDqmjZnEzaKGq4nifPljWdCCzEZDvSvd_mg-O7-ROBehJ_WB9pzdfON6TZoy8xwlKbwTJFpPCNzfWVEQGhH-_3_lMMwrG4aZWe0dkTLhzRIM2M9V1eoxXB13IKo-chbmv1cDP1tadG2ChM2kw6QbyDvNHAiyV0GoRBQeAgjuduk2a48-vvteYc3mdoNzb9Bi5WsJo95Wi8MrEGHkVLz1eQKgExiDWS-XwEmHHNLMN4c1GEaaZuiyfX3IPWveMPRSCgz_gcYxFl7t61p0bwtAwYJnldTCOp6QQCf8Huw2KcChWhouavImZTeHgeZ1ywsX4Wr68Mx0sOCdID5a45sYVSsE8WsAKmWbiMdtRi0JdtXsIvEhJ8tsHa5KK5YO0YZxzII9oJ79aQ34RbbPvPK4pW_Zz3NLRJZje0CbI7Gg2WJ2aMNY9wKcGchRmVjjUQzVBGDkD9B4ixPtmr_qIczPIGKdNdDP9Wp-aLq5sjG8Wg23VGBmh3tpKpVGGMrR_tQZln431iOOVvkk-v2F9SfwEaEWRK2NRN6b7Ar6jtzWlu5v3DSvOMvtQsoLcP53mazA3Tb6KeOjTJ-z-V_JyiF4KE1pqxX7Y6zSXnNFgvZ3dQfRcVBUMFBFeGouLs3SyNWepbX9MgD0RMkPk"},
        'cancelHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv068cCyk_aNeNPxddL6XE3EFuXyOcyB3K4cAyUjdk_waukg-uT1OxpKmKMUbrxHnnibkmZPguM97E6QbwcPS2ekN9IULQ3P-NbI0KhvWjfPw9sfddfHz18sK2iwUa0SMfJ3rO21Y-4naxbH_Hjd8gcXyQQrSpfJUziKYjwTJMxKHPXw", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://propadeleg.skedda.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://propadeleg.skedda.com/booking?viewdate=2022-07-30", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'fetchUrl':'https://propadeleg.skedda.com:443/bookingslists?',
        'fetchCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068C-RrCSE_zkRjMQF6UvcHLxDH3_0ZT1BDV0RO-szaKxXNB6ah-BxS85A5PcsvY8I_iyktCnZlHlKw2ZQIwZUjkEvIlwVnj3H4su3stZYtIDlry8o_H46zXYFHF47unHj0", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069hlzlvKlyOAiidBJ0gN2GVVOTqcit71UNYUMZgDUcmGmqpD4Jgs6cDqmjZnEzaKGq4nifPljWdCCzEZDvSvd_mg-O7-ROBehJ_WB9pzdfON6TZoy8xwlKbwTJFpPCNzfWVEQGhH-_3_lMMwrG4aZWe0dkTLhzRIM2M9V1eoxXB13IKo-chbmv1cDP1tadG2ChM2kw6QbyDvNHAiyV0GoRBQeAgjuduk2a48-vvteYc3mdoNzb9Bi5WsJo95Wi8MrEGHkVLz1eQKgExiDWS-XwEmHHNLMN4c1GEaaZuiyfX3IPWveMPRSCgz_gcYxFl7t61p0bwtAwYJnldTCOp6QQCf8Huw2KcChWhouavImZTeHgeZ1ywsX4Wr68Mx0sOCdID5a45sYVSsE8WsAKmWbiMdtRi0JdtXsIvEhJ8tsHa5KK5YO0YZxzII9oJ79aQ34RbbPvPK4pW_Zz3NLRJZje0CbI7Gg2WJ2aMNY9wKcGchRmVjjUQzVBGDkD9B4ixPtmr_qIczPIGKdNdDP9Wp-aLq5sjG8Wg23VGBmh3tpKpVGGMrR_tQZln431iOOVvkk-v2F9SfwEaEWRK2NRN6b7Ar6jtzWlu5v3DSvOMvtQsoLcP53mazA3Tb6KeOjTJ-z-V_JyiF4KE1pqxX7Y6zSXnNFgvZ3dQfRcVBUMFBFeGouLs3SyNWepbX9MgD0RMkPk"},
        'fetchHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv068cCyk_aNeNPxddL6XE3EFuXyOcyB3K4cAyUjdk_waukg-uT1OxpKmKMUbrxHnnibkmZPguM97E6QbwcPS2ekN9IULQ3P-NbI0KhvWjfPw9sfddfHz18sK2iwUa0SMfJ3rO21Y-4naxbH_Hjd8gcXyQQrSpfJUziKYjwTJMxKHPXw", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://propadeleg.skedda.com/booking?viewdate=2022-07-30", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'fieldsUrl':'https://propadeleg.skedda.com:443/webs',
        'fieldsCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068C-RrCSE_zkRjMQF6UvcHLxDH3_0ZT1BDV0RO-szaKxXNB6ah-BxS85A5PcsvY8I_iyktCnZlHlKw2ZQIwZUjkEvIlwVnj3H4su3stZYtIDlry8o_H46zXYFHF47unHj0", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069hlzlvKlyOAiidBJ0gN2GVVOTqcit71UNYUMZgDUcmGmqpD4Jgs6cDqmjZnEzaKGq4nifPljWdCCzEZDvSvd_mg-O7-ROBehJ_WB9pzdfON6TZoy8xwlKbwTJFpPCNzfWVEQGhH-_3_lMMwrG4aZWe0dkTLhzRIM2M9V1eoxXB13IKo-chbmv1cDP1tadG2ChM2kw6QbyDvNHAiyV0GoRBQeAgjuduk2a48-vvteYc3mdoNzb9Bi5WsJo95Wi8MrEGHkVLz1eQKgExiDWS-XwEmHHNLMN4c1GEaaZuiyfX3IPWveMPRSCgz_gcYxFl7t61p0bwtAwYJnldTCOp6QQCf8Huw2KcChWhouavImZTeHgeZ1ywsX4Wr68Mx0sOCdID5a45sYVSsE8WsAKmWbiMdtRi0JdtXsIvEhJ8tsHa5KK5YO0YZxzII9oJ79aQ34RbbPvPK4pW_Zz3NLRJZje0CbI7Gg2WJ2aMNY9wKcGchRmVjjUQzVBGDkD9B4ixPtmr_qIczPIGKdNdDP9Wp-aLq5sjG8Wg23VGBmh3tpKpVGGMrR_tQZln431iOOVvkk-v2F9SfwEaEWRK2NRN6b7Ar6jtzWlu5v3DSvOMvtQsoLcP53mazA3Tb6KeOjTJ-z-V_JyiF4KE1pqxX7Y6zSXnNFgvZ3dQfRcVBUMFBFeGouLs3SyNWepbX9MgD0RMkPk"},
        'fieldsHeaders': {"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv068cCyk_aNeNPxddL6XE3EFuXyOcyB3K4cAyUjdk_waukg-uT1OxpKmKMUbrxHnnibkmZPguM97E6QbwcPS2ekN9IULQ3P-NbI0KhvWjfPw9sfddfHz18sK2iwUa0SMfJ3rO21Y-4naxbH_Hjd8gcXyQQrSpfJUziKYjwTJMxKHPXw", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://propadeleg.skedda.com/booking", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
    },
    'padelhousecourts':{
        'subUrl':'https://padelhousecourts.skedda.com:443/bookings',
        'subCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_ttf4VD7vGQHm0Z2b6DirsIrOqk3ggeKOswHGzEFIYaeYHjfL_Qese7EJwmm1l_5wqRsyv-C9v8C2lLyRPlroN_9Y5IH51BMm0A28yAhSUtOQy0ritJ48_e6BklovyT9w", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068H7cSNx_TBg04xedtzhr4hwUC5irsHycTWF1-O-F0AR5dS0BFEqzmYTSOlOPq8rbr6JtW5D1qf0rQq0AaXaYDbk-H9RbwOhTxRGydZF3MQ9fSROJOdhSZGl1poMxoDgdPamBFHuRObLz1fmwECwna_EXF9boieyrfH6o3HJh-X8zkFDV5jkeYVNRY64G4CDwCIGY6mRKGE0fBUKCXmrAwxw4N3RyYMfZsX653AUrhURUVSjVRuxVSPHcRcS9B1Q6SJzQVbbGmnrnPPTBYpSWGZk0FgtsnAMrlbfeEgT_vT8kWOoTgbA5bw-qRnzuBXrNnjLc1d_aKSFTPauN0wXtSp2BWDtQxChO_cxfzGct_UbIcXLQ-3oFH2yBhS2B1nfhpJkbYXlVTykbsLKTqJ0Np-W60taNpwpNQxO6LgpmLnctp5c66HblAsbVMD9DG0TG82Dw645IsLYflZ18Z_Y8sbczwk3EJZ1aaOedPSxE8hyskNdfJVghDSNO6QledyUATQ8U8WLz1TKpTKcTJPmNBSTfwTE8j4BqWvGuzyMBKxudspYFumSOjw-7w5tQE4vI48pErVNkJDv01UBRCSWnwTqfmJ2N8Dtqdi-4TYnu38gZB-xTDZZNePb6PMXWhJrkIO80tQz-0wsKdSnYH6fgTalSY_L-OT8I1dlFsNuMTH9ojis0eiK9ImyyXLnc5e9-0j_VJk58e7GER14SjKS6vA"},
        'subHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv06-qvQnjn77pb_khvxys7wvSY7AO-8dM9AZuBINFvmNtKMw8hJUedAMBIJyU4Yh-ORaQQd1RixRkAAr1GebFv7tkdpVSLwTmHck8JTIT8BSBstTZLgl1D9C_Pz5xtjZoPNGOe5gkzMc7pCM6OgDuvO5uxwV6r3dpTzjMXQ-6JS3D9g", "Sec-Ch-Ua-Mobile": "?0", "Content-Type": "application/json; charset=UTF-8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://padelhousecourts.skedda.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://padelhousecourts.skedda.com/booking?nbend=2022-08-02T17%3A00%3A00&nbspaces=733441&nbstart=2022-08-02T16%3A00%3A00&viewdate=2022-08-02&viewend=2022-09-14", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'subJson':{"booking": {"addConference": False, "allowInviteOthers": False, "arbitraryerrors": None, "attendees": [], "chargeTransactionId": None, "checkInAudits": None, "createdDate": None, "customFields": [{"id": "notes", "value": None}], "decoupleBooking": None, "decoupleDate": None, "end": "2022-08-02T17:00:00", "endOfLastOccurrence": None, "hideAttendees": False, "lockInMargin": 0, "paymentStatus": 2, "piId": None, "price": 300, "recurrenceRule": None, "spaces": ["733441"], "start": "2022-08-02T16:00:00", "syncToExternalCalendar": False, "title": None, "type": 1, "venue": "164925", "venueuser": "2389402"}},
        'cancelUrl':'https://padelhousecourts.skedda.com:443/bookings/',
        'cancelCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_ttf4VD7vGQHm0Z2b6DirsIrOqk3ggeKOswHGzEFIYaeYHjfL_Qese7EJwmm1l_5wqRsyv-C9v8C2lLyRPlroN_9Y5IH51BMm0A28yAhSUtOQy0ritJ48_e6BklovyT9w", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068H7cSNx_TBg04xedtzhr4hwUC5irsHycTWF1-O-F0AR5dS0BFEqzmYTSOlOPq8rbr6JtW5D1qf0rQq0AaXaYDbk-H9RbwOhTxRGydZF3MQ9fSROJOdhSZGl1poMxoDgdPamBFHuRObLz1fmwECwna_EXF9boieyrfH6o3HJh-X8zkFDV5jkeYVNRY64G4CDwCIGY6mRKGE0fBUKCXmrAwxw4N3RyYMfZsX653AUrhURUVSjVRuxVSPHcRcS9B1Q6SJzQVbbGmnrnPPTBYpSWGZk0FgtsnAMrlbfeEgT_vT8kWOoTgbA5bw-qRnzuBXrNnjLc1d_aKSFTPauN0wXtSp2BWDtQxChO_cxfzGct_UbIcXLQ-3oFH2yBhS2B1nfhpJkbYXlVTykbsLKTqJ0Np-W60taNpwpNQxO6LgpmLnctp5c66HblAsbVMD9DG0TG82Dw645IsLYflZ18Z_Y8sbczwk3EJZ1aaOedPSxE8hyskNdfJVghDSNO6QledyUATQ8U8WLz1TKpTKcTJPmNBSTfwTE8j4BqWvGuzyMBKxudspYFumSOjw-7w5tQE4vI48pErVNkJDv01UBRCSWnwTqfmJ2N8Dtqdi-4TYnu38gZB-xTDZZNePb6PMXWhJrkIO80tQz-0wsKdSnYH6fgTalSY_L-OT8I1dlFsNuMTH9ojis0eiK9ImyyXLnc5e9-0j_VJk58e7GER14SjKS6vA"},
        'cancelHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv06-qvQnjn77pb_khvxys7wvSY7AO-8dM9AZuBINFvmNtKMw8hJUedAMBIJyU4Yh-ORaQQd1RixRkAAr1GebFv7tkdpVSLwTmHck8JTIT8BSBstTZLgl1D9C_Pz5xtjZoPNGOe5gkzMc7pCM6OgDuvO5uxwV6r3dpTzjMXQ-6JS3D9g", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://padelhousecourts.skedda.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://padelhousecourts.skedda.com/booking?viewdate=2022-08-02&viewend=2022-09-14", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'fetchUrl':'https://padelhousecourts.skedda.com:443/bookingslists?',
        'fetchCookies': {"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_ttf4VD7vGQHm0Z2b6DirsIrOqk3ggeKOswHGzEFIYaeYHjfL_Qese7EJwmm1l_5wqRsyv-C9v8C2lLyRPlroN_9Y5IH51BMm0A28yAhSUtOQy0ritJ48_e6BklovyT9w", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068H7cSNx_TBg04xedtzhr4hwUC5irsHycTWF1-O-F0AR5dS0BFEqzmYTSOlOPq8rbr6JtW5D1qf0rQq0AaXaYDbk-H9RbwOhTxRGydZF3MQ9fSROJOdhSZGl1poMxoDgdPamBFHuRObLz1fmwECwna_EXF9boieyrfH6o3HJh-X8zkFDV5jkeYVNRY64G4CDwCIGY6mRKGE0fBUKCXmrAwxw4N3RyYMfZsX653AUrhURUVSjVRuxVSPHcRcS9B1Q6SJzQVbbGmnrnPPTBYpSWGZk0FgtsnAMrlbfeEgT_vT8kWOoTgbA5bw-qRnzuBXrNnjLc1d_aKSFTPauN0wXtSp2BWDtQxChO_cxfzGct_UbIcXLQ-3oFH2yBhS2B1nfhpJkbYXlVTykbsLKTqJ0Np-W60taNpwpNQxO6LgpmLnctp5c66HblAsbVMD9DG0TG82Dw645IsLYflZ18Z_Y8sbczwk3EJZ1aaOedPSxE8hyskNdfJVghDSNO6QledyUATQ8U8WLz1TKpTKcTJPmNBSTfwTE8j4BqWvGuzyMBKxudspYFumSOjw-7w5tQE4vI48pErVNkJDv01UBRCSWnwTqfmJ2N8Dtqdi-4TYnu38gZB-xTDZZNePb6PMXWhJrkIO80tQz-0wsKdSnYH6fgTalSY_L-OT8I1dlFsNuMTH9ojis0eiK9ImyyXLnc5e9-0j_VJk58e7GER14SjKS6vA"},
        'fetchHeaders': {"Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://padelhousecourts.skedda.com/booking?viewdate=2022-08-02&viewend=2022-09-14", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'fieldsUrl':'https://padelhousecourts.skedda.com:443/webs',
        'fieldsCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_ttf4VD7vGQHm0Z2b6DirsIrOqk3ggeKOswHGzEFIYaeYHjfL_Qese7EJwmm1l_5wqRsyv-C9v8C2lLyRPlroN_9Y5IH51BMm0A28yAhSUtOQy0ritJ48_e6BklovyT9w", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068H7cSNx_TBg04xedtzhr4hwUC5irsHycTWF1-O-F0AR5dS0BFEqzmYTSOlOPq8rbr6JtW5D1qf0rQq0AaXaYDbk-H9RbwOhTxRGydZF3MQ9fSROJOdhSZGl1poMxoDgdPamBFHuRObLz1fmwECwna_EXF9boieyrfH6o3HJh-X8zkFDV5jkeYVNRY64G4CDwCIGY6mRKGE0fBUKCXmrAwxw4N3RyYMfZsX653AUrhURUVSjVRuxVSPHcRcS9B1Q6SJzQVbbGmnrnPPTBYpSWGZk0FgtsnAMrlbfeEgT_vT8kWOoTgbA5bw-qRnzuBXrNnjLc1d_aKSFTPauN0wXtSp2BWDtQxChO_cxfzGct_UbIcXLQ-3oFH2yBhS2B1nfhpJkbYXlVTykbsLKTqJ0Np-W60taNpwpNQxO6LgpmLnctp5c66HblAsbVMD9DG0TG82Dw645IsLYflZ18Z_Y8sbczwk3EJZ1aaOedPSxE8hyskNdfJVghDSNO6QledyUATQ8U8WLz1TKpTKcTJPmNBSTfwTE8j4BqWvGuzyMBKxudspYFumSOjw-7w5tQE4vI48pErVNkJDv01UBRCSWnwTqfmJ2N8Dtqdi-4TYnu38gZB-xTDZZNePb6PMXWhJrkIO80tQz-0wsKdSnYH6fgTalSY_L-OT8I1dlFsNuMTH9ojis0eiK9ImyyXLnc5e9-0j_VJk58e7GER14SjKS6vA"},
        'fieldsHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv068fxJdMI1g8I2tpAd0HwYtqcTs5yImFz7Mpjx94XAeFsHqSIAxkoS82lPsEDbmSw0lmnMSt43P0rshI1AUe9fzFrkJ10GxegqnEuTJz6_SacEEgRj1db42nzFCjOe7ag1DWJjnUr3qOz4q6H3YW9otx_D4dX_ab7EtojbmKIkuQkQ", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://padelhousecourts.skedda.com/booking?viewdate=2022-08-02&viewend=2022-09-14", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        },
    'therushegypt': {
        'subUrl':'https://therushegypt.skedda.com:443/bookings',
        'subCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_ttf4VD7vGQHm0Z2b6DirsIrOqk3ggeKOswHGzEFIYaeYHjfL_Qese7EJwmm1l_5wqRsyv-C9v8C2lLyRPlroN_9Y5IH51BMm0A28yAhSUtOQy0ritJ48_e6BklovyT9w", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068H7cSNx_TBg04xedtzhr4hwUC5irsHycTWF1-O-F0AR5dS0BFEqzmYTSOlOPq8rbr6JtW5D1qf0rQq0AaXaYDbk-H9RbwOhTxRGydZF3MQ9fSROJOdhSZGl1poMxoDgdPamBFHuRObLz1fmwECwna_EXF9boieyrfH6o3HJh-X8zkFDV5jkeYVNRY64G4CDwCIGY6mRKGE0fBUKCXmrAwxw4N3RyYMfZsX653AUrhURUVSjVRuxVSPHcRcS9B1Q6SJzQVbbGmnrnPPTBYpSWGZk0FgtsnAMrlbfeEgT_vT8kWOoTgbA5bw-qRnzuBXrNnjLc1d_aKSFTPauN0wXtSp2BWDtQxChO_cxfzGct_UbIcXLQ-3oFH2yBhS2B1nfhpJkbYXlVTykbsLKTqJ0Np-W60taNpwpNQxO6LgpmLnctp5c66HblAsbVMD9DG0TG82Dw645IsLYflZ18Z_Y8sbczwk3EJZ1aaOedPSxE8hyskNdfJVghDSNO6QledyUATQ8U8WLz1TKpTKcTJPmNBSTfwTE8j4BqWvGuzyMBKxudspYFumSOjw-7w5tQE4vI48pErVNkJDv01UBRCSWnwTqfmJ2N8Dtqdi-4TYnu38gZB-xTDZZNePb6PMXWhJrkIO80tQz-0wsKdSnYH6fgTalSY_L-OT8I1dlFsNuMTH9ojis0eiK9ImyyXLnc5e9-0j_VJk58e7GER14SjKS6vA"},
        'subHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_bQeQcPWx1ILgEFlXe6YSRQZHfgbVnPVnavIN02G3v1m3C7AT1TxhVgl0XpC4PjYEqfxc12UqC9Zra2UaJb9DmyZ5Pp3Xdg2JuQ9fBU2xM3Dg6ddw08b6OShrtJn9xkRJe-bK_i3TSrNzwDFtB1CsnWlU0R8xj6PZq7Rr5e9S8vg", "Sec-Ch-Ua-Mobile": "?0", "Content-Type": "application/json; charset=UTF-8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://therushegypt.skedda.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://therushegypt.skedda.com/booking?nbend=2022-07-31T09%3A00%3A00&nbspaces=694226&nbstart=2022-07-31T08%3A00%3A00&viewdate=2022-07-31", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'subJson':{"booking": {"addConference": False, "allowInviteOthers": False, "arbitraryerrors": None, "attendees": [], "chargeTransactionId": None, "checkInAudits": None, "createdDate": None, "customFields": [{"id": "notes", "value": None}], "decoupleBooking": None, "decoupleDate": None, "end": "2022-07-31T09:00:00", "endOfLastOccurrence": None, "hideAttendees": False, "lockInMargin": 4, "paymentStatus": 1, "piId": None, "price": 400, "recurrenceRule": None, "spaces": ["694226"], "start": "2022-07-31T08:00:00", "syncToExternalCalendar": False, "title": None, "type": 1, "venue": "160630", "venueuser": "2382939"}},
        'cancelUrl':'https://therushegypt.skedda.com:443/bookings/',
        'cancelCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_ttf4VD7vGQHm0Z2b6DirsIrOqk3ggeKOswHGzEFIYaeYHjfL_Qese7EJwmm1l_5wqRsyv-C9v8C2lLyRPlroN_9Y5IH51BMm0A28yAhSUtOQy0ritJ48_e6BklovyT9w", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068H7cSNx_TBg04xedtzhr4hwUC5irsHycTWF1-O-F0AR5dS0BFEqzmYTSOlOPq8rbr6JtW5D1qf0rQq0AaXaYDbk-H9RbwOhTxRGydZF3MQ9fSROJOdhSZGl1poMxoDgdPamBFHuRObLz1fmwECwna_EXF9boieyrfH6o3HJh-X8zkFDV5jkeYVNRY64G4CDwCIGY6mRKGE0fBUKCXmrAwxw4N3RyYMfZsX653AUrhURUVSjVRuxVSPHcRcS9B1Q6SJzQVbbGmnrnPPTBYpSWGZk0FgtsnAMrlbfeEgT_vT8kWOoTgbA5bw-qRnzuBXrNnjLc1d_aKSFTPauN0wXtSp2BWDtQxChO_cxfzGct_UbIcXLQ-3oFH2yBhS2B1nfhpJkbYXlVTykbsLKTqJ0Np-W60taNpwpNQxO6LgpmLnctp5c66HblAsbVMD9DG0TG82Dw645IsLYflZ18Z_Y8sbczwk3EJZ1aaOedPSxE8hyskNdfJVghDSNO6QledyUATQ8U8WLz1TKpTKcTJPmNBSTfwTE8j4BqWvGuzyMBKxudspYFumSOjw-7w5tQE4vI48pErVNkJDv01UBRCSWnwTqfmJ2N8Dtqdi-4TYnu38gZB-xTDZZNePb6PMXWhJrkIO80tQz-0wsKdSnYH6fgTalSY_L-OT8I1dlFsNuMTH9ojis0eiK9ImyyXLnc5e9-0j_VJk58e7GER14SjKS6vA"},
        'cancelHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_bQeQcPWx1ILgEFlXe6YSRQZHfgbVnPVnavIN02G3v1m3C7AT1TxhVgl0XpC4PjYEqfxc12UqC9Zra2UaJb9DmyZ5Pp3Xdg2JuQ9fBU2xM3Dg6ddw08b6OShrtJn9xkRJe-bK_i3TSrNzwDFtB1CsnWlU0R8xj6PZq7Rr5e9S8vg", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://therushegypt.skedda.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://therushegypt.skedda.com/booking?viewdate=2022-07-31", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'fetchUrl':'https://therushegypt.skedda.com:443/bookingslists?',
        'fetchCookies': {"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_ttf4VD7vGQHm0Z2b6DirsIrOqk3ggeKOswHGzEFIYaeYHjfL_Qese7EJwmm1l_5wqRsyv-C9v8C2lLyRPlroN_9Y5IH51BMm0A28yAhSUtOQy0ritJ48_e6BklovyT9w", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068fQw-puEeLXXvCciVXfYLls0t-grPoSChjFPZDg2HNCSlTfNCZHbyRl21kzQfBredLthxkzAJ2Ko0GdTTlcsaVo_dDACSK38ac8gJYcV8hxrTQ5xZ3BOWWI3KIUEkeY8vKq67rQMNWkRKrsx_8JB9t9H5fXwFltYS7Go6O-XxRkVPUPHQU6jdG0G34DiPi7WNuDxfVl338qv56ebnmlTkn95c8qvzbfyzsGFl9kPvkkS7N9KQ3LUrRXFRoB49mOPDDfsDCcwTmJcOjrLguRAmI9Pxb09_KhbopK-y_ZdgAYKSOzuFW_Sqw7dbjcXPLY_64JPuRSubPG_k_wV5J6mApJ6NQ2TxLYI_8a5EhYRPXZ25-D9z41qTsG-J9c0dq25Vhe8F14degFNwab9wiXeLv8uLbKHvkEIUtxfpL8Z0yDSHp3dYP9u21BTzu8_cck-K9hMwosCkCkW5Suqh0jcyDDDfOhpm1xRXrCqsWGe1skihc3n6sZN_Eq0oaFsSwg7GA9S8vW70KAW1ne-fsZEJZO5weNTpzFN6s-yuDecryxKyRid1bhS1TsEqEnvDWPpBiupwb-P--_pQO--DxU9rdOGeZ529OqYFOp90_MfCBDJT5JWJ_-mYVumywIJ2WeFA_YRw4Pi3taewpa5NshaqJ6nYXUbbgCSqEGMuVZbb0WYsmbBLKsDNdVB6eRH6B3yk"},
        'fetchHeaders': {"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv06-CGSlq6iEd1pzzX30TJ6_Mw8GwAwDQsgNPcABcmUZJ66Iuh0zgMyqLcWKFr1Z6OtwuLjZ0ACib8ioJ5F1qKSmU5KaAfXGfuBW7SB5x7PO4Ap5GPqRHnEa8XqNrQIHmogyeMXlQ5kMaQ-tyqca67raSxIlQVmaItxjNWTcrEvZRQA", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://therushegypt.skedda.com/booking?viewdate=2022-07-31", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'fieldsUrl':'https://therushegypt.skedda.com:443/webs',
        'fieldsCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_ttf4VD7vGQHm0Z2b6DirsIrOqk3ggeKOswHGzEFIYaeYHjfL_Qese7EJwmm1l_5wqRsyv-C9v8C2lLyRPlroN_9Y5IH51BMm0A28yAhSUtOQy0ritJ48_e6BklovyT9w", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv068fQw-puEeLXXvCciVXfYLls0t-grPoSChjFPZDg2HNCSlTfNCZHbyRl21kzQfBredLthxkzAJ2Ko0GdTTlcsaVo_dDACSK38ac8gJYcV8hxrTQ5xZ3BOWWI3KIUEkeY8vKq67rQMNWkRKrsx_8JB9t9H5fXwFltYS7Go6O-XxRkVPUPHQU6jdG0G34DiPi7WNuDxfVl338qv56ebnmlTkn95c8qvzbfyzsGFl9kPvkkS7N9KQ3LUrRXFRoB49mOPDDfsDCcwTmJcOjrLguRAmI9Pxb09_KhbopK-y_ZdgAYKSOzuFW_Sqw7dbjcXPLY_64JPuRSubPG_k_wV5J6mApJ6NQ2TxLYI_8a5EhYRPXZ25-D9z41qTsG-J9c0dq25Vhe8F14degFNwab9wiXeLv8uLbKHvkEIUtxfpL8Z0yDSHp3dYP9u21BTzu8_cck-K9hMwosCkCkW5Suqh0jcyDDDfOhpm1xRXrCqsWGe1skihc3n6sZN_Eq0oaFsSwg7GA9S8vW70KAW1ne-fsZEJZO5weNTpzFN6s-yuDecryxKyRid1bhS1TsEqEnvDWPpBiupwb-P--_pQO--DxU9rdOGeZ529OqYFOp90_MfCBDJT5JWJ_-mYVumywIJ2WeFA_YRw4Pi3taewpa5NshaqJ6nYXUbbgCSqEGMuVZbb0WYsmbBLKsDNdVB6eRH6B3yk"},
        'fieldsHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv06-CGSlq6iEd1pzzX30TJ6_Mw8GwAwDQsgNPcABcmUZJ66Iuh0zgMyqLcWKFr1Z6OtwuLjZ0ACib8ioJ5F1qKSmU5KaAfXGfuBW7SB5x7PO4Ap5GPqRHnEa8XqNrQIHmogyeMXlQ5kMaQ-tyqca67raSxIlQVmaItxjNWTcrEvZRQA", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://therushegypt.skedda.com/booking?viewdate=2022-07-31", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
    }
}

@app.route("/")
def home():
    return 'a'

@app.route("/book",methods = ['POST','GET'])
def book():
    timeFrom = str(request.values.get('timeFrom'))
    timeTo = str(request.values.get('timeTo'))
    spaces = str(request.values.get('spaces'))  
    title = str(request.values.get('title'))
    subDomain = str(request.values.get('subDomain'))
    subDomainData = subDomainsSessions[subDomain]
    spaces = spaces.split(',')
    bookID = skedda.book(timeFrom,timeTo,spaces,title,subDomainData)
    if bookID > 0:
        return jsonify({'BookID':bookID})
    
    return jsonify({'BookID':'False'})

@app.route("/cancel",methods = ['POST','GET'])
def cancel():
    bookID = str(request.values.get('bookID'))
    subDomain = str(request.values.get('subDomain'))
    subDomainData = subDomainsSessions[subDomain]
    if skedda.cancel(bookID,subDomainData):
        return jsonify({'status':'Cancled'})
    return jsonify({'status':'Error'})

@app.route("/fetch",methods = ['POST','GET'])
def fetch():
    apiData = [
        'Grand Plaza blue court',
        'Grand Plaza GreenSuperCourt',
        'Beverly Red Court',
        'Beverly Super Panoramic',
        'Beverly Blue Court',
        'ELSEGINY CLUB COURT 1',
        'ELSEGINY CLUB COURT 2',
        'Panoramic Padel Super Court',
        'Standard STX Court',
        'Pickelball'
    ]
    timeEnd = str(request.values.get('timeEnd'))
    dateEnd = str(request.values.get('dateEnd'))
    timeTo = str(request.values.get('timeTo'))
    dateTo = str(request.values.get('dateTo'))
    title = str(request.values.get('title'))
    subDomain = str(request.values.get('subDomain'))
    subDomainData = subDomainsSessions[subDomain]
    fetchedData = skedda.fetchBooking(timeEnd,dateEnd,timeTo,dateTo,subDomainData)
    finalResult = []
    if fetchedData != 0:
        #Get Spaces
        spacesNameIds = retriveFieldsIds(subDomainData,apiData)
        if spacesNameIds != 0:
            bookingData = json.loads(fetchedData)
            bookingData = bookingData['bookings']
            for book in bookingData:
                for id in book['spaces']:
                    #print('-> ',id)
                    for clientData in spacesNameIds:
                        #print('<- ',clientData)
                        if id == clientData['spaceId']:
                            #Found Book
                            temp = {'start':book['start'],'end':book['end'],'spaceName':clientData['spaceName'],'spaceId':clientData['spaceId']}
                            finalResult.append(temp)
            
            #print(finalResult)
        return jsonify(finalResult)
    return jsonify({'status':'Error'})

def retriveFieldsIds(subDomainData,apifData):
    Data = skedda.fetchIds(subDomainData)
    SpacesNameId = []
    if Data != 0:
        Data = json.loads(Data)
        #Get Spaces
        Spaces = Data['spaces']
        for spa in Spaces:
            if spa['name'] in apifData:
    
                temp = {'spaceName':spa['name'],'spaceId':spa['id']}
                SpacesNameId.append(temp)
    
        return SpacesNameId
    else:
        print('Error')
        return 0







#simple payload
#fetchBooking('23:59:59','2022-09-14','00:00:00','2022-07-19')


if __name__ == "__main__":
    app.run()