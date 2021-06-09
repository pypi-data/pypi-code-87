import re
from datetime import timedelta
from typing import List, Tuple, Any, Callable, Union, Optional

import traceback
import os
import inflection as inflection
from arrow import Arrow
from django.db import models

from django_koldar_utils.django.fields.ArrowField import ArrowField



class Orm:

    _table_convention = "verbose"

    @classmethod
    def set_table_naming_convention(cls, v: str):
        """
        Change the way each model table are generated.

        :param v: naming convention.
            - verbose: we use "=" inside table names and we generate relationships name as they were predicates
            - standard: we use "." in table names and we generate realtionship names by concatenating the table names with "_"
        """
        cls._table_convention = v

    DO_NOT_CREATE_INVERSE_RELATION = "+"
    """
    Value to put in a ForeignKeyField in "relateD_name". If you do this, the reverse relation won't be created at all 
    """

    @classmethod
    def get_current_app_name(cls) -> str:
        for frame in reversed(list(filter(lambda x: "<string>" not in x, filter(lambda x: os.path.join("utils", "Orm.py") not in x,
                                                          filter(lambda x: "pydev" not in x,
                                                                 traceback.format_stack()))))):
            frame_str = str(frame)
            # something like "app_name/models.py"
            for f in ["models", "admin", "apps", "graphql_types", "mutations", "queries", "tests", "urls", "views"]:
                try:
                    index = frame_str.index(f + ".py")
                    file_name = frame_str[:index]
                    file_name = str(re.sub(r"^\s+File\s+\"", "", file_name))
                    app_name = os.path.basename(os.path.dirname(file_name))
                    return app_name
                except ValueError:
                    pass
        else:
            raise ValueError(f"Cannot find app name!")

    @classmethod
    def create_table_name(cls, model_cls: str) -> str:
        app_name = Orm.get_current_app_name()
        app_name = app_name.replace("_section", "")
        if cls._table_convention == "verbose":
            return f"{app_name}={model_cls}"
        elif cls._table_convention == "standard":
            return f"{app_name}.{model_cls}"
        else:
            raise ValueError(f"invalid table convention value {cls._table_convention}!")

    @classmethod
    def create_n_n_table_name(cls, name: str, basemodels: List[str]):
        """
        Create a new relationship name This name is the name fo the table representing the relationship name
        :param name:
        :param basemodels:
        :return:
        """
        app_name = Orm.get_current_app_name()
        app_name = app_name.replace("_section", "")
        result = []
        for m in basemodels:
            if isinstance(m, str):
                # the string may be of type "app_name.model". if so, remove the app_name part
                m = m.split(".")[-1]
                result.append(m)
            elif isinstance(m, type):
                result.append(type(m).__name__)
            else:
                raise TypeError(f"Invalid model type {type(m)}")

        if cls._table_convention == "verbose":
            return f"{app_name}={name}({','.join(result)})"
        elif cls._table_convention == "standard":
            return f"{name}_{'_'.join(result)}"
        else:
            raise ValueError(f"invalid table convention value {cls._table_convention}!")


    @staticmethod
    def generic_field_simple(field_type: type, null: bool, blank: bool, default: Union[Any, Callable[[], Any]],
                          help_text: str):
            """
            :param field_type: type of the field to create
            :param null: If True, Django will store empty values as NULL in the database
            :param blank: Note that this is different than null. null is purely database-related, whereas blank is
                validation-related. If a field has blank=True, form validation will allow entry of an empty value.
                If a field has blank=False, the field will be required.
            :param default: The default value for the field. This can be a value or a callable object.
                If callable it will be called every time a new object is created.
                You cannot use lambdas, but only named fields.
            :param help_text: Extra “help” text to be displayed with the form widget. It’s useful for documentation
                even if your field isn’t used on a form. The strnig is not HTML escaped.
            :return:
            """
            return Orm.generic_field(
                field_type=field_type,
                null=null,
                blank=blank,
                choices=None,
                db_column=None,
                db_index=False,
                default=default,
                error_messages=None,
                help_text=help_text,
                primary_key=False,
                unique=False,
                unique_for_date=None,
                unique_for_year=None,
                unique_for_month=None,
                verbose_name=None,
                validators=[],
                max_length=None
            )

    @staticmethod
    def generic_field(field_type: type, null: bool, blank: bool, choices: List[Tuple[Any, Any]], db_column: Optional[str], db_index: bool, default: Union[Any, Callable[[], Any]], error_messages: Optional[List[str]], help_text: str, primary_key: bool, unique: bool, unique_for_date: Optional[str], unique_for_month: Optional[str], unique_for_year: Optional[str], verbose_name: Optional[str], validators: List[Callable[[Any], None]], max_length: int):
        """
        :param field_type: type of the field to create
        :param null: If True, Django will store empty values as NULL in the database
        :param blank: Note that this is different than null. null is purely database-related, whereas blank is
            validation-related. If a field has blank=True, form validation will allow entry of an empty value.
            If a field has blank=False, the field will be required.
        :param choices: If choices are given, they’re enforced by model validation and the default form widget will
            be a select box with these choices instead of the standard text field.
        :param db_column: The name of the database column to use for this field. If this isn’t given,
            Django will use the field’s name
        :param db_index: If True, a database index will be created for this field.
        :param default: The default value for the field. This can be a value or a callable object.
            If callable it will be called every time a new object is created.
            You cannot use lambdas, but only named fields.
        :param error_messages: The error_messages argument lets you override the default messages that the
            field will raise. Pass in a dictionary with keys matching the error messages you want to overrid
        :param help_text: Extra “help” text to be displayed with the form widget. It’s useful for documentation
            even if your field isn’t used on a form. The strnig is not HTML escaped.
        :param primary_key: is True, the field is a primary key. primary_key=True implies null=False and unique=True.
            Only one primary key is allowed on an object.
        :param unique: If True, this field must be unique throughout the table.
        :param unique_for_date: Set this to the name of a DateField or DateTimeField to require that this field
            be unique for the value of the date field.
        :param unique_for_month: Like unique_for_date, but requires the field to be unique with respect to the month.
        :param unique_for_year: Like unique_for_date and unique_for_month.
        :param verbose_name: A human-readable name for the field
        :param validators:  A list of validators to run for this field
        :param max_length: in models like CharField, the length of the field
        :return:
        """
        d = dict(
            null=null,
            blank=blank,
            choices=choices,
            db_column=db_column,
            db_index=db_index,
            default=default,
            error_messages=error_messages,
            help_text=help_text,
            primary_key=primary_key,
            unique=unique,
            unique_for_date=unique_for_date,
            unique_for_month=unique_for_month,
            unique_for_year=unique_for_year,
            verbose_name=verbose_name,
            validators=validators,
            max_length=max_length,
        )
        return field_type(**d)

    @staticmethod
    def required_long_string(help_text: str) -> models.CharField:
        return Orm.generic_field(
            field_type=models.CharField,
            null=False,
            blank=False,
            default=None,
            help_text=help_text,

            choices=None,
            db_column=None,
            db_index=False,
            error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None,
            unique_for_year=None,
            unique_for_month=None,
            verbose_name=None,
            validators=[],
            max_length=255
        )

    @classmethod
    def relationship_many_to_many(cls, from_model: Union[str, type], to_model: Union[str, type],
                                         relationship_model: Union[str, type], related_name: str, help_text: str = None) -> models.ManyToManyField:
        """
        one author has many publications and each publication is made by many authros.
        This should be put in the "author". The model output name should be something repersenting the other end of the
        relationship itself (without considering the through model), so something like "authors".
        The related_name should have the same name as the resulting value of "relationship_many_to_many_inverse".
        :param from_model: author
        :param to_model: publication
        :param help_text: help text
        :return:
        """
        return models.ManyToManyField(
            from_model,
            help_text=help_text,
            through=relationship_model,
            related_name=related_name
        )

    @classmethod
    def relationship_many_to_many_in_through_inverse(cls, from_model: Union[str, type], to_model: Union[str, type],
                                          relationship_model: Union[str, type]) -> models.Manager:
        """
        Represents the manager that is used to fetch the "through" model. Needs to be put at both ends of the
        N-N relationship.

        The output name should be the same as the "related_name" in the "through" model of the method
        "relationship_many_to_many_in_through".

        :param from_model: model where the relationship starts
        :param to_model: model where the relaionship ends
        :param relationship_model: model of the through relationship
        :see https://gist.github.com/jacobian/827937#file-models-py:
        """
        pass

    @classmethod
    def relationship_many_to_many_inverse(cls, from_model: Union[str, type], to_model: Union[str, type],
                                          relationship_model: Union[str, type]) -> models.Manager:
        """
        one author has many publications and each publication is made by many authros.
        This should be put in the "publications". The result value should be somethign repersenting
        the relationship, like "written_by"
        :param from_model: author
        :param to_model: publication
        :param help_text: help text
        :return:
        """
        pass

    @classmethod
    def relationship_many_to_many_in_through(cls, to_model: Union[str, type], on_delete, related_name: str) -> models.ForeignKey:
        """
        one author has many publications and each publication is made by many authros.
        This should be put in the model represneting hte relationship itself. For example:
            publication = relationship_many_to_many_though(Publication, models.CASCADE)
            author = relationship_many_to_many_though(Author, models.CASCADE)
        :param to_model: publication
        :param on_delete: what to do whenever a delete is performed
        :param related_name: inverse relation from "to_model" to gain access to this relationship
        :return:
        """
        return models.ForeignKey(to_model, on_delete=on_delete, related_name=related_name)

    @classmethod
    def relationship_many_to_many_simple(cls, from_model: Union[str, type], to_model: Union[str, type],
                                 relationship_name: str, related_name: str, help_text: str = None) -> models.ManyToManyField:
        """
        one author has many publications and each publication is made by many authros.
        This should be put in the "author"
        :param from_model: author
        :param to_model: publication
        :param on_delete: what to do whenever a delete is performed
        :param help_text: help text
        :param related_name: name of the inverse relations
        :return:
        """
        return models.ManyToManyField(
            from_model,
            help_text=help_text,
            related_name=related_name,
            db_table=Orm.create_n_n_table_name(relationship_name, [from_model, to_model])
        )

    @classmethod
    def relationship_many_to_many_simple_inverse(cls, from_model: Union[str, type], to_model: Union[str, type],
                                         relationship_name: str, help_text: str = None) -> models.Manager:
        """
        one author has many publications and each publication is made by many authros.
        This should be put in the "publications"
        :param from_model: author
        :param to_model: publication
        :param help_text: help text
        :return:
        """
        pass

    @classmethod
    def relationship_one_to_many(cls, single_model: Union[str, type], multi_model: Union[str, type],
                                 relationship_name: str) -> models.Manager:
        """
        one author has many contacts. This should be put in the "author" (but an authro has at least one contact).
        The relation needs to be positioned on the single_model entity

        :note:
        The name of the return value in the model must be the related name of the inverse relation

        :param single_model: author
        :param multi_model: contacts
        :param relationship_name: name of the relation
        :return:
        """
        pass

    @classmethod
    def relationship_one_to_many_inverse(cls, single_model: Union[str, type], multi_model: Union[str, type], on_delete,
                                         related_name: str, relationship_name: str, related_query_name: str = None, help_text: str = None) -> models.ForeignKey:
        """
        one author has many contacts. This should be put in the "contacts" (but an authro has at least one contact).

        :param single_model: author
        :param multi_model: contacts
        :param on_delete: what to do whenever a delete is performed
        :param related_name: name of the field that s the return value of :relationship_one_to_many: on the single_model
        :param related_query_name: name fo the django query
        :param relationship_name: name of the "one to many" realtionship.
        :param help_text: help text
        :return:
        """
        return models.ForeignKey(
            single_model,
            on_delete=on_delete,
            help_text=help_text,
            null=False,
            related_name=related_name,
            related_query_name=related_query_name,
            db_column=f"id_{relationship_name}_{single_model}"
        )

    @classmethod
    def relationship_zero_to_many(cls, single_model: Union[str, type], multi_model: Union[str, type],
                                 relationship_name: str) -> models.Manager:
        """
        one author has many articles. This should be put in the "author". (but an authro can have zero articles)
        The relation needs to be positioned on the single_model entity

        :note:
        The name of the return value in the model must be the related name of the inverse relation

        :param single_model: author
        :param multi_model: contacts
        :param relationship_name: name of the relation
        :return:
        """
        pass

    @classmethod
    def relationship_zero_to_many_inverse(cls, single_model: Union[str, type], multi_model: Union[str, type], on_delete,
                                         related_name: str, relationship_name: str, related_query_name: str = None, help_text: str = None) -> models.ForeignKey:
        """
        one author has many articles. This should be put in the "article".  (but an authro can have zero articles)
        :param single_model: author
        :param multi_model: articles
        :param on_delete: what to do whenever a delete is performed
        :param related_name: name of the field that s the return value of :relationship_zero_to_many: on the single_model
        :param related_query_name: name fo the django query
        :param relationship_name: name of the "one to many" realtionship.
        :param help_text: help text
        :return:
        """
        return models.ForeignKey(
            single_model,
            on_delete=on_delete,
            help_text=help_text,
            null=True,
            related_name=related_name,
            related_query_name=related_query_name,
            db_column=f"id_{relationship_name}_{single_model}"
        )

    @classmethod
    def relationship_one_to_one(cls, from_model: Union[str, type], to_model: Union[str, type], relationship_name: str, on_delete, related_name: str, related_query_name: str = None, help_text: str = None) -> models.OneToOneField:
        """
        one author has one name. This should be put in the "author"
        :param from_model: author
        :param to_model: name
        :param on_delete: what to do whenever a delete is performed
        :param help_text: help text
        :return:
        """
        return models.OneToOneField(
            to_model,
            on_delete=on_delete,
            help_text=help_text,
            null=False,
            blank=False,
            related_name=related_name,
            related_query_name=related_query_name,
            db_column=f"id_{relationship_name}_{to_model}"
        )

    @classmethod
    def relationship_one_to_one_inverse(cls, from_model: Union[str, type], to_model: Union[str, type],
                                        relationship_name: str) -> models.Manager:
        """
        one author has one name. This should be put in the "name"
        :param from_model: author
        :param to_model: name
        :return:
        """
        pass

    @classmethod
    def relationship_one_to_zeroone(cls, from_model: Union[str, type], to_model: Union[str, type], relationship_name: str, on_delete,
                                related_name: str, related_query_name: str = None, help_text: str = None) -> models.OneToOneField:
        """
        one author has one name. This should be put in the "author"
        :param from_model: author
        :param to_model: name
        :param on_delete: what to do whenever a delete is performed
        :param help_text: help text
        :return:
        """
        return models.OneToOneField(
            to_model,
            on_delete=on_delete,
            help_text=help_text,
            null=True,
            blank=True,
            related_name=related_name,
            related_query_name=related_query_name,
            db_column=f"id_{relationship_name}_{to_model}"
        )

    @classmethod
    def relationship_one_to_zeroone_inverse(cls, from_model: Union[str, type], to_model: Union[str, type],
                                        relationship_name: str, help_text: str = None) -> models.Manager:
        """
        one author has one name. This should be put in the "name"
        :param from_model: author
        :param to_model: name
        :param help_text: help text
        :return:
        """
        pass

    def required_indexed_string(self, description: str, default_value: Union[str, Callable[[], str]] = None, max_length: int = None) -> models.CharField:
        """
        Tells Django that the model has a string field. If default value is set, it is the value added to the database
        if the user does not provide a value. The field itself is non nullable. We will create an index for quick recovery

        :param description: text used to explain what the field does
        :param default_value: value to set the field to if the developer does not add a value by herself
        :param max_length: maximum number of hcaracters in the string. If left unspecified, it is 255
        :return: string type
        """
        if max_length is None:
            max_length = 255
        return Orm.generic_field(
            field_type=models.CharField,
            null=False,
            blank=False,
            default=default_value,
            help_text=description,
            choices=None,
            db_column=None,
            db_index=True,
            error_messages=None,
            primary_key=False,
            unique=True,
            unique_for_date=None,
            unique_for_year=None,
            unique_for_month=None,
            verbose_name=None,
            validators=[],
            max_length=max_length
        )

    @classmethod
    def required_string(cls, description: str, default_value: Union[str, Callable[[], str]] = None, max_length: int = None) -> models.CharField:
        """
        Tells Django that the model has a string field. If default value is set, it is the value added to the database
        if the user does not provide a value. The field itself is non nullable

        :param description: text used to explain what the field does
        :param default_value: value to set the field to if the developer does not add a value by herself
        :param max_length: maximum number of hcaracters in the string. If left unspecified, it is 255
        :return: string type
        """
        if max_length is None:
            max_length = 255
        return Orm.generic_field(
            field_type=models.CharField,
            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=False,
            default=default_value,
            error_messages=None,
            help_text=description,
            primary_key=False,
            unique=False,
            unique_for_date=None,
            unique_for_year=None,
            unique_for_month=None,
            verbose_name=None,
            validators=[],
            max_length=max_length
        )

    @classmethod
    def required_email(cls, description: str, max_length: int = None, default_value: Union[str, Callable[[], str]] = None) -> models.EmailField:
        """
        Tells Django that the model has a string field. If default value is set, it is the value added to the database
        if the user does not provide a value. The field itself is non nullable

       :param description: text used to explain what the field does
        :param default_value: value to set the field to if the developer does not add a value by herself
        :param max_length: maximum number of hcaracters in the string. If left unspecified, it is 255
        :return: string type
        """
        if max_length is None:
            max_length = 255
        return Orm.generic_field(
            field_type=models.EmailField,
            null=False,
            blank=False,
            max_length=max_length,
            default=default_value,
            help_text=description,
            choices=None,
            db_column=None,
            db_index=False,
            error_messages=None,
            primary_key=False,
            unique=False,
            unique_for_date=None,
            unique_for_year=None,
            unique_for_month=None,
            verbose_name=None,
            validators=[],
        )

    @classmethod
    def required_unique_string(cls, description: str, default_value: Union[str, Callable[[], str]] = None, max_length: int = None) -> models.CharField:
        """
        Tells Django that the model has a string field. If default value is set, it is the value added to the database
        if the user does not provide a value. The field itself is non nullable

        :param description: text used to explain what the field does
        :param default_value: value to set the field to if the developer does not add a value by herself
        :param max_length: maximum number of hcaracters in the string. If left unspecified, it is 255
        :return: string type
        """
        if max_length is None:
            max_length = 255
        return Orm.generic_field(
            field_type=models.CharField,
            null=False,
            blank=False,
            default=default_value,
            help_text=description,
            unique=True,

            choices=None,
            db_column=None,
            db_index=False,
            error_messages=None,
            primary_key=False,
            unique_for_date=None,
            unique_for_year=None,
            unique_for_month=None,
            verbose_name=None,
            validators=[],
            max_length=max_length
        )

    @classmethod
    def nullable_string(cls, description: str, default_value: Union[str, Callable[[], str]] = None, max_length: int = None) -> models.CharField:
        """
        Tells Django that the model has a string field. If default value is set, it is the value added to the database
        if the user does not provide a value. The field itself may be null

        :param description: text used to explain what the field does
        :param default_value: value to set the field to if the developer does not add a value by herself
        :param max_length: maximum number of characters in the string. If left unspecified, it is 255
        :return: string type
        """
        if max_length is None:
            max_length = 255
        return Orm.generic_field(
            field_type=models.CharField,
            null=True,
            blank=False,
            default=default_value,
            help_text=description,

            unique=False,
            choices=None,
            db_column=None,
            db_index=False,
            error_messages=None,
            primary_key=False,
            unique_for_date=None,
            unique_for_year=None,
            unique_for_month=None,
            verbose_name=None,
            validators=[],
            max_length=max_length
        )

    @classmethod
    def required_blank_string(cls, help_text: str, default_value: Union[str, Callable[[], str]] = None, max_length: int = None) -> models.CharField:
        if max_length is None:
            max_length = 255
        return Orm.generic_field_simple(
            field_type=models.CharField,
            null=False,
            blank=True,
            default=default_value,
            help_text=help_text
        )

    @classmethod
    def required_blank_text(cls, description: str,
                            default_value: Union[str, Callable[[], str]] = None) -> models.TextField:
        """
        Tells Django that the model has a text field: this means that it is a simple string that si assume to be very long.
        The field may be blank, but never null

        If default value is set, it is the value added to the database
        if the user does not provide a value. The field itself is non nullable

        :param description: text used to explain what the field does
        :param default_value: value to set the field to if the developer does not add a value by herself
        """
        return Orm.generic_field(
            field_type=models.TextField,
            null=False,
            blank=True,
            choices=None,
            db_column=None,
            db_index=False,
            default=default_value,
            error_messages=None,
            help_text=description,
            primary_key=False,
            unique=False,
            unique_for_date=None,
            unique_for_year=None,
            unique_for_month=None,
            verbose_name=None,
            validators=[],
            max_length=None
        )

    @staticmethod
    def required_duration(help_text: str, default_value: Union[timedelta, Callable[[], timedelta]] = None) -> models.DurationField:
        return Orm.generic_field_simple(
            field_type=models.DurationField,
            null=False,
            blank=False,
            default=default_value,
            help_text=help_text
        )

    @staticmethod
    def required_datetime(help_text: str,
                          default_value: Union[Arrow, Callable[[], Arrow]] = None) -> ArrowField:
        """
        tell django that this model has a date time that needs to be set
        """
        return Orm.generic_field_simple(
            field_type=ArrowField,
            null=False,
            blank=False,
            default=default_value,
            help_text=help_text
        )

    @staticmethod
    def nullable_datetime(help_text: str,
                          default_value: Union[Arrow, Callable[[], Arrow]] = None) -> ArrowField:
        return Orm.generic_field_simple(
            field_type=ArrowField,
            null=True,
            blank=False,
            default=default_value,
            help_text=help_text
        )

    @classmethod
    def required_boolean(cls, description: str, default_value: Union[bool, Callable[[], bool]] = None) -> models.BooleanField:
        return Orm.generic_field_simple(
            field_type=models.BooleanField,
            null=False,
            blank=False,
            default=default_value,
            help_text=description
        )

    @staticmethod
    def primary_id(column_name: str = None) -> models.BigAutoField:
        """
        create a rpimary id
        :param column_name: name of the column to create
        :return:
        """
        if column_name is None:
            column_name = "id"
        return models.BigAutoField(db_column=column_name, primary_key=True)
