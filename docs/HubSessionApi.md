# gu_rest_api.HubSessionApi

All URIs are relative to *http://127.0.0.1:61622*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_hub_session_peers**](HubSessionApi.md#add_hub_session_peers) | **POST** /sessions/{sessionId}/peers | Manually adds peers to hub session
[**create_hub_session**](HubSessionApi.md#create_hub_session) | **POST** /sessions | Creates new hub session.
[**get_hub_session**](HubSessionApi.md#get_hub_session) | **GET** /sessions/{sessionId} | Gets hub session info
[**get_hub_session_config**](HubSessionApi.md#get_hub_session_config) | **GET** /sessions/{sessionId}/config | Gets configuration from stash
[**list_hub_sessions**](HubSessionApi.md#list_hub_sessions) | **GET** /sessions | Lists current hub sessions.
[**sessions_session_id_delete**](HubSessionApi.md#sessions_session_id_delete) | **DELETE** /sessions/{sessionId} | 
[**sessions_session_id_patch**](HubSessionApi.md#sessions_session_id_patch) | **PATCH** /sessions/{sessionId} | Hub session update
[**set_hub_session_config**](HubSessionApi.md#set_hub_session_config) | **PUT** /sessions/{sessionId}/config | Sets configuration stash


# **add_hub_session_peers**
> list[str] add_hub_session_peers(session_id, request_body)

Manually adds peers to hub session

### Example

* Api Key Authentication (serviceToken): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: serviceToken
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
request_body = NULL # list[str] | 

try:
    # Manually adds peers to hub session
    api_response = api_instance.add_hub_session_peers(session_id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->add_hub_session_peers: %s\n" % e)
```


* Api Key Authentication (systemName): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
request_body = NULL # list[str] | 

try:
    # Manually adds peers to hub session
    api_response = api_instance.add_hub_session_peers(session_id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->add_hub_session_peers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **request_body** | [**list[str]**](list.md)|  | 

### Return type

**list[str]**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hub_session**
> str create_hub_session(hub_session=hub_session)

Creates new hub session.

Allowed fileds:  * name        - human readable session name * expires     - session expiration timestamp * allocation  - resource allocation mode.

### Example

* Api Key Authentication (serviceToken): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: serviceToken
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
hub_session = gu_rest_api.HubSession() # HubSession |  (optional)

try:
    # Creates new hub session.
    api_response = api_instance.create_hub_session(hub_session=hub_session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->create_hub_session: %s\n" % e)
```


* Api Key Authentication (systemName): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
hub_session = gu_rest_api.HubSession() # HubSession |  (optional)

try:
    # Creates new hub session.
    api_response = api_instance.create_hub_session(hub_session=hub_session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->create_hub_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_session** | [**HubSession**](HubSession.md)|  | [optional] 

### Return type

**str**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_session**
> HubSession get_hub_session(session_id)

Gets hub session info

### Example

* Api Key Authentication (serviceToken): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: serviceToken
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # Gets hub session info
    api_response = api_instance.get_hub_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->get_hub_session: %s\n" % e)
```


* Api Key Authentication (systemName): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # Gets hub session info
    api_response = api_instance.get_hub_session(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->get_hub_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 

### Return type

[**HubSession**](HubSession.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_session_config**
> ConfigStash get_hub_session_config(session_id)

Gets configuration from stash

### Example

* Api Key Authentication (serviceToken): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: serviceToken
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # Gets configuration from stash
    api_response = api_instance.get_hub_session_config(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->get_hub_session_config: %s\n" % e)
```


* Api Key Authentication (systemName): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    # Gets configuration from stash
    api_response = api_instance.get_hub_session_config(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->get_hub_session_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 

### Return type

[**ConfigStash**](ConfigStash.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hub_sessions**
> list[HubSession] list_hub_sessions(limit=limit, offset=offset)

Lists current hub sessions.

### Example

* Api Key Authentication (serviceToken): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: serviceToken
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
limit = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)

try:
    # Lists current hub sessions.
    api_response = api_instance.list_hub_sessions(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->list_hub_sessions: %s\n" % e)
```


* Api Key Authentication (systemName): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
limit = 50 # int |  (optional) (default to 50)
offset = 0 # int |  (optional) (default to 0)

try:
    # Lists current hub sessions.
    api_response = api_instance.list_hub_sessions(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->list_hub_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**list[HubSession]**](HubSession.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_delete**
> sessions_session_id_delete(session_id)



### Example

* Api Key Authentication (serviceToken): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: serviceToken
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    api_instance.sessions_session_id_delete(session_id)
except ApiException as e:
    print("Exception when calling HubSessionApi->sessions_session_id_delete: %s\n" % e)
```


* Api Key Authentication (systemName): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id

try:
    api_instance.sessions_session_id_delete(session_id)
except ApiException as e:
    print("Exception when calling HubSessionApi->sessions_session_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sessions_session_id_patch**
> sessions_session_id_patch(session_id, hub_session_command=hub_session_command)

Hub session update

### Example

* Api Key Authentication (serviceToken): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: serviceToken
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
hub_session_command = gu_rest_api.HubSessionCommand() # HubSessionCommand |  (optional)

try:
    # Hub session update
    api_instance.sessions_session_id_patch(session_id, hub_session_command=hub_session_command)
except ApiException as e:
    print("Exception when calling HubSessionApi->sessions_session_id_patch: %s\n" % e)
```


* Api Key Authentication (systemName): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
hub_session_command = gu_rest_api.HubSessionCommand() # HubSessionCommand |  (optional)

try:
    # Hub session update
    api_instance.sessions_session_id_patch(session_id, hub_session_command=hub_session_command)
except ApiException as e:
    print("Exception when calling HubSessionApi->sessions_session_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **hub_session_command** | [**HubSessionCommand**](HubSessionCommand.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_hub_session_config**
> dict(str, object) set_hub_session_config(session_id, request_body)

Sets configuration stash

### Example

* Api Key Authentication (serviceToken): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: serviceToken
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APIKEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APIKEY'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
request_body = NULL # dict(str, object) | New config stash value

try:
    # Sets configuration stash
    api_response = api_instance.set_hub_session_config(session_id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->set_hub_session_config: %s\n" % e)
```


* Api Key Authentication (systemName): 
```python
from __future__ import print_function
import time
import gu_rest_api
from gu_rest_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: systemName
configuration = gu_rest_api.Configuration()
configuration.api_key['X-GU-APPNAME'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-GU-APPNAME'] = 'Bearer'

# create an instance of the API class
api_instance = gu_rest_api.HubSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
request_body = NULL # dict(str, object) | New config stash value

try:
    # Sets configuration stash
    api_response = api_instance.set_hub_session_config(session_id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubSessionApi->set_hub_session_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **request_body** | [**dict(str, object)**](object.md)| New config stash value | 

### Return type

**dict(str, object)**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

