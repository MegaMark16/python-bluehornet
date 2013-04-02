python-bluehornet
=================

A python API interface for BlueHornet, an email marketing service provider

It's fairly limited right now, but functionality will be added over time as needed.

Here are a few examples::

    api = BlueHornetAPI(BLUE_HORNET_API_KEY, BLUE_HORNET_API_SECRET)

    # Check the validity of one or more email addresses:
    response = api.check_email('johndoe@gmail.com','bob@example.com')

    # Add a new subscriber
    response = api.add_subscriber(email='test@example.com',
                                  firstname='Test',
                                  lastname='Subscriber')

    # Retrieve a list of subscribers
    response = api.retrieve_active(extended='1')
