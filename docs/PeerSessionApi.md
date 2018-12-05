# gu_rest_api.PeerSessionApi

All URIs are relative to *http://127.0.0.1:61622*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_peer_session**](PeerSessionApi.md#create_peer_session) | **POST** /sessions/{sessionId}/peers/{nodeId}/deployments | Creates new deploymnet
[**delete_peer_session**](PeerSessionApi.md#delete_peer_session) | **DELETE** /sessions/{sessionId}/peers/{nodeId}/deployments/{deploymentId} | 
[**update_peer_session**](PeerSessionApi.md#update_peer_session) | **PATCH** /sessions/{sessionId}/peers/{nodeId}/deployments/{deploymentId} | Sends multiple commands for peer


# **create_peer_session**
> str create_peer_session(session_id, node_id, peer_session_spec)

Creates new deploymnet

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
api_instance = gu_rest_api.PeerSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
peer_session_spec = gu_rest_api.PeerSessionSpec() # PeerSessionSpec | 

try:
    # Creates new deploymnet
    api_response = api_instance.create_peer_session(session_id, node_id, peer_session_spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerSessionApi->create_peer_session: %s\n" % e)
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
api_instance = gu_rest_api.PeerSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
peer_session_spec = gu_rest_api.PeerSessionSpec() # PeerSessionSpec | 

try:
    # Creates new deploymnet
    api_response = api_instance.create_peer_session(session_id, node_id, peer_session_spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeerSessionApi->create_peer_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **node_id** | **str**| GU Network node identifier | 
 **peer_session_spec** | [**PeerSessionSpec**](PeerSessionSpec.md)|  | 

### Return type

**str**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_peer_session**
> delete_peer_session(session_id, node_id, deployment_id)



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
api_instance = gu_rest_api.PeerSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 

try:
    api_instance.delete_peer_session(session_id, node_id, deployment_id)
except ApiException as e:
    print("Exception when calling PeerSessionApi->delete_peer_session: %s\n" % e)
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
api_instance = gu_rest_api.PeerSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 

try:
    api_instance.delete_peer_session(session_id, node_id, deployment_id)
except ApiException as e:
    print("Exception when calling PeerSessionApi->delete_peer_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **node_id** | **str**| GU Network node identifier | 
 **deployment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_peer_session**
> update_peer_session(session_id, node_id, deployment_id, command)

Sends multiple commands for peer

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
api_instance = gu_rest_api.PeerSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 
command = NULL # list[Command] | 

try:
    # Sends multiple commands for peer
    api_instance.update_peer_session(session_id, node_id, deployment_id, command)
except ApiException as e:
    print("Exception when calling PeerSessionApi->update_peer_session: %s\n" % e)
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
api_instance = gu_rest_api.PeerSessionApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 
command = NULL # list[Command] | 

try:
    # Sends multiple commands for peer
    api_instance.update_peer_session(session_id, node_id, deployment_id, command)
except ApiException as e:
    print("Exception when calling PeerSessionApi->update_peer_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **node_id** | **str**| GU Network node identifier | 
 **deployment_id** | **str**|  | 
 **command** | [**list[Command]**](list.md)|  | 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

