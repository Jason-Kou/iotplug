import requests
import sys

def control_plug(command):
    # define command-line parameters
    # replace with your own endpoint url and put your own certifications in the my_thing folder
    endpoint = "abcdef12345-ats.iot.us-west-2.amazonaws.com"
    topic = "topic_1"
    cert = "iotplug/my_thing/device.pem.crt"
    key = "iotplug/my_thing/private.pem.key"
    message = command


    # create and format values for HTTPS request
    publish_url = 'https://' + endpoint + ':8443/topics/' + topic + '?qos=1'
    publish_msg = message.encode('utf-8')

    # make request
    # print([cert, key])
    publish = requests.request('POST',
                publish_url,
                data=publish_msg,
                cert=[cert, key])

    # print results
    print("Response status: ", str(publish.status_code))
    if publish.status_code == 200:
            # print("Response body:", publish.text)
            return("Response body:", publish.text)
    
if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None
    return_val = control_plug("turn_off")