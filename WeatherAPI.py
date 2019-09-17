import requests

CREDENTIALS = {'API_KEY':'INSERT_ACTUAL_KEY_HERE'}


def createSession():
    return requests.Session()


def authenticateSession(api_key, session_object):
    """ Authenticate Session Object with given API Key
    :param api_key: API Access Key
    :param session_object: Session Object
    :return:
    """
    try:
        session_object.auth(api_key)
    except:
        print('Error, API Key was rejected.')


def CheckResponse(code):
    """ Analyze the given response code.
    :param code: Integer value
    :return: String response describing API response code
    """
    response_codes = {200:'Success',
                      301:'Server Redirecting to new endpoint.',
                      401:'Credentials Not Authenticated',
                      400:'Bad Request',
                      403:'Access forbidden, check permissions',
                      404:'Resource Not Found'
                     }
    try:
        print(f'Code:{code} -> {response_codes[code]}')
        return code
    except:
        print('Error, the response code is not documented here. Google it.')


def Make_API_Request():
    """ Make API Query
    :return:
    """
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID='+CREDENTIALS['API_KEY'])
    print('Attempting to Query API...')
    CheckResponse(response.status_code)
    if response.status_code==200:
        print('Success.')
    else:
        print('Error, could not access API resources. Resolve issue.')


if __name__=="__main__":
    Make_API_Request()
    authenticateSession(CREDENTIALS['API_KEY'], createSession())
