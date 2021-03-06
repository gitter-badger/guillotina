2.1.20 (unreleased)
-------------------

- Nothing changed yet.


2.1.19 (2017-12-08)
-------------------

- Properly use super() for security map classes so things can be overridden
  with custom permission adapters.
  [vangheem]


2.1.18 (2017-12-06)
-------------------

- get_owners will lookup to parent object for owner.
  [vangheem]

- if IGetOwner returns none, no owner will be set on object
  [vangheem]


2.1.17 (2017-12-06)
-------------------

- Fix getting sharing information for database objects
  [vangheem]


2.1.16 (2017-12-06)
-------------------

- Fix compatibility with aiohttp 2.3.6
  [vangheem]


2.1.15 (2017-12-06)
-------------------

- Provide security cache implementation
  [vangheem]

- In case there is no method raise an error
  [ramon]


2.1.14 (2017-11-30)
-------------------

- Improve performance of json schema serialization
  [vangheem]


2.1.13 (2017-11-29)
-------------------

- Fix ContextBehavior implementation to get data correctly from object
  [vangheem]


2.1.12 (2017-11-28)
-------------------

- Handle restart transaction error from cockroach on retrieving data from db
  [vangheem]


2.1.11 (2017-11-22)
-------------------

- Set task request for async utility
  [vangheem]


2.1.10 (2017-11-21)
-------------------

- Raising aiohttp http exception is handled correctly in publisher
  [vangheem]


2.1.9 (2017-11-21)
------------------

- Fix dockers test infrastructure to not conflict with multiple tests running
  at the same time.
  [vangheem]


2.1.8 (2017-11-21)
------------------

- Adding X-Forwarded-Proto in order to allow https rewrite of absolute url
  [ramon]

- Adding PROPFIND HTTP Verb
  [ramon]

- Be able to provide a custom router using the `router` setting
  [vangheem]


2.1.7 (2017-11-15)
------------------

- Add `id` index
  [vangheem]


2.1.6 (2017-11-15)
------------------

- Make sure to abort all error responses
  [vangheem]


2.1.5 (2017-11-14)
------------------

- Track timing of various parts of request. Helps with providing metrics
  [vangheem]


2.1.4 (2017-11-14)
------------------

- Be able to provide request.uid value from request header `X-FORWARDED-REQUEST-UID`.
  [vangheem]


2.1.3 (2017-11-10)
------------------

- Implement copy_cloud_file on DBFile
  [vangheem]


2.1.2 (2017-11-08)
------------------

- Handle CancelledError on server close
  [vangheem]


2.1.1 (2017-11-08)
------------------

- Clean up async tasks better
  [vangheem]


2.1.0 (2017-11-07)
------------------

- Remove use of buildout for development/travis
  [vangheem]

- Upgrade to aiohttp > 2.3.0
  [vangheem]

- Fix iter_data method for DBFile(no uri attribute)
  [vangheem]

- Verify service method signatures when configuration is loaded
  [vangheem]


2.0.6 (2017-11-06)
------------------

- Use adapter lookup correctly for value serializer
  [vangheem]


2.0.5 (2017-11-06)
------------------

- Do not do async suscribers in a gather since we can lose get_current_request context
  [vangheem]


2.0.4 (2017-11-06)
------------------

- Fix MockTransaction implementation
  [vangheem]


2.0.3 (2017-11-06)
------------------

- Provide correct signature for default value converter
  [vangheem]


2.0.2 (2017-11-06)
------------------

- Handle missing component lookups more correctly for factories that return None
  for the value.
  [vangheem]


2.0.1 (2017-11-06)
------------------

- DeserializationError and ValueDeserializationError should implement message
  attribute
  [vangheem]


2.0.0 (2017-11-06)
------------------

- Make components more pythonic:
    - guillotina.component.getMultiAdapter -> get_multi_adapter
    - guillotina.component.getAdapter -> get_adapter
    - guillotina.component.getUtility -> get_utility
    - guillotina.component.queryUtility -> query_utility
    - guillotina.component.getUtilitiesFor -> get_utilities_for
    - guillotina.component.getAllUtilitiesRegisteredFor -> get_all_utilities_registered_for
    - guillotina.component.getGlobalSiteManager -> get_global_components
    - guillotina.component.provideUtility -> provide_utility
  [vangheem]

- Allow passing arguments to component lookup factories with `args=[]` and `kwargs={}` params
  [vangheem]

- Optimize serialization framework to use less and faster adapter lookups
  [vangheem]

- Added `guillotina.profile.profilable` decorator to be able to tell line_profiler
  what functions to profile.

- Integrate line_profiler with `--line-profiler`, `--line-profiler-matcher="*foobar*"`
  and `--line-profiler-output`.
  [vangheem]

- Pre-render resolve_dotted_name on authentication plugins
  [vangheem]

- Implement aiotask_context for request object lookup
  [vangheem]

- Add `@configure.value_deserializer` and `@configure.value_serializer`
  configurators
  [vangheem]

- Remove transform framework
  [vangheem]

- Remove RichText since it was not used and didn't make much sense
  [vangheem]


1.6.1 (2017-10-20)
------------------

- Fix logging for large objects
  [vangheem]

- Make sure to use ujson everywhere it makes sense
  [vangheem]


1.6.0 (2017-10-18)
------------------

- Require aiohttp < 2.3.0
  [vangheem]

- Adding Dublin Core behavior as a context field so there is not two titles.
  [ramon]


1.5.7 (2017-10-16)
------------------

- pdb!
  [vangheem]


1.5.6 (2017-10-16)
------------------

- More docs fixes
  [vangheem]


1.5.5 (2017-10-15)
------------------

- Update docs and finish training.
  [vangheem]

- Fix websocket token authentication.
  [vangheem]


1.5.4 (2017-10-14)
------------------

- More documentation updates and fixes
  [vangheem]


1.5.3 (2017-10-14)
------------------

- Update does and default values to match docs
  [vangheem]


1.5.2 (2017-10-13)
------------------

- Be able to override aiohttp access_log_format
  [vangheem]


1.5.1 (2017-10-12)
------------------

- Add back missing imports from guillotina.files
  [vangheem]


1.5.0 (2017-10-12)
------------------

- Provide default cloud file implementation
  [vangheem]


1.4.7 (2017-10-10)
------------------

- Add `run` command to allow running scripts from the command line against
  a guillotina configuration.
  [vangheem]


1.4.6 (2017-10-09)
------------------

- Fix logging conflict ID message
  [vangheem]


1.4.5 (2017-10-09)
------------------

- provide `guillotina.testing.configure_with` and `guillotina.testing.get_settings`
  functions to help configure test environment settings.
  [vangheem]

- Do not require `title` for creating containers
  [vangheem]


1.4.4 (2017-10-04)
------------------

- `index.with_accessor` decorator did not return the original function so you
  could not reuse the function.
  [vangheem]


1.4.3 (2017-10-03)
------------------

- Fix cache data being undefined for reading cloud data
  [vangheem]


1.4.2 (2017-10-03)
------------------

- More logging for conflict errors
  [vangheem]


1.4.1 (2017-10-03)
------------------

- Handle value is None for cloud deserializer
  [vangheem]


1.4.0 (2017-10-02)
------------------

- Remove unused etcd/locking support
  [vangheem]


- Provide base classes and utilities for cloud storage implementations
  [vangheem]


1.3.26 (2017-10-02)
-------------------

- Add `@move`, `@duplicate` and `@ids` endpoints
  [vangheem]


1.3.25 (2017-10-02)
-------------------

- Change how much sub-items we should by default from 200 to 20
  [vangheem]


1.3.24 (2017-09-29)
-------------------

- Fix error when rendering plain text from response
  [vangheem]


1.3.23 (2017-09-28)
-------------------

- Track errors rendering view and make sure to not index data when there has
  been a error on the view(like conflict error).
  [vangheem]


1.3.22 (2017-09-28)
-------------------

- Allow overriding indexers
  [vangheem]

- Add default head endpoint
  [vangheem]


1.3.21 (2017-09-27)
-------------------

- Add `Request.uid` property and issue a unique id to each request object to
  be using with logging.
  [vangheem]


1.3.20 (2017-09-26)
-------------------

- Conflict errors now log with traceback and additional info
  [vangheem]


1.3.19 (2017-09-25)
-------------------

- Fix adding metadata to index data
  [vangheem]


1.3.18 (2017-09-25)
-------------------

- Provide extra logging data for more loggers
  [vangheem]


1.3.17 (2017-09-25)
-------------------

- Do not call ObjectLoadedEvent on object traversal
  [vangheem]

- Be able to provide omit/include on GET requests to limit number of fields
  that are returned in the payload
  [vangheem]

- Limit max object cache size to 5mb
  [vangheem]

- Optimize indexing for patch operations to only index changed data instead
  of the full object
  [vangheem]


1.3.16 (2017-09-21)
-------------------

- Provide `check_writable_request` configuration to allow customizing what
  requests are writable requests
  [vangheem]


1.3.15 (2017-09-21)
-------------------

- executing request futures should be a Task since finishing execution of
  the request object causes it to be deleted
  [vangheem]


1.3.14 (2017-09-21)
-------------------

- Fix executing futures in web service
  [vangheem]


1.3.13 (2017-09-21)
-------------------

- Add add_future, get_future and execute_futures methods to Request class
  [vangheem]

- Move indexing to be done in a future instead of after commit hook
  [vangheem]


1.3.12 (2017-09-21)
-------------------

- Change uncaught exception status code to 500
  [vangheem]


1.3.11 (2017-09-21)
-------------------

- Add another connection closed handler
  [vangheem]

- Fix logging of large objects
  [vangheem]


1.3.10 (2017-09-15)
-------------------

- When loading schema cache, also set factory cache
  [vangheem]


1.3.9 (2017-09-01)
------------------

- add `save_file` method to the file manager interface
  [vangheem]


1.3.8 (2017-09-01)
------------------

- provide `@component-subscribers` endpoint to inspect configured subscribers
  [vangheem]

- Add request._tm and request._txn when using `use_db()` with shell command
  [vangheem]


1.3.7 (2017-08-25)
------------------

- Add text/plain content negotation response type
  [vangheem]

- Fix content negotiation bug where we could not parse more complex Accept headers
  [vangheem]


1.3.6 (2017-08-15)
------------------

- directly provide base request interfaces instead of dynamically applying them
  [vangheem]

- Provide iter_data method on cloud file manager
  [vangheem]


1.3.5 (2017-08-08)
------------------

- Do not provide default values for all request object values
  [vangheem]


1.3.4 (2017-08-08)
------------------

- Implement Guillotina Request object and store view info on it
  [vangheem]


1.3.3 (2017-08-07)
------------------

- Recover when postgresql gets restarted
  [vangheem]

- Only show traceback if in debug mode
  [vangheem]


1.3.2 (2017-08-04)
------------------

- Change IQueueUtility to being a regular Queue instead of a PriorityQueue. A
  PriorityQueue request comparison functions to be implemented on the added
  objects.
  [vangheem]


1.3.1 (2017-08-04)
------------------

- Throw a 412 response code if type not allowed
  [vangheem]

- Be able to generate custom api doc files
  [vangheem]


1.3.0 (2017-08-01)
------------------

- Fix instance where we were doing a permission lookup with title instead of id
  [bloodbare]


1.2.0a6 (2017-07-28)
--------------------

- Fix issue where dynamic behaviors were not getting indexed
  [vangheem]


1.2.0a5 (2017-07-24)
--------------------

- managed_transaction context manager did not properly restore read only write
  flag on current request
  [vangheem]


1.2.0a4 (2017-07-24)
--------------------

- Make sure `allow_access` setting works on class based views as well
  [vangheem]


1.2.0a3 (2017-07-24)
--------------------

- Fix issue where stacked service configuration would not work with function
  services since they would get changed into views that were not from the
  original package.
  [vangheem]


1.2.0a2 (2017-07-18)
--------------------

- Fix upstream fetch issue on cockroach
  [bloodbare]

- Provide `jsapps` option to render single page javascript applications
  [vangheem]


1.2.0a1 (2017-07-17)
--------------------

- Support ssl for cockroachdb
  [bloodbare]

- Switch to defaulting to yaml for configuration but still supporting json
  [vangheem]


1.1.0a116 (2017-07-13)
----------------------

- Fix starting with request without txn would cause an error with managed_transaction
  [vangheem]


1.1.0a115 (2017-07-10)
----------------------

- Be able to provide utility for getting the owner of a new resource
  [vangheem]


1.1.0a114 (2017-07-10)
----------------------

- Add `get_owner` utility
  [vangheem]


1.1.0a113 (2017-07-03)
----------------------

- Be able to customize cors handling
  [vangheem]

- Add new `guillotina.Public` permission and assign it to anoymous role
  [vangheem]

- Provide default permission as guillotina.AccessContent for services
  [vangheem]


1.1.0a112 (2017-06-28)
----------------------

- do not register for writing object when assigning __parent__ pointer
  [vangheem]

- add `get_containers` command
  [vangheem]


1.1.0a111 (2017-06-26)
----------------------

- Change guillotina.Member title
  [vangheem]


1.1.0a110 (2017-06-25)
----------------------

- Provide more logging information for errors
  [vangheem]

1.1.0a19 (2017-06-23)
---------------------

- get_principals_with_access_content and get_roles_with_access_content was not
  checking against all roles
  [vangheem]


1.1.0a18 (2017-06-22)
---------------------

- Add PUT method for @sharing endpoint
  [vangheem]


1.1.0a17 (2017-06-22)
---------------------

- Add get_all_possible_schemas_for_type utility function
  [vangheem]


1.1.0a16 (2017-06-21)
---------------------

- Move deleting objects to a task queue since deleting large leafs could cause
  postgresql to slow down.
  [vangheem]


1.1.0a15 (2017-06-19)
---------------------

- Document @tusupload, @download and @upload endpoints
  [vangheem]

- Do not throw error for invalid jwt token
  [vangheem]


1.1.0a14 (2017-06-14)
---------------------

- Proxy params values from cloud file manager to field manager
  [vangheem]


1.1.0a13 (2017-06-10)
---------------------

- Manually rollback transaction if pg thinks we're in one that isn't managed by us
  [vangheem]


1.1.0a12 (2017-06-10)
---------------------

- Make sure we do not have an existing transaction set when starting a new
  transaction
  [vangheem]


1.1.0a11 (2017-06-09)
---------------------

- Move fixtures in conftest.py to fixtures.py. This might break your tests
  that depend on guillotina folks!
  [vangheem]


1.1.0a10 (2017-06-08)
---------------------

- Handle deadlocks at conflict errors
  [vangheem]


1.1.0a9 (2017-06-08)
--------------------

- Fix issue where new annotations would not get registered as new objects on
  transaction and added objects on the transaction would get registered twice
  and cause conflicts
  [vangheem]

1.1.0a8 (2017-06-07)
--------------------

- Fix AttributeError on commit
  [vangheem]


1.1.0a7 (2017-05-29)
--------------------

- Make sure etcd docker containers do not conflict
  [vangheem]

1.1.0a6 (2017-05-29)
--------------------

- Do not name etcd docker image in tests
  [vangheem]


1.1.0a5 (2017-05-27)
--------------------

- Group objects should not get reindexing triggered on them
  [vangheem]


1.1.0a4 (2017-05-26)
--------------------

- Add more special characters for valid id
  [vangheem]


1.1.0a3 (2017-05-26)
--------------------

- Put restrictions on what valid ids for content are
  [vangheem]


1.1.0a2 (2017-05-26)
--------------------

- Significant performance fixes to lock implementation with etcd
  [vangheem]

- Provide more helper utilities for shell, so it's less error-prone
  [vangheem]

- Fix `tidonly` transaction strategy
  [vangheem]


1.1.0a1 (2017-05-24)
--------------------

- Provide payload on container creation
  [vangheem]

- Fix type check on creating container
  [vangheem]

- Provide async task for cockroach to cleanup children since there is no cascade support
  [vangheem]

- Fix cockroachdb transaction support as it behaves differently than postgresql
  [vangheem]

- Include cockroachdb in our CI testing
  [vangheem]

- Simplify docker testing infrastructure
  [vangheem]

- Fix cockroachdb integration
  [vangheem]


1.0.0a28 (2017-05-18)
---------------------

- managed_transaction context manager can now adopt modified objects from
  outer transaction
  [vangheem]


1.0.0a27 (2017-05-17)
---------------------

- add new `guillotina.transactions.managed_transaction` context manager
  [vangheem]


1.0.0a26 (2017-05-17)
---------------------

- Only initialize database if needed instead of running initialize statements
  on every app startup
  [vangheem]

- rename get_class_dotted_name to get_dotted_name
  [vangheem]

1.0.0a25 (2017-05-15)
---------------------

- Handle connection is closed error when starting transaction
  [vangheem]


1.0.0a24 (2017-05-13)
---------------------

- Fix transaction conflict retry handle
  [vangheem]

- fix scenario where prepared statements would get cached with wrong db connection
  [vangheem]

- Enforce transaction ids match when updating objects and throw a ConflictError
  when there is a mismatch. This can happen in cases where there is stale cache
  being pulled.
  [vangheem]

- Remove use of `merge` transaction strategy. Better to just abort and retry
  instead of costly merge resolution issues
  [vangheem]


1.0.0a23 (2017-05-11)
---------------------

- Fix get_container test utility
  [vangheem]


1.0.0a22 (2017-05-11)
---------------------

- Fix QueueUtility to properly get transaction object before working on view
  [vangheem]

- Update storage caching interfaces to make them easier to use
  [vangheem]


1.0.0a21 (2017-05-09)
---------------------

- Reuse transaction object if same request object is provided. This helps when
  working with the same persistent objects across one request object.
  [vangheem]


1.0.0a20 (2017-05-09)
---------------------

- Tie every request to one transaction instead of trying to juggle pool of
  transactions in transaction manager.
  [vangheem]

- Only issue transaction id for write operations
  [vangheem]

- Use sequence for transaction id for postgresql and serial for cockroachdb
  [vangheem]


1.0.0a19 (2017-05-08)
---------------------

- Fix conflict error retries and make tests for it
  [vangheem]


1.0.0a18 (2017-05-08)
---------------------

- Make sure to be able to handle int, float responses as well
  [vangheem]


1.0.0a17 (2017-05-05)
---------------------

- Implement locks on pg connections for everything except cursors
  [vangheem]


1.0.0a16 (2017-05-04)
---------------------

- Be careful with locks on transaction to prevent deadlocks
  [vangheem]


1.0.0a15 (2017-05-04)
---------------------

- Make sure to lock access to queries on the pg database per connection. This
  fixes asyncpg errors when you attempted to do actions async actions on
  one transaction. Where it was easiest to have problem was asyncio.gather
  [vangheem]

- add creators/contributors as context properties for the IDublinCore behavior
  instead of trying to get the data from the annotation
  [vangheem]

- utils.get_content_path should be based from root of container, not root of database
  [vangheem]

- Fix another memory leak in get_current_request and add test for it
  [vangheem]

- Provide more robust conflict resolution on fields of content and annotations
  [vangheem]


1.0.0a14 (2017-04-25)
---------------------

- Fix issue where annotations would get duplicated
  [vangheem]

- rename __annotations_data_key to __annotations_data_key__ in Annotation behavior
  [vangheem]

- Prevent aiohttp sessions from not closing by using context managers everywhere
  [vangheem]


1.0.0a13 (2017-04-24)
---------------------

- root ThreadPoolExecutor was removed in previous release. Some packages use this
  feature
  [vangheem]

- Rename PServerJSONEncoder to GuillotinaJSONEncoder
  [vangheem]


1.0.0a12 (2017-04-24)
---------------------

- Provide conflict resolution across transactions
  [vangheem]

- Be able to query storage for total number of objects
  [vangheem]

- Provide basic async blob support interface
  [vangheem]

- Fix annotation behaviors that use __local__properties__ not storing data
  properly on content object
  [vangheem]

- Do not re-load behavior data if it's already been loaded from db
  [vangheem]

- Provide new IObjectLoadedEvent to do things with object when it's loaded
  from the database
  [vangheem]


1.0.0a11 (2017-04-15)
---------------------

- Fix memory leak in get_current_request C implementation
  [vangheem]

- use asyncio.shield in commit and abort handlers to make sure they finish
  even if task is cancelled
  [vangheem]

- Fix case where abort would cause asyncio CancelledError to occur
  [vangheem]


1.0.0a10 (2017-04-13)
---------------------

- Provide ability to configure logging with json config
  [vangheem]


1.0.0a9 (2017-04-12)
--------------------

- Be able to provide `aiohttp_settings` in config.json to configure parts of
  aiohttp application
  [vangheem]

- async_keys on database type did not await
  [vangheem]


1.0.0a8 (2017-04-11)
--------------------

- Fix annotation data not getting indexed properly. Getting index data needs
  to be async.
  [vangheem]


1.0.0a7 (2017-04-10)
--------------------

- be able to configure __allow_access__ with service function by using
  the `allow_access` configuration option

- rename modified to modification_date and created to creation_date
  [vangheem]


1.0.0a6 (2017-04-06)
--------------------

- Fix container objects not having current transaction when new objects are
  registered for them
  [vangheem]


1.0.0a5 (2017-04-04)
--------------------

- Be able to override base configuration in addon applications
  [vangheem]

- Fix use of default layer in app_settings
  [vangheem]


1.0.0a4 (2017-04-03)
--------------------

- json schema support in service definitions
  [vangheem]

- rename `subjects` to `tags` for IDublinCore behavior
  [vangheem]

- rename permissions:
  `guillotina.AddPortal` -> `guillotina.AddContainer`
  `guillotina.DeletePortals` -> `guillotina.DeleteContainers`
  `guillotina.GetPortals` -> `guillotina.GetContainers`
  [vangheem]

- You can now reference modules in your static file configuration: `mymodule:static`
  [vangheem]

- Static directories will now serve default index.html files
  [vangheem]

- Fix static directory support
  [vangheem]

- Add auto reload support with the aiohttp_autoreload library
  [vangheem]

- Upgrade to aiohttp 2
  [vangheem]

- Remove the dependencies six and requests
  [vangheem]

- Rename `portal_type` to `type_name` as "portal" does not make sense anymore
  [vangheem]


1.0.0a3 (2017-03-23)
--------------------

- Fix automatically creating id when none provided for content creation
  [vangheem]

1.0.0a2 (2017-03-23)
--------------------

- Change guillotina commands to be sub-commands of main `bin/guillotina`
  command runner so developer do not need to register separate scripts
  for each command. Fixes #27
  [vangheem]

- Change Site portal type to Container
  [vangheem]

- Fix get_current_request to correctly look for python None object when finding
  the request object
  [vangheem]

- Fix `gshell` command to work with aysncio loop so you can run `await` statements
  with the shell. Compatibility done with aioconsole.
  [vangheem]

- Provide support for utilizing `middlewares` option for aiohttp server
  [vangheem]


1.0.0a1 (2017-03-17)
--------------------

- move zope.schema, zope.component, zope.configuration into guillotina
  [vangheem]

- move get_current_request to guillotina.utils
  [vangheem]

- create_content and create_content_in_container are not async functions
  [vangheem]

- remove zope.security, zope.location, zope.dublincore, plone.behavior,
  zope.dottedname, zope.lifecycleevent
  [vangheem]

- rename to guillotina
  [vangheem]

- Remove plone:api zcml directive
  [vangheem]


1.0a14 (unreleased)
-------------------

- Rename "address" option to "port" and add "host" option to bind something different
  than the default 0.0.0.0
  [vangheem]


1.0a13 (2017-02-27)
-------------------

Fixes:

- Fix static file configuration
  [vangheem]


1.0a12 (2017-02-27)
-------------------

Fixes:

- HTML renderer can now handle html responses correctly
  [vangheem]

- Renamed settingsForObject to settings_for_object
  [vangheem]


1.0a11 (2017-02-22)
-------------------

Fixes:

- Handle NotADirectoryError error when attempting to load b/w compat zcml
  [vangheem]

Breaking changes:

- ACL is now in the object itself so the permission will not be maintained
  [ramonnb]

New features:

- Executing pending tasks after requests has returned
  [ramonnb]

- Adding the payload on the events that modifies the objects
  [ramonnb]

- Defining local and global roles so they can be used to define @sharing
  On indexing security information we only get the AccessContent permission.
  [ramonnb]

- Install addons can have the context
  [ramonnb]

- Merging zope.securitypolicy
  [ramonnb]

- Adding C optimization for get_current_request
  [ramonnb]


1.0a10 (2017-02-01)
-------------------

Fixes:

- Fix issue where correct aiohttp response would not be generated always
  [vangheem]

New features:

- be able provide your own database factories by providing named utilities for
  the IDatabaseConfigurationFactory interface
  [vangheem]

- install, uninstall methods for addon class can now be async
  [vangheem]

- Support for newt.db
  [ramonnb]

- Be able to define adapters, subscribers, permissions, roles, grant
  with decorators, not zcml
  [vangheem]

- No more zcml in core
  [vangheem]


1.0a9 (2017-01-18)
------------------

Fixes:

- Use guillotina.schema getter and setter to set attributes
  [ramonnb]

New features:

- Be able to define addons using decorators, not zcml
  [vangheem]

- Be able to define behaviors using decorators, not zcml
  [vangheem]

- Be able to define content types using decorators, not zcml
  [vangheem]

- Catalog reindex as async operation
  [ramonnb]

- RelStorage Support (postgres)
  [ramonnb]

- Adding HTTP Precondition exception
  [ramonnb]

- New way to create services with decorators instead of zcml/json configuration
  [vangheem]

- Add functionality like virtualhost monster to define the urls
  [ramonnb]

- Add new pcreate command
  [vangheem]

- Add new pmigrate command and migration framework
  [vangheem]

- Provide base guillotina.commands.Command class to provide your own commands.
  Commands have been moved in code so you'll need to re-run buildout to get
  pserver to work after this update.
  [vangheem]

- Automatically give authenticated users new `guillotina.Authenticated` role
  [vangheem]

- Handle error when deserializing content when not authenticated and checking
  permissions
  [vangheem]

- add `pshell` command
  [vangheem]

- Role member for Manager group
  [ramonnb]


Breaking changes:

- plone:api zcml directive deprecated in favor of decorator variant
  [vangheem]


1.0a8 (2016-12-18)
------------------

- On deserialization errors, provide error info on what fields could not be
  deserialized in the api response.
  [vangheem]

- Be able to provide data from serializable exception data to be used with
  ErrorResponse objects with Exceptions that implement ISerializableException.
  [vangheem]

- Add Events to enable audit of activity
  [ramonnb]

- Add the JSON Field
  [ramonnb]

- Fix various function naming standard issues to not use camel case.
  [vangheem]

- Fix imports with isort.
  [gforcada]

- remove local component registry
  [vangheem]

- GET @search(plone.SearchContent) passed to search method and
  POST @search(plone.RawSearchContent) passed to query method
  on ICatalogUtility. GET is now meant to be query the search utility will
  do something clever with and POST is meant to be a raw query passed to utility
  [vangheem]

- provide new `plone.SearchContent`, `plone.RawSearchContent` and
  `plone.ManageCatalog` permissions
  [vangheem]

- provide IConstrainTypes adapter interface to override allowed types in a folder
  [vangheem]

- provide dynamic behavior for objects
  [ramonnb]

- provide basic command line utility to interact with APIs
  [vangheem]

- fix fallback cors check
  [vangheem]

- Added zope.event async version on guillotina.events (notify and async handlers)
  [ramonnb]

- Improve code analysis, add configurations for it and remove all tabs.
  [gforcada]

1.0a7 (2016-11-24)
------------------

- add jwt token validator
  [vangheem]

- Add to finalize an AsyncUtil when its finishing the software
  [ramonnb]

- Remove `AUTH_USER_PLUGINS` and `AUTH_EXTRACTION_PLUGINS`. Authentication now
  consists of auth extractors, user identifiers and token validators.
  [vangheem]

- Correctly check parent object for allowed addable types
  [vangheem]

- Get default values from schema when attribute on object is not set
  [ramonnb]


1.0a6 (2016-11-21)
------------------

- Move authorization to after traversal
  [vangheem]

- Fix issue where you could not save data with the API
  [vangheem]


1.0a5 (2016-11-21)
------------------

- Adding zope.event compatible async handlers for ElasticSearch and other events handlers [@bloodbare]
- Adding PostCommit and PreCommit Hooks that can be async operations [@bloodbare]


1.0a4 (2016-11-19)
------------------
