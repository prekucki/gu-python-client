# gu_rest_api.DefaultApi

All URIs are relative to *http://127.0.0.1:61622*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peers_node_id_deployments_get**](DefaultApi.md#peers_node_id_deployments_get) | **GET** /peers/{nodeId}/deployments | 
[**peers_node_id_deployments_post**](DefaultApi.md#peers_node_id_deployments_post) | **POST** /peers/{nodeId}/deployments | 


# **peers_node_id_deployments_get**
> list[PeerSessionSpec] peers_node_id_deployments_get(node_id, deployment_id)



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
api_instance = gu_rest_api.DefaultApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 

try:
    api_response = api_instance.peers_node_id_deployments_get(node_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->peers_node_id_deployments_get: %s\n" % e)
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
api_instance = gu_rest_api.DefaultApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 

try:
    api_response = api_instance.peers_node_id_deployments_get(node_id, deployment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->peers_node_id_deployments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| GU Network node identifier | 
 **deployment_id** | **str**|  | 

### Return type

[**list[PeerSessionSpec]**](PeerSessionSpec.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peers_node_id_deployments_post**
> str peers_node_id_deployments_post(node_id, deployment_id, peer_session_spec)



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
api_instance = gu_rest_api.DefaultApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 
peer_session_spec = gu_rest_api.PeerSessionSpec() # PeerSessionSpec | 

try:
    api_response = api_instance.peers_node_id_deployments_post(node_id, deployment_id, peer_session_spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->peers_node_id_deployments_post: %s\n" % e)
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
api_instance = gu_rest_api.DefaultApi(gu_rest_api.ApiClient(configuration))
node_id = 'node_id_example' # str | GU Network node identifier
deployment_id = 'deployment_id_example' # str | 
peer_session_spec = gu_rest_api.PeerSessionSpec() # PeerSessionSpec | 

try:
    api_response = api_instance.peers_node_id_deployments_post(node_id, deployment_id, peer_session_spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->peers_node_id_deployments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| GU Network node identifier | 
 **deployment_id** | **str**|  | 
 **peer_session_spec** | [**PeerSessionSpec**](PeerSessionSpec.md)|  | 

### Return type

**str**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

