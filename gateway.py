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
        'subCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069DHRzzCKzaydsNKIt_JtZjSvvkIacc2GpJlTTrkED5qO8CoYV_S3bgUhCimlCCdJnqTzaq15M3O4ZMnJ-NO_iMCInIKFw3ERhdyolMpY2w1B_PVmkPK_PFI_tTNdUHTpA", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv06-fnuvNoNwLGz22jxMfeGrWgYk8nbtOBDrV8hvxj3B1V385HQuYcY4Sc0uGgN5rZ3B7oXVJL623mxAeyGxqGehmGBSpmIZZbnu1iut2McjCoOsgWT3kES96-jG-4_pR3bIaqpCm9JACcupCUNSWF77OhAlo7HQqL_GAbjnQWXdWKLzrUEpGmcuwU2bAngBFrlVAdbuctDOj4RiobuJIybILENqX5UBW-RBvQeKyOm3PDNcmMNZSelQa-JeVGK2o-hA506scQsD1zyeeeihW2fdLraWKE5C0zGm2Dize2SxKwpjicLyS0fCQyN9NJ3GhqBnbAwcO62ZdAcV0H239AKb6Ffq_OVo3GY8Et4X8dVRo6KKUdsQXdq1XKHqbOx_iUz1PK_z98zBg5rg471mnyJr65WbjIsSuRHtcWRbNd5PC40AIRiRArIhQeX54DOdBfBxEQwDpfbo9ZXsLbR2rUqV5Ph1zStQd6mtNdCQow_ySJTCtHbJHVxfTKw-gkfohQUdOjUcfjghZ4XGh7D4z_2Y18Na-0wHhvpFmYnKyQIyVGYSo4q9y6YijRCYQFPhOQlN2FyVkS-VKQXmoOYyFFCttP9OW_aCCHFUs4wn2J6rztxZsgUdU9vzpRL06GMEGOxomHkbttVdOxRFDcNdWcqMOKo3sKf08-XeErqgBZZIwUQDCrq1pSQ1Z4voD0DgVKow"},
        'subHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv06_Sv4vtDq6NIi--ARsC9aMxY7C2yo4nYl5Uj83l9IB8ZDD21oKC5keroKYoXaaV0ytPga6MfEVmR8N8bRePKzVnO-d6vf-ZGafn1gI5tRnR-CY5MXmCK8mxK92iikLzEIRrpetKJQ1w6CmGRei74196eLQPnluVTPBd2l9e_wGBVQ", "Sec-Ch-Ua-Mobile": "?0", "Content-Type": "application/json; charset=UTF-8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://padelhousecourts.skedda.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://padelhousecourts.skedda.com/booking?nbend=2022-07-20T10%3A00%3A00&nbspaces=840355&nbstart=2022-07-20T09%3A00%3A00&viewdate=2022-07-20", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'subJson':{"booking": {"addConference": False, "allowInviteOthers": False, "arbitraryerrors": None, "attendees": [], "chargeTransactionId": None, "checkInAudits": None, "createdDate": None, "customFields": [{"id": "notes", "value": None}], "decoupleBooking": None, "decoupleDate": None, "end": "2022-07-20T10:00:00", "endOfLastOccurrence": None, "hideAttendees": False, "lockInMargin": 4, "paymentStatus": 2, "piId": None, "price": 200, "recurrenceRule": None, "spaces": ["840355"], "start": "2022-07-20T09:00:00", "syncToExternalCalendar": False, "title": None, "type": 1, "venue": "164925", "venueuser": "2337504"}},
        'cancelUrl':'https://padelhousecourts.skedda.com:443/bookings/',
        'cancelCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069DHRzzCKzaydsNKIt_JtZjSvvkIacc2GpJlTTrkED5qO8CoYV_S3bgUhCimlCCdJnqTzaq15M3O4ZMnJ-NO_iMCInIKFw3ERhdyolMpY2w1B_PVmkPK_PFI_tTNdUHTpA", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069BtITHyrtLGjrVaUARy7b9QfAJlbAF49_bXbYDLQG9WeipX5nsjgpqJVtU7KVFk5-8ZjpgAEE5yDZi4WEd0p38sf0tKCDDExTb9lU7nfFCXXfEpEohVFclMLZ6QRviM1wQH7dudvZrr_CRK-mSG7s1IXpN8OEO5diwzFogE3182NYvHOhqM62GcouYW_XdQfCqPUzgWX9a6LB5Zs5T-J9YIexg2__lJ5DBBL1BZpD_axhl6mHBIEJZ-Z-KiNBzym_6CiScqfX6awyn3hvX4qdcnozNFvcSizs9krbvJ1nD50P5NJV2kbZyTQsf1j0bU4SlvNyCNnnPQgCbMXGlBQFSBP26y6KKIs1N4bK69dFCocIRUm1f3__a1EjiZV0zfwRzJVLOwtoUStC4g83LrCvP53uJkhtN90028DS_BTKvMjzEVmEyT8QgOLY8V50auvPu-rPSp4wjh7e5Yx4StEGn5pPZAho5iG_u4rri9xItFby-Tey_zwAcUdYPWESNj9UIyTRhyHZ0hRDueqSpb2lRok8x0y7e5peNSjiQahpso4OUscLX0uOvfnp0Y-P-3_1bEBiqGOfKznDYO_XuISVf5uw6vQzA88sU17aQWIXSuaVzTy9yrjwDfSZxeBN7jXMXxRnIj-0LrM_MPIPd-OC0e5nMygWRy3mhwHbwJ7fpzg"},
        'cancelHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv069wYb_gaDqD4_DagQJ3-4BdxhXNETj2SHm_YWowpblmoMpd5zbpRNzuGsCXw-nwja7PX6fe4y8ic_d8Dr10nqSO4CmBHaVu3bbpBu-XuWEMaZ0KOg2mpLjqLFm8TtuM19gAZ9jRGxD9QGnXtduKso0ig2hLQar354WQfq4NjNru_A", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://padelhousecourts.skedda.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://padelhousecourts.skedda.com/booking?viewdate=2022-07-20", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'fetchUrl':'https://padelhousecourts.skedda.com:443/bookingslists?',
        'fetchCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069DHRzzCKzaydsNKIt_JtZjSvvkIacc2GpJlTTrkED5qO8CoYV_S3bgUhCimlCCdJnqTzaq15M3O4ZMnJ-NO_iMCInIKFw3ERhdyolMpY2w1B_PVmkPK_PFI_tTNdUHTpA", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069BtITHyrtLGjrVaUARy7b9QfAJlbAF49_bXbYDLQG9WeipX5nsjgpqJVtU7KVFk5-8ZjpgAEE5yDZi4WEd0p38sf0tKCDDExTb9lU7nfFCXXfEpEohVFclMLZ6QRviM1wQH7dudvZrr_CRK-mSG7s1IXpN8OEO5diwzFogE3182NYvHOhqM62GcouYW_XdQfCqPUzgWX9a6LB5Zs5T-J9YIexg2__lJ5DBBL1BZpD_axhl6mHBIEJZ-Z-KiNBzym_6CiScqfX6awyn3hvX4qdcnozNFvcSizs9krbvJ1nD50P5NJV2kbZyTQsf1j0bU4SlvNyCNnnPQgCbMXGlBQFSBP26y6KKIs1N4bK69dFCocIRUm1f3__a1EjiZV0zfwRzJVLOwtoUStC4g83LrCvP53uJkhtN90028DS_BTKvMjzEVmEyT8QgOLY8V50auvPu-rPSp4wjh7e5Yx4StEGn5pPZAho5iG_u4rri9xItFby-Tey_zwAcUdYPWESNj9UIyTRhyHZ0hRDueqSpb2lRok8x0y7e5peNSjiQahpso4OUscLX0uOvfnp0Y-P-3_1bEBiqGOfKznDYO_XuISVf5uw6vQzA88sU17aQWIXSuaVzTy9yrjwDfSZxeBN7jXMXxRnIj-0LrM_MPIPd-OC0e5nMygWRy3mhwHbwJ7fpzg"},
        'fetchHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv069wYb_gaDqD4_DagQJ3-4BdxhXNETj2SHm_YWowpblmoMpd5zbpRNzuGsCXw-nwja7PX6fe4y8ic_d8Dr10nqSO4CmBHaVu3bbpBu-XuWEMaZ0KOg2mpLjqLFm8TtuM19gAZ9jRGxD9QGnXtduKso0ig2hLQar354WQfq4NjNru_A", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://padelhousecourts.skedda.com/booking?viewdate=2022-07-20", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        'fieldsUrl':'https://padelhousecourts.skedda.com:443/webs',
        'fieldsCookies':{"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069DHRzzCKzaydsNKIt_JtZjSvvkIacc2GpJlTTrkED5qO8CoYV_S3bgUhCimlCCdJnqTzaq15M3O4ZMnJ-NO_iMCInIKFw3ERhdyolMpY2w1B_PVmkPK_PFI_tTNdUHTpA", "X-Skedda-ApplicationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv069BtITHyrtLGjrVaUARy7b9QfAJlbAF49_bXbYDLQG9WeipX5nsjgpqJVtU7KVFk5-8ZjpgAEE5yDZi4WEd0p38sf0tKCDDExTb9lU7nfFCXXfEpEohVFclMLZ6QRviM1wQH7dudvZrr_CRK-mSG7s1IXpN8OEO5diwzFogE3182NYvHOhqM62GcouYW_XdQfCqPUzgWX9a6LB5Zs5T-J9YIexg2__lJ5DBBL1BZpD_axhl6mHBIEJZ-Z-KiNBzym_6CiScqfX6awyn3hvX4qdcnozNFvcSizs9krbvJ1nD50P5NJV2kbZyTQsf1j0bU4SlvNyCNnnPQgCbMXGlBQFSBP26y6KKIs1N4bK69dFCocIRUm1f3__a1EjiZV0zfwRzJVLOwtoUStC4g83LrCvP53uJkhtN90028DS_BTKvMjzEVmEyT8QgOLY8V50auvPu-rPSp4wjh7e5Yx4StEGn5pPZAho5iG_u4rri9xItFby-Tey_zwAcUdYPWESNj9UIyTRhyHZ0hRDueqSpb2lRok8x0y7e5peNSjiQahpso4OUscLX0uOvfnp0Y-P-3_1bEBiqGOfKznDYO_XuISVf5uw6vQzA88sU17aQWIXSuaVzTy9yrjwDfSZxeBN7jXMXxRnIj-0LrM_MPIPd-OC0e5nMygWRy3mhwHbwJ7fpzg"},
        'fieldsHeaders':{"Sec-Ch-Ua": "\"Chromium\";v=\"103\", \".Not/A)Brand\";v=\"99\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv06--adb8nwLL1biTArEcuCzGdbKyTvHx4Y_y82Q97n-dq9v-CPYiHZIdUNHrWm03XGew9aKGnsF1sCpweWS9t0iQxb3SJ1fxMgd8cHMaOQxgsbe33UCXWrJX5pFPUZHWsBEMDSUcog58G2LyDcHBigLsyi9q0BCzaLx4qh6dJYLpYw", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://padelhousecourts.skedda.com/booking?viewdate=2022-07-20", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"},
        },
    '':''
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
    apiData = ['Ghazala bay 2','Grand Plaza blue court','Beverly Red Court','Beverly Super Panoramic','Maadi Court 1','Maadi Court 2']
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