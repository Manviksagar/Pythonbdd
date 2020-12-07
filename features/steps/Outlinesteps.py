from behave import *

@given(u'user is on LandingPage')
def step5(context):
   print("Sag")


@when(u'user navigates to LandingPage Page')
def step6(context):
    print("Sag")


@when(u'user enters "{username}" and "{Password}"')
def step7(context, username,Password):
    print("Sag" +username + Password)


@then(u'success message is populated')
def step8(context):
    print("Sag")


@when(u'user enters allu.cucumber@gmail.com and Cucumber@blog')
def step9(context):
    print("Sag")

