from django import template
from django.forms import TextInput, Select, CheckboxSelectMultiple, SelectMultiple, CheckboxInput, RadioSelect

register = template.Library()

def get_input_type(widget_type):
    if widget_type == TextInput:
        input_type = 'text'
    elif widget_type == Select or widget_type == SelectMultiple:
        input_type = 'select'
    elif widget_type == CheckboxSelectMultiple or widget_type == CheckboxInput or widget_type == RadioSelect:
        input_type = 'radiocheck'
    else:
        input_type = 'text'
    return input_type

@register.simple_tag
def standard_widget(field, use_placeholder=False, use_required=True, placeholder=None, custom_class=None, input_type=None):
    attrs = {}
    if placeholder:
        attrs['placeholder'] = placeholder
    elif use_placeholder:
        placeholder = field.label
        attrs['placeholder'] = placeholder
    if use_required and field.field.required:
        attrs['required'] = 'required'

    if field.field.show_hidden_initial:
        return field.as_widget(attrs=attrs) + field.as_hidden(only_initial=True)

    # get input type
    if not input_type:
        input_type = get_input_type(type(field.field.widget))

    # set the classes
    classes = ['input-%s' % input_type]
    if field.errors:
        classes += ['input-error']
    if custom_class:
        classes += [custom_class]
    attrs['class'] = ' '.join(classes)

    return field.as_widget(attrs=attrs)


@register.inclusion_tag('standard_form/field.html', takes_context=True)
def standard_field(context, field, use_placeholder=False, use_required=True, input_type=None):
    if not input_type:
        input_type = get_input_type(type(field.field.widget))
    return context.update({
        'field': field,
        'form_use_placeholder': use_placeholder,
        'form_use_required': use_required,
        'form_input_type': input_type,
    })


@register.inclusion_tag('standard_form/form.html', takes_context=True)
def standard_form(context, form, use_placeholder=False, use_required=True):
    #TODO: use classy tags for arguments
    return context.update({
        'form': form,
        'form_use_placeholder': use_placeholder,
        'form_use_required': use_required,
    })

