from behave import *

@given(u'user login with valid credentials')
def Step1(context):
    print("Sag")


@when(u'login with username and password')
def step2(context):
    print("Sag")


@when(u'click on submit')
def step3(context):
    print("Sag")


@then(u'user login to home page')
def step4(context):
    print("Sag")


