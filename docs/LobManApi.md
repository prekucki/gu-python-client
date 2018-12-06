# gu_rest_api.LobManApi

All URIs are relative to *http://127.0.0.1:61622*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_blob**](LobManApi.md#upload_blob) | **PUT** /sessions/{sessionId}/blobs/{blobId} | Uploads a binary content to the hub.


# **upload_blob**
> upload_blob(session_id, blob_id, body=body)

Uploads a binary content to the hub.

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
api_instance = gu_rest_api.LobManApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
blob_id = 'blob_id_example' # str | Blob identifier
body = '/path/to/file' # file |  (optional)

try:
    # Uploads a binary content to the hub.
    api_instance.upload_blob(session_id, blob_id, body=body)
except ApiException as e:
    print("Exception when calling LobManApi->upload_blob: %s\n" % e)
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
api_instance = gu_rest_api.LobManApi(gu_rest_api.ApiClient(configuration))
session_id = 56 # int | HUB session id
blob_id = 'blob_id_example' # str | Blob identifier
body = '/path/to/file' # file |  (optional)

try:
    # Uploads a binary content to the hub.
    api_instance.upload_blob(session_id, blob_id, body=body)
except ApiException as e:
    print("Exception when calling LobManApi->upload_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **int**| HUB session id | 
 **blob_id** | **str**| Blob identifier | 
 **body** | **file**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

