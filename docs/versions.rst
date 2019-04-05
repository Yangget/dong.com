Versions
========

Improvements and Bug fixes on 1.12.5
------------------------------------

- Fix, #928 Copy role modal not showing

Improvements and Bug fixes on 1.12.4
------------------------------------

- Fix, #911 fabmanager missing session rollback() when user add fails
- Fix, #910 Next page on OAuth

Improvements and Bug fixes on 1.12.3
------------------------------------

- Fix, #762 Instantiate AdminActions only after DOM finishes loading
- New, #883 Changed templates so that is possible to use Jinja2 StrictUndefined
- Fix, #891 Missing import reduce python3 compatibility
- Fix, #862 fabmanager appbuilder parameter is now working

Improvements and Bug fixes on 1.12.2
------------------------------------

- Fix, #832 don't install examples as a package with flask-appbuilder
- Fix, #760 Select all checkbox, in related view, selects checkboxes from all related views
- New, #833 LDAPS TLS config options
- New, #829 Aditional filtering in LDAP search

Improvements and Bug fixes on 1.12.1
------------------------------------

- New, #826 Greek support i18n
- New, #813 Dependencies unpinned
- Fix, #828 list and form widget rendering html InLine, regression from #797

Improvements and Bug fixes on 1.12.0
------------------------------------

- Fix, #797 Remove safe filter from template
- New, #911 BREAKING CHANGES, bumped Flask-Login dependency to >=0.3,<0.5

Improvements and Bug fixes on 1.11.1
------------------------------------

- Fix, Unlock flask required version, new 0.12.4. does not cause issues anymore

Improvements and Bug fixes on 1.11.0
------------------------------------

- New, #615 Azure AD as Oauth provider
- New, #678 fabmanager create-user command
- Fix, #628 Remove double-instantiation of declarative base, problem with flask-migrate
- New, #735 Added french translations
- Fix, minor typo EMail to Email

Improvements and Bug fixes on 1.10.0
------------------------------------

- Fix, #712 improvement on parsing timezone dates
- Fix, #701 permission deletion
- Fix, #700 Non unique associations on security models
- New, #694 Accept SQLAlchemy custom types defined by TypeDecorator
- New, #686 Removed support for python 2.6

Improvements and Bug fixes on 1.9.6
-----------------------------------

- Fix, #663 Allow remote user to be auto registered.
- New, #639 Composite key support for SQLAlchemy.
- New, #661 Add feature to allow form to be processed prior to populating model.

Improvements and Bug fixes on 1.9.5
-----------------------------------

- New, #655 add feature to allow form prefill.
- New, #631 add sqlalchemy support for binary types.
- New, #626 support for traditional Chinese.
- New, #626 possible to disable update permissions on startup.

Improvements and Bug fixes on 1.9.4
-----------------------------------

- New, #596 font-awesome from 4.3 to 4.7.

Improvements and Bug fixes on 1.9.3
-----------------------------------

- Fix, #544 for possible sql injection on order by clauses.
- Fix, #550 check whether `session_form_edit_pk` still exist in db, on CompactCRUDMixin.
- Fix, #553 for AttributeError when edit_columns on a view in related_views does not include relationship.
- New, #562 Bump flask-babel version to 0.11.1, and pin.
- Fix, #444 Create LDAP user firstname/lastname may return as bytes instead of str.
- Fix, Fix divergence on versions between setup and requirements, pinned versions.

Improvements and Bug fixes on 1.9.2
-----------------------------------

- New, #528 support for enum type (SQLA only).
- Fix, Possible sql injection vulnerability.

Improvements and Bug fixes on 1.9.1
-----------------------------------

- Fix, #489 python3 compatibility fix for unicode api_read.
- Fix, #491 [api/update] only update keys specified in POST data.
- Fix, #492 [cosmetics] making row button (show/edit/delete) not primary.
- Fix, #493 [cosmetic] left-align the text in dropdowns.
- New, #508 Updated bootswatch to version 3.3.7 five new themes included.
- New, #512 Docs now use readthedocs theme.
- New, #503 FileUploadField: process_on_store() and process_on_delete().
- Fix, #511 Added new parameter to fabmanager babel-extract to include aditional keywords, defaults to **lazy_gettext, gettext, _, __**
- New, #483 new parameter for LDAP username formatting AUTH_LDAP_USERNAME_FORMAT.

Improvements and Bug fixes on 1.9.0
-----------------------------------

- Fix, Decorator oauth_user_info_getter was not according the docs, parameter bug.
- Fix, #474 Missing menu deviders
- Fix, #472 Prevent masquerade attacks through oauth providers.
- New, Optional TLS for LDAP Authentication.
- Fix, Factory setup was failing when babel get locale was being called.
- New, Bootstrap updated to version 3.3.7.
- New, flask-sqlalchemy updated to version 2.1.
- New, #453 Added support for users to login with their username or email address.
- Fix, #467 two instances of urls being generated wrongly when running under a prefix.
- Fix, redirect to actual index view rather than '/' on logout for DBAuthView.
- Fix, form actions not working under a prefix for CompactCRUDMixin.
- Fix, #457 Don't overwrite csrf_token on form fill.
- Fix, #453 [rest api] improve error messages, and return item object upon create/update.
- New, flask-babel update.
- Fix, #409 Google Oauth login and self registration.
- New, #402 column_formatters to ModelView.
- New, #374 default autosizing to app image (if any).
- New, #393 More sensible default page size.
- Fix, #397 security: don't crash on oauth errors.
- Fix, #395 flask_wtf.Form has been renamed to FlaskForm.
- Fix, #354 Improved spanish translation.
- Fix, #352 some i18n related bugs.

Improvements and Bug fixes on 1.8.1
-----------------------------------

- Fix, #341 for supporting multiple select2 fields.
- Fix, #340 Better chinese translations.
- New, #338 Support of Mongoengine Document inheritance.

Improvements and Bug fixes on 1.8.0
-----------------------------------

- New, Support for python 3.5, now uses flask-babel instead of flask-babelpkg.

Improvements and Bug fixes on 1.7.1
-----------------------------------

- Fix, REST API endpoints for fetching related data columns crashed.
- Fix, #332 Realign deprecated references to `flask.ext`.

Improvements and Bug fixes on 1.7.0
-----------------------------------

- New, REST API endpoints for fetching related data columns.
- New, REST endpoint for fetching data with simple output (select2 to consume).
- New, AJAX select fields.
- New, AJAX select fields that can be setup to be related, when the user chooses on master, the slave show only related data.

Improvements and Bug fixes on 1.6.3
-----------------------------------

- Fix, Filters were broken on 1.6.2, impact on searches and Unique validators.

Improvements and Bug fixes on 1.6.2
-----------------------------------

- New, Support for Japanese. Thanks to @giyokun.
- Fix, #312 Solves String encoding causing column labels to be prefixed with 'b' in Python 3x.
- Fix, #322 Solves Error on Inline cookie cached, when a record is deleted and it's pk is on the edit cookie.
- Fix, Bug with numeric filters, converting to correct python type.

Improvements and Bug fixes on 1.6.1
-----------------------------------

- New, Allowing apps to alter title using a jinja block #284
- Fix, Prevented user's password being written to debug.
- New, Added login failed message to log.
- Fix, Fixes #273 by not registering a view that will not exist for LDAP
- New, added missing filters for date types for generic models.
- New, #316, Adding FilterInFunction to models.sqla.filters.
- New, AUTH_LDAP_APPEND_DOMAIN to always append a certain domain on LDAP user's login.

Improvements and Bug fixes on 1.6.0
-----------------------------------

- Fix, GenericInterface.get(pk) bug created on 1.5.0 correction, missing optional extra base_filter parameter
- New, Simple addon system. Possible modular instalation of views, models and functionality.

Improvements and Bug fixes on 1.5.0
-----------------------------------

- New, #261, possible for the user to edit their first name and last name.
- Fix, #251, record url from some user can be accessed by any user, show, edit and delete are now constrained by base_filter.
- Fix, #265, Fixed double word in views.rst
- Fix, #247, bug when ordering view columns where None values are in.
- Fix, pinned flask-sqlalchemy to version 2.0.
- New, type checks disables on AuditMixin, it allows the use of this mixin when extending the User model.
- New, possible to filter fields using dot notation, automatic joins of other models.
- Fix, actions on user profile to resetmypasswordview made generic, the view can be safely override.
- Fix, actions on user profile to resetpasswordview made generic, the view can be safely override.

Improvements and Bug fixes on 1.4.7
-----------------------------------

- New, #228 new property, search_form_query_rel_fields to filter combo lists on search related fields.

Improvements and Bug fixes on 1.4.6
-----------------------------------

- Fix, #223 Proxy support.
- Fix, #219 Making the inline crud stateless, CompatCRUDMixin.
- Fix, #216 English issues found during translation.
- New, config key, FILE_ALLOWED_EXTENSIONS, issue #221.
- New, #217, Polish translations.
- Fix, flask-login version pin on 0.2.11.

Improvements and Bug fixes on 1.4.5
-----------------------------------

- Fix, #211, UTF-8 encoding for the json label strings. REST API bug.
- Fix, #209, Several improvements to queries on MongoDB.
- Fix, #206, registration form fields aren't being validated.
- Fix, #205, self.registeruser_model rather than RegisterUser.
- Fix, #195, Silent failure of validators_columns on CompactCRUDMixin.
- Fix, #197, 'Mixed Content' message when behind an https reverse proxy
- Fix, Bug fixed for problem with columns that drilldown model.model.name.
- New, Support for Numeric SQLAlchemy type.

Improvements and Bug fixes on 1.4.4
-----------------------------------

- Fix, #188 but fix created a display bug on empty queries with related views.
- Fix, #186 LDAP configuration - Invalid DN syntax on OpenLDAP. Introduced AUTH_LDAP_BIND_USER and AUTH_LDAP_BIND_PASSWORD 
- New, decorator for mapping custom Model property to real db property, supports sorting on custom properties. @renders.
- New, various new filters for generic models. #193.

Improvements and Bug fixes on 1.4.3
-----------------------------------

- Fix, #188 fix bug, actions return access denied on actions for lists."

Improvements and Bug fixes on 1.4.2
-----------------------------------

- New, search_form_extra_fields property.
- New, SimpleFormView and PublicFormView form_post can return a flask response.
- New, ListLinkWidget, replaces the show buttom by a link on the first table col.

Improvements and Bug fixes on 1.4.1
-----------------------------------

- New, ListWidget, ListItem, ListThumbnail, ListBlock templates inherite from base_list.html.
- Fix, MultipleView javascript bug with 2 (or more?) charts #177.
- New, baselib.html was replaced by navbar.html, navbar_menu.html, nabar_right.html.


Improvements and Bug fixes on 1.4.0
-----------------------------------

- Fix, #168 fixed output when fabmanager is unable to import app.
- Fix, Moved userXXXmodelview properties to BaseSecurityManager.
- Fix, Copied XXX_model properties to BaseSecurityManager.
- New, SimpleFormView and PublicFormView now subclass BaseFormView.
- New, class method for BaseView's get_default_url, returns the default_view url.
- New, OAuth authentication method.
- New, Search for role with a particular set of permissions on views or menus.
- New, Possible to filter MongoEngine ObjectId's.
- Fix, MongoEngine (MongoDB) ObjectId's not included in search forms.
- Fix, Menu html and icons rework.
- New, add_exclude_columns.
- New, edit_exclude_columns.
- New, show_exclude_columns.
- New, exclude_columns on tests.
- New, docs for exclude_columns.
- New, remove id warning for MongoDB on filters.
- Fix, missing translations.

Improvements and Bug fixes on 1.3.7
-----------------------------------

- Fix, Changed length of username model field from 32 to 64 characters.
- Fix, Changed LDAP Auth and registration logic.
- Fix, Removed LDAP auth indirect bind.
- Fix, Redirect update missing on chart views
- Fix, Charts with unicode data.
- New, add_user on data interfaces accepts new parameter for hashed_password.

Improvements and Bug fixes on 1.3.6
-----------------------------------

- SimpleFormView.form_post can return null to redirect back or a Flask response (render or redirect).
- Changed the way related views are initialized, no bind to the related_views property.
- #144 New MultipleView for rendering multiple BaseViews on the same page.
- Can now import all views from flask_appbuilder.

Improvements and Bug fixes on 1.3.5
-----------------------------------

- Issue #115, Modal text is now html instead of text.

Improvements and Bug fixes on 1.3.4
-----------------------------------

- Issue #119, confirm HTML is included at the begining of body see baselayout.html.

Improvements and Bug fixes on 1.3.3
-----------------------------------

- BaseInterface.get_values changed to iterator (does not return list but list iterator).
- REST CRUD API added.
- Interface datamodels do not flash messages, they log messages on public property tuple 'message'.
- Issue #113, changed html5shiv and respond to import after bootstrap.
- Issue #117, added FilterEqualFunction to MongoDB filters.
- Issue #118, SQLAlchemy version 0.9.9 does not have as_declarative decorator, temp fix by fixing to 0.9.8.
- New, json exposed method was removed from ModelView you must use API now.

Improvements and Bug fixes on 1.3.2
-----------------------------------

- #90 Py3 compact fix for urllib and StringIO.

Improvements and Bug fixes on 1.3.1
-----------------------------------

- Fix, Group by chart with multiple series not displaying data.

Improvements and Bug fixes on 1.3.0
-----------------------------------

- New, block template **head_js** on init.html, affects all templates, better js override or add.
- New, base_template parameter on AppBuilder to override the top template, better css and js inclusion.
- Fix, fixed menu brand with image (APP_ICON), better display.
- New, included boostrap-theme THEME.
- Fix, internal API change, BaseIterface/SQLAInterface method get_model_relation new name: get_related_model.
- New, internal QuerySelectField QuerySelectMultipleField based on BaseInterface.
- New, edit_form_query_rel_fields, add_form_query_rel_fields changed, accepts dict instead of list (BREAKING CHANGE).
- Fix, Filter rework datamodel is no longer optional for construct (BREAKING CHANGE).
- Fix, Filter methods no longer require datamodel parameter (BREAKING CHANGE).
- Fix, All SQLAlchemy Filter's moved to flask_appbuilder.models.sqla.filters.
- New, All Filters are accessible from datamodel class, ex: datamodel.FilterEqual
- New, Charts will be database ordered (better performance), and can accept dotted cols on relations.
- Fix, on menus with dividers if next item has no permission, divider was shown.
- New, Bootstrap update to 3.3.1
- New, Select2 update to 3.5.1
- New, support for many to many relations on ModelView related_view.
- New, AppBuilder.add_link supports endpoint names on href parameter, internally will try to use url_for(href).
- Fix, Zero division catch on aggregate average function.
- New, added form validators for field min and max length.
- New, Image size can be configured per column, ImageColumn support size and thumbnail size parameters.

Improvements and Bug fixes on 1.2.1
-----------------------------------

- Fix, New auth REMOTE_USER bug, always logged in Admin user, db query filter bug.

Improvements and Bug fixes on 1.2.0
-----------------------------------

- Fix, BaseInterface new property for overriding filter converter class, better interface for new classes.
- Fix, search_widget property changed from BaseCRUDView to BaseModelView.
- Fix, Openid auth rework, no hacking done.
- Fix, exclude possible order by for columns that are functions. #67
- Fix, BaseFilter, FilterRelation, BaseFilterRelation changed module from flask.ext.appbuilder.models.base
  to flask.ext.appbuilder.models.filter. (BREAKING CHANGE)
- Fix, sqla filters changed from flask.ext.appbuilder.filters to flask.ext.appbuilder.sql.filters. (BREAKING CHANGE)
- New, AUTH_TYPE = 4 Web server auth via REMOTE_USER enviroment var.
- Fix, #71 set_index_view removed, doc correction.
- Fix, #72 improved german translations.
- Fix, #69 added SQLAlchemy Sequence to pk's to support ORACLE.
- Fix, #69 improved chinese translations.
- Fix, #66 improved spanish translations.

Improvements and Bug fixes on 1.1.3
-----------------------------------

- Fix, User role column was not translated, since 1.1.2.
- Fix, when only one language setup, menu dropdown was not correct.
- Fix, theme default generates 404, issue #60.
- Fix, use of reduce as builtin, python3 problem, issue #58.

Improvements and Bug fixes on 1.1.2
-----------------------------------

- Fix, changing language was redirecting back.

Improvements and Bug fixes on 1.1.1
-----------------------------------

- New, allows order on relationships by implicit declaration of col with dotted notation.
- New, get_order_columns_list receives optional list_columns to narrow search and auto include dotted cols.
- New, dotted columns are also automatically pretty labeled.
- Fix, is<Type col> on SQLInterface handles exceptions for none existing cols.
- Fix, back special URL included on a new View called UtilView, removes bug: when replacing IndexView the back crashes.

Improvements and Bug fixes on 1.1.0
-----------------------------------

- Fix, changed WTForm validator Required to DataRequired.
- Fix, changed WTForm TextField to StringField.
- New, AUTH_USER_REGISTRATION for self user registration, on ldap it's used automatic registration based on ldap attrs.
- New, AUTH_USER_REGISTRATION for auth db will present registration form, send email with configurable html for activation.
- New, AUTH_USER_REGISTRATION for auth oid will present registration form, send email with configurable html for activation.
- New, Added property to AppBuilder that returns the frameworks version.
- New, User extension mixin (Beta).
- New, allows dotted attributes on list_columns, to fetch values from related models.
- New, AuthOIDView with oid_ask_for and oid_ask_for_optional, for easy dev override of view.
- New, Access Denied log a warning with info.
- Fix, OpenID login improvement.

Improvements and Bug fixes on 1.0.1
-----------------------------------

- Fix, field icon for date and datetime that selects calendar, changes mouse cursor to hand.
- New, render_field changed, could be a breaking feature, if you wrote your own forms. no more <td> on each field.
- New, pull request #44, ldap bind options.
- Fix, pull request #48, bug with back button url not working when using uwsgi under sub-domain.
- New, AppBuilder accepts new parameter security_manager_class, useful to override any security view or auth method.


Improvements and Bug fixes on 1.0.0
-----------------------------------

- New, dynamic package version from python file version.py.
- New, extra_args property, for injecting extra arguments to templates.
- Fix, Removed footer with link "Powered by F.A.B.".
- Fix, Added translation for "Access is denied". ES,GE,RU,ZH
- New, Yes and no questions with bootstrap modal.
- Fix, Added multiple actions support on other list widgets.
- Fix, missing translations for "User info" and "Audit info".

Improvements and Bug fixes on 0.10.7
------------------------------------

- Fix, actions break on MasterDetail or related views.

Improvements and Bug fixes on 0.10.6
------------------------------------

- New, Support for multiple actions.

Improvements and Bug fixes on 0.10.5
------------------------------------

- Fix, Russian translations from pull request #39

Improvements and Bug fixes on 0.10.4
------------------------------------

- Fix, merge problem. issue #38

Improvements and Bug fixes on 0.10.3
------------------------------------

- Fix, inserted script in init.html moved to ab.js on static/js.
- Fix, performance improvement on edit, only one form initialization.
- New, New back mechanism, with 5 history records. issue #35.
- New, json endpoint for model querys, with same parameters has list endpoint.
- New, support for boolean columns search, filter with FilterEqual or FilterNotEqual.

Improvements and Bug fixes on 0.10.2
------------------------------------

- Fix, get order columns was including relations.
- New, possibility to include primary key and foreign key on forms and views.
- Fix, python 3 errors on GenericModels, metaclass compatibility.

Improvements and Bug fixes on 0.10.1
------------------------------------

- New, decorator '@permission_name' to override endpoint access permission name.
- Fix, edit_form_query_rel_fields error only on 0.10.0, issue #30.
- Fix, only add permissions to methods with @has_access decorator.
- Fix, prevents duplicate permissions.

Improvements and Bug fixes on 0.10.0
------------------------------------

- New, template block on add.html template, add_form.
- New, template block on edit.html template, edit_form.
- New, template block on show.html template, show_form.
- New, template block on show_cascade.html template, relative_views.
- New, template block on edit_cascade.html template, relative_views.
- New, API Change, DataModel is now BaseInterface and on flask.ext.appbuilder.models.base
- New, API Change, SQLAModel is now SQLAInterface
- New, API Change, SQLAInterface inherits from BaseInterface (not DataModel)
- New, API Change, SQLAInterface is on flask.ext.appbuilder.models.sqla.interface
- New, API Change, Filters for sqla are on flask.ext.appbuilder.models.sqla.filters
- New, API Change, BaseFilter is on flask.ext.appbuilder.model.base
- Fix, nullable Float and Integer bug issue #26
- New, default model sqlalchemy support on forms (issue #26). static and callable value

Improvements and Bug fixes on 0.9.3
-----------------------------------

- Fix, DateTimeField Fix issue #22.
- New, bootstrap updated to version 3.1.1.
- New, fontawesome updated to version 4.1.0.

Improvements and Bug fixes on 0.9.2
-----------------------------------

- Fix, label for 'username' was displaying 'Failed Login Count', Chart definition override.

Improvements and Bug fixes on 0.9.1
-----------------------------------

- New, Support for application factory *init_app* (Flask ext approved guide line).
- New, Flexible group by charts with multiple series and formatters, no need for ChartView or TimeChartView.
- New, internal AppBuilder rebuild.

Improvements and Bug fixes on 0.9.0
-----------------------------------

- New, class name change 'BaseApp' to 'AppBuilder', import like: from flask.ext.appbuilder import AppBuilder
- New, can import expose decorator like: flask.ext.appbuilder import expose
- New, Changed 'Base' declarative name to 'Model' no need to add BaseMixin.
- New, No automatic dev's model creation, must invoke appbuilder.create_db()
- New, Change GeneralView to ModelView.
- Fix, Multiple database support correction.

Improvements and Bug fixes on 0.8.5
-----------------------------------

- New, security cleanup method, useful if you have changed a menu's name or view class name.
- Fix, internal security management optimization.
- New, security management method security_cleanup, will remove unused permissions, views and menus.
- Fix, removed automatic migration from version 0.3.
- New, adding views has classes without configuring the views db.session, session will
    be the same has the security tables.
- Fix, Security menu with wrong label and view association on 'Permission Views/Menu'.

Improvements and Bug fixes on 0.8.4
-----------------------------------

- Fix, js for remembering latest accordion was working like toggle (bs bug?).

Improvements and Bug fixes on 0.8.3
-----------------------------------

- Portuguese Brazil translations

Improvements and Bug fixes on 0.8.2
-----------------------------------

- Fix, possible to register on the menu different links to the same view class.
- Fix, init of baseapp missing init of baseviews list.

Improvements and Bug fixes on 0.8.1
-----------------------------------

- New, Python 3 partial support (babel will not work, caused by the babel package itself).
- Fix, Removed Flask-wtf requirement version limitation.
- New, test suite with nose.

Improvements and Bug fixes on 0.8.0
-----------------------------------

- New, Language, Simplified Chinese support.
- New, Language, Russian support.
- New, Language, German support.
- Fix, various translations.
- Fix,New support for virtual directory no need to install on root url, relative urls fixes.

Improvements and Bug fixes on 0.7.8
-----------------------------------

- New, login form style.
- Fix, Auto creation of user's models from Base.
- Fix, Removed double flash message on reset password form.
- New, support for icons on menu categories.
- New, remove "-" bettwen icons and menu labels.
- New, added optional parameter "label" and "category_label" for menu items. better security and i18n.

Improvements and Bug fixes on 0.7.7
-----------------------------------

- Fix, removed unnecessary log output.

Improvements and Bug fixes on 0.7.6
-----------------------------------

- Fix, TimeChartView not ordering dates correctly.

Improvements and Bug fixes on 0.7.5
-----------------------------------

- New, charts can be included has related views, can use it has tab, collapse and master-detail templates.
- Fix, login ldap, double message login failed correction.
- Fix, search responsive correction.
- New, accordion related view will record last choice on cookie.
- New, footer page, this can be overridden.

Improvements and Bug fixes on 0.7.4
-----------------------------------

- New, internal change, list functional header on lib.
- Fix, removed audit columns from user info view. Only shown on security admin.

Improvements and Bug fixes on 0.7.3
-----------------------------------

- Fix, removed forced cast to int on json conversion for DirectChartView. Better support for float.
- New, List for simple master detail, master works like a menu on the left side.
- Fix, fixed buttons size for show, edit, delete on lists. Buttons will not adapt to vertical.
- Fix, if no permissions for show, edit, delete, no empty cell is shown <th> or <td>.
- New, internal change, crud buttons on lib.

Improvements and Bug fixes on 0.7.2
-----------------------------------

- Fix, reported issue #15. Order by causes error on postgresql.

Improvements and Bug fixes on 0.7.1
-----------------------------------

- New, DirectChart support for xcol datetime.date type (Date or DateTime Model type).
- Fix, base_order property for DirectChartView.

Improvements and Bug fixes on 0.7.0
-----------------------------------

- New, ListBlock with pagination.
- New, Menu separator raises exception if it does not have a correct category.
- New, ShowBlockWidget different show detail presentation.
- Fix, login failed was not displaying error message.
- New, password is saved hashed on database.
- New, better database exceptions on security module
- New, User model columns: last_login, login_count, fail_login_count.
- New, User model column AuditMixin columns (created_on, changed_on, created_by_fk, changed_by_fk).
- New, AuditMixin allows null on FK columns.
- Fix, Add user on non sqlite db, failed if no email provided. Unique db constraint.
- Fix, form convert field exception handling (for method fields).
- New, support for "one to one" relations and "one to many", on forms, and filters (beta).
- Fix, ChartView unicode correction.
- New, DirectChartView to present database queries on numeric columns with multiple series.
- Fix, Adds all missing permissions to the role admin. Allways
- Fix, Removed User.active from possible search.
- New, unicode review for future python 3 support.

Improvements and Bug fixes on 0.6.14
------------------------------------

- Fix, url on time chart views to allow search on every group by column.
- New, support for float database type.

Improvements and Bug fixes on 0.6.13
------------------------------------

- BaseChartView *group_by_columns* empty list validation.
- Fix, url's for charts were changed to allow search on every group by column.

Improvements and Bug fixes on 0.6.11, 0.6.12
--------------------------------------------

- New, *get_file_orginal_name* helper function to remove UUID from file name.
- Fix, bug on related views was not adding new models. Impossible to insert on related views.

Improvements and Bug fixes on 0.6.10
------------------------------------

- Fix, Chart month bug, typo on code.

Improvements and Bug fixes on 0.6.9
-----------------------------------

- Fix, template table display not showing top first line.
- Fix, search widget permits dropdowns with overflow.
- Fix, removed style tag on init.html.
- New, ab.css for F.A.B custom styles.
- New, search widget with dropdown list of column choices, instead of buttons.

Improvements and Bug fixes on 0.6.8
-----------------------------------

- Fix, LDAP server key was hardcoded.

Improvements and Bug fixes on 0.6.7
-----------------------------------

- New, LDAP Authentication type, tested on MS Active Directory.

Improvements and Bug fixes on 0.6.6
-----------------------------------

- New, automatic support for required field validation on related dropdown lists.
- Fix, does not allow empty passwords on user creation.
- Fix, does not allow a user without a role assigned.
- Fix, OpenID bug. Needs flask-openID > 1.2.0

Improvements and Bug fixes on 0.6.5
-----------------------------------

- Fix, allow to filter multiple related fields on forms. Support for Many to Many relations.

Improvements and Bug fixes on 0.6.4
-----------------------------------

- Field widget removed from forms module to new fieldwidgets, this can be a breaking feature.
- Form creation code reorg (more simple and readable).
- New, form db login with icons.
- New, No need to define menu url on chart views (when registering), will work like GeneralViews.
- New, related form field filter configuration, add_form_query_rel_fields and edit_form_query_rel_fields.

Improvements and Bug fixes on 0.6.3
-----------------------------------

- Fix, Add and edit form will not surpress fields if filters come from user search. will only surpress on related views behaviour.
- New, added pagination to list thumbnails.
- Fix, no need to have a config.py to configure key for image upload and file upload.
- New, new config key for resizing images, IMG_SIZE.

Improvements and Bug fixes on 0.6.2
-----------------------------------

- New, compact view with add and edit on the same page has lists. Use of CompactCRUDMixin Mixin.
- Break, GeneralView (BaseCRUDView) related_views attr, must be filled with classes intead of instances.
- Fix, removed Flask-SQlAlchemy version constraint.
- Fix, TimeChartView resolved error with null dates. 
- Fix, registering related_views with instances will raise proper error.
- Fix, filter not supported with report a warning not an error.
- Fix, ImageColumn and FileColumn was being included has a possible filter.

Improvements and Bug fixes on 0.5.7
-----------------------------------

- New, package using python's logging module for correct and flexible logging of info and errors.

Improvements and Bug fixes on 0.5.6
-----------------------------------

- Fix, list_block, list_thumbnail, list_item, bug on set_link_filter.

Improvements and Bug fixes on 0.5.5
-----------------------------------

- New, group by on time charts returns month name and year.
- Fix, better redirect, example: after delete, previous search will be preserved.
- New, widgets module reorg.
- Fix, add and edit with filter was not remving filtered columns, with auto fill.

Improvements and Bug fixes on 0.5.4
-----------------------------------

- Fix, missing import on baseviews, flask.request

Improvements and Bug fixes on 0.5.3
-----------------------------------

- Fix, security.manager api improvement.
- New, property for default order list on GeneralView.
- Fix, actions not permitted will not show on UI.
- Fix, BaseView, BaseModelView, BaseCRUDView separation to module baseviews.
- Fix, Flask-SQlAlchemy requirement version block removed.

Improvements and Bug fixes on 0.5.2
-----------------------------------

- Fix, Auto remove of non existent permissions from database and remove permissions from roles.

Improvements and Bug fixes on 0.5.1
-----------------------------------

- New, top menu support, no need to create category with submenus.
- New, reverse flag for navbar on Menu property.
- New, update bootwatch.

Improvements and Bug fixes on 0.5.0
-----------------------------------

- fix, security userinfo without has_access decorator.
- fix, encoding on search widget (List users breaks on portuguese).
- New, safe back button.
- fix, oid authentication failed.
- New, Change flask-babel to flask-babelpkg to support independent extension translations.
- fix, login forms with complete translations.
- New, actions on records use @action decorator.
- New, support for primary keys of any type.
- New, Font-Awesome included

Improvements and Bug fixes on 0.4.3
-----------------------------------

- New, Search (filter) with boolean types.
- New, Added search to users view.
- New, page size selection.
- New, filter Relation not equal to.

Improvements and Bug fixes on 0.4.1, 0.4.2
------------------------------------------

- Removed constraint in flask-login requirement for versions lower than 0.2.8, can be used 0.2.7 or lower and 0.2.9 and higher.
- fix, BaseCRUDView init properties correction.
- fix, delete user generates general error key.
- Changed default page_size to 10.

Improvements and Bug fixes on 0.4.0
-----------------------------------

- fix, page was "remenbered" by class, returned empty lists on queries and inline lists.
- New Filters class and BaseFilter with many subclasses. Restructing internals to enable feature.
- New UI for search widget, dynamic filters showing the possibilities from filters. Starts with, greater then, etc...
- New possible filters for dates, greater then, less, equal filters.
- Restructuring of query function, simplified.
- Internal class inherit change: BaseView, BaseModelView, BaseCRUDView, GeneralView.
- Internal class inherit change: BaseView, BaseModelView, BaseChartView, (ChartView|TimeChartView).
- Argument URL filter change "_flt_<index option filter>_<Col name>=<value>"
- New, no need to define search_columns property, if not defined all columns can be added to search.
- New, no need to define list_columns property, if not defined only the first orderable column will be displayed.
- New, no need to define order_columns property, if not defined all ordered columns will be defined.
- fix, class init properties correction
- New property base_filters to always filter the view, accepts functions and values with current filters
- Babel actualization for filters in spanish and portuguese

Improvements and Bug fixes on 0.3.17
------------------------------------

- fix, Redirect to login when access denied was broken.

Improvements and Bug fixes on 0.3.16
------------------------------------

- fix, Reset password form

Improvements and Bug fixes on 0.3.15
------------------------------------

- Html non compliance corrections
- Charts outside panel correction

Improvements and Bug fixes on 0.3.12
------------------------------------

- New property add_form_extra_fields to inject extra fields on add form
- New property edit_form_extra_fields to inject extra fields on edit form
- Add and edit form order correction, order in add_columns, edit_columns or fieldsets
- Correction of bootstrap inclusion

Improvements and Bug fixes on 0.3.11
------------------------------------

- Bootstrap css and js included in the package
- Jquery included in the package
- Google charts jsapi included in the package
- requirement and setup preventing install for flask-login 0.2.8 only 0.2.7 or earlier, bug on init.html

Improvements and Bug fixes on 0.3.10
------------------------------------

- New config key APP_ICON to include an image to the navbar.
- Removed "Home" on the menu
- New Widget for displaying lists of items ListItem (Widget)
- New widget for displaying lists on blocks thumbnails
- Logout translation on portuguese and spanish


Improvements and Bug fixes on 0.3.9
-----------------------------------

- Chart views with equal presentation has list views.
- Chart views with search possibility
- BaseMixin with automatic table name like flask-sqlalchemy, no need to use db.Model.
- Pre, Post methods to override, removes decorator classmethod

Improvements and Bug fixes on 0.3.0
-----------------------------------

- AUTH_ROLE_ADMIN, AUTH_ROLE_PUBLIC not required to be defined.
- UPLOAD_FOLDER, IMG_UPLOAD_FOLDER, IMG_UPLOAD_URL not required to be defined.
- AUTH_TYPE not required to be defined, will use default database auth
- Internal security changed, new internal class SecurityManager
- No need to use the base AppBuilder-Skeleton, removed direct import from app directory.
- No need to use init_app.py first run will create all tables and insert all necessary permissions.
- Auto migration from version 0.2.X to 0.3.X, because of security table names change.
- Babel translations for Spanish
- No need to initialize LoginManager, OID.
- No need to initialize Babel (Flask-Babel) (since 0.3.5).
- General import corrections
- Support for PostgreSQL


Improvements and Bug fixes on 0.2.0
-----------------------------------

- Pagination on lists.
- Inline (panels) will reload/return to the same panel (via cookie).
- Templates with url_for.
- BaseApp injects all necessary filter in jinja2, no need to import.
- New Chart type, group by month and year.
- No need to define route_base on View Classes, will assume class name in lower case.
- No need to define labels for model's columns, they will be prettified.
- No need to define titles for list,add,edit and show views, they will be generated from the model's name.
- No need to define menu url when registering a BaseView will be infered from BaseView.defaultview.
- OpenID pictures not showing.
- Security reset password corrections.
- Date null Widget correction.
- list filter with text
- Removed unnecessary keys from config.py on skeleton and examples.
- Simple group by correction, when query does not use joined models.
- Authentication with OpenID does not need reset password option.

