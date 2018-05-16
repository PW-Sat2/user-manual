def validate_tc(tc):
    tc.build()

def dump_ctor(telecommandType):
    import inspect
    args = inspect.getargspec(telecommandType.__init__)
    names = args.args[1:]
    names = map(lambda x: '<{}>'.format(x), names)
    joined = ', '.join(names)
    print '{}({})'.format(telecommandType.__name__, joined).replace('_', '\_')

def get_uplink_apid(telecommandType):
    x = telecommandType.__new__(telecommandType)
    print('0x%02X' % x.apid())

def get_downlink_apid(responseFrameType):
    x = responseFrameType.__new__(responseFrameType)
    print('0x%02X' % x.ReceivedAPID)
