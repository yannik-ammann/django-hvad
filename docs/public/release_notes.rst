#############
Release Notes
#############

.. release 1.1.0

*****************************
1.1.0 - upcoming release
*****************************

.. note:: This version is being developed. If you feel like helping, or want the
          very latest feature, you can install it from the `github repository`_.
          Otherwise, please get a `packaged release`_ instead.

New features:

- It is now possible to use translated fields in the
  :attr:`~django.db.models.Options.unique_together` and
  :attr:`~django.db.models.Options.index_together` settings on
  :doc:`TranslatableModel <models>`. They cannot be mixed in a single constraint
  though, as table-spanning indexes are not supported by SQL databases.

Compatibility warnings:

- Deprecated :meth:`~hvad.manager.TranslationManager.using_translations` has been removed.
  It can be safely replaced by :meth:`~hvad.manager.TranslationManager.language`.
- Deprecated :class:`~hvad.manager.TranslationFallbackManager` has been removed. Please
  use manager's :meth:`~hvad.manager.TranslationManager.untranslated` method instead.
- Deprecated :class:`~hvad.models.TranslatableModelBase` metaclass has been removed.
  Since release 0.5, hvad does not trigger metaclass conflicts anymore – :issue:`188`.
- Overriding the language in :meth:`QuerySet.get() <django.db.models.query.QuerySet.get>`
  and :meth:`QuerySet.filter() <django.db.models.query.QuerySet.filter>` was
  deprecated in release 0.5, and has now been removed. Either use the
  :meth:`~hvad.manager.TranslationManager.language` method to set the
  correct language, or specify
  :meth:`language('all') <hvad.manager.TranslationManager.language>` to filter
  manually through ``get`` and ``filter`` – :issue:`182`.
- ``TranslatableModel``'s Internal attribute ``_shared_field_names`` has been removed.

Deprecation list:

- Passing ``unique_together`` or ``index_together`` as a ``meta`` option on
  :class:`~hvad.models.TranslatedFields` is now deprecated and will be unsupported
  in release 1.3. Put them in the model's :djterm:`Meta <meta-options>`
  instead, alongside normal fields.
- Calling ``save()`` on an invalid :ref:`TranslatableModelForm <translatablemodelform>`
  is a bad practice and breaks on regular Django forms. This is now deprecated,
  and relevant checks will be removed in release 1.3. Please check the form is
  valid before saving it.
- Generic views in ``hvad.views`` have been refactored to follow Django generic
  view behaviors. As a result, several non-standard methods are now deprecated.
  Please replace them with their Django equivalents — check :issue:`225`.

.. release 1.0.0

*****************************
1.0.0 - current release
*****************************

Released on December 19, 2014

Python and Django versions supported:

- Django 1.3 is no longer supported.
- Python 2.6 is no longer supported. Though it is likely to work for the time
  being, it has been dropped from the tested setups.

New features:

- :ref:`TranslatableModelForm <translatablemodelform>` has been refactored to make
  its behavior more consistent. As a result, it exposes two distinct language
  selection modes, *normal* and *enforce*, and has a clear API for manually
  overriding the language — :issue:`221`.
- The new features of :func:`~django.forms.models.modelform_factory` introduced by
  Django 1.6 and 1.7 are now available on
  :ref:`translatable_modelform_factory <translatablemodelformfactory>` as
  well — :issue:`221`.
- :ref:`TranslationQueryset <TranslationQueryset-public>` now has a
  :ref:`fallbacks() <fallbacks-public>` method when running on
  Django 1.6 or newer, allowing the queryset to use fallback languages while
  retaining all its normal functionalities – :issue:`184`.
- Passing additional ``select`` items in method
  :meth:`~django.db.models.query.QuerySet.extra` is now supported. — :issue:`207`.
- It is now possible to use :ref:`TranslationQueryset <TranslationQueryset-public>`
  as default queryset for translatable models. — :issue:`207`.
- A lot of tests have been added, hvad now has 100% coverage on its core modules.
  Miscellaneous glitches found in this process were fixed.
- Added MySQL to tested database backends on Python 2.7.

Compatibility warnings:

- :ref:`TranslatableModelForm <translatablemodelform>` has been refactored to make
  its behavior more consistent. The core API has not changed, but edge cases are
  now clearly specified and some inconsistencies have disappeared, which could
  create issues, especially:

  - Direct use of the form class, without passing through the
    :ref:`factory method <translatablemodelformfactory>`. This used to have an
    unspecified behavior regarding language selection. Behavior is now
    well-defined. Please ensure it works the way you expect it to.

Fixes:

- :ref:`TranslatableModelForm <translatablemodelform>`'s
  :meth:`~django.forms.Form.clean` can now return `None` as per the new semantics
  introduced in Django 1.7. — :issue:`217`.
- Using ``Q object`` logical combinations or
  :meth:`~django.db.models.query.QuerySet.exclude` on a translation-aware
  manager returned by :func:`~hvad.utils.get_translation_aware_manager` no longer
  yields wrong results.
- Method :meth:`~django.db.models.query.QuerySet.get_or_create` now properly deals
  with Django 1.6-style transactions.

.. release 0.5.2

*****************************
0.5.2
*****************************

Released on November 8, 2014

Fixes:

- Admin does not break anymore on M2M fields on latest Django versions. — :issue:`212`.
- Related fields's :meth:`~django.db.models.fields.related.RelatedManager.clear`
  method now works properly (it used to break on MySQL, and was inefficient on
  other engines) — :issue:`212`.

.. release 0.5.1

*****************************
0.5.1
*****************************

Released on October 24, 2014

Fixes:

- Ecountering a regular (un-translatable) model in a deep `select_related` does
  not break anymore. — :issue:`206`.
- Language tabs URI are now correctly generated when changelist filters are used.
  — :issue:`203`.
- Admin language tab selection is no longer lost when change filters are active.
  — :issue:`202`.

.. release 0.5.0

*****************************
0.5.0
*****************************

Released on September 11, 2014

New features:

- New :ref:`translationformset_factory <translationformset>` and its companion
  :class:`~hvad.forms.BaseTranslationFormSet` allow building a formset to work
  on an instance's translations. Please have at look at its detailed
  :ref:`documentation <translationformset>` – :issue:`157`.
- Method :meth:`~hvad.manager.TranslationQueryset.language` now accepts the
  special value ``'all'``, allowing the query to consider all translations – :issue:`181`.
- Django 1.6+'s new :meth:`~django.db.models.query.QuerySet.datetimes` method is
  now available on :class:`~hvad.manager.TranslationQueryset` too – :issue:`175`.
- Django 1.6+'s new :meth:`~django.db.models.query.QuerySet.earliest` method is
  now available on :class:`~hvad.manager.TranslationQueryset`.
- Calls to :meth:`~hvad.manager.TranslationQueryset.language`, passing ``None``
  to use the current language now defers language resolution until the query is
  evaluated. It can now be used in form definitions directly, for instance for
  passing a custom queryset to :class:`~django.forms.ModelChoiceField` – :issue:`171`.
- Similarly, :meth:`~hvad.manager.FallbackQueryset.use_fallbacks` can now be
  passed ``None`` as one of the fallbacks, and it will be replaced with current
  language at query evaluation time.
- All queryset classes used by :class:`~hvad.manager.TranslationManager` can now
  be customized thanks to the new :attr:`~hvad.manager.TranslationManager.fallback_class`
  and :attr:`~hvad.manager.TranslationManager.default_class` attributes.
- Abstract models are now supported. The concrete class must still declare a
  :class:`~hvad.models.TranslatedFields` instance, but it can be empty – :issue:`180`.
- Django-hvad messages are now available in Italian – :issue:`178`.
- The :attr:`Meta.ordering <django.db.models.Options.ordering>` model setting
  is now supported on translatable models. It accepts both translated and shared
  fields – :issue:`185`, :issue:`12`.
- The :meth:`~hvad.manager.TranslationQueryset.select_related` method is no longer
  limited to 1 level depth – :issue:`192`.
- The :meth:`~hvad.manager.TranslationQueryset.select_related` method semantics
  is now consistent with that of regular querysets. It supports passing ``None``
  to clear the list and mutiple calls mimic Django behavior. That is: cumulative
  starting from Django 1.7 and substitutive before – :issue:`192`.

Deprecation list:

- The deprecated ``nani`` module was removed.
- Method :meth:`~hvad.manager.TranslationManager.using_translations` is now deprecated.
  It can be safely replaced by :meth:`~hvad.manager.TranslationManager.language`
  with no arguments.
- Setting ``NANI_TABLE_NAME_SEPARATOR`` was renamed to ``HVAD_TABLE_NAME_SEPARATOR``.
  Using the old name will still work for now, but issue a deprecation warning,
  and get removed in next version.
- CSS class ``nani-language-tabs`` in admin templates was renamed to
  ``hvad-language-tabs``. Entities will bear both classes until next version.
- Private ``_real_manager`` and ``_fallback_manager`` attributes of
  :class:`~hvad.manager.TranslationQueryset` have been removed as the indirection
  served no real purpose.
- The :class:`~hvad.manager.TranslationFallbackManager` is deprecated and will
  be removed in next release. Please use manager's
  :meth:`~hvad.manager.TranslationManager.untranslated` method instead.
- The :class:`~hvad.models.TranslatableModelBase` metaclass is no longer
  necessary and will be removed in next release. hvad no longer triggers metaclass
  conflicts and ``TranslatableModelBase`` can be safely dropped – :issue:`188`.
- Overriding the language in :meth:`QuerySet.get() <django.db.models.query.QuerySet.get>`
  and :meth:`QuerySet.filter() <django.db.models.query.QuerySet.filter>` is now
  deprecated. Either use the :meth:`~hvad.manager.TranslationManager.language`
  method to set the correct language, or specify
  :meth:`language('all') <hvad.manager.TranslationManager.language>` to filter
  manually through ``get`` and ``filter`` – :issue:`182`.

Fixes:

- Method :meth:`~django.db.models.query.QuerySet.latest` now works when passed
  no field name, properly getting the field name from the model's
  :attr:`Meta.get_latest_by <django.db.models.Options.get_latest_by>` option.
- :class:`~hvad.manager.FallbackQueryset` now leverages the better control on
  queries allowed in Django 1.6 and newer to use only one query to resolve
  fallbacks. Old behavior can be forced by adding ``HVAD_LEGACY_FALLBACKS = True``
  to your settings.
- Assigning value to translatable foreign keys through its ``_id`` field no
  longer results in assigned value being ignored – :issue:`193`.
- Tests were refactored to fully support PostgreSQL – :issue:`194`

.. release 0.4.1

*****************************
0.4.1
*****************************

Released on June 1, 2014

Fixes:

- Translations no longer remain in database when deleted depending on
  the query that deleted them – :issue:`183`.
- :meth:`~hvad.models.TranslatableModel.get_available_languages` now
  uses translations if they were prefetched with
  :meth:`~django.db.models.query.QuerySet.prefetch_related`.  Especially, using
  :meth:`~hvad.admin.TranslatableAdmin.all_translations` in
  :attr:`~django.contrib.admin.ModelAdmin.list_display` no longer results in one
  query per item, as long as translations were prefetched –
  :issue:`179`, :issue:`97`.


.. release 0.4.0

*****************************
0.4.0
*****************************

Released on May 19, 2014

New Python and Django versions supported:

- django-hvad now supports Django 1.7 running on Python 2.7, 3.3 and 3.4.
- django-hvad now supports Django 1.6 running on Python 2.7 and 3.3.

New features:

- :class:`~hvad.manager.TranslationManager`'s queryset class can now be overriden by
  setting its :attr:`~hvad.manager.TranslationManager.queryset_class` attribute.
- Proxy models can be used with django-hvad. This is a new feature, please
  use with caution and report any issue on github.
- :class:`~hvad.admin.TranslatableAdmin`'s list display now has direct links
  to each available translation.
- Instance's translated fields are now available to the model's
  :meth:`~django.db.models.Model.save` method when saving a
  :class:`~hvad.forms.TranslatableModelForm`.
- Accessing a translated field on an untranslated instance will now raise an
  :exc:`~exceptions.AttributeError` with a helpful message instead of letting the
  exception bubble up from the ORM.
- Method :meth:`~hvad.manager.TranslationQueryset.in_bulk` is now available on
  :class:`~hvad.manager.TranslationQueryset`.

Deprecation list:

- Catching :exc:`~django.core.exceptions.ObjectDoesNotExist` when accessing
  a translated field on an instance is deprecated. In case no translation
  is loaded and none exists in database for current language, an
  :exc:`~exceptions.AttributeError` is raised instead. For the transition,
  both are supported until next release.

Removal of the old ``'nani'`` aliases was postponed until next release.

Fixes:

- Fixed an issue where :class:`~hvad.admin.TranslatableAdmin` could overwrite the
  wrong language while saving a form.
- :meth:`~hvad.models.TranslatableModel.lazy_translation_getter` now tries
  translations in :setting:`LANGUAGES` order once it has failed with current
  language and site's main :setting:`LANGUAGE_CODE`.
- No more deprecation warnings when importing only from ``hvad``.
- :class:`~hvad.admin.TranslatableAdmin` now generates relative URLs instead
  of absolute ones, enabling it to work behind reverse proxies.
- django-hvad does not depend on the default manager being named
  'objects' anymore.
- Q objects now work properly with :class:`~hvad.manager.TranslationQueryset`.

.. release-0.3

*****************************
0.3
*****************************

New Python and Django versions supported:

- django-hvad now supports Django 1.5 running on Python 2.6 and 2.6.

Deprecation list:

- Dropped support for django 1.2.
- In next release, the old 'nani' module will be removed.


.. release-0.2

*****************************
0.2
*****************************

The package is now called 'hvad'. Old imports should result in an import error.

Fixed django 1.4 support

Fixed a number of minor issues



.. release-0.1.4

*****************************
0.1.4 (Alpha)
*****************************

Released on November 29, 2011

- Introduces :meth:`lazy_translation_getter`


.. release-0.1.3

*****************************
0.1.3 (Alpha)
*****************************

Released on November 8, 2011

- A new setting was introduced to configure the table name separator, ``NANI_TABLE_NAME_SEPARATOR``.

  .. note::

       If you upgrade from an earlier version, you'll have to rename your tables yourself (the general template is
       ``appname_modelname_translation``) or set ``NANI_TABLE_NAME_SEPARATOR`` to the empty string in your settings (which
       was the implicit default until 0.1.0)

.. release-0.0.4

*****************************
0.0.4 (Alpha)
*****************************

.. release-0.0.3

*************
0.0.3 (Alpha)
*************

Released on May 26, 2011.

* Replaced our ghetto fallback querying code with a simplified version of the
  logic used in Bert Constantins `django-polymorphic`_, all credit for our now
  better FallbackQueryset code goes to him.
* Replaced all JSON fixtures for testing with Python fixtures, to keep tests
  maintainable.
* Nicer language tabs in admin thanks to the amazing help of Angelo Dini.
* Ability to delete translations from the admin.
* Changed hvad.admin.TranslatableAdmin.get_language_tabs signature.
* Removed tests from egg.
* Fixed some tests possibly leaking client state information.
* Fixed a critical bug in hvad.forms.TranslatableModelForm where attempting to
  save a translated model with a relation (FK) would cause IntegrityErrors when
  it's a new instance.
* Fixed a critical bug in hvad.models.TranslatableModelBase where certain field
  types on models would break the metaclass. (Many thanks to Kristian
  Oellegaard for the fix)
* Fixed a bug that prevented abstract TranslatableModel subclasses with no
  translated fields.


.. release-0.0.2

*************
0.0.2 (Alpha)
*************

Released on May 16, 2011.

* Removed language code field from admin.
* Fixed admin 'forgetting' selected language when editing an instance in another
  language than the UI language in admin.


.. release-0.0.1

*************
0.0.1 (Alpha)
*************

Released on May 13, 2011.

* First release, for testing purposes only.


.. _django-polymorphic: https://github.com/bconstantin/django_polymorphic
.. _github repository: https://github.com/KristianOellegaard/django-hvad
.. _packaged release: https://pypi.python.org/pypi/django-hvad
