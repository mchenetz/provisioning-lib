#######################################################################################################################
# Cisco Meraki Provisioning API Python 3.x Module
#
# Overview
# The purpose of this Python module is to provide a standard Python module to interact with the Meraki Provisioning API.
# Each method in this function interacts seamlessly with the API and either returns data from the method call or a
# status message indicating the result of the API call
#
# Dependencies
# - Python 3.x
# - 'requests' module
#
#######################################################################################################################
import json
import requests
from merakilibs import tzlist, getUrl


def getorgdevices(apikey, organizationid):
    geturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/inventory'.format(str(organizationid))
    return getUrl(geturl, apikey)

def getnetworkdevices(apikey, networkid):
    geturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/devices'.format(str(networkid))
    return getUrl(geturl, apikey)

def getorgadmins(apikey, organizationid):
    geturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/admins'.format(str(organizationid))
    return getUrl(geturl, apikey)

def getnetworklist(apikey, organizationid):
    geturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/networks'.format(str(organizationid))
    return getUrl(geturl, apikey)

def getlicensestate(apikey, organizationid):
    geturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/licenseState'.format(str(organizationid))
    return getUrl(geturl, apikey)

def getdevicedetail(apikey, networkid, serialnumber):
    geturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/devices/{1}'.format(str(networkid), str(serialnumber))
    return getUrl(geturl, apikey)

def getnetworkdetail(apikey, networkid):
    geturl = 'https://dashboard.meraki.com/api/v0/networks/{0}'.format(str(networkid))
    return getUrl(geturl, apikey)

def getconfigtemplates(apikey, organizationid):
    geturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/configTemplates'.format(str(organizationid))
    return getUrl(geturl, apikey)

def getsnmpsettings(apikey, organizationid):
    geturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/snmp'.format(str(organizationid))
    return getUrl(geturl, apikey)

def getvpnpeers(apikey, networkid):
    geturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/siteToSiteVpn'.format(str(networkid))
    return getUrl(geturl, apikey)

def getsamlroles(apikey, organizationid):
    geturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/samlRoles'.format(str(organizationid))
    return getUrl(geturl, apikey)

def getswitchstacks(apikey, networkid):
    geturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/switchStacks'.format(str(networkid))
    return getUrl(geturl, apikey)

def getswitchstackmembers(apikey, networkid, stackid):
    geturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/switchStacks/{1}'.format(str(networkid), str(stackid))
    return getUrl(geturl, apikey)

def getvlans(apikey, networkid):
    geturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/vlans'.format(str(networkid))
    return getUrl(geturl, apikey)

def getvlandetail(apikey, networkid, vlanid):
    geturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/vlans/{1}'.format(str(networkid), str(vlanid))
    return getUrl(geturl, apikey)

def gettemplates(apikey, organizationid):
    geturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/configTemplates'.format(str(organizationid))
    return getUrl(geturl, apikey)

def getnonmerakivpnpeers(apikey, organizationid):
    geturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/thirdPartyVPNPeers'.format(str(organizationid))
    return getUrl(geturl, apikey)

def getadmins(apikey, organizationid):
    geturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/admins'.format(str(organizationid))
    return getUrl(geturl, apikey)

def getNetworkbyName(name, apikey, organizationid):
 for net in getnetworklist(apikey, organizationid):
     if net['name']==name:
         return (net['id'])


def bindtotemplate(apikey, networkid, templateid, autobind='false'):
    posturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/bind'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    putdata = {
        'configTemplateId': format(str(templateid)),
        'autobind': format(str(autobind))
    }
    dashboard = requests.post(posturl, data=json.dumps(putdata), headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    elif statuscode == '200':
        print('Network ID {0} bound to configuration template ID {1}'.format(str(networkid), str(templateid)))
        return None


def unbindfromtemplate(apikey, networkid):
    posturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/unbind'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.post(posturl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    elif statuscode == '200':
        print('Network ID {0} unbound from configuration template'.format(str(networkid)))
        return None


def deltemplate(apikey, organizationid, templateid):
    delurl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/configTemplates/{1}'.format(str(organizationid),
                                                                                                str(templateid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.delete(delurl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 404 is specifically returned, inform that configuration template does not exist
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 204:
        print('Deleted template {0} from Organization ID {1}'.format(str(templateid), str(organizationid)))
        return None
    elif dashboard.status_code == 404:
        print('Configuration Template ID {0} cannot be found, please confirm ID'.format(str(templateid)))
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print('Deletion of Template ID {0} unsuccessful - HTTP Status Code: {1}'.format(str(templateid),
                                                                                        str(statuscode)))
        return None


def updatevlan(apikey, networkid, vlanid, vlanname, mxip, subnetip):
    puturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/vlans/{1}'.format(str(networkid), str(vlanid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    putdata = {
        'name': format(str(vlanname)),
        'applianceIp': format(str(mxip)),
        'subnet': format(str(subnetip))
    }
    putdata = json.dumps(putdata)
    dashboard = requests.put(puturl, data=putdata, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print(statuscode)
        return json.loads(dashboard.text)


def addvlan(apikey, networkid, vlanid, vlanname, mxip, subnetip):
    posturl = 'https://dashboard.meraki.com/api/v0/networks/{0}/vlans'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    postdata = {
        'id': format(str(vlanid)),
        'name': format(str(vlanname)),
        'applianceIp': format(str(mxip)),
        'subnet': format(str(subnetip))
    }
    postdata = json.dumps(postdata)
    dashboard = requests.post(posturl, data=postdata, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 201:
        print('Added VLAN {0} to MX'.format(str(vlanid)))
        return None
    elif dashboard.status_code == 400:
        print('Network is bound to a template - Unable to delete VLAN')
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print(statuscode)
        return None


def delvlan(apikey, networkid, vlanid):
    delurl = 'https://dashboard.meraki.com/api/v0/networks/{0}/vlans/{1}'.format(str(networkid), str(vlanid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.delete(delurl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 204:
        print('Deleted VLAN {0} from MX'.format(str(vlanid)))
        return None
    elif dashboard.status_code == 400:
        print('Network is bound to a template - Unable to delete VLAN')
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None


def addadmin(apikey, organizationid, email, name, orgaccess=None, tags=None, tagaccess=None, networks=None,
             netaccess=None):
    posturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/admins'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }

    posttags = []

    if orgaccess is None and tags is None and networks is None:
        print("Administrator accounts must be granted access to either the Organization, Networks, or Tags")
        return None

    if tags is not None and tagaccess is None:
        print("If tags are defined you must define matching access arguments.\nFor example, tags = ['tag1', 'tag2'], "
              "must have matching access arguments: tagaccess = 'full', 'read-only'")
        return None
    elif tagaccess is not None and tags is None:
        print("If tag access levels are defined you must define matching tag arguments\nFor example, tags = "
              "['tag1', 'tag2'] must have matching access arguments: tagaccess = 'full', 'read-only'")
        return None
    elif tagaccess is None and tags is None:
        pass
    elif len(tags) != len(tagaccess):
        print("The number of tags and access arguments must match.\n")
        print("For example, tags = ['tag1', 'tag2'] must have matching access arguments: tagaccess = "
              "['full', 'read-only']")
        return None
    elif tags is not None and tagaccess is not None:
        x = 0
        while x < len(tags):
            posttags.append({'tag': tags[x], 'access': tagaccess[x]})
            x += 1
    else:
        pass

    postnets = []

    if networks is not None and netaccess is None:
        print("If networks are defined you must define matching access arguments\nFor example networks = "
              "['net1', 'net2'] must have matching access arguments: netaccess = 'full', 'read-only'")
        return None
    elif netaccess is not None and networks is None:
        print("If network access levels are defined you must define matching network arguments\nFor example, networks"
              " = ['net1', 'net2'] must have matching access arguments: netaccess = 'full', 'read-only'")
        return None
    elif netaccess is None and networks is None:
        pass
    elif len(networks) != len(netaccess):
        print("The number of networks and access arguments must match.\n")
        print("For example, networks = ['net1', 'net2'] must have matching access arguments: netaccess = "
              "['full', 'read-only']")
        return None
    elif networks is not None and netaccess is not None:
        x = 0
        while x < len(networks):
            postnets.append({'id': networks[x], 'access': netaccess[x]})
            x += 1
    else:
        pass
    postdata = []
    if len(posttags) == 0 and len(postnets) == 0:
        postdata = {
            'orgAccess': orgaccess,
            'email': format(str(email)),
            'name': format(str(name))
        }

    elif len(posttags) > 0 and len(postnets) == 0:
        postdata = {
            'name': format(str(name)),
            'email': format(str(email)),
            'orgAccess': orgaccess,
            'tags': posttags
        }

    elif len(postnets) > 0 and len(posttags) == 0:
        postdata = {
            'name': format(str(name)),
            'email': format(str(email)),
            'orgAccess': orgaccess,
            'networks': postnets
        }

    elif len(postnets) > 0 and len(posttags) > 0:
        postdata = {
            'name': format(str(name)),
            'email': format(str(email)),
            'orgAccess': orgaccess,
            'tags': posttags,
            'networks': postnets
        }
    dashboard = requests.post(posturl, data=json.dumps(postdata), headers=headers)
    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 201:
        print('Added Administrator {0} to Organization ID {1}'.format(str(email), str(organizationid)))
        return None
    elif dashboard.status_code == 400:
        print('Unable to add administrator')
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print(statuscode)
        return None


def deladmin(apikey, organizationid, adminid):
    delurl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/admins/{1}'.format(str(organizationid),
                                                                                       str(adminid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.delete(delurl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 204:
        print('Deleted Admin ID {0} from Organization ID {1}'.format(str(adminid), str(organizationid)))
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None



def addnetwork(apikey, organizationid, name, nettype, tags, tz):
    posturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/networks'.format(str(organizationid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }

    validtz = False
    for zone in tzlist:
        if validtz is False and format(str(tz)) == zone:
            validtz = True
            break
        else:
            validtz = False

    if validtz is False:
        print('Please enter a valid tz value from https://en.wikipedia.org/wiki/List_of_tz_database_time_zones')
        return None

    postdata = {
        'name': format(str(name)),
        'type': format(str(nettype)),
        'tags': format(str(tags)),
        'timeZone': format(str(tz))
    }
    postdata = json.dumps(postdata)
    dashboard = requests.post(posturl, data=postdata, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 201:
        print('Added Network {0} to Organization'.format(str(name)))
        return json.loads(dashboard.text)
    elif dashboard.status_code == 400:
        print('A network with the name "{0}" already exists in the organization'.format(str(name)))
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print('An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'
              .format(str(statuscode)))
        return None
    else:
        print('Unknown error - HTTP Status Code {0}'.format(str(statuscode)))
        return None


def delnetwork(apikey, networkid):
    delurl = 'https://dashboard.meraki.com/api/v0/networks/{0}'.format(str(networkid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    dashboard = requests.delete(delurl, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    # If HTTP 400 is specifically returned, inform that network is currently bound to a template
    #

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 204:
        print('Deleted Network ID {0} from Organization'.format(str(networkid)))
        return None
    elif dashboard.status_code == 404:
        print('Network ID {0} does not exist, please enter a valid network ID')
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None


def updateadmin(apikey, organizationid, adminid, email, name=None, orgaccess=None, tags=None, tagaccess=None,
                networks=None, netaccess=None):

    puturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/admins/{1}'.format(str(organizationid),
                                                                                       str(adminid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
        }

    puttags = []

    if orgaccess is None and tags is None and networks is None and name is None:
        print("Administrator account updates must include Organization, Networks, or Tags permission changes or an "
              "updated name attribute")
        return None

    if tags is not None and tagaccess is None:
        print("If tags are defined you must define matching access arguments.\nFor example, tags = ['tag1', 'tag2'], "
              "must have matching access arguments: tagaccess = 'full', 'read-only'")
        return None
    elif tagaccess is not None and tags is None:
        print("If tag access levels are defined you must define matching tag arguments\nFor example, tags = "
              "['tag1', 'tag2'] must have matching access arguments: tagaccess = 'full', 'read-only'")
        return None
    elif tagaccess is None and tags is None:
        pass
    elif len(tags) != len(tagaccess):
        print("The number of tags and access arguments must match.\n")
        print("For example, tags = ['tag1', 'tag2'] must have matching access arguments: tagaccess = "
              "['full', 'read-only']")
        return None
    elif tags is not None and tagaccess is not None:
        x = 0
        while x < len(tags):
            puttags.append({'tag': tags[x], 'access': tagaccess[x]})
            x += 1
    else:
        pass

    putnets = []

    if networks is not None and netaccess is None:
        print("If networks are defined you must define matching access arguments\nFor example networks = "
              "['net1', 'net2'] must have matching access arguments: netaccess = 'full', 'read-only'")
        return None
    elif netaccess is not None and networks is None:
        print("If network access levels are defined you must define matching network arguments\nFor example, networks"
              " = ['net1', 'net2'] must have matching access arguments: netaccess = 'full', 'read-only'")
        return None
    elif netaccess is None and networks is None:
        pass
    elif len(networks) != len(netaccess):
        print("The number of networks and access arguments must match.\n")
        print("For example, networks = ['net1', 'net2'] must have matching access arguments: netaccess = "
              "['full', 'read-only']")
        return None
    elif networks is not None and netaccess is not None:
        x = 0
        while x < len(networks):
            putnets.append({'id': networks[x], 'access': netaccess[x]})
            x += 1
    else:
        pass
    putdata = []
    if name is not None:
        if len(puttags) == 0 and len(putnets) == 0:
            putdata = {
                'orgAccess': orgaccess,
                'email': format(str(email)),
                'name': format(str(name))
            }

        elif len(puttags) > 0 and len(putnets) == 0:
            putdata = {
                'name': format(str(name)),
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'tags': puttags
                }

        elif len(putnets) > 0 and len(puttags) == 0:
            putdata = {
                'name': format(str(name)),
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'networks': putnets
                }

        elif len(putnets) > 0 and len(puttags) > 0:
            putdata = {
                'name': format(str(name)),
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'tags': puttags,
                'networks': putnets
                }
    elif name is None:
        if len(puttags) > 0 and len(putnets) == 0:
            putdata = {
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'tags': puttags
                }

        elif len(putnets) > 0 and len(puttags) == 0:
            putdata = {
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'networks': putnets
                }

        elif len(putnets) > 0 and len(puttags) > 0:
            putdata = {
                'email': format(str(email)),
                'orgAccess': orgaccess,
                'tags': puttags,
                'networks': putnets
                }
    print(puturl, putdata)
    dashboard = requests.put(puturl, data=json.dumps(putdata), headers=headers)
#
# Check for HTTP 4XX/5XX response code.
# If 4XX/5XX response code, print error message with response code and return None from function
# If HTTP 400 is specifically returned, inform that network is currently bound to a template
#

    statuscode = format(str(dashboard.status_code))

    if dashboard.status_code == 200:
        print('Successfully modified Administrator {0} in Organization ID {1}'.format(str(email), str(organizationid)))
        return None
    elif dashboard.status_code == 400:
        print('Unable to modify Administrator')
        return None
    elif statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print(statuscode)
        return None


def updatenonmerakivpn(apikey, orgid, peername, peerip, secret, remotenets, tags):
    puturl = 'https://dashboard.meraki.com/api/v0/organizations/{0}/thirdPartyVPNPeers'.format(str(orgid))
    headers = {
        'x-cisco-meraki-api-key': format(str(apikey)),
        'Content-Type': 'application/json'
    }
    putdata = {
        'name': format(str(peername)),
        'publicIp': format(str(peerip)),
        'privateSubnets': remotenets,
        'secret': format(str(secret)),
        'tags': tags
    }
    print(putdata)
    print(puturl)
    putdata = json.dumps(putdata)
    dashboard = requests.put(puturl, data=putdata, headers=headers)

    #
    # Check for HTTP 4XX/5XX response code.
    # If 4XX/5XX response code, print error message with response code and return None from function
    #

    statuscode = format(str(dashboard.status_code))
    if statuscode[:1] == '4' or statuscode[:1] == '5':
        print(
            'An error has occurred accessing the Meraki Dashboard API - HTTP Status Code: {0}'.format(str(statuscode)))
        return None
    else:
        print(statuscode)
        return json.loads(dashboard.text)


