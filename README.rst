====================
django Standard Form
====================

Quick and simple django templatetags for displaying forms.


Installation
============

1) ``pip install django-standard-form``

2) add ``'standard_form'`` to your ``INSTALLED_APPS``


Usage
=====

* Most basic example:

::

    {% load standard_form %}
    
    <form action="" method="post" class="frm">
        {% csrf_token %}
        <fieldset class="frm-horizontal">
            {% standard_form form %}
            {% standard_submit %}
        </fieldset>
    </form>


* Rendering fields individually:

::


    <form action="" method="post" class="frm">
        {% csrf_token %}
        <fieldset class="frm-horizontal">
            <ol>
                <li>{% standard_field form.field_name_one %}</li>
            </ol>
        </fieldset>
        <fieldset class="frm-vertical">
            <ol>
                <li>{% standard_field form.field_name_two %}</li>
            </ol>
            {% standard_submit %}
        </fieldset>
    </form>


* Rendering widgets individually:

::

    <form action="" method="post" class="frm">
        {% csrf_token %}
        <fieldset class="frm-horizontal">
            <ol>
                 <li>
                     <label for="id_{{ form.field_name_one.name }}">My label or other stuff</label>
                     <div class="field">{% standard_widget form.field_name_one %}</div>
                 </li>
                 <li>
                     <label class="empty"></label>
                     <div class="field"><input type="submit" class="btn" value="{% trans 'Go' %}" /></div>
                 </li>
            </ol>
        </fieldset>
    </form>

* All available options:

::

    {% standard_field form.field_name_one 'no_required no_required_helper no_help_text no_error_text' custom_class='input-block' placeholder='This one has all the available options' label='My label' %}

