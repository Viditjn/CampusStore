#Commented Something
db.define_table('Items',
                Field('rid','reference auth_user',default=auth.user.id,writable=False,readable=False),
                Field('Zone'),
                Field('Name',requires=IS_NOT_EMPTY()),
                Field('Discription','text',requires=IS_NOT_EMPTY()),
                Field('Selling_Price','integer',requires=IS_NOT_EMPTY()),
                Field('Initial_Price','integer',requires=IS_NOT_EMPTY()),
                Field('How_Old','integer',requires=IS_NOT_EMPTY()),
                Field('Bargaining','boolean'),
                Field('Image','upload'),
                Field('available','boolean',default=True,writable=False,readable=False),
                auth.signature
               )
db.Items.Zone.requires=IS_IN_SET(['Stationary','Furniture','Books','Gadgets','Vehicles','Others'])

db.define_table('wishlist',
                Field('Items', 'reference Items'),
                Field('wish_by', 'reference auth_user', default=auth.user_id)
                )
