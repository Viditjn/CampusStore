# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
@auth.requires_login()
def index():
    response.flash = T("Welcom to Our Store!")
    rows = db(db.Items).select()
    return locals()

@auth.requires_login()
def shop():
    form = SQLFORM(db.Items).process()
    if form.accepted: redirect(URL('index'))
    return locals()

@auth.requires_login()
def stationary():
    rows = db(db.Items.Zone=='Stationary').select()
    return locals()

@auth.requires_login()
def furniture():
    rows = db(db.Items.Zone=='Furniture').select()
    return locals()

@auth.requires_login()
def books():
    rows = db(db.Items.Zone=='Books').select()
    return locals()

@auth.requires_login()
def gadgets():
    rows = db(db.Items.Zone=='Gadgets').select()
    return locals()

@auth.requires_login()
def vehicles():
    rows = db(db.Items.Zone=='Vehicles').select()
    return locals()

@auth.requires_login()
def others():
    rows = db(db.Items.Zone=='Others').select()
    return locals()

@auth.requires_login()
def myitem():
    rows = db(db.Items.rid==auth.user_id).select()
    return locals()

@auth.requires_login()
def show():
     item=db.Items(request.args(0))
     return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
