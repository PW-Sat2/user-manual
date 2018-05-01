def dump_tc(tc):
    print ' '.join([format(x, '02X') for x in tc.build()])

def dump_ctor(tc):
    import inspect
    args = inspect.getargspec(tc.__init__)
    names = args.args[1:]
    names = map(lambda x: '<{}>'.format(x), names)
    joined = ', '.join(names)
    print '{}({})'.format(tc.__name__, joined).replace('_', '\_')

def get_uplink_apid(tc):
    x = tc.__new__(tc)
    print('0x%02x' % x.apid())

def get_downlink_apid(tc):
    x = tc.__new__(tc)
    print('0x%02x' % x.ReceivedAPID)
