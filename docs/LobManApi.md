# gu_rest_api.LobManApi

All URIs are relative to *http://127.0.0.1:61622*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_blob**](LobManApi.md#create_blob) | **POST** /sessions/{sessionId}/blob | Creates new lob
[**download_blob**](LobManApi.md#download_blob) | **GET** /sessions/{sessionId}/blob/{blobId} | 
[**list_hub_session_blobs**](LobManApi.md#list_hub_session_blobs) | **GET** /sessions/{sessionId}/blob | Lists currently allocated lobs
[**upload_blob**](LobManApi.md#upload_blob) | **PUT** /sessions/{sessionId}/blob/{blobId} | 


# **create_blob**
> str create_blob(session_id)

Creates new lob

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
session_id = 'session_id_example' # str | 

try:
    # Creates new lob
    api_response = api_instance.create_blob(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobManApi->create_blob: %s\n" % e)
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
session_id = 'session_id_example' # str | 

try:
    # Creates new lob
    api_response = api_instance.create_blob(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobManApi->create_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

**str**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_blob**
> file download_blob(session_id, blob_id)



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
session_id = 'session_id_example' # str | 
blob_id = 'blob_id_example' # str | Blob identifier

try:
    api_response = api_instance.download_blob(session_id, blob_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobManApi->download_blob: %s\n" % e)
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
session_id = 'session_id_example' # str | 
blob_id = 'blob_id_example' # str | Blob identifier

try:
    api_response = api_instance.download_blob(session_id, blob_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobManApi->download_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **blob_id** | **str**| Blob identifier | 

### Return type

**file**

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hub_session_blobs**
> list[BlobInfo] list_hub_session_blobs(session_id)

Lists currently allocated lobs

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
session_id = 'session_id_example' # str | 

try:
    # Lists currently allocated lobs
    api_response = api_instance.list_hub_session_blobs(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobManApi->list_hub_session_blobs: %s\n" % e)
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
session_id = 'session_id_example' # str | 

try:
    # Lists currently allocated lobs
    api_response = api_instance.list_hub_session_blobs(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LobManApi->list_hub_session_blobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

### Return type

[**list[BlobInfo]**](BlobInfo.md)

### Authorization

[serviceToken](../README.md#serviceToken), [systemName](../README.md#systemName)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_blob**
> upload_blob(session_id, blob_id, body=body)



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
session_id = 'session_id_example' # str | 
blob_id = 'blob_id_example' # str | Blob identifier
body = '/path/to/file' # file |  (optional)

try:
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
session_id = 'session_id_example' # str | 
blob_id = 'blob_id_example' # str | Blob identifier
body = '/path/to/file' # file |  (optional)

try:
    api_instance.upload_blob(session_id, blob_id, body=body)
except ApiException as e:
    print("Exception when calling LobManApi->upload_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
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

