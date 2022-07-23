import requests
import json

#Credentails
userEmail = 'mmehrez@easetechinv.com'
userPass = 'dyfse6-heQcom-gyrvab'
loginUrl = 'https://app.skedda.com/account/login'
session = requests.session()

# def login():
#     #Credentails
#     userEmail = 'mmehrez@easetechinv.com'
#     userPass = 'dyfse6-heQcom-gyrvab'
#     LoginCookies = {"X-Skedda-RequestVerificationCookie": "CfDJ8NxpOdIu2RNGqqOeU3Fv06-xgfO4XgMCx2ZYEwIlkzaE0ReeW7LHg-3WK5In3sPzCG9Uo9P4C300i-cICMcWSqkZW1gJ4tKfNfa-7POiu56NE0pwaQCbwqDEUE1O-nERLluZ1KWxpg7DjH5Upv-EFAE"}
#     loginHeaders = {"Sec-Ch-Ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "X-Skedda-Requestverificationtoken": "CfDJ8NxpOdIu2RNGqqOeU3Fv068_NwwJ9hjYwXRFKnvQ2SD2gEwdPYUHBulKY1GhIsw5cLZ2Rk8_y8egi6tPjk2Xnz0tfTi3MpPEAIDVi712SOyr6-jHaGyjw3F9hCzq2yGEeq6IJqsZHq-T4k08KlOOqTg", "Sec-Ch-Ua-Mobile": "?0", "Content-Type": "application/json; charset=UTF-8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Accept": "*/*", "Origin": "https://app.skedda.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://app.skedda.com/account/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
#     LoginJson = {"login": {"arbitraryerrors": None, "password": userPass, "rememberMe": False, "username": userEmail}}
#     loginResult = session.post(loginUrl, headers=loginHeaders, cookies=LoginCookies, json=LoginJson)
#     print(loginResult.text)



def book(timeFrom,timeTo,spaces,title,subDomainData):
    bookUrl = subDomainData['subUrl']
    bookCookies = subDomainData['subCookies']
    bookHeaders = subDomainData['subHeaders']
    bookJson=subDomainData['subJson']
    replaceNewAtt = bookJson['booking']
    replaceNewAtt['start'] = timeFrom
    replaceNewAtt['end'] = timeTo
    replaceNewAtt['spaces'] = spaces
    replaceNewAtt['title'] = title
    bookJson['booking'] = replaceNewAtt
    bookResult = session.post(bookUrl, headers=bookHeaders, cookies=bookCookies, json=bookJson)
    if bookResult.status_code == 200:
        data = bookResult.text
        data = json.loads(data)
        data = data['booking']
        bookID = data['id']
        print('Booked Successfully')
        return bookID
    else:
        print('-- Error ---')
        print(bookResult.text)
        return 0
        
    
def cancel(bookID,subDomain):
    cancelUrl = subDomain['cancelUrl']+bookID
    cancelCookies = subDomain['cancelCookies']
    #cancelHeaders = Cookies
    cancelHeaders = subDomain['cancelHeaders']
    CancelResult = session.delete(cancelUrl, headers=cancelHeaders, cookies=cancelCookies)
    if CancelResult.status_code == 204:
        print('Booking Cancled')
        return True
    else:
        print('error')
        return False


def fetchBooking(timeEndFrom,dateEndFrom,timeStartTo,dateStartTo,subDomainData):
    queryStart = dateStartTo+'T'+timeStartTo
    queryEnd = dateEndFrom+'T'+timeEndFrom
    fetchUrl = subDomainData['fetchUrl']
    urlQuery = 'end={End}&start={Start}'.format(End = queryEnd, Start = queryStart)
    fetchUrl += urlQuery
    fetchHeaders = subDomainData['fetchHeaders']
    fetchCookies = subDomainData['fetchCookies']
    fetchResults = session.get(fetchUrl, headers=fetchHeaders, cookies=fetchCookies)
    if fetchResults.status_code == 200:
        return fetchResults.text
    else:
        print('Error')
        return 0

def fetchIds(subDomainData):
    fetchUrl = subDomainData['fieldsUrl']
    fetchHeaders = subDomainData['fieldsHeaders']
    fetchCookies = subDomainData['fieldsCookies']
    fetchResults = session.get(fetchUrl, headers=fetchHeaders, cookies=fetchCookies)
    if fetchResults.status_code == 200:
        print('Data Fetched')
        return fetchResults.text
    else:
        print('Error')
        return 0





    





