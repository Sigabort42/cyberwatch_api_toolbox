# Cyberwatch API Toolbox documentation

## Available methods

#### Ping

Send a GET request to `/api/v2/ping` to validate that the API is working.

###### Usage example and expected result:

```python
>>> CBWApi(URL, API_KEY, SECRET_KEY).ping()
INFO:root:OK
True
```

#### Servers

Send a GET request to `/api/v2/servers` to retrieve the list of all servers.

###### Usage example and expected result:

```python
>>> CBWApi(URL, API_KEY, SECRET_KEY).servers()
[<cbw_api_toolbox.cbw_objects.cbw_server.CBWServer ...]
```

#### Server

Send a GET request to `/api/v2/servers/{SERVER_ID}` to retrieve the information of SERVER_ID.

##### Usage example and expected result:

```python
>>> CBWApi(URL, API_KEY, SECRET_KEY).server(SERVER_ID)
[<cbw_api_toolbox.cbw_objects.cbw_server.CBWServer]
```

#### Update server

Send a PATCH request  `/api/v2/servers/{SERVER_ID}` to update the information of SERVER_ID.

```python
>>> CBWApi(URL, API_KEY, SECRET_KEY).update_server(SERVER_ID, INFO)
>>>True
```

#### Delete server

Send a DELETE request `/api/v2/servers/{SERVER_ID}` to delete SERVER_ID.

```python
>>> CBWApi(URL, API_KEY, SECRET_KEY).delete_server(SERVER_ID)
>>>True
```

#### Remote accesses

Send a GET request `/api/v2/remote_accesses` to retrieve the list of all remote accesses.

```python
>>> CBWApi(URL, API_KEY, SECRET_KEY).remote_accesses()
[<cbw_api_toolbox.cbw_objects.cbw_remote_access.CBWRemoteAccess...]
```

#### Remote access

Send a GET request `/api/v2/remote_accesses/{REMOTE_ACCESS_ID}` to retrieve the information of REMOTE_ACCESS_ID.

```python
>>> CBWApi(URL, API_KEY, SECRET_KEY).remote_access(REMOTE_ACCESS_ID)
[<cbw_api_toolbox.cbw_objects.cbw_remote_access.CBWRemoteAccess]
```

#### Create remote access

Send a POST request `/api/v2/remote_accesses` to create a remote access

```python
>>> CBWApi(URL, API_KEY, SECRET_KEY).create_remote_access(INFO)
INFO:root:remote access successfully created {ADDRESS}
True
```

#### Update remote access

Send a PATCH request `/api/v2/remote_accesses/{REMOTE_ACCESS_ID}` to update the information of REMOTE_ACCESS_ID

```python
>>> CBWApi(URL, API_KEY, SECRET_KEY).update_remote_access(REMOTE_ACCESS_ID, INFO)
True
```

#### Delete remote access

Send a DELETE request `/api/v2/remote_accesses/{REMOTE_ACCESS_ID}` to delete REMOTE_ACCESS_ID

```python
>>> CBWApi(URL, API_KEY, SECRET_KEY).delete_remote_access(REMOTE_ACCESS_ID)
True
```

## Available objects and their attributes

#### Server


| Attribute                 | Type          | Description                       | Exemple of possible value                         |
|---------------------------|:-------------:|:---------------------------------:|---------------------------------------------------|
| id                        | String (hash) | Unique id of the computer         | 4a78524087574c12453dea248a91cadb                  |
| agent_version             | String        | Agent version used for supervision in case of agent supervision. Empty for agentless connections| DESKTOP-AAA111                                    |
| applications              | List          | List of the computer's applications|                                                  |
| boot_at                   | Date          | Date of the computer boot         | 2016-05-30T09:54:58.000+02:00                     |
| category                  | String        | Computer category                 | server                                            |
| criticality               | String        | Computer criticality              | criticality_medium                                |
| cve_announcements         | List          | All available listings            | CVE-2019-3842                                     |
| cve_announcements_count   | Int           | Number of CVE                     | 3                                                 |    
| deploying_period          | Object        | The time of deployment            | [DeployingPeriod](#Deploying-period)
| description               | String        | Description of the machine        | "machine of production"                           |
| groups                    | List          | Groups of the machine             | "Production, Development"                         |
| hostname                  | String        | Name of the machine               | "XXX.XXX.XXX.XXX"                                 |
| ignoring_policy           | Object        | Ignoring policy of the computer   | [IgnoringPolicy](#Ignoring-policy)                |
| last_communication        | String        | Last communication of the machine | "2019-04-08T15:46:22.000+02:00"                   |
| os                        | Object        | Os of the machine                 | [Os](#Os)                                         |
| packages                  | Object        | List of the computer's packages   | [Packages](#Packages)                             |
| reboot_required           | Bool          | Reboot required for the computer (generally after applying patches)| false            |
| remote_ip                 | String        | IP of the machine                 | XXX.XXX.XXX.XXX                                   |
| security_announcements    | Object        | List of the computer's security announcements| [SecurityAnnouncements](#Security-announcements)|
| status                    | List          | Computer status                   | comment: "Communication failure"                  |
| updates                   | Object        | Available updates for the computer| [Updates](#Updates)                               |
| updates_count             | Int           | Number of available updates for the computer| 3                                       |


#### Deploying period

| Attribute                 | Type          | Description                       | Exemple of possible value                         |
|---------------------------|:-------------:|:---------------------------------:|---------------------------------------------------|
| name                      | String        | Name of the deploying period      | "test"                                            |
| autoplanning              | Bool          | Automatically generate update scripts for computers in the deploying period| false    |
| autoreboot                | Bool          | Automatically generate reboot scripts for computers in the deploying period| false    |
| start_time                | String        | Time start of deployment          | "00:00"                                           |
| end_time                  | String        | End of deployment                 | "06:00"                                           |
| next_occurence            | String (date) | Date of the next deployment       | "2019-04-27T00:00:00.000+02:00"                   |

#### Os

| Attribute                 | Type          | Description                       | Exemple of possible value                         |
|---------------------------|:-------------:|:---------------------------------:|---------------------------------------------------|
| key                       | String        | Key of the os                     | "ubuntu_1804_64"                                  |
| name                      | String        | Name of Os                        | "Ubuntu 18.04"                                    |
| arch                      | String        | Arhitecture of Os                 | "x86_64"                                          |
| eol                       | String        | End of support of the os          | "2023-04-26T02:00:00.000+02:00"                   |
| short_name                | String        | Short name of the os              | "Ubuntu 18.04"                                    |
| type                      | String        | Os type                           | "Os::Ubuntu"                                      |
| hash_index                | String (hash) | Hash identifier                   | "c3f4de66dd34cec0156bb439002bc4..."               |
| created_at                | String (date) | Date of created                   | "2019-04-08T11:01:20.000+02:00"                   |
| updated_at                | String (date) | Date of updated                   | "2019-04-08T11:01:20.000+02:00"                   |

#### Ignoring policy

| Attribute                 | Type          | Description                       | Exemple of possible value                         |
|---------------------------|:-------------:|:---------------------------------:|---------------------------------------------------|
| ignoring_policy_items     | Object        | Items of the ignoring policy      | [IgnoringPolicyItems](#Ignoring-policy-items)     |
| name                      | String        | Name of ignoring policy           | "test_policy"                                     |

#### Ignoring policy items

| Attribute                 | Type          | Description                       | Exemple of possible value                         |
|---------------------------|:-------------:|:---------------------------------:|---------------------------------------------------|
| keyword                   | String        | Keyword of the packages           | ""                                                |
| version                   | String        | Version of the packages           | ""                                                |

#### Packages

| Attribute                 | Type          | Description                       | Exemple of possible value                         |
|---------------------------|:-------------:|:---------------------------------:|---------------------------------------------------|
| vendor                    | NoneType      | Vendor of the packages            | null                                              |
| product                   | String        | Name of packages                  | "gpg-wks-server"                                  |
| hash_index                | String (hash) | Hash identifier                   | "0160e4a3d38518a2660ff61b89c1407df"               |
| type                      | String        | Packages type                     | "Packages::Deb"                                   |
| version                   | String        | Version of packages               | "2.2.4-1ubuntu1.2"                                |

#### Security announcements

| Attribute                 | Type          | Description                       | Exemple of possible value                         |
|---------------------------|:-------------:|:---------------------------------:|---------------------------------------------------|
| type                      | String        | Security type                     | "SecurityAnnouncements::Ubuntu"                   |
| sa_code                   | String        | Security alert code               | "USN-3938-1"                                      |
| created_at                | String (date) | Date of created                   | "2019-04-08T02:00:00.000+02:00"                   |
| updated_at                | String (date) | Date of updated                   | "2019-04-10T09:20:07.000+02:00"                   |
| link                      | String        | Link of the security              | "https://usn.ubuntu.com/3938-1"                   |
| cve_code                  | String        | CVE Code public                   | "CVE-2019-3842"                                   |

#### Updates

| Attribute                 | Type          | Description                       | Exemple of possible value                         |
|---------------------------|:-------------:|:---------------------------------:|---------------------------------------------------|
| ignored                   | Bool          | Ignore of update                  | false                                             |
| patchable                 | Bool          | Update is possible                | true                                              |
| cve_announcements         | Object        | All the update availbale cve      | [CveAnnouncements](#Cve-announcements)            |
| current                   | Object        | Current version of packages       | [Current](#Current)                               |
| target                    | Object        | Target version of packages        | [Target](#Current)                                 |
| created_at                | String (date) | Date of created                   | "2019-04-09T17:13:07.000+02:00"                   |
| updated_at                | String (date) | Date of updated                   | "2019-04-09T17:13:07.000+02:00"                   |

#### Cve announcements

| Attribute                 | Type          | Description                       | Exemple of possible value                         |
|---------------------------|:-------------:|:---------------------------------:|---------------------------------------------------|
| id_cve                    | Int           | Id Cyberwatch of the vulnerability| 22                                                |
| server_id                 | Int           | Id Cyberwatch of the server       | 21                                                |
| target_id                 | Int           | Id target cve                     | 239309                                            |
| current_id                | Int           | Id current cve                    | 174477                                            |
| created_at                | String (date) | Date of created                   | "2019-04-09T17:13:07.000+02:00"                   |
| updated_at                | String (date) | Date of updated                   | "2019-04-09T17:13:07.000+02:00"                   |
| ignored                   | Bool          | Ignore of CVE                     | false                                             |
| patchable                 | Bool          | Update is possible                | true                                              |
| cve_code                  | String        | Cve code for packages             | "CVE-2019-5953"                                   |
| content                   | String        | Description of the cve code       | "In systemd before v242-r…her than \"allow_any\"."|
| published                 | String        | Date of publication               | "2019-04-09T23:29:03.000+02:00"                   |
| last_modified             | String        | Last modification                 | "2019-04-26T16:45:22.000+02:00"                   |
| cve_score                 | Float         | score of vulnerablity according to cve| 4.4                                           |
| created_at                | String (date) | Date of created                   | "2019-04-08T22:17:34.000+02:00"                   |
| updated_at                | String (date) | Date of updated                   | "2019-04-29T09:33:37.000+02:00"                   |

#### Current

| Attribute                 | Type          | Description                       | Example of possible value                         |
|---------------------------|:-------------:|:---------------------------------:|---------------------------------------------------|
| vendor                    | NoneType      | Vendor of the packages            | null                                              |
| product                   | String        | Package name                      | "libsystemd0"                                     |
| hash_index                | String (hash) | Hash identifier                   | "13a61dd2bfe0fbb063a97b66c6234759"                |
| type                      | String        | Package type in Cyberwatch        | "Packages::Deb"                                   |
| version                   | String        | Package version                   | "237-3ubuntu10.13"                                |
